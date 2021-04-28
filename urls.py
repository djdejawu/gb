from datetime import date
from views import *


def secret_front(request):
    request['data'] = date.today()


def other_key(request):
    request['key'] = 'key'


def other_front(request):
    request['data'] = 'data'


fronts = [secret_front, other_front]

routes = {
    '/': Index(),
    '/about/': About(),
    '/login': AccessDenied(),
    '/404': NotFound()
}
