from suburbicon.templater import render


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', data=request.get('data', None))


class NotFound:
    def __call__(self, request):
        return '404 Not found', '404 Page Not Found'


class AccessDenied:
    def __call__(self, request):
        return '403 Forbiden', '403 Access Denied'


class About:
    def __call__(self, request):
        return '200 OK', 'about' #render('about.html', data=request.get('key', None))

class InternalError:
    def __call__(self, request):
        return '500 Internal Server Error', '500 Internal Server Error'