from fastapi import FastAPI, Response
from random import randint
from time import asctime
from users.router import router as users_router

app = FastAPI(
    title = 'Dict'
    )

app.include_router(users_router)

@app.get('/')
async def start_page():
    return {'ping': 'now cc'}



@app.get('/new_word')
async def get_new_word(word:str='', translation:str='', explanation:str='', interpretation:str=''):

    return {"response":"success",
            "word": word,
            "translation": translation,
            "explanation":explanation,
            "interpretation":interpretation
            }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=80, reload=True)
