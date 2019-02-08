from django.shortcuts import render_to_response,get_object_or_404,render,redirect
from django.contrib import auth 
from .form import login_form
from django.urls import reverse


def home_introduce(request):
    content={}
    return render_to_response('firweb_home.html',content)


def login(request):
    # username=request.POST.get('username','')
    # password=request.POST.get('password','')
    # user = auth.authenticate(request, username=username, password=password)
    # if user is not None:
    #     auth.login(request, user)
    #     return redirect('/')
    # else:
    #     return render(request,'error.html',{'message':'用户或密码错误'})
    if request.method == 'POST':
        loginform = login_form(request.POST)
        if loginform.is_valid():
               user = loginform.cleaned_data['user']
               auth.login(request, user)
               return redirect(request.GET.get('from',reverse('home')))
    else:
        loginform = login_form()
    content = {}
    content['loginform'] = loginform
    return render(request,'login.html',content)