from pydantic import BaseModel

# Create ToDoRequest Base Model
class UserSchema(BaseModel):
    username: str
    password: str



class UserLoginSchema(BaseModel):
    username: str 
    password: str 


class PostSchema(BaseModel):
    content: str