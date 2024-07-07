from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.schemas import UserPublic, UserSchema

app = FastAPI()


@app.get('/')
def read_root():
    return 'é nóis!'


@app.post('/users/', response_model=UserPublic, status_code=HTTPStatus.CREATED)
def create_user(user: UserSchema):
    # faz as validações (consulta no banco de o username e email já existem)
    # casso não existirem salva no banco e retorna OK
    return user
