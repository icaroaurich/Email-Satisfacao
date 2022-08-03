import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

print("Lendo arquivo: email.auh")
f = open('email.auh', 'r')
lista = []
for linha in f:lista.append(linha)
email_usado = lista[0][:-1]
senha = str(lista[1][:-1])
porta = lista[2][:-1]
servidor = lista[3][:-1]
print("Dados para envio de email confirmados!")

enviar_para = input("Para qual e-mail enviar?: ")

assunto = "Pesquisa Satisfação TI Grupo Brasileiro - Divisão Honda"
msg = MIMEMultipart()

msg['From'] = email_usado
msg['To'] = enviar_para
msg['Subject'] = assunto
chamado = input("Chamado: ")
htmlold = '''
    <body>"<h4>Para concluir o chamado pedimos que responda essa rápida pesquisa de Satisfação quanto ao nosso serviço realizado ⚠.</h4>
    <h1><li>O número do seu chamado é :<u>{chamado}</u></li></h1>
    <h1><li>LINK: <a href="https://forms.gle/JgL4uZyvvPeYZkv27">FORMULARIO</a></li></h1>
    <h4>A sua resposta é de extrema importância para o Grupo e <b><i>tomará apenas 2 a 3 minutos do seu tempo.</i></b> ✅</h4>
    <h4>Não deixe de responder, somente assim saberemos como podemos melhorar.</h4>
    </body>
    '''
body = f"<body><h4>Para concluir o chamado pedimos que responda essa rápida pesquisa de Satisfação quanto ao nosso serviço realizado ⚠.</h4>    <h1><li>O número do seu chamado é :<u>{chamado}</u></li></h1>    <h1><li>LINK: <a href="+"https://forms.gle/JgL4uZyvvPeYZkv27"+">FORMULARIO</a></li></h1>    <h4>A sua resposta é de extrema importância para o Grupo e <b><i>tomará apenas 2 a 3 minutos do seu tempo.</i></b> ✅</h4>    <h4>Não deixe de responder, somente assim saberemos como podemos melhorar.</h4>    </body>"

msg.attach(MIMEText(body, 'html'))

try:
    print("iniciando envio de email")
    print("Acessando o servidor e porta")
    server = smtplib.SMTP(servidor, porta)
    print("Iniciando TLS")
    server.starttls()
    print("Logando no e-mail")
    server.login(email_usado, senha)
    print("Colocando informações no corpo do e-mail")
    text = msg.as_string()
    print(f"Enviando para {enviar_para}")
    server.sendmail(email_usado, enviar_para, text)
    server.quit()
    print('\nEmail enviado com sucesso!')
    print(f"Email enviado para {enviar_para}")
except:print("\nEmail não foi enviado, possiveis motivos:\n1 - Email informado está errado\n2 - Senha informada está errada\n3 - Porta informada está errada\n4 - Servidor informado está errado\n5 - E-mail não está liberado para APPS menos seguros\n6 - E-mail de destino incorreto")