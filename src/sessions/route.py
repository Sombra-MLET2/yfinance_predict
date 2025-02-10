from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette.exceptions import HTTPException
from starlette.responses import JSONResponse
from dtos.session_dto import Token, User
from infra.database import get_db
from infra.loggers import logger
from sessions.create_token import create_access_token
from sessions.create_user import create_user
from sessions.find_user import find_user
from sessions.password_hash import verify_password

sessions_router = APIRouter(
    prefix="/sessions",
    tags=["sessions"],
    responses={401: {"description": "Invalid credentials"},
               500: {"description": "Internal server error"}}
)


@sessions_router.post("/")
async def add_user(user: User, db: Session = Depends(get_db)):
    logger.info(f'Creating user {user.email}')
    user_created = create_user(user, db)
    if not user_created:
        return JSONResponse(status_code=409, content={'message': f'User {user.email} already exists'})
    return JSONResponse(status_code=201, content={})


@sessions_router.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    logger.info(f'Login attempt by {form_data.username}')
    user_db = find_user(db, form_data.username)
    if user_db is None or not verify_password(form_data.password, user_db.hashed_password):
        logger.warning(f'Login failed for user {form_data.username}')
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token({'sub': user_db.email})
    return Token(access_token=access_token,
                 token_type="bearer")


@sessions_router.post("/api-token")
async def login_api(user: User, db: Session = Depends(get_db)):
    logger.info(f'Login attempt by {user.email}')
    user_db = find_user(db, user.email)
    if user_db is None or not verify_password(user.password, user_db.hashed_password):
        logger.warning(f'Login failed for user {user.email}')
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token({'sub': user_db.email})
    return Token(access_token=access_token,
                 token_type="bearer")
