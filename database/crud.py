from sqlalchemy.orm import Session
from models.model import User
from authentication.hashing import checkPassword
from .schema import (User as user_table, Products as product_table , Cart as cart_table)





async def does_email_exist(email:str, db:Session):
    result = db.query(user_table).filter(user_table.email == email).first()

    if result:return True



async def create_user(user:User,db:Session, verify_id:str):
    from controller.hex import generate_hex
    from authentication.hashing import hashPassword

    new_user =user_table(user_id=generate_hex(6),fullname=user.fullname,email=user.email,\
    
    password=hashPassword(user.password), id_verify=verify_id)

    db.add(new_user)

    db.commit()

    db.refresh(new_user)


async def auth_user(email:str, password:str, db:Session):
    user:user_table =  db.query(user_table).filter(user_table.email == email).first()

    if checkPassword(password, user.password):return True


async def is_user_verified(email:str, db:Session):
    user:user_table =  db.query(user_table).filter(user_table.email == email).first()

    return user.is_verified
