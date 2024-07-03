import pytest



@pytest.fixture
def app():
    from flask import Flask
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_hello_world(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello, World!'

#from app import fhwebsite as flask_app
#import fhwebsite as flask_app

# @pytest.fixture
# def app():
#     yield flask_app

# @pytest.fixture
# def client(app):
#     return app.test_client()

# def test_hello_world(client):
#     response = client.get('/')
#     assert response.status_code == 200
#     assert response.data == b'Hello, World!'