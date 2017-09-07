from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth.models import Group
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import UserCreationForm


def registration(request):
    if request.method == 'POST':
        data = request.POST
        form = UserCreationForm(data)

        if form.is_valid():
            # создаем и добавляем пользователя в нужную группу
            try:
                group = Group.objects.get(name=data['groupname'])
            except ObjectDoesNotExist:
                return HttpResponse(status=400)
            else:
                new_user = form.save()
                group.user_set.add(new_user)

            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)
    else:
        return HttpResponse(status=405)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return HttpResponse(status=200)
            else:
                return HttpResponse(status=403)
        else:
            return HttpResponse(status=400)
    else:
        return HttpResponse(status=405)


def logout(request):
    auth.logout(request)
    return HttpResponse(status=200)
