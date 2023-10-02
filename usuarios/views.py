from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        primeiro_nome = request.POST.get('primeiro_nome')
        ultimo_nome = request.POST.get('ultimo_nome')
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        pessoa = User.objects.filter(username=username)
        mail = User.objects.filter(email=email)

        if len(primeiro_nome.strip()) == 0 or len(ultimo_nome.strip()) == 0 or len(username.strip()) == 0 or len(email.strip()) == 0:
            messages.add_message(request, constants.WARNING, 'Por favor preencha todos os campos!')
            return redirect('/usuarios/cadastro')

        if not senha == confirmar_senha: 
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem!')   
            return redirect('/usuarios/cadastro')
        
        if len(senha) < 6:
            messages.add_message(request, constants.INFO, 'Sua senha deve possuir mais de seis digitos!')
            return redirect('/usuarios/cadastro')
        
        if pessoa.exists():
            messages.add_message(request, constants.ERROR, 'Esse usuário já existe, tente outro nome!')
            return redirect('/usuarios/cadastro')
        
        if mail.exists():
            messages.add_message(request, constants.ERROR, 'Esse e-mail já está cadastrado no sistema, tente outro por favor!')
            return redirect('/usuarios/cadastro')
        
        try:
            # Username deve ser único!
            user = User.objects.create_user(
                first_name=primeiro_nome,
                last_name=ultimo_nome,
                username=username,
                email=email,
                password=senha,
            )

            user.save()

            messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso!')
            return redirect('/usuarios/cadastro')
        
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno no servidor!')
            return redirect('/usuarios/cadastro')

