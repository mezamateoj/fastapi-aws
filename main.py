from fastapi import FastAPI
import uvicorn

from my_lib.logic import wiki, search_wiki, phrase

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Wiki Api. Call /search or /article or /summary"}


@app.get("/search/{value}")
async def search(value: str):
    """Search a title article on wikipedia"""

    values = search_wiki(value)
    return {"Wiki results": values}


@app.get("/article/{title}")
async def get_article(title: str):
    """Search an article on wikipedia based on title"""

    article = wiki(title)
    return {"article": article}


@app.get("/summary/{title}")
async def get_phrases(title: str):
    """Search an article on wikipedia based on title
    returns: all the phrases on the article and the article
    """

    article_phrases = phrase(title)
    return {"article summary": article_phrases}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
