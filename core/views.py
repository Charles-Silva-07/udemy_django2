from django.shortcuts import render
from .forms import ContatoForm
from django.contrib import messages # usada para exibir as menssages de alert de sucesso erro para o bootstrap


def index(request):
    return render(request, 'index.html')


def contato(request):

    form = ContatoForm(request.POST or None) # nosso form pode conter dados ou não
    if str(request.method) == 'POST':
        print(f'Post{request.POST}')
        if form.is_valid():
            nome = form.cleaned_data['nome'] # o cleaned_date pega o nome do template ´para imprimir logo abaixo
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print('Mensagem Enviado com sucesso')
            print(f'Nome: {nome}')
            print(f'E-mail: {email}')
            print(f'Assunto: {assunto}')
            print(f'Mensagem: {mensagem}')

            messages.success(request, 'E-mail enviado com sucesso') # vai ser mostrado no template
            form = ContatoForm() # vai limpar o formulário a pos ter enviado

        else:
            messages.error(request, 'Erro ao enviar e-mail')
    context = {
        'form': form
    }

    return render(request, 'contato.html', context)


def produto(request):
    return render(request, 'produto.html')
