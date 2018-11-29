from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
#from django.contrib.auth.auth_views import LoginView

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['eruditus.d@gmail.com'],
            )
            return HttpResponseRedirect('/contact/thanks')
    else:
        form = ContactForm()
    return render(request, 'contactApp/contact_form.html',
        {'form': form,
        'contactActive': True})

#def LoginView():


        