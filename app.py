from flask import Flask, render_template

app = Flask("", template_folder="", static_folder="")

@app.route('/') # декоратор, приписывающий к пути / функцию index
def index():
    return render_template("index.html")

app.run()
