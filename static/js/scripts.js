/*!
* Start Bootstrap - Shop Homepage v5.0.5 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project
$(function(){
    var current = location.pathname;
    $('nav li a').each(function(){
        var $this = $(this);
        // if the current path is like this link, make it active
        if($this.attr('href') == "/" && current == "/"){
            $this.addClass('active');
        }
        if($this.attr('href').indexOf(current) !== -1 && current != "/"){
            $this.addClass('active');
        }
    })
})