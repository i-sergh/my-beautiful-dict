from fastapi import FastAPI, Response
from random import randint
from time import asctime

app = FastAPI(
    title = 'Dict'
    )


@app.get('/')
async def start_page():
    return {'ping': 'now cc'}

@app.post('/create-new-user')
def create_new_user(new_user_data):

    return Response(content={'code':200, 'result':'success', 'new_user':'new_user_data' })


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
