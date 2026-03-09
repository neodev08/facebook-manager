import os
from dotenv import load_dotenv

load_dotenv()

FACEBOOK_APP_ID_= os.getenv("FACEBOOK_APP_ID")
FACEBOOK_APP_SECRET = os.getenv("FACEBOOK_APP_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")