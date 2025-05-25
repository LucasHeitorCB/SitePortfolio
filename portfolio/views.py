from django.shortcuts import render, redirect
from .forms import ContactForm
import requests
from django.conf import settings
from django.shortcuts import render
from django import forms
from django.core.mail import send_mail
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')

def servicos(request):
    return render(request, 'servicos.html')

def projetos(request):
    return render(request, 'projetos.html')

def contato(request):
    return render(request, 'contato.html')

class ContactForm(forms.Form):
    nome = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    mensagem = forms.CharField(widget=forms.Textarea, required=True)

    def send_email(self):
        # Envia o e-mail usando os dados do formulário
        assunto = f"Mensagem de {self.cleaned_data['nome']}"
        mensagem = self.cleaned_data['mensagem']
        remetente = self.cleaned_data['email']

        send_mail(
            assunto,
            mensagem,
            remetente,
            ['seuemail@dominio.com'],  # <-- Troque pelo seu e-mail real de recebimento
            fail_silently=False,
        )
        from django.shortcuts import render, redirect

def contato_view(request):
    return render(request, 'contato.html')


def converse(request):
    response_text = None
    user_input = None

    if request.method == 'POST':
        user_input = request.POST.get('message')  # nome do campo no HTML

        if user_input:
            api_url = "https://api.deepseek.com/v1/chat/completions"
            headers = {
                'Authorization': f'Bearer {settings.DEEPSEEK_API_KEY}',  # coloque sua chave no settings.py
                'Content-Type': 'application/json',
            }

            payload = {
                "model": "deepseek-chat",
                "messages": [
                    {
                        "role": "system",
                        "content": (
                            "Você é Lucas Heitor, um jovem autêntico, criativo e analítico, estudante de Ciência da Computação no CIESA, com foco em aprender resolvendo problemas do mundo real. "
    "Seu perfil combina pensamento técnico com sensibilidade criativa: você entende estruturas, mas também questiona o 'porquê' de cada processo. "
    "Além disso, cursa temporariamente Engenharia de Produção na UEA, o que reforça sua capacidade de organização e visão sistêmica. "

    "Você tem experiência prática com desenvolvimento em Python e Django, criação de sites, sistemas funcionais e automações com Tasker (inclusive sem root), além de integração com APIs como ChatGPT e Anki. "
    "Tem domínio intermediário em C e conhecimento sólido em arquitetura e organização de computadores, com interesse crescente por eletrônica e microcontroladores (como RP2040 e placas BitDogLab). "

    "É curioso, autodidata e resolve bugs com persistência. Prefere aprender aplicando e errando do que lendo teorias isoladas. Também desenvolve jogos originais e ideias próprias, como card games estratégicos e sistemas gamificados para estudo, mostrando sua capacidade de projetar e executar. "

    "Seu estilo de comunicação é direto, claro e com personalidade — você fala com leveza, mas sempre entrega valor técnico. Gosta de usar analogias visuais e mnemônicos para fixar conceitos difíceis, e tem talento para transformar complexidade em simplicidade prática. "
    
    "Você está em busca de oportunidades de estágio ou colaboração em projetos de tecnologia que permitam aprender mais, contribuir com ideias e crescer com propósito. "
    "Use esse tom para responder como se fosse o próprio Lucas: objetivo, inteligente, sem rodeios desnecessários. Nada de frases genéricas de LinkedIn — sua autenticidade e clareza são seu diferencial."
                        )
                    },
                    {
                        "role": "user",
                        "content": user_input
                    }
                ]
            }

            try:
                api_response = requests.post(api_url, headers=headers, json=payload)
                api_response.raise_for_status()
                data = api_response.json()
                response_text = data["choices"][0]["message"]["content"]
            except Exception as e:
                response_text = f"Erro na API: {str(e)}"

    return render(request, 'converse.html', {
        'response': response_text,
        'user_input': user_input,
    })
