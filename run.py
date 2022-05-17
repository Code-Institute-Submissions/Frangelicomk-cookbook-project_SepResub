import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
# from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static', 'assets')

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'PUsG,-0id*1DKs(LXS}yp8PVTf`jzc'

mongo = PyMongo(app)

messages = [{'title': 'Message One',
             'description': 'Message One Content'},
            {'title': 'Message Two',
             'description': 'Message Two Content'}
            ]


@app.route("/")
def index():
    """
    Formats index.html, take recipes from database and
    puts them on index.html

    """
    recipes = mongo.db.recipes.find()
    recipesModified = []
    if session.get("user"):
        favorites = mongo.db.user_favorites.find({"username": session["user"]})
        for r in recipes:
            for f in favorites:
                r['isFavorite'] = False
                if(r['recipe_name'] == f['recipe_name']):
                    r['isFavorite'] = True
            recipesModified.append(r)
        return render_template("index.html", recipes=recipesModified)
    return render_template("index.html", recipes=recipes)


@app.route("/recipe/<recipe_name>")
def recipe(recipe_name):
    """
    Formats index.html, take recipes from database and
    puts them on index.html

    """
    
    mongo.db.recipes.find_one({"recipe_name": recipe_name})
    print(recipe, recipe_name)
    return render_template("recipe.html", recipe=recipe)


@app.route("/favorite_recipe/<recipe_name>")
def favorite_recipe(recipe_name):
    """
    Formats index.html, take recipes from database and
    puts them on index.html

    """

    favorites = []
    checkIfFavorite = mongo.db.user_favorites.find({"recipe_name": recipe_name, "username": session["user"]})
    for x in checkIfFavorite:
        favorites.append(x)
    # if already favorited
    if len(favorites) >= 1: 
        mongo.db.user_favorites.delete_one({"recipe_name": recipe_name, "username": session["user"]})
    else:
        mongo.db.user_favorites.insert_one({
            "recipe_name": recipe_name, 
            "username": session["user"]})
    return redirect(url_for("index"))


@app.route("/about")
def about():
    """
    Formats the structure of about.html

    """
    return render_template("about.html", page_title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Registration auth, checks if user already exists in database.
    This function was coppied from Code Institute Mini Project

    """
    if not session.get("user"):
        if request.method == "POST":
            # check if username already exists in db
            existing_user = mongo.db.users.find_one(
                {"username": request.form.get("username").lower()})

            if existing_user:
                flash("Username already exists")
                return redirect(url_for("register"))
            register_user = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(
                    request.form.get("password"))}
            mongo.db.users.insert_one(register_user)

            # put the new user into 'session' cookie
            session["user"] = request.form.get("username").lower()
            flash("Registration Successful!")
            return redirect(url_for("favorites", username=session["user"]))

        return render_template("register.html")
    return redirect(url_for("index"))


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    This function check whether the user has logged in or if the username
    and password are matching the database of a registered user
    This function was coppied from Code Institute Mini Project

    """
    if not session.get("user"):
        if request.method == "POST":
            # check if username exists in db
            existing_user = mongo.db.users.find_one(
                {"username": request.form.get("username").lower()})

            if existing_user:
                # ensure hashed password matches user input
                if check_password_hash(
                        existing_user["password"],
                        request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for(
                        "favorites", username=session["user"]))
                else:
                    # invalid password match
                    flash("Incorrect Username and/or Password")
                    return redirect(url_for("login"))

            else:
                # username doesn't exist
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        return render_template("login.html")
    return redirect(url_for("index"))


@app.route("/favorites<username>", methods=["GET", "POST"])
def favorites(username):
    """
    Favorites html only appears if user is logged in

    """
    if session.get("user"):
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        return render_template("favorites.html", username=username)
    return render_template(
        "login.html")


@app.route("/logout")
def logout():
    """
    Log out button only appears if user is logged in

    """
    if session.get("user"):
        flash("You have been logged out")
        session.pop("user")
        return redirect(url_for("login"))


@app.route('/add_recipe', methods=('GET', 'POST'))
def add_recipe():
    """
    add_recipe only appears if user is logged in

    """
    if session.get("user"):
        if request.method == 'POST':
            newrecipe = {
                "cousine_name": request.form.get('cousine_name'),
                "recipe_name": request.form.get('recipe_name'),
                "description": request.form.get('description'),
                "ingredients": request.form.get('ingredients'),
                "cover": request.form.get("cover")
            }
            mongo.db.recipes.insert_one(newrecipe)
            flash("Recipe Added")
            return redirect(url_for("index"))
    recipes = mongo.db.recipes.find().sort("recipe_name", 1)
    return render_template("add_recipe.html", recipes=recipes)


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
