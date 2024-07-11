from http import HTTPStatus

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import select

from fast_zero.models import User
from fast_zero.schemas import UserSchema, UserPublic, UserList
from fast_zero.database import get_session


app = FastAPI()


@app.get('/')
def read_root():
    return 'é nóis!'


@app.post('/users/', response_model=UserPublic, status_code=HTTPStatus.CREATED)
def create_user(user: UserSchema):
    session = get_session()
    # Verifica se já existe username ou email cadastrados no banco
    # e sobe erro caso positivo
    db_user = session.scalar(select(User).where(
        (User.username == user.username) |
        (User.email == user.email)))
    if db_user:
        if db_user.username == user.username:
            raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                                detail='Usuário já cadastrado!')
        elif db_user.email == user.email:
            raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                                detail='E-mail já cadastrado!')
    # casso não existirem salva no banco e retorna OK
    db_user = User(
        username=user.username,
        email=user.email,
        password=user.password)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

# --- Lista todos os usuários
@app.get('/users/', response_model=UserList)
def read_users(session = Depends(get_session)):

    user = session.scalars(select(User))
    return {'users': user}