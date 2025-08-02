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


########################
#Retrieve All Selected Categories#
########################

@app.route('/', methods=['GET', 'POST'])
def list_categories():
    if request.method == 'POST':
        categoriesfield = request.form.getlist('category')
        addressfield = request.form.get('address')
    
        categories_str = ','.join(categoriesfield)
        
        print(categoriesfield)
        print(addressfield)

        # Use 'category' param here to match GET handler and template
        return redirect(url_for('list_categories', 
                            category=categories_str, 
                            address=addressfield))
    
    # GET
    categories_str = request.args.get('category', '')
    categoriesfield = categories_str.split(',') if categories_str else []
    
    addressfield = request.args.get('address')
    print(categoriesfield)
    print(addressfield)
        
    return render_template('index.html',
                           address=addressfield,
                           category=categoriesfield)