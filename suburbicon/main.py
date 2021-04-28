from urls import *
import quopri


# class NotFound:
#    def __call__(self, request):
#        return '404 WHAT', '404 PAGE Not Found'


class Framework:
    def __init__(self, routes_obj, fronts_obj):
        self.routes_list = routes_obj
        self.fronts_list = fronts_obj

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        print(path)
        if path is '/login':
            view = AccessDenied()
        if not path.endswith('/'):
            path = f'{path}/'
        if path in self.routes_list:
            view = self.routes_list[path]
        else:
            view = NotFound()
        request = {}

        for front in self.fronts_list:
            front(request)
        code, body = view(request)
        start_response(code, [('Content-type', 'text/html')])
        return [body.encode('UTF-8')]

    @staticmethod
    def decode_value(data):
        new_data = {}
        for k, v in data.items():
            val = bytes(v.replace('%', '=').replace('+', ' '), 'UTF-8')
            val_decode_str = quopri.decodestring(val).decode('UTF-8')
            new_data[k] = val_decode_str
        return new_data
