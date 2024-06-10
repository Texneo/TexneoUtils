from botcity.plugins.email import BotEmailPlugin

def dispara_notificacao(to, subject, body):

    email = BotEmailPlugin()

    # Configure SMTP with the gmail server
    email.configure_smtp("smtp.office365.com", 587)
    email.login("no.reply.service@texneo.com", "Goh49972")

    rodape = "<br><br><p><b>Observação:</b> Este e-mail foi gerado automaticamente via RPA - 003. Em caso de dúvida entre em contato com a equipe de TI - Automação.</p>"

    body += rodape

    # Sending the email message
    email.send_message(subject, body, to, use_html=True)

    email.disconnect()