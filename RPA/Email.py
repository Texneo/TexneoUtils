from botcity.plugins.email import BotEmailPlugin

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

    email = BotEmailPlugin()

    # Configure SMTP with the gmail server
    email.configure_smtp("smtp.office365.com", 587)
    email.login(usuario, senha)

    corpo += f"<br><br><p><b>Observação:</b> Este e-mail foi gerado automaticamente via RPA - {id_rpa}. Em caso de dúvida entre em contato com a equipe de TI - Automação.</p>"

    # Sending the email message
    email.send_message(titulo, corpo, destinatarios, use_html=True)

    email.disconnect()