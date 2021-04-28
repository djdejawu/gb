from suburbicon.main import Framework
from urls import routes, fronts
from wsgiref.simple_server import make_server


port = 8000
app = Framework(routes, fronts)

with make_server('', port, app) as wsgi:
    print("Server started at port " + str(port))
    wsgi.serve_forever()
