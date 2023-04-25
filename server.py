from flask import Flask, render_template, redirect, flash, request
import jinja2

from melons import get_all

app = Flask(__name__)
app.jinja_env.undefiend = jinja2.StrictUndefined

@app.route('/')
def homepage():
        return render_template('base.html')

@app.route('/melons')
def all_melons():
      '''return all melons for purchase'''
      melons = get_all()
      return render_template('all_melons.html', melons=melons)
if __name__ == '__main__':
    app.run(debug=True)