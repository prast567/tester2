from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    #return render_template('index.html')
    return "Hello World!"

if __name__ == '__main__':
    app.run()