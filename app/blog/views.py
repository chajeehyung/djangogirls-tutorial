from django.utils import timezone

from django.http import HttpResponse

# Create your views here.

def post_list(request):
    current_time = timezone.now()

    return HttpResponse(
        '<html>'
        '<body>'
        '<h1>Post list</h1>'
        '<p>{}</p>'
        '</body>'
        '</html>'.format(
            current_time.strftime('%y. %m. %d<br>%H:%M:%S')
        )

    )