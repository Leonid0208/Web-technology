  
def application(environ, start_response):
    # for i in environ['QUERY_STRING']:
    if environ['QUERY_STRING']:
        s = str(environ['QUERY_STRING']).split('&')
        data = bytes('\n'.join(s), encoding='utf8')
    else:
        data = b''
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ]
    start_response(status, response_headers)
    return iter([data])
