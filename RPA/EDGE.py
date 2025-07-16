from botcity.web.browsers.edge import default_options
from botcity.web import Browser, WebBot
from time import sleep
import os, time, traceback

from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium import webdriver

def colocar_em_primeiro_plano(dbot):
    """
    Coloca aplicação do Edge em primeiro plano.
    """
    dbot.connect_to_app(class_name='Chrome_WidgetWin_1', found_index=0)
    janela_edge = dbot.app.top_window()
    janela_edge.set_focus()

def configurar(wbot, url_inicial="https://www.google.com", max_tentativas=3, espera=5):

    # Instantiate the WebBot
    bot = WebBot()

    # Configure whether or not to run on headless mode
    bot.headless = False

    profile_path = "C:\\Users\\bot-python-01\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\"

    # Fetch the default options for my preferred browser
    # Pass in the headless, download_folder_path and user_data_dir
    # to be used when building the default_options
    def_options = default_options(
        headless=bot.headless,
        user_data_dir=profile_path  # Inform the profile path that wants to start the browser
    ) 

    # Update the options to use the customized Options.
    bot.options = def_options
    # Set the WebDriver path
    bot.driver_path = "C:\Users\\bot-python-01\\Desktop\\edgedriver_win64\\msedgedriver.exe"

    wbot = bot
