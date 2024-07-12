from fastapi import FastAPI, Request
from pydantic import BaseModel
from jinja2 import Environment, FileSystemLoader
from fastapi.responses import HTMLResponse
import markdown as md
import uvicorn


class RequestModel(BaseModel):
    markdown: str


app = FastAPI()
jinja_env = Environment(loader=FileSystemLoader("Templates"))
jinja_template = jinja_env.get_template("blog")
@app.get("/convert/", response_class=HTMLResponse)
async def convert():
    str =  "# hello everyone\ntoday we are gonna **discuss**.\n- so first of all, the first step\n> please note: be careful"
    html = md.markdown(str, output_format='html')
    return jinja_template.render(blog=html)


# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)