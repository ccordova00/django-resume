from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import datetime

from .forms import LoginForm

@login_required
def dashboard(request):
    return render(request,
                  'dashboard.html',
                  {'section':'dashboard'})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(request,
                                username = cleaned_data['username'],
                                password = cleaned_data['password']
                                )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated '\
                                        'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request,
                  'login.html',
                  {'form':form})


def home_view(request):
    return render(request,
           'home.html',
           {'home_active': True})

def current_datetime(request):
    now = datetime.datetime.now()
    ''' old way
    t = get_template('current_datetime.html')
    html = t.render({'current_date':now})
    return HttpResponse(html)
    '''
    return render(request,
                  'current_datetime.html',
                  {'current_date': now,
                   'home_active': True})
    

def hours_ahead(request, offset): # offset is passed in from the url 
                                  # ie. /time/plus/12/
    # don't assume it's coming from a url
    try:                    
        offset = int(offset)
    except ValueError:
        raise Http404()

    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "In %s hour(s), it will be %s." % (offset, dt)
    return HttpResponse(html)

def show_meta(request):
    meta_items = request.META.items()
    meta_items = sorted(meta_items)
    
    return render(request,
                  'show_meta.html',
                  {'meta_items': meta_items})

def show_ip(request):
    remote_ip = request.META.get('REMOTE_ADDR', 'unknown')
    html = "Your IP is %s" % remote_ip
    return HttpResponse(html)
