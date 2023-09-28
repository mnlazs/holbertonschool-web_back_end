<p align="center">
  <img src="1791986.png" alt="Ejemplo de imagen centrada" width=20px>
</p>

# User Authentication Service

This is a simple User Authentication Service implemented using Python and Flask for educational purposes. In real-world scenarios, it is recommended to use established authentication libraries and frameworks to handle user authentication securely.

## Resources

- [Flask Documentation](https://flask.palletsprojects.com/en/2.1.x/)
- [Requests Module](https://docs.python-requests.org/en/master/)
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

## Learning Objectives

By completing this project, you will gain the following knowledge and skills:

- How to declare API routes in a Flask application
- How to get and set cookies
- How to retrieve request form data
- How to return various HTTP status codes

## Requirements

- Allowed editors: vi, vim, emacs
- All code will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7
- All code files should end with a new line
- The first line of all code files should be `#!/usr/bin/env python3`
- You must include a `README.md` file at the root of the project folder
- Your code should adhere to the `pycodestyle` style (version 2.5)
- SQLAlchemy 1.3.x should be used
- All code files must be executable
- File lengths will be checked using `wc`
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- Documentation should provide a meaningful explanation of the module, class, or method's purpose (length will be verified)
- All functions should be type annotated
- The Flask app should only interact with `Auth` and not directly with the database (`DB`)
- Only public methods of `Auth` and `DB` should be used outside these classes

### User Authentication Service - FAQ

This FAQ provides answers to common questions related to the User Authentication Service implemented in this project.

## How to Declare API Routes in a Flask App

In a Flask app, you can declare API routes using the `@app.route()` decorator. Here's how:

1. Import the Flask class and create an instance of the application:

   ```python
   from flask import Flask

   app = Flask(__name__)
   ```

2. Define functions that will run when a specific route is accessed. Use the `@app.route()` decorator to associate a function with a specific route:

   ```python
   @app.route('/api/route')
   def api_function():
       # Code for the view goes here
       return "Hello, World!"
   ```

3. Start the Flask application using `app.run()` within the `if __name__ == '__main__'` block:

   ```python
   if __name__ == '__main__':
       app.run()
   ```

Now, when you access the `/api/route` route in your application, the `api_function()` will run and return "Hello, World!".

## How to Get and Set Cookies

To get and set cookies in a Flask application, you can use the `flask.request` object to access incoming cookies and the `flask.make_response` function to set cookies in the response.

**Getting Cookies:**

```python
from flask import request

@app.route('/get_cookie')
def get_cookie():
    my_cookie = request.cookies.get('cookie_name')
    return f"The value of the cookie is: {my_cookie}"
```

**Setting Cookies:**

```python
from flask import make_response

@app.route('/set_cookie')
def set_cookie():
    response = make_response("Cookie set successfully")
    response.set_cookie('cookie_name', 'cookie_value')
    return response
```

In the example, we use `request.cookies.get()` to retrieve a cookie's value and `response.set_cookie()` to set a new cookie in the response.

## How to Retrieve Request Form Data

To retrieve data from a request form in a Flask application, you can use the `request.form` object. Here's an example:

```python
from flask import request

@app.route('/process_form', methods=['POST'])
def process_form():
    name = request.form.get('name')
    email = request.form.get('email')
    # Process the form data here
    return f"Name: {name}, Email: {email}"
```

In this example, we expect a POST request with `name` and `email` fields in the form, and we retrieve them using `request.form.get()`.

## How to Return Various HTTP Status Codes

You can return different HTTP status codes in a Flask application using the `flask.abort()` function or specifying the status code as the second argument in the `flask.make_response()` function.

**Using abort():**

```python
from flask import abort

@app.route('/not_found')
def not_found():
    abort(404)
```

**Using make_response():**

```python
from flask import make_response

@app.route('/access_denied')
def access_denied():
    response = make_response("Access denied", 403)
    return response
```

In these examples, we are returning HTTP status codes 404 (Not Found) and 403 (Forbidden) respectively.

These are answers to common questions about declaring API routes, getting and setting cookies, retrieving request form data, and returning various HTTP status codes in a Flask application.
