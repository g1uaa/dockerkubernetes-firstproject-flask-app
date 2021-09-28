"""
app
"""
from flask import Flask

# provide app name as dunder name to Flask and create an app instance
# from Flask UI class
app = Flask(__name__)

# map the root url of the app to this python function (which has been
# mapped to Flask UI func
@app.route("/")
def hello_world():
    """A dummy docstring."""
    return "KEEP LEARNING, KEEP MOVING AHEAD"

if __name__ == "__main__":
    """ when we run my module 'app.py' as a script from cmd line as:
        python app.py, then
        run the app and pass: host, port and debug etc info"""
    app.run(port=5001, debug=True)
