from routes import *

if __name__ == '__main__':
    portchoice = '5001'  
    print("-"*70)
    print(f"If you are on Linux/Your Own Computer: Please open your browser to: http://127.0.0.1:{portchoice}/")
    print("-"*70)
    app.run(debug=True, host='0.0.0.0', port=int(portchoice))