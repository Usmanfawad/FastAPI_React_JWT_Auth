from fastapi import Body, status, Depends



from .config import *
from .models import *
from .schemas import *

from .auth_handler import signJWT
from .auth_bearer import JWTBearer

from sqlalchemy.orm import Session


users = []
posts = []

#Helper function to log user in!
def check_user(data: UserLoginSchema):
    for user in users:
        if user.username == data.username and user.password == data.password:
            return True
    return False


@app.post("/posts", dependencies=[Depends(JWTBearer())], tags=["posts"])
async def add_post(post: PostSchema) -> dict:
    print("blabla")
    return {
        "data": "post added."
    }

@app.post("/")
async def root():
    return "haha"

@app.post("/user/signup", tags=["user"])
async def create_user(user: UserSchema = Body(...)):
    users.append(user) # replace with db call, making sure to hash the password first
    print(users)
    return signJWT(user.username)

@app.post("/user/login", tags=["user"])
async def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.username)
    return {
        "error": "Wrong login details!"
    }
