import random

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


# Create your views here.

def post_list(request):
    # templates = loader.get_template('blog/post_list.html')
    # context = {
    #     'pokemon' : random.choice('피카츄','꼬부기')
    # }
    # content = templates.render(context, request)
    # return HttpResponse(content)

    context = {
        'pokemon': random.choice('피카츄', '꼬부기')
    }

    return render(
        request = request,
        template_name = 'blog/post_list.html',
        context = context,
    )