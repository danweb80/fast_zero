from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return 'é nóis!'


@app.post('/users/', response_model=UserPublic, status_code=HTTPStatus.CREATED)
def create_user(user: UserSchema):
    engine = create_engine()
    with Session as session:
        db_user = session.scalar(
            select(User.where(User.username == user.username |
                              User.email == user.email))
        if (db_user):
            if (db_user.username == user.username):
                raise HTTPException(statuscode=HTTPStatus.BAD_REQUEST,
                                    detail='Usuário já cadastrado')
            elif (db_user.email == user.email):
                raise HTTPException(statuscode=HTTPStatus.BAD_REQUEST,
                                    detail='E-mail já cadastrado')
        # casso não existirem salva no banco e retorna OK
        db_user = User()
        return user
