from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert

from typing import Annotated

from fastapi import APIRouter, Depends, Response

from dbengine import get_async_session
from users.schemas import NewUser
#from models import Users

router = APIRouter(
    prefix='/user',
    tags=['user']
)

@router.post('/new-user')
async def register_new_user(payload: Annotated[NewUser, Depends()], session: AsyncSession=Depends(get_async_session)):
    #query = insert()
    print(payload)
    #new_user = Users(**payload.model_dump())
    #print(new_user)
    return  Response(content={'code':200, 'result':'success' })