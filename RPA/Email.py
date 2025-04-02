
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

def disparar_notificacao(destinatarios, titulo, corpo, id_rpa, usuario, senha):

    """

     Dispara e-mail.

    ->
     destinatarios: Lista de Strings contendo o e-mail dos destinatários do e-mail.
     titulo: Título do e-mail.
     corpo: Corpo do e-mail.
     id_rpa: ID do robô que está disparando a notificação.
     usuario: usuário para acesso ao SMTP.
     senha: usuário para acesso ao SMTP.

    """

    # Criação do objeto MIMEMultipart
    msg = MIMEMultipart()
    msg['From'] = usuario
    msg['To'] = str(destinatarios).split(";")
    msg['Subject'] = titulo

    # Adicionando o corpo do e-mail
    msg.attach(MIMEText(corpo + f"<br><br><p><b>Observação:</b> Este e-mail foi gerado automaticamente via RPA - {id_rpa}. Em caso de dúvida entre em contato com a equipe de TI - Automação.</p>", 'html'))

    # Conectar ao servidor SMTP e enviar o e-mail
    try:
        server = smtplib.SMTP("smtp.office365.com", 587)
        server.starttls()  # Ativa a criptografia TLS
        server.login(usuario, senha)
        text = msg.as_string()
        server.sendmail(usuario, destinatarios, text)
    except Exception as e:
        raise e
    finally:
        server.quit()



def disparar_email_anexo(destinatarios, titulo, corpo, id_rpa, usuario, senha, anexo):

    # Criação do objeto MIMEMultipart
    msg = MIMEMultipart()
    msg['From'] = usuario
    msg['To'] = str(destinatarios).split(";")
    msg['Subject'] = titulo

    # Adicionando o corpo do e-mail
    msg.attach(MIMEText(corpo + f"<br><br><p><b>Observação:</b> Este e-mail foi gerado automaticamente via RPA - {id_rpa}. Em caso de dúvida entre em contato com a equipe de TI - Automação.</p>", 'html'))

    # Abrindo o arquivo para anexo

    if(anexo):
        try:
            with open(anexo, "rb") as attachment:
                # Criando o objeto MIMEBase
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())

                # Codificando o anexo em base64
                encoders.encode_base64(part)

                # Adicionando cabeçalho de tipo do arquivo
                part.add_header('Content-Disposition', f'attachment; filename="{anexo.split("/")[-1]}"')

                # Anexando ao e-mail
                msg.attach(part)

        except Exception as e:
            print(f"Erro ao anexar o arquivo: {e}")

    # Conectar ao servidor SMTP e enviar o e-mail
    try:
        server = smtplib.SMTP("smtp.office365.com", 587)
        server.starttls()  # Ativa a criptografia TLS
        server.login(usuario, senha)
        text = msg.as_string()
        server.sendmail(usuario, destinatarios, text)
    except Exception as e:
        raise e
    finally:
        server.quit()
