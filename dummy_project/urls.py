from django.urls import path
from django.views.generic import TemplateView

import time
def timestamp():
    return str(int(time.time()*100)%10000/100)

urlpatterns = [
    path('', TemplateView.as_view(
        template_name='index.html',
        extra_context=dict(timestamp=timestamp),
    )),
    path('form_post_and_go_back/', TemplateView.as_view(template_name='form_post_and_go_back.html')),
    path('manual_invalidate_and_go_back/', TemplateView.as_view(template_name='manual_invalidate_and_go_back.html')),
    path('form_post_and_close/', TemplateView.as_view(template_name='form_post_and_close.html')),
]
