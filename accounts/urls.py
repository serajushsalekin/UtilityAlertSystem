from django.conf.urls import url
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from .views import Signup, Login

urlpatterns = [
    # url(r'^login/$', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
    url(r'^signup/$', Signup.as_view(), name='signup'),
]
