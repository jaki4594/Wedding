from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template("zaki_wedding/index.html")
    # return HttpResponse("Hello, world. You're at the polls index.")
    context = {
        "latest_question_list": '',
    }
    return HttpResponse(template.render(context,request))