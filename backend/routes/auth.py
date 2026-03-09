from flask import Blueprint, redirect, request
import config
import requests

auth_routes = Blueprint("auth", __name__)

@auth_routes.route("/login")
def login():

    url = (
        "https://www.facebook.com/v19.0/dialog/oauth"
        f"?client_id={config.FACEBOOK_APP_ID}"
        f"&redirect_uri={config.REDIRECT_URI}"
        "&scope=pages_show_list,pages_manage_posts,pages_read_engagement"
    )

    return redirect(url)


@auth_routes.route("/auth/callback")
def callback():

    code = request.args.get("code")

    if not code:
        return {"error": "Authorization code not received"}, 400

    token_url = "https://graph.facebook.com/v19.0/oauth/access_token"

    params = {
        "client_id": config.FACEBOOK_APP_ID,
        "client_secret": config.FACEBOOK_APP_SECRET,
        "redirect_uri": config.REDIRECT_URI,
        "code": code
    }

    response = requests.get(token_url, params=params)

    if response.status_code != 200:
        return {"error": "Failed to get access token", "details": response.json()}, 400

    return response.json()