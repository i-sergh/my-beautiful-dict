from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, text

import asyncio

from dbengine import async_session_macker
from users.model import Users

async def test_connection():
    async with async_session_macker() as session:
        
        print(session)
        query = select(Users.__table__)
        print(query)
        result = await session.execute(query)
        print([list(val) for val in result.all()])

asyncio.run(test_connection())
