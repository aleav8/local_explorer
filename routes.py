# Importing the Flask Framework
from flask import Flask, render_template, flash, session, request
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

@app.route('/categories', methods=['POST'])
def list_categories():
    '''
    List all categories selected
    '''
    print("Route /categories was called")
    sys.stdout.flush()
    
    # Retrieve user input from GET request
    categoriesfield = request.form.getlist('category')
    print(categoriesfield)
    
    addressfield = request.form.get('address')
    print(addressfield)
    
    longitudefield = request.form.get('longitude')
    print(longitudefield)
    
    latitudefield = request.form.get('latitude')
    print(latitudefield)
        
    page['title'] = 'Selected Categories'
    return render_template('list_categories.html', page=page, session=session, categories=categoriesfield, address=addressfield, longitude=longitudefield, latitude=latitudefield)    

if __name__ == '__main__':
    portchoice = '5001'  
    print("-"*70)
    print(f"If you are on Linux/Your Own Computer: Please open your browser to: http://127.0.0.1:{portchoice}/")
    print("-"*70)
    app.run(debug=True, host='0.0.0.0', port=int(portchoice))