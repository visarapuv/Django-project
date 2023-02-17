# pages/views.py
from django.http import HttpResponse
import json

def homePageView(request):
    data = {
        "Message" : "Hello World!"
    }
    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')