from django.shortcuts import render

from .forms import ConvertURL

def convert(request):
    """
    Convert submitted string to URL encoding
    """

    if request.method == 'POST':
        form = ConvertURLForm(
