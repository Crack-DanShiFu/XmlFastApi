import os
import uvicorn
from starlette.responses import Response, HTMLResponse, JSONResponse, RedirectResponse
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def index():
    return RedirectResponse('/getXml')


@app.get('/getXml/{file_path:path}')
async def getXml(file_path: str):
    if 'static' not in file_path:
        file_path = 'static'
    if os.path.exists(file_path):
        if os.path.isfile(file_path):
            return Response(open(file_path).read())
        ls = os.listdir(file_path)
        htmlContent = ''
        for l in ls:
            htmlContent += '<p><a href="' + file_path.split('/')[-1] + '/' + l + '">' + str(l) + '</a></p>'
        return HTMLResponse(htmlContent)
    return '路径错误'


@app.get('/getXmlList/{file_path:path}')
async def getXmlList(file_path: str):
    if os.path.exists(file_path) and not os.path.isfile(file_path):
        return os.listdir(file_path)
    return []

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, debug=True)
