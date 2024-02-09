from pathlib import Path
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service # para o uso do  navegador
from selenium.webdriver.common.by import By # para seleção por nome
from selenium.webdriver.support.wait import WebDriverWait # para esperar o carregamento dos itens da pagina online

from selenium.webdriver.support import expected_conditions as EC 
ROOT_FOLDER = Path(__file__).parent
CHROMEDRIVER_EXEC = ROOT_FOLDER /'chromedriver.exe'
def make_chrome_options(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option) # type: ignore

    chrome_service = Service(executable_path=str(CHROMEDRIVER_EXEC))

    chrome_browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options,
    )
    
    return chrome_browser

if __name__ == "__main__":   
    TIME_TO_SLEEP = 10

    options = ('--disable-gpu', '--no-sandbox',)
    browser = make_chrome_options(*options)
    browser.get("https://www.google.com")

    search_input = WebDriverWait(browser,TIME_TO_SLEEP).until(
        EC.presence_of_element_located((By.NAME, 'q'))
        )
    search_input.send_keys('Hello world')

    time.sleep(10)