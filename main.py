from bottle import route, run, template, static_file, get, post, delete, request, error
from sys import argv
import json
import pymysql



# STATIC ROUTES


@get("/")
def index():
    return template("about.html")


@get('/js/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='js')


# ATTN: IS BELOW NEEDED?
@get('/js/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='')


@get('/css/modern-business.css>')
def stylesheets():
    return static_file('modern-business.css', root='css')


@get('/images/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='images')


@error(404)
def error404(error):
    return "Nothing to see here"


run(host='localhost', port=7000)