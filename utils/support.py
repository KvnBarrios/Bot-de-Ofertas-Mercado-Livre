from selenium.common.exceptions import TimeoutException
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from utils.config_manager import env_webdriver
from selenium import webdriver


def get_webdriver():
    """
    Retorna o webdriver. Você pode chamar Chrome e Firefox pela linha de comando.
    Por padrão é o Firefox Headless
    """

    if env_webdriver == 'chromedriver':
        return webdriver.Chrome()
    if env_webdriver == 'firefoxdriver':
        return webdriver.Firefox()

    caps = DesiredCapabilities.FIREFOX
    caps["marionette"] = True
    options = Options()
    options.add_argument('--headless')
    return webdriver.Firefox(firefox_options=options, capabilities=caps)


def wait_for_element(driver, locator=None, seconds=15):

    """

    :param driver: browser driver
    :param seconds: ten seconds in default mode, but you can set
    :type locator: web_element
    :return webelement
    """
    wait = WebDriverWait(driver, seconds)
    try:
        return wait.until(ec.visibility_of_element_located(locator))
    except TimeoutException as err:
        print('Elemento não encontrado na página: {} ({})'.format(err.stacktrace, locator))
    except AttributeError as none_error:
        print('Elemento não encontrado na página: {} ({})'.format(none_error, locator))


def wait_for_elements(driver, locator=None, seconds=15):
    """

    :rtype:
    :param driver: browser driver
    :param seconds: ten seconds in default mode, but you can set
    :type locator: web_element
    """
    wait = WebDriverWait(driver, seconds)
    try:
        return wait.until(ec.visibility_of_any_elements_located(locator))
    except TimeoutException as err:
        print('Elemento não encontrado na página: ', err.stacktrace)
    except AttributeError as none_error:
        print('Elemento não encontrado na página: {} ({})'.format(none_error, locator))
