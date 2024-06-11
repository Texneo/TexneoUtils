from botcity.web import By

def logar(wbot, usuario, senha):

    """

    Preenche dados de Login e acessa o Consistem.

    wbot: Instância do web bot ativa.

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

    Desloga da instância ativa do Consistem.

    wbot: Instância do web bot ativa.

    """

    botao_deslogar = wbot.find_element(selector="//i[@class='red shutdown icon']", by=By.XPATH)
    wbot.wait_for_element_visibility(element=botao_deslogar, visible=True, waiting_time=2000)
    botao_deslogar.click()
    wbot.type_left()
    wbot.enter()

def acessa_tela_consistem(wbot, tela):

    """
    
    Acessa tela do Consistem a partir do código.

    wbot: Instância do web bot ativa.
    tela: Código da tela que deseja abrir.

    """

    menu = wbot.find_element(selector="//i[@class='computer icon']", by=By.XPATH)
    wbot.wait_for_element_visibility(element=menu, waiting_time=10000)      
    menu.click()
    busca = wbot.find_element(selector="//div[@class='ui mini fluid action left icon input csw_sidebar_input']", by=By.XPATH)
    wbot.wait_for_element_visibility(element=busca, visible=True, waiting_time=10000)
    busca.click()

    wbot.control_a()
    wbot.paste(tela)
    wbot.enter()
    wbot.wait(1500)