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

@app.route('/cart')
def shopping_cart():
      '''Gets all the melons that were added to the cart.csv'''
      return render_template('cart.html')

@app.route('/melon/<melon_id>')
def single_melon(melon_id):
      '''Get's a single melon the user selects, also provides a button to add the melon to the cart'''
      return render_template('melon_details.html')

@app.route('/add_to_cart/<melon_id>')
def add_to_cart(melon_id):
      '''Adds a melon to the cart'''
      return f'{melon_id} added to the cart!'



if __name__ == '__main__':
    app.run(debug=True)