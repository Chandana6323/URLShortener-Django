from django.shortcuts import render, redirect
from .models import URL
import random
import string


def generate_code():
    return ''.join(
        random.choices(
            string.ascii_letters + string.digits,
            k=6
        )
    )


def home(request):

    short_url = None

    if request.method == 'POST':

        original_url = request.POST.get('url')

        code = generate_code()

        URL.objects.create(
            original_url=original_url,
            short_code=code
        )

        short_url = request.build_absolute_uri(code)

    return render(
        request,
        'index.html',
        {'short_url': short_url}
    )


def redirect_url(request, code):

    url = URL.objects.get(short_code=code)

    return redirect(url.original_url)