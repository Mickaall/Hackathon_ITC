from bottle import route, run, template, static_file, get, post, delete, request, error, TEMPLATE_PATH

from sys import argv
import json
import pymysql

TEMPLATE_PATH.insert(0, '')
# CONNECT TO THE DATABASE
connection = pymysql.connect(host='db4free.net',
                             user='hackathonmike',
                             password='HACKathon123',
                             db='itchackathon',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)


# LIST CATEGORIES
@get("/categories")
def list_categories():
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM category"
            cursor.execute(sql)
            result = cursor.fetchall()
            return json.dumps({"STATUS": "SUCCESS",
                               "CATEGORIES": result,
                               "CODE": 200})
    except:
        return json.dumps({"STATUS": "ERROR",
                           "MSG": "Internal error",
                           "CODE": 500})


# LIST LOCATIONS
@get("/locations")
def list_locations():
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM location"
            cursor.execute(sql)
            result = cursor.fetchall()
            return json.dumps({"STATUS": "SUCCESS",
                               "LOCATIONS": result,
                               "CODE": 200})
    except:
        return json.dumps({"STATUS": "ERROR",
                           "MSG": "Internal error",
                           "CODE": 500})


# STATIC ROUTES


@get("/")
@route("/about.html")
@get("/map.html")
def index():
    return template("about.html")



@route("/map.html")
def map():
    return static_file('map.html', root='')

@route("/services.html")
def services():
    return static_file('services.html', root='')


@route("/blog-home-1.html")
def blog1():
    return static_file("blog-home-1.html", root='')


@route("/blog-home-2.html")
def blog2():
    return static_file("blog-home-2.html", root='')

@route("/blog-post.html")
def blog_post():
    return static_file("blog-post.html", root='')


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