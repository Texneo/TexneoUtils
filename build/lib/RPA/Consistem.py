from botcity.web import By

def logar(wbot, usuario, senha):

    """

    Preenche dados de Login e acessa o Consistem.

    wbot:  Instância do web bot ativa.

    """

    campo_usuario = wbot.find_element(selector="//div[@class='ui left icon input loginTextField ']", by=By.XPATH)
    wbot.wait_for_element_visibility(element=campo_usuario, visible=True, waiting_time=10000)
    campo_usuario.click()
    wbot.paste(usuario)
    wbot.tab()
    wbot.paste(senha)
    wbot.enter()

def deslogar(wbot):

    """

    Desloga da instancia ativa do Consistem.

    wbot: Instância do web bot ativa.

    """

    botao_deslogar = wbot.find_element(selector="//i[@class='red shutdown icon']", by=By.XPATH)
    wbot.wait_for_element_visibility(element=botao_deslogar, visible=True, waiting_time=2000)
    botao_deslogar.click()
    wbot.type_left()
    wbot.enter()