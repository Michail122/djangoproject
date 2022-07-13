from django.shortcuts import render,redirect, HttpResponseRedirect
from django.http import HttpResponse
from .models import Game, GameManger
from .forms import GameForm #UserRegistrationForm
from django.contrib.auth.decorators import login_required

def index(request):
    my_games = Game.objects.order_by('-id')
    return render(request, 'main/index.html', {"games": my_games})


def about(request):
    return render(request, 'main/about.html')


def init(request):
    # Game.objects.create_game("cs_go")
    # Game.objects.create_game("dota_2")
    return render(request, 'main/about.html')

def create (request):
    error=''
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            error='Данные введи нормально, долбаеб блэт ( **)/'

    form=GameForm()
    data={
        'form':form,
        'error': error
    }
    return render(request,'main/create.html',data)

def login(request):
    return render(request, 'main/login.html')

# def register(request):
#     if request.method == 'POST':
#         user_form = UserRegistrationForm(request.POST)
#         if user_form.is_valid():
#             # Create a new user object but avoid saving it yet
#             new_user = user_form.save(commit=False)
#             # Set the chosen password
#             new_user.set_password(user_form.cleaned_data['password'])
#             # Save the User object
#             new_user.save()
#             return render(request, 'account/register_done.html', {'new_user': new_user})
#     else:
#         user_form = UserRegistrationForm()
#     return render(request, 'account/register.html', {'user_form': user_form})
@login_required
def logout(request):
    # auth.\
    logout(request)
    # return redirect(get_next_url(request))

# class register(DataMixin, CreateView):
#     form_class =UserCrationForm
#     template_name='register.html'
#     success_url=reverse_lazy('login')
