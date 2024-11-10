from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

# Create your views here.


def sign_up_by_html(request):
    users = ['Nick', 'Alex', 'Pedro', 'Donald']
    info = {}
    context = {
        'info': info
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        print(f'Username: {username}')
        print(f'Password: {password}')
        print(f'Повтор пароля: {repeat_password}')
        print(f'Age: {age}')

        if password == repeat_password and int(age) >= 18 and str(username) not in users:
            return HttpResponse(f'Приветствуем, {username}!')
        else:
            if password != repeat_password:
                info.update({'error': 'Пароли не совпадают'})
            elif int(age) < 18:
                info.update({'error': 'Вы должны быть старше 18'})
            elif str(username) in users:
                info.update({'error': 'Пользователь уже существует'})
            return render(request, 'fifth_task/registration_page.html', context)

    return render(request, 'fifth_task/registration_page.html', context)


def sign_up_by_django(request):
    users = ['Nick', 'Alex', 'Pedro', 'Donald']
    info = {}
    context = {
        'info': info, 'UserRegister': UserRegister()
    }
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            # print(f'{username}, {password}, {repeat_password}, {age}')

            if password == repeat_password and int(age) >= 18 and str(username) not in users:
                return HttpResponse(f'Приветствуем, {username}!')
            else:
                if password != repeat_password:
                    info.update({'error': 'Пароли не совпадают'})
                elif int(age) < 18:
                    info.update({'error': 'Вы должны быть старше 18'})
                elif str(username) in users:
                    info.update({'error': 'Пользователь уже существует'})
                return render(request, 'fifth_task/registration_page.html', context)
    else:
        form = UserRegister()
    return render(request,'fifth_task/registration_page.html', {'form': form})




