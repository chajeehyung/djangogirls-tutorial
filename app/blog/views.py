import random
import re
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Post


# Create your views here.

def post_list(request):
    # templates = loader.get_template('blog/post_list.html')
    # context = {
    #     'pokemon' : random.choice('피카츄','꼬부기')
    # }
    # content = templates.render(context, request)
    # return HttpResponse(content)
    posts = Post.objects.order_by('-created_date')


    context = {
        'posts': posts,

    }
    return render(
        request,
        'blog/post_list.html',
        context,
    )

def post_detail(request, pk):
    # m = re.search(r'^/posts/(?P<pk>\d+)/$', request.path)
    # pk = m.group('pk')
    # request.path 에 있는 문자열을
    # /posts/12345/
    # /posts/3/
    # 위의 정규표현식을 적절히
    # 12345와 3문자열을 추출
    # 추출한 결과를 HttpResponse에 리턴
    post = Post.objects.get(id=pk)

    context = {
        'post':post
    }

    return render(
        request,
        'blog/post_detail.html',
        context,
    )

    # return HttpResponse(post.title)