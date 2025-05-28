from flask import Flask, render_template

app = Flask("PlushShop", template_folder="", static_folder="")

@app.route('/') # декоратор, приписывающий к пути / функцию index
def index():
    return render_template("index.html")


@app.route('/cart')
def cart():
    return render_template("cart.html")

@app.route('/help')
def help():
    return render_template("help.html")


app.run()
