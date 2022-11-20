from fastapi import Depends
from code.access_token import oauth2_scheme, get_current_user
from datetime import datetime


def get_current_time(token: str = Depends(oauth2_scheme)):
    if get_current_user(token):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return {"Current time": current_time}
