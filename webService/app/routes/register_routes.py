from flask import render_template
from internalFunctions.logic import add_integer

def register_routes(app):
    @app.route('/')
    def home():
        result_integer = add_integer('home')
        return render_template('index.html', integer=result_integer)

    @app.route('/info')
    def info():
        result_integer = add_integer('info')
        return render_template('info.html', integer=result_integer)

    @app.route('/about')
    def about():
        result_integer = add_integer('about')
        return render_template('about.html', integer=result_integer)


    #@app.route('/linearRegression')
    #def linearRegression():
    #    result_integer = add_integer('linearRegression')
    #    return render_template('linearRegression.html', integer=result_integer, graph = None)

