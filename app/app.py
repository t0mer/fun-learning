import os, json, requests, uvicorn, time, socket, re
from urllib.parse import urlparse
from os import environ, path
from loguru import logger
from card import RfIdCard
from fastapi import FastAPI, Request, File, Form, UploadFile
from pydantic import BaseModel
from fastapi.responses import UJSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from starlette.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from starlette_exporter import PrometheusMiddleware, handle_metrics
from sqliteconnector import SqliteConnector



tag_id = ""


app = FastAPI(title="Tag Server", description="Manage RFId Tags", version="1.0.0")
logger.info("Configuring app")
app.mount("/dist", StaticFiles(directory="dist"), name="dist")
app.mount("/js", StaticFiles(directory="dist/js"), name="js")
app.mount("/css", StaticFiles(directory="dist/css"), name="css")
templates = Jinja2Templates(directory="templates/")
app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", handle_metrics)
db = SqliteConnector()


origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.get("/tag/bind")
def teach(request: Request):
    try:
        return templates.TemplateResponse('bind.html', context={'request': request, 'version':"1.0.0"})
    except Exception as e:
        logger.error(str(e))

@app.post("/api/tag/bind")
async def bind_new_tag(request:Request):
    global tag_id
    data = await request.json()
    CardId = data["tagid"]
    HebrewLetterId = data["heb"]
    EnglishLetterId = data["eng"]
    NumberId = data["math"]
    try:
        if not all ([CardId,HebrewLetterId,EnglishLetterId,NumberId]):
            raise Exception("CardId, HebrewLetterId, EnglishLetterId or NumberId are empty, please validate")

        card = RfIdCard(CardId=CardId,HebrewLetterId=HebrewLetterId,EnglishLetterId=EnglishLetterId,NumberId=NumberId)
        result, message = db.add_new_card(card)
        logger.debug(message)
        if result:
                return JSONResponse(status_code=200, content = json.loads('{"message":"'+ message +'","success":"true"}'))
        else:
            return JSONResponse(status_code=400, content = json.loads('{"message":"'+ message +'","success":"false"}'))
    except Exception as e:
        logger.error(str(e))
        return JSONResponse(status_code=400, content = json.loads('{"message":"'+ str(e) +'","success":"false"}'))
    finally:
        tag_id = ""

@app.get("/api/tag/scan")
def get_new_tag(request: Request):
    global tag_id
    try:
        if tag_id:
            
            return JSONResponse(status_code=200, content = json.loads('{"tag_id":"'+ tag_id +'","success":"true"}'))
        else:
            return JSONResponse(status_code=200, content = json.loads('{"tag_id":"'+ tag_id +'","success":"false"}'))
    except Exception as e:
        logger.error(str(e))
        return JSONResponse(status_code=500, content = json.loads('{"message":"'+ str(e) +'","success":"false"}'))

@app.get("/api/tag/clear")
def clear_tag(request: Request):
    """
    Clear the current tag Id (Reset).
    """
    global tag_id
    try:
        tag_id =""
    except Exception as e:
        logger.error(str(e))
        return "0"

@app.get("/api/tag/read")
def preview(request: Request, Id : str =""):
    """
    Scan for new tags
    """
    global tag_id
    try:
        tag_id = Id
        logger.info("Authorized")
        return 1
    except Exception as e:
        logger.error(str(e))
        return 0
        # return JSONResponse(content = '{"image_url":"error.png","success":"false"}')


@app.get("/api/hebrewletters")
def get_hebrew_letters(request: Request):
    try:
        return JSONResponse(status_code=200, content=db.get_hebrew_letters(True))
    except Exception as e:
        logger.error(str(e))
        return JSONResponse(status_code=400, content = json.loads('{"message":"'+ str(e) +'","success":"false"}'))

@app.get("/api/englishletters")
def get_hebrew_letters(request: Request):
    try:
        return JSONResponse(status_code=200, content=db.get_english_letters(True))
    except Exception as e:
        logger.error(str(e))
        return JSONResponse(status_code=400, content = json.loads('{"message":"'+ str(e) +'","success":"false"}'))

@app.get("/api/numbers")
def get_hebrew_letters(request: Request):
    try:
        return JSONResponse(status_code=200, content=db.get_numbers(True))
    except Exception as e:
        logger.error(str(e))
        return JSONResponse(status_code=400, content = json.loads('{"message":"'+ str(e) +'","success":"false"}'))



@app.get("/api/tags")
def get_tags(request: Request):
    try:
        return JSONResponse(status_code=200, content=db.get_cards(True))
    except Exception as e:
        logger.error(str(e))
        return JSONResponse(status_code=400, content = json.loads('{"message":"'+ str(e) +'","success":"false"}'))


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8087)


# analayze



