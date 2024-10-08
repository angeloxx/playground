from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

def test_hello_world():
    assert hello_world() == 'Hello World!'

if __name__ == '__main__':
    app.run()