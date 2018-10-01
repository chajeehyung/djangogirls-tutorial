import random
import re
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

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
def post_create(request):
    # Template : blog/post_create.html
    # URL: /posts/create/
    # URL NAME : post-create

    # 1. 템플릿에 하나의 <form>요소 구현
    #     input[name = 'title']
    #     textarea[name='title']
    #     button[type='submit']
    # 2. post_create.html을 보여주는 링크를 base.html에 구현
    #     {% url 태그를 사용할 것%}
    # :pram request
    # :return
    if request.method == 'POST':
        # Post 요청이 왔을경우
        # 새글을 작성하고 원하는 페이지로 돌아가도록 함
        # HttpResponse를 돌려줌
        # 제목: <제목데이터><br>내용: <내 데이터>용
        # 위 문자열을 가지고 response돌려주기
        title = request.POST['title']
        text = request.POST['text']

        # object.create() 메서드를 사용해서
        # 새 Post 객체를 생성하며 db에 저장 (create() 실행의 반환값은 'post' 변수에 할)
        # title, text는 request.POST에서 가져온 내용
        # author는 request.user
        # 리턴하는 결과는 같은 문자열이지만,
        # 문자열을 생성할때 만들어진 Post 객체('post변수')의 title속성, text 속성을 사용
        post = Post.objects.create(
            author = request.user,
            title = title,
            text = text,
        )
        next_path = reverse('post-list')
        # next_path = '/blog-posts/'
        # return HttpResponseRedirect(next_path)
        return  redirect('post-list')
    else:
        return render(request,'blog/post_create.html')