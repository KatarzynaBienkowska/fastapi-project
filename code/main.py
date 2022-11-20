from fastapi import FastAPI, File, UploadFile, Depends
from fastapi.responses import StreamingResponse
from fastapi.security import OAuth2PasswordRequestForm

from code.prime import is_prime as is_prime_result
from code.picture_invert import invert_picture as inverted_picture
from code.access_token import Token, oauth2_scheme
from code.access_token import login_for_access_token as oauth_login
from code.get_time import get_current_time as time_result


app = FastAPI()


@app.get("/prime/{number}")
def is_prime(number: int):
    return is_prime_result(number)


@app.post("/picture/invert")
def invert_picture(file: UploadFile = File(...)):
    return StreamingResponse(inverted_picture(file), media_type="image/jpeg")


@app.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    return oauth_login(form_data)


@app.get("/time")
def get_current_time(token: str = Depends(oauth2_scheme)):
    return time_result(token)
