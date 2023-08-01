from django.shortcuts import render
from django.conf.urls.i18n import i18n_patterns
from django.urls import include, path
from django.utils.translation import gettext_lazy as _, activate, get_language
def login_view(request):
    trans = translate(language='vi')


    if request.user.is_authenticated:
        return redirect('home')

    # Otherwise, render the login template
    return render(request, 'login.html')

def translate(language):
    cur_language = get_language()
    try:
        activate(language)
        text = _('Login')
    finally:
        activate(cur_language)
    return text

