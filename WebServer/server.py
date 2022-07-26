from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')                 # Decorator
def hello_world():
    return render_template('./index.html')


@app.route('/he')  
def hello_world2():
    return "Hello World1!"
# print(hello_world())
# print(__name__)

