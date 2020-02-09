from flask import Flask
from flask import request
import sqlite3

app=Flask(__name__)

@app.route('/')
def root():
    db = sqlite3.connect('users.db')
    cursor = db.cursor()
    cursor.execute ('CREATE TABLE if NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)')
    
      #cursor.execute(INSERT INTO users(username,password)VALUES("Olawale","Password123"))
      #db.commit()

    cursor.execute('SELECT * FROM users')
    data = cursor.fetchall()

    return str(data)


@app.route('/register')
def create():
    #Connects to db
    db =sqlite3.connect(users.db)
    cursor = db.cursor()

    #get args from the register request 
    username = requests.args.get('username')
    password = request.args.get('password')

    #Insert data into the db.
    cursor.execute('INSERT INTO users(username, password) VALUES("%s", "%s")' % (usernamae,password))
    db.commit()

    #close db connection
    db.close()
    return 'Registered as :' + username + '!'

@app.route('/projects')
def projects():

    db = sqlite3.connect('projects.db')
    cursor = db.cursor()
    cursor.execute ('CREATE TABLE if NOT EXISTS projects (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT)')
 
 
@app.route('/actions')
def createActions():
    db = sqlite3.connect('actions.db')
    cursor = db.cursor()
    cursor.execute ('CREATE TABLE if NOT EXISTS actions (id INTEGER PRIMARY KEY AUTOINCREMENT, project_id INTEGER, description TEXT, note TEXT)')
 

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
