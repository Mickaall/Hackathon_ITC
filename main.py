from bottle import route, run, template, static_file, get, post, delete, request, error
from sys import argv
import json
import pymysql



# STATIC ROUTES


@get("/")
def index():
    return template("about.html")


# ----------------------------------------------------------------
# JAVASCRIPT -----------------------------------------------------
# ----------------------------------------------------------------

@get('/vendor/bootstrap/js/<filename:re:.*\.js>')
def js_bootstrap(filename):
    return static_file(filename, root='vendor/bootstrap/js')


@get('/vendor/jquery/<filename:re:.*\.js>')
def js_jquery(filename):
    return static_file(filename, root='vendor/jquery')


@get('/js/<filename:re:.*\.js>')
def js_logic(filename):
    return static_file(filename, root='js')


@get('/<filename:re:.*\.js>')
def js_root(filename):
    return static_file(filename, root='')


# ----------------------------------------------------------------
# CSS ------------------------------------------------------------
# ----------------------------------------------------------------

@get('/vendor/bootstrap/css/<filename:re:.*\.css>')
def stylesheets_bootstrap(filename):
    return static_file(filename, root='vendor/bootstrap/css')


@get('/css/<filename:re:.*\.css>')
def stylesheets_css(filename):
    return static_file(filename, root='css')


# ----------------------------------------------------------------
# OTHER ----------------------------------------------------------
# ----------------------------------------------------------------

@get('/images/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='images')


@error(404)
def error404(error):
    return "Nothing to see here"


run(host='localhost', port=7000)