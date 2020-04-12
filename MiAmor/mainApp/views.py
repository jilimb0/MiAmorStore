import random
from django.http import HttpResponse
from django.template.loader import get_template

quotes = ['Dont worry', 'Be happy', 'Smile', 'In every moment, remember', 'Somebody is love you']


def index(request):
    t = get_template('mainApp/homePage.html')
    c = {
        'quote': quotes[random.randint(1, len(quotes) - 1)]
    }

    return HttpResponse(t.render(c, request))
