from pydantic import BaseModel

# Create ToDoRequest Base Model
class UserRequest(BaseModel):
    username: str
    password: str

    