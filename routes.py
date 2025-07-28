# Importing the Flask Framework
from flask import Flask, render_template, flash, session, request, redirect, url_for
import sys

# appsetup
page = {}
session = {}

# Initialise the FLASK application
app = Flask(__name__)
app.secret_key = 'SoMeSeCrEtKeYhErE'

# Debug = true if you want debug output on error ; change to false if you dont
app.debug = True

#####################################################
##  INDEX
#####################################################

# What happens when we go to our website (home page)
@app.route("/")
def home():
    page['title'] = 'Welcome'
    return render_template('index.html', session=session, page=page)

########################
#Retrieve All Selected Categories#
########################

@app.route('/categories', methods=['GET', 'POST'])
def list_categories():
    if request.method == 'POST':
        categoriesfield = request.form.getlist('category')
        latitudefield = request.form.get('latitude')
        longitudefield = request.form.get('longitude')
        # Convert lists to multiple query params or comma separated string
        categories_str = ','.join(categoriesfield)
        
        print(categoriesfield)
        print(longitudefield)
        print(latitudefield)


        # Redirect to GET URL with params
        return redirect(url_for('list_categories', categories=categoriesfield, longitude=longitudefield, latitude=latitudefield))
    
    # GET: get params from URL
    categories_str = request.args.get('category', '')
    categoriesfield = categories_str.split(',') if categories_str else []
    latitudefield = request.args.get('latitude')
    longitudefield = request.args.get('longitude')
    
    print(categoriesfield)
    print(longitudefield)
    print(latitudefield)
        
    page['title'] = 'Selected Categories'
    return render_template('list_categories.html', page=page, session=session, categories=categoriesfield, longitude=longitudefield, latitude=latitudefield)    

if __name__ == '__main__':
    portchoice = '5001'  
    print("-"*70)
    print(f"If you are on Linux/Your Own Computer: Please open your browser to: http://127.0.0.1:{portchoice}/")
    print("-"*70)
    app.run(debug=True, host='0.0.0.0', port=int(portchoice))