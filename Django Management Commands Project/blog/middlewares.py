from django.utils.deprecation import MiddlewareMixin


class CustomHeaderMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.META['HTTP_TOKEN'] = "invalid_token"
