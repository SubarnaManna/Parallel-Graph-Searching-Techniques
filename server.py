"""
Flask Application Starter Template
---------------------------------

This template provides a basic foundation for building web applications with Flask.
It includes:

-   Flask setup
-   Basic routing
-   HTML templating with Jinja2
-   Configuration management
-   Error handling
-   Logging
-   Basic app structure

To get started:

1.  Install Flask: `pip install Flask`
2.  Save this code as a Python file (e.g., `app.py`).
3.  Run the application: `python app.py`
4.  Open your web browser and go to http://127.0.0.1:5000/

"""

import os
from flask import Flask, render_template, request, redirect, url_for, abort
import logging

# 1. Configuration
# ---------------
# -   Configuration is often stored in a separate file or environment variables.
# -   For simplicity, we'll define some basic configuration here.
# -   In a real application, consider using a library like `python-decouple`
#     or `Flask-Environments`.

class Config:
    """Base configuration class."""
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')  # Use an env variable!
    LOG_LEVEL = logging.INFO  # Default log level


class DevelopmentConfig(Config):
    """Configuration for development environment."""
    DEBUG = True
    LOG_LEVEL = logging.DEBUG


class ProductionConfig(Config):
    """Configuration for production environment."""
    #  In production, make sure DEBUG is False.
    LOG_LEVEL = logging.WARNING


class TestingConfig(Config):
    """Configuration for testing environment."""
    TESTING = True
    DEBUG = True  #  Allow debugging during testing if needed
    LOG_LEVEL = logging.DEBUG
    SECRET_KEY = 'test_secret' #  Important for testing, but not for production!


# 2. Application Setup
# -------------------
# -   Create the Flask application instance.
# -   Load configuration.
# -   Set up logging.

# Create Flask app
app = Flask(__name__)

# Select and load the configuration.  The default is DevelopmentConfig.
# You would normally use an environment variable to control this.
# E.g., export FLASK_ENV=production
flask_env = os.environ.get('FLASK_ENV', 'development')  # Default to 'development'
if flask_env == 'production':
    app.config.from_object(ProductionConfig)
elif flask_env == 'development':
    app.config.from_object(DevelopmentConfig)
elif flask_env == 'testing':
    app.config.from_object(TestingConfig)
else:
    app.config.from_object(DevelopmentConfig)  # Fallback to development


# Set up logging
logging.basicConfig(level=app.config['LOG_LEVEL'])
logger = logging.getLogger(__name__)  # Get the logger for this module

# Log a message to indicate the environment.
logger.info(f"Running in {flask_env} mode.")
logger.info(f"DEBUG is {app.config['DEBUG']}")


# 3. Route Definitions
# --------------------
# -   Define the application's routes (URLs).
# -   Use decorators to associate functions with routes.
# -   Handle different HTTP methods (GET, POST, etc.).
# -   Demonstrate URL parameters.
# -   Demonstrate rendering HTML templates.

@app.route('/')
def index():
    """
    The home page.  Renders a simple HTML template.
    """
    logger.debug("Accessing the index page.")
    return render_template('index.html', title='Welcome to Flask')


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    """
    A simple example with a URL parameter.
    """
    if name:
        logger.debug(f"Saying hello to {name}")
        return render_template('hello.html', name=name)
    else:
        logger.debug("Saying hello to the world")
        return render_template('hello.html', name='World')



@app.route('/form', methods=['GET', 'POST'])
def form_example():
    """
    A form example that handles both GET and POST requests.
    """
    if request.method == 'POST':
        # Get data from the form.  Use get() to avoid KeyError if the
        # field is not present.  Provide a default value.
        name = request.form.get('name', '')
        email = request.form.get('email', '')
        logger.info(f"Form submitted with name: {name}, email: {email}")
        return render_template('form_result.html', name=name, email=email)
    else:
        #  It's a GET request, so display the form.
        return render_template('form.html')


@app.route('/user/<int:user_id>')
def user_profile(user_id):
    """
    Example of using a URL parameter with a specified data type (integer).
    """
    logger.debug(f"Accessing user profile for user ID: {user_id}")
    #  In a real app, you would fetch user data from a database.
    if user_id < 0:
        abort(400, description="Invalid user ID")  #  abort() for errors
    elif user_id == 0:
        user = {'name': 'Anonymous', 'email': 'anonymous@example.com'}
    elif user_id == 1:
        user = {'name': 'John Doe', 'email': 'john.doe@example.com'}
    else:
        abort(404, description="User not found")
    return render_template('user_profile.html', user=user)



# 4. Error Handling
# -----------------
# -   Customize error pages.
# -   Flask provides default error handling, but you can override it.

@app.errorhandler(400)
def bad_request(error):
    """Custom error page for 400 Bad Request."""
    logger.warning(f"Bad request: {error}")
    return render_template('400.html', error=error), 400  #  Return code


@app.errorhandler(404)
def page_not_found(error):
    """Custom error page for 404 Not Found."""
    logger.warning(f"Page not found: {error}")
    return render_template('404.html', error=error), 404  # Return the HTTP status code


@app.errorhandler(500)
def internal_server_error(error):
    """Custom error page for 500 Internal Server Error."""
    logger.error(f"Internal server error: {error}")
    return render_template('500.html', error=error), 500



# 5. Application Entry Point
# ------------------------
# -   The `if __name__ == '__main__':` block is executed when the script is run
#     directly (not imported as a module).
# -   It's used to start the Flask development server.
# -   **Important:** Don't use the built-in development server in production.
#     Use a production-ready WSGI server like Gunicorn or uWSGI.

if __name__ == '__main__':
    # Start the Flask development server.
    #  -   debug=True:  Enable hot reloading and the debugger.  ONLY FOR DEVELOPMENT.
    #  -   host='0.0.0.0':  Make the server accessible from outside (optional).
    app.run(debug=app.config['DEBUG'], host='0.0.0.0')
