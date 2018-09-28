from django.template import loader
from django.http import HttpResponse


# Create your views here.

def post_list(request):
    templates = loader.get_template('blog/post_list.html')
    context = {}
    content = templates.render(context, request)
    return HttpResponse(content)