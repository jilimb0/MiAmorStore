import random

from django.http import HttpResponse
from django.template.loader import get_template

quotes = ['No hay invierno que sea para siempre', 'Amor me llena de sol','Querer te fue mi error y ahora lo sé',
'Camino se hace al andar','Hello my name is future','Cuando llueva busca arcoíris','Cuando oscurezca busca estrellas',
'Live, work, create', 'Joy comes in the morning','The best is yet to come ? Lo mejor está por venir','The future is unwritten ?',
'Confía en la magia de los nuevos comienzos','No soy agresiva soy directa','La confianza en si mismo es el primer secreto del éxito',
'No hay nada imposible', 'Eres TÚ quien debe cambiar las cosas', 'Hombre sin sonrisa no abre tienda',
'Si el plan no funciona cambia el plan pero no cambies la meta','Después de la tormenta llega la idea',
'Todo logro empieza de la decisión de intentarlo','Vengo a robar tu corazoncito', 'Ds lo mejor de ti y lo mejor vendrá',
'Tu único límite es tu mente', 'Go up and never stop', 'F.U. virus','La felicidad no existe.','Lo único que existe es el deseo de ser feliz’',
'Donde hay mucho amor, hay muchos errores. Donde no hay amor, todo es error','Планете необходимо глобальное потепление сердец',
'Забей и поспи', 'There is no friend as loyal as a book',"I love sleep. My life has the tendency to fall apart when I'm awake, you know?",
'The first draft of anything is shit','I drink to make other people more interesting',"You can't get away from yourself by moving from one place to another",
'My aim is to put down on paper what I see and what I feel in the best and simplest way', 'Mi paz mental no tiene precio',
'No gastes energías en cosas que no suman', 'Hazlo, y si te da miedo, hazlo con miedo', 'Si la vida te da limones pide sal y tequila',
'El que piensa positivo ve lo invisible']

def index(request):
    t = get_template('mainApp/homePage.html')
    c = {
        'quote': quotes[random.randint(1, len(quotes) - 1)]
    }

    return HttpResponse(t.render(c, request))


def tshirts(request):
    ts = get_template('mainApp/t-shirts.html')
    return HttpResponse(ts.render({}, request))


def shoppers(request):
    sh = get_template('mainApp/shoppers.html')
    return HttpResponse(sh.render({}, request))

def sweatshirts(request):
    b = get_template('mainApp/sweatshirts.html')
    return HttpResponse(b.render({}, request))


def notes(request):
    n = get_template('mainApp/notes.html')
    return HttpResponse(n.render({}, request))


def stickers(request):
    st = get_template('mainApp/stickers.html')
    return HttpResponse(st.render({}, request))


def constructor(request):
    c = get_template('mainApp/constructor.html')
    return HttpResponse(c.render({}, request))


def login(request):
    si = get_template('mainApp/login.html')
    return HttpResponse(si.render({}, request))