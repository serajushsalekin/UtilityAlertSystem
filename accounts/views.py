from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from .forms import SignupForm, LoginForm
from twilio.rest import Client
from accounts.models import UserProfile


@login_required(login_url='login')
@user_passes_test(lambda u: u.is_admin, reverse_lazy('login'))
def index(request):
    account_sid = 'AC78832fb6055c441b66f50ceb1a17ab6f'
    auth_token = '1390569b6e2fdc3a8cc9e6cb728d2a51'
    client = Client(account_sid, auth_token)
    sid = None
    if request.method == "POST":
        msg = request.POST.get('body')
        postal_code = request.POST.get('code')
        user = UserProfile.objects.filter(postal_code=postal_code)
        print(user)
        try:
            for user_num in user:
                print(user_num.phone)
                message = client.messages.create(
                    body=msg,
                    from_='+14758897597',
                    # to='+8801756870767'
                    to=user_num.phone
                )

                print(message.sid)
                sid = message.sid
        except:
            return HttpResponse("<h3 style=\"text-align: center\">Someting went wrong!<br>Message didn't sent<h3>")
    context = {
        'message_id': sid
    }
    return render(request, 'master.html', context)


class Signup(CreateView):
    template_name = 'accounts/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('login')


# class Login(LoginView):
#     template_name = 'accounts/login.html'
#     form_class = LoginForm
#
#     def get(self, request, *args, **kwargs):
#         if self.request.user.is_authenticated and self.request.user.is_staff:
#             return redirect('{}'.format(self.request.GET.get('next', 'home')))
#
#         return super(Login, self).get(request, *args, **kwargs)
@login_required(login_url='login')
@user_passes_test(lambda u: u.is_admin, reverse_lazy('login'))
def tem(request):
    users = UserProfile.objects.all()
    return render(request, 'index.html', {'users': users})


@login_required(login_url='login')
@user_passes_test(lambda u: u.is_admin, reverse_lazy('login'))
def sms_list(request):
    return render(request, 'sms.html', {})


class Login(FormView):
    template_name = 'accounts/login.html'
    form_class = LoginForm

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        print(email)
        password = form.cleaned_data.get('password')
        is_staff = form.cleaned_data.get('is_staff')
        # print(is_staff)
        is_admin = form.cleaned_data.get('is_admin')
        # print(is_admin)
        request = self.request
        user = authenticate(request, username=email, password=password)
        # if user is not None:
        #     login(request, user)
        #     return redirect('home')
        #         staff = authenticate(request, username=email, password=password)
        #         admin = authenticate(request, username=email, password=password)
        if user is not None:
            print('staff: '+str(user.is_staff))
            print('admin: '+str(user.is_admin))
            print(user.is_active)
            if user.is_active and not user.is_admin:
                login(request, user)
                # return redirect('home')
                raise Http404
            elif user.is_admin and user.is_staff and user.is_active:
                login(request, user)
                # return render(request, 'admin/index.html', {})
                return redirect('home')
            else:
                return HttpResponse('wrong idea to login!')

        return super(Login, self).form_invalid(form)


@login_required(login_url='login')
@user_passes_test(lambda u: u.is_admin, reverse_lazy('login'))
def users(request):
    user_profile = UserProfile.objects.all()

    context = {
        'users': user_profile
    }
    return render(request, 'accounts/usrs.html', context)


@login_required(login_url='login')
@user_passes_test(lambda u: u.is_admin, reverse_lazy('login'))
def search(request):
    q = request.GET.get('q', None)
    user = None
    if q is not None:
        user = UserProfile.objects.filter(postal_code=q)
    context = {
        'person': user
    }
    return render(request, 'searcch.html', context)
