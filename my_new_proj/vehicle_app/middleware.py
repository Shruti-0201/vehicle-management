from django.http import HttpResponseForbidden

ALLOWED_IPS = ['127.0.0.1']  # Replace with allowed IPs

class IPFilterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        if ip not in ALLOWED_IPS:
            return HttpResponseForbidden("Access Denied: IP not allowed")
        return self.get_response(request)
