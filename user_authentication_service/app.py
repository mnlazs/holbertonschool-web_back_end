#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, jsonify, request, abort, redirect
from sqlalchemy.orm.exc import NoResultFound
from auth import Auth
from uuid import uuid4

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"])
def welcome():
    """Maneja las llamadas HTTP get"""
    message = {"message": "Bienvenue"}
    return jsonify(message)


@app.route('/users', methods=['POST'])
def register_user() -> str:

    try:
        email = request.form['email']
        password = request.form['password']
    except KeyError:
        abort(400)

    try:
        user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

    msg = {"email": email, "message": "user created"}
    return jsonify(msg)


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ POST /sessions"""
    form_data = request.form

    if "email" not in form_data:
        return jsonify({"message": "email required"}), 400
    elif "password" not in form_data:
        return jsonify({"message": "password required"}), 400
    else:

        email = request.form.get("email")
        pswd = request.form.get("password")

        if AUTH.valid_login(email, pswd) is False:
            abort(401)
        else:
            session_id = AUTH.create_session(email)
            response = jsonify({
                "email": email,
                "message": "logged in"
            })
            response.set_cookie('session_id', session_id)

            return response


@app.route("/sessions", methods=["DELETE"])
def logout():
    """ Method to log out """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect("/", 302)
    abort(403)


@app.route("/profile", methods=["GET"])
def profile():
    """ User profile method """
    session_id = request.cookies.get('session_id')
    if session_id:
        try:
            user = AUTH.get_user_from_session_id(session_id)
            response = jsonify({"email": "{}".format(user.email)})
            return response, 200
        except ValueError:
            return None
    abort(403)


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token() -> str:
    """generate a token and respond with a 200 HTTP status"""
    try:
        email = request.form['email']
    except KeyError:
        abort(403)

    try:
        reset_token = AUTH.get_reset_password_token(email)
    except ValueError:
        abort(403)

    msg = {"email": email, "reset_token": reset_token}

    return jsonify(msg), 200


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password() -> str:
    """ Update the password
    PUT /reset_password
    Updates password with reset token
    Return:
        - 400 if bad request
        - 403 if not valid reset token
        - 200 and JSON Payload if valid
    """
    try:
        email = request.form['email']
        reset_token = request.form['reset_token']
        new_password = request.form['new_password']
    except KeyError:
        abort(400)

    try:
        AUTH.update_password(reset_token, new_password)
    except ValueError:
        abort(403)

    msg = {"email": email, "message": "Password updated"}
    return jsonify(msg), 200
