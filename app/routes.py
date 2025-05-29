import os
import secrets

from dotenv import load_dotenv
from flask import Blueprint, redirect, session, render_template

load_dotenv()

BASE_URL = "https://yutify.onrender.com"

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/authorize")
def authorize():
    """
    Redirect the user to the authorization endpoint
    to ask for permission to access their data.
    """

    auth_endpoint = "/authorize"

    client_id = os.getenv("CLIENT_ID")
    redirect_uri = os.getenv("REDIRECT_URI")
    response_type = "code"
    scope = "activity"
    state = secrets.token_urlsafe()

    # Store the state in the session for later validation
    session["state"] = state

    # Construct the authorization URL with the necessary parameters
    authorization_url = (
        f"{BASE_URL}{auth_endpoint}?client_id={client_id}&redirect_uri={redirect_uri}"
        f"&response_type={response_type}&scope={scope}&state={state}"
    )

    # Redirect the user to the authorization URL
    # This is where the user will be asked to grant or deny access.
    return redirect(authorization_url)
