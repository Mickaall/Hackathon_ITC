from bottle import route, run, template, static_file, get, post, request, redirect, TEMPLATE_PATH, error

from sys import argv
import json
import pymysql
import os

TEMPLATE_PATH.insert(0, '')

# ----------------------------------------------------------------
# CONNECT TO THE DATABASE ----------------------------------------
# ----------------------------------------------------------------

connection = pymysql.connect(host='db4free.net',
                             user='hackathonmike',
                             password='HACKathon123',
                             db='itchackathon',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)


# ----------------------------------------------------------------
# CONNECT TO THE DATABASE ----------------------------------------
# ----------------------------------------------------------------

@get("/recc")
def load_recc():
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM recommendation LIMIT 1'
            cursor.execute(sql)
            result = cursor.fetchall()
            if result:
                return json.dumps({'STATUS': 'SUCCESS',
                                   'RECC': result,
                                   'CODE': 200})
            else:
                return json.dumps({'STATUS': 'ERROR',
                                   'MSG': "no alerts found",
                                   'CODE': 404})

    except:
        return json.dumps({'STATUS': 'ERROR',
                           'MSG': "Internal error",
                           'CODE': 500})


# ----------------------------------------------------------------
# FILE UPLOAD ----------------------------------------------------
# ----------------------------------------------------------------


@post('/upload')
def do_upload():
    x = "It's a dog"
    y = "The breed is a Chiwawa"
    z = "Go to Gan Meir"
    upload = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.png', '.jpg', '.jpeg'):
        return "File extension not allowed."
    save_path = "images"
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    file_path = "{path}/{file}".format(path=save_path, file=upload.filename)
    upload.save(file_path)
    return redirect('portfolio-item.html')


# ----------------------------------------------------------------
# ADD AN ALERT ---------------------------------------------------
# ----------------------------------------------------------------

@post("/alert")
def add_alert():

    cat = request.POST.get('category')
    if cat == '1':
        category = "Cleanliness"
    elif cat == '2':
        category = "Fight"
    elif cat == '3':
        category = "Park Condition"
    elif cat == '4':
        category = "Weather"
    elif cat == '5':
        category = "Other"

    description = request.POST.get('desc')

    loc = request.POST.get('location')
    if loc == '1':
        location = "Gan Meir"
    elif loc == '2':
        location = "Gan Hakovshim"
    elif loc == '3':
        location = "Beach"

    try:
        with connection.cursor() as cursor:
            sql = 'INSERT INTO alerts VALUES(%s, %s, %s)'
            data = (category, description, location)
            cursor.execute(sql, data)
            connection.commit()
    except:
        return json.dumps({"STATUS": "ERROR",
                           "MSG": "Missing Parameters",
                           "CODE": 400})


@get("/alerts")
def load_alerts():
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM alerts LIMIT 5'
            cursor.execute(sql)
            result = cursor.fetchall()
            if result:
                return json.dumps({'STATUS': 'SUCCESS',
                                   'ALERTS': result,
                                   'CODE': 200})
            else:
                return json.dumps({'STATUS': 'ERROR',
                                   'MSG': "no alerts found",
                                   'CODE': 404})

    except:
        return json.dumps({'STATUS': 'ERROR',
                           'MSG': "Internal error",
                           'CODE': 500})


@get("/alerts-gm")
def load_alerts_gm():
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM alerts WHERE location = "Gan Meir"'
            cursor.execute(sql)
            result = cursor.fetchall()
            if result:
                return json.dumps({'STATUS': 'SUCCESS',
                                   'ALERTS': result,
                                   'CODE': 200})
            else:
                return json.dumps({'STATUS': 'ERROR',
                                   'MSG': "no alerts found",
                                   'CODE': 404})

    except:
        return json.dumps({'STATUS': 'ERROR',
                           'MSG': "Internal error",
                           'CODE': 500})


@get("/alerts-gh")
def load_alerts_gh():
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM alerts WHERE location = "Gan Hakovshim"'
            cursor.execute(sql)
            result = cursor.fetchall()
            if result:
                return json.dumps({'STATUS': 'SUCCESS',
                                   'ALERTS': result,
                                   'CODE': 200})
            else:
                return json.dumps({'STATUS': 'ERROR',
                                   'MSG': "no alerts found",
                                   'CODE': 404})

    except:
        return json.dumps({'STATUS': 'ERROR',
                           'MSG': "Internal error",
                           'CODE': 500})


@get("/alerts-b")
def load_alerts_b():
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM alerts WHERE location = "Beach"'
            cursor.execute(sql)
            result = cursor.fetchall()
            if result:
                return json.dumps({'STATUS': 'SUCCESS',
                                   'ALERTS': result,
                                   'CODE': 200})
            else:
                return json.dumps({'STATUS': 'ERROR',
                                   'MSG': "no alerts found",
                                   'CODE': 404})

    except:
        return json.dumps({'STATUS': 'ERROR',
                           'MSG': "Internal error",
                           'CODE': 500})

# ----------------------------------------------------------------
# LIST CATEGORIES & LOCATIONS ------------------------------------
# ----------------------------------------------------------------

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


# ----------------------------------------------------------------
# STATIC ROUTES --------------------------------------------------
# ----------------------------------------------------------------

@get("/")
@route("/about.html")
@get("/fake_map.html")
def index():
    return template("about.html")


@route("/fake_map.html")
def map():
    return static_file('fake_map.html', root='')


@route("/services.html")
def services():
    return static_file('services.html', root='')


@route("/portfolio-item.html")
def recc():
    return static_file('portfolio-item.html', root='')


@route("/blog-home-1.html")
def blog1():
    return static_file("blog-home-1.html", root='')


@route("/blog-home-2.html")
def blog2():
    return static_file("blog-home-2.html", root='')


@route("/blog-post.html")
def blog_post():
    return static_file("blog-post.html", root='')


@route("/game.html")
def game():
    return static_file("game.html", root='')


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