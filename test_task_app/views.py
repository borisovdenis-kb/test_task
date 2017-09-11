from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import auth
from django.contrib.auth.models import Group
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response
from rest_framework.authentication import SessionAuthentication


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


def registration(request):
    context = {
        "incorrect_gp_name": False,
    }
    if request.method == 'POST':
        data = request.POST
        form = UserCreationForm(data)

        if form.is_valid():
            try:
                group = Group.objects.get(name=data['groupname'])
            except ObjectDoesNotExist:
                context['incorrect_gp_name'] = True
                return render_to_response("registration_page.html", context)
            else:
                new_user = form.save()
                group.user_set.add(new_user)

            return HttpResponseRedirect("/login")
        else:
            context['errors'] = form.errors.as_data()
            return render_to_response("registration_page.html", context)
    else:
        return render_to_response('registration_page.html')


def login(request):
    context = {
        "login_error": False
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect("/")
            else:
                return HttpResponse(status=403)
        else:
            context['login_error'] = True
            return render_to_response('login_page.html', context)
    else:
        return render_to_response('login_page.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login")


def home(request):
    if request.user.is_authenticated():
        context = {
            "user": request.user,
            "gp_name": request.user.groups.get().name
        }
        return render_to_response('home_page.html', context)
    else:
        return HttpResponseRedirect('/login')
