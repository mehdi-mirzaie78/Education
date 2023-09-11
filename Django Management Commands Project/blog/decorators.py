from django.shortcuts import redirect


class AuthenticationRequired:
    def __init__(self, function, redirect_url='home'):
        self.function = function
        self.redirect_url = redirect_url

    def __call__(self, *args, **kwargs):
        request = args[0]
        if request.META.get("HTTP_TOKEN") == 'valid_token':
            return self.function(*args, **kwargs)
        return redirect(self.redirect_url)
