from flask import Flask

app = Flask(__name__)

@app.route('/') #127.0.0.1:5000
def index_page():
    return '<h1> Welcome </h1>'

@app.route('/view-status')
def status_view():
    return '<h2> Currently the page is deployed on local system </h2>'

@app.route('/user/<userid>') #Dynamic Routing
def user(userid):
    return f"<h3> Welcome User No: {userid} </h3>"

@app.route('/latin/<name>') #Dynamic Routing
def puppy_latin(name):
    if name[-1] == 'y':
        name = name[: -1] + 'iful'
    else:
        name = name[: -1] + 'y'
    return f"<h3> Latin name of puppy: {name} </h3>"

if __name__ == '__main__':
    app.run()