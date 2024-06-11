from botcity.web import By

def logar(wbot, usuario, senha):

    """

    Preenche dados de Login e acessa o Consistem.

    ->
    wbot: Instância do web bot ativa.

    <-
    string: Retorna 'Sucesso' em caso de Login realizado com sucesso. Do contrário retorna o erro de Login.

    """

    campo_usuario = wbot.find_element(selector="//div[@class='ui left icon input loginTextField ']", by=By.XPATH)
    wbot.wait_for_element_visibility(element=campo_usuario, visible=True, waiting_time=10000)
    campo_usuario.click()
    wbot.paste(usuario)
    wbot.tab()
    wbot.paste(senha)
    wbot.enter()

    try:
        span_erro_login = wbot.find_element(selector="//div[@class='loginErrorMessageItem']/span", by=By.XPATH)
        wbot.wait_for_element_visibility(element=span_erro_login, visible=True, waiting_time=10000)

        return span_erro_login.text
    
    except Exception as e:

        return "Sucesso"

def deslogar(wbot):

    """

    Desloga da instância ativa do Consistem.

    ->
    wbot: Instância do web bot ativa.

    """

    botao_deslogar = wbot.find_element(selector="//i[@class='red shutdown icon']", by=By.XPATH)
    wbot.wait_for_element_visibility(element=botao_deslogar, visible=True, waiting_time=2000)
    botao_deslogar.click()
    wbot.type_left()
    wbot.enter()

def acessar_tela(wbot, tela):

    """
    
    Acessa tela do Consistem a partir do código.

    ->
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