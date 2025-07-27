from flask import Flask #flask web framework for running this file
import threading 
app = Flask("") #creating an instance of flask 
@app.route('/') #this means , that the decorator in flask allows us to associate url with a function , or something idk
def home():
    return 'Bot is working!'  #to let us know Bot is working 
def run():
    app.run(host='0.0.0.0',port=8080) #the host being 0.9.0.0 allows us to enable all ip addresses to work 
def keep_alive(): #called in main.py
    t=threading.Thread(target=run)
    t.start() #starting the thread , which runs the run func defined prev

