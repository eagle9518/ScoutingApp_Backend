from functools import wraps
from flask import request, redirect, url_for, session

import cloudinary
import cloudinary.uploader
import cloudinary.api

import os

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print(session.get('email'))
        if session.get("email") is None:
            return redirect("/google/authorize")
        return f(*args, **kwargs)
    return decorated_function

cloudinary.config(
    cloud_name = os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key = os.getenv("CLOUDINARY_API_KEY"),
    api_secret = os.getenv("CLOUDINARY_API_SECRET")
)

def upload_image(file):
    r = cloudinary.uploader.upload(file)
    img_url = r["secure_url"]
    return img_url

def create_message(email_text):
    import sendgrid
    return sendgrid.helpers.mail.Mail(
        from_email=os.environ["FROM_EMAIL"],
        to_emails=os.environ["TO_EMAIL"],
        subject='SCOUTING APP V2 - unhandled exception occurred!',
        plain_text_content=email_text,
    )
