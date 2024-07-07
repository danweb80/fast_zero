from fastapi import FastAPI
from fast_zero.schemas import UserSchema, UserPublic
from http import HTTPStatus

app = FastAPI()

@app.get('/')
def read_root():
    return 'Coelhinho peludo!'

@app.post('/users/', response_model=UserPublic, status_code=HTTPStatus.CREATED)
def create_user(user: UserSchema):
    return user