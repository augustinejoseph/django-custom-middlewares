from django.urls import reverse

class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Incoming request.............")
        return self.get_response(request)
    

class ForceLoginMiddleware:
    def __init__(self, request):
        self.request = request
    
    def __call__(self, request):
        if not request.user.is_authenticated and request.path != reverse('login'):
            return reverse('login')
        else:
            return(self.request(request))