import random
import string

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from .forms import SignUpForm, ActivationCodeForm


def generate_code():
    characters = string.ascii_letters + string.digits + string.punctuation
    code = ''.join(random.choice(characters) for _ in range(20))
    return code


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password2']
            first_name = generate_code()

            # Отправка кода подтверждения на почту.
            send_mail(
                'Ваш код подтверждения',
                f'Ваш код подтверждения: {first_name}',
                'testserver@test.ru',
                [email],
                fail_silently=False,
            )

            # Создание пользователя, но не сохраняем его еще.
            user = User(username=username,
                        email=email,
                        first_name=first_name,
                        is_active=False
                        )
            user.set_password(password)
            user.save()

            # Перенаправим на страницу для ввода кода.
            return redirect('get_verify_code')

    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def verify_code(request):
    if request.method == 'POST':
        form = ActivationCodeForm(request.POST)
        if form.is_valid():
            temp_code = form.cleaned_data.get('first_name')
            if User.objects.filter(first_name=temp_code):
                user = User.objects.get(first_name=temp_code)
                user.first_name = ''
                user.is_active = True  # Активируем пользователя.
                user.save()
                return redirect('login')  # Перенаправление на страницу входа.
            else:
                form.add_error(None, "Код подтверждения не совпадает.")
                return render(request, 'registration/verify_code.html', {'form': form})

        return render(request, 'registration/verify_code.html', {'form': form})
    else:
        form = ActivationCodeForm()
        return render(request, 'registration/verify_code.html', {'form': form})
