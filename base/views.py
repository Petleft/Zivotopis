from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Room, typprace, Message
from .forms import RoomForm

#Login page setup
def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('Domovskástránka')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Tento uživatel neexistuje!!')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Domovskástránka')
        else:
            messages.error(request, "Uživatel neexistuje, nebo je špatné heslo!")

    context = {'page': page}
    return render(request, 'base/login_register.html', context)

# setup logout button
def logoutUser(request):
    logout(request)
    return redirect('Domovskástránka')

# setup register button
def registerUser(request):
    page = 'register'
    form = UserCreationForm()
# setup register form from django forms
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('Domovskástránka')
        else:
            messages.error(request, "Nastala chyba při registraci, zkuste se registrovat znovu!")
    return render(request, 'base/login_register.html', {'form': form})

#Home page view
def Home(request):
    context = {'infoome': infoome , 'prac': prac, 'stud': stud, 'vlas': vlas, 'zaj': zaj, 'nab': nab}
    return render(request, 'base/home.html', context)

# def  page about me
def Me(request, pk):
    me = None
    for i in infoome:
        if i['id'] == int(pk):
            me = i
    context = {'me': me}
    return render(request, 'Infoome.html', context)

# def page about working experience
def Pracovnizkus(request, pk):
    Prac = None
    for i in prac:
        if i['id'] == int(pk):
            Prac = i
    context = {'Prac': Prac}
    return render(request, 'Pracovnizkusenosti.html', context)

# def page about my studies
def Studium(request, pk):
    Studs = None
    for i in stud:
        if i['id'] == int(pk):
            Studs = i
    context = {'stud': stud}
    return render(request, 'Studium.html', context)

# def page about my atributes
def Vlastnosti(request, pk):
    Vlas = None
    for i in vlas:
        if i['id'] == int(pk):
            Vlas = i
    context = {'Vlas': Vlas}
    return render(request, 'Vlastnosti.html', context)

#def page about my hobbys
def Zajmy(request, pk):
    Zajm = None
    for i in zaj:
        if i['id'] == int(pk):
            Zajm = i
    context = {'Zajm': Zajm}
    return render(request, 'Zájmy.html', context)

# def page for adding and managing jobs offers
def Nabidky(request, pk):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    rooms = Room.objects.filter(
        Q(typ_práce__name__icontains=q) |
        Q(Hodinový_plat__icontains=q) |
        Q(Hodiny_za_den__icontains=q) 
        )
    Typs = typprace.objects.all()
    room_count = rooms.count()

    context = {'rooms': rooms, 'Typs': Typs, 'room_count': room_count }
    return render(request, 'Nabidky.html', context)

# def room where will be the job offer shown
def room(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all().order_by('-created')
    dotazující = room.dotazující.all()
    if request.method == 'POST':
        message = Message.objects.create(
            user= request.user,
            room= room,
            body= request.POST.get('body')
        )
        return redirect('room', pk=room.id)

    context = {'room': room, 'room_messages': room_messages, 'dotazující': dotazující}
    return render(request, 'room.html', context)

# setup requirement to login user for him to add a offer
@login_required(login_url='login')
def Vytvornabidku(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Nabidky/0')

    context = {'form': form}
    return render(request, 'uprava_nabidky.html', context)

# setup requirement to login user for him to change offer
@login_required(login_url='login')
def Upraveninabidky(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
# only user that created the offer can change atributes about it
    if request.user != room.Zadávající:
        return HttpResponse('Nemáte oprávnění upravovat cizí nabídky práce!!')
#save offer update
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid:
            form.save()
            return redirect('/Nabidky/0')
    context = {'form': form}
    return render(request, 'uprava_nabidky.html', context)

# setup requirement to login user for him to delete offer
@login_required(login_url='login')
def Smazaninabidky(request, pk):
    room = Room.objects.get(id=pk)
#setup that only user that created offer can delete it
    if request.user != room.Zadávající:
        return HttpResponse('Nemáte oprávnění upravovat cizí nabídky práce!!')

    if request.method == 'POST':
        room.delete()
        return redirect('/Nabidky/0')
    context = {'obj': room}
    return render(request, 'Vymazani.html', context)



# not needed will delete
nab = [
    {'id':0, 'name': 'Seznam nabídek práce'},
]

infoome = [
    {'id':1, 'name': 'Základní informace o mé osobě.'},
]
prac = [
    {'id':2, 'name': 'Mé dosavadní pracovní zkušenosti.'},
]

stud= [
    {'id':3, 'name': 'Studium.'},
]

vlas = [
    {'id':4, 'name': 'Mé vlastnosti schopnosti.'},
]

zaj = [
    {'id':5, 'name': 'Mé zájmy.'},
]
# Create your views here.
