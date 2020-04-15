from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


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



