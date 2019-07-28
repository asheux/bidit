from django.http import HttpResponseForbidden
import pdb

class FilterHostsMiddleware:
    def __init__(self, process_request):
        self.process_request = process_request

    def __call__(self, request):
        return self.process_request(request)

    def process_request(self, request):
        allow_hosts = ['localhost', '127.0.0.1']
        host = request.get_host()
        pdb.set_trace()

        if host[len(host) - 9:] == 'bidit.com':
            allow_hosts.append(host)
        elif host[:7] == '192.168':
            allow_hosts.append(host)
        if host not in allow_hosts:
            return HttpResponseForbidden

        return None

