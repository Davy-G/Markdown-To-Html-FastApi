from fastapi import FastAPI, Request
from pydantic import BaseModel
from jinja2 import Environment, FileSystemLoader
import markdown as md
import uvicorn


class RequestModel(BaseModel):
    markdown: str


app = FastAPI()
jinja_env = Environment(loader=FileSystemLoader("Templates"))
jinja_template = jinja_env.get_template("blog")
@app.post("/convert/")
async def convert(markdown: RequestModel):
    html = md.markdown(markdown.markdown)
    return jinja_template.render(blog=html)


# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)