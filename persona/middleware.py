from django.http import JsonResponse
import traceback

class CustomExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        response_data = {
            "error": True,
            "description": str(exception),
            "trace": traceback.format_exc()
        }
        return JsonResponse(response_data, status=500)
