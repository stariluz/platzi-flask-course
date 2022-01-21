from flask import render_template, redirect, url_for, request, session, make_response, flash
import unittest
from app import create_app
from app.forms import LoginForm
from django
app=create_app()

##COMANDOS
@app.cli.command()
def test():
    tests=unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)
    
##FORMAS

###ERRORES
@app.errorhandler(404)
def page_dont_exist(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def page_dont_exist(error):
    return render_template('500.html', error=error)

###RUTAS
@app.route("/")
def index():
    user_ip=request.remote_addr
    message="SE ACCEDIO A LA RUTA INDEX"
    session['user_ip'] = user_ip
    session['message']=message
    return redirect(url_for("home"))

@app.route("/home")
def home():
    if not "user_ip" in session:
        return redirect(url_for("index"))
    
    user_ip = session.get('user_ip')
    message = session.get('message')
    username = session.get('username')
    
    todos_btns=[
        "Home",
        "Hello",
        "Apps",
        "Login"
    ]
    context={
        "todos_btns": todos_btns,
        "user_ip": user_ip,
        "message": message,
        "username": username
    }
    return render_template("home.html", **context)