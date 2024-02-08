from flask import Flask, request
from Controller import UserController

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/user', methods=['POST'])
def save_user():
    return UserController.save(request)

@app.route('/login', methods=['POST'])
def get_user():
    return UserController.get_accounts(request)

if __name__ == '__main__':
    app.run()
