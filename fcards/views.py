from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from fcards.forms import SignUpForm


@login_required(login_url='/accounts/login/')
def index(request):
    return HttpResponse('Hi there')

def signup(request):
    print('here')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)

            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration_form.html', {'form': form})

