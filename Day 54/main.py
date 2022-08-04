from flask import Flask
app = Flask(__name__)
def bold(function):
    def wrapper_fun():
        return f"<b>{function()}</b>"
    return wrapper_fun
def emphasis(function):
    def wrapper_fun():
        return f"<em>{function()}</em>"
    return wrapper_fun
def underline(function):
    def wrapper_fun():
        return f"<u>{function()}</u>"

    return wrapper_fun
@app.route('/')
def hello_world():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"


@app.route("/bye")
@bold
@emphasis
@underline
def say_bye():
    return "Bye"



@app.route("/username/<name>/<int:number>")
def greet(name,number):
    return f"Hi there {name}, you are {number} years old"

if __name__ == "__main__":
    app.run(debug=True)


class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
        return wrapper

@authenticated_decorator
def create_blog(user):
    print(f"THis is {user.name}'s new blog post.")

new_user = User("Shresth")
new_user.is_logged_in = True
create_blog(new_user)