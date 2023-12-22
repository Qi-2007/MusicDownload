from flaskSystem.App import app
from flaskSystem.App import c
@app.post("/common/getHttp")
def getHttpResponse():
    return {
        'code': 200,
        'list': [],
        'locate':c.get_folder(),
        'threadNumber':c.getCurrentResize(),
        'page': 1
    }


def init():
    pass
