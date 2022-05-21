from fastapi import APIRouter,Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

index_route = APIRouter()
templates = Jinja2Templates(directory="resource/template/")

@index_route.get("/",response_class=HTMLResponse)
async def get_index_page(request: Request):
    """
    return index page
    """

    return templates.TemplateResponse("index.html", {"request": request})