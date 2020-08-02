from selenium import webdriver
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)


logging.debug('Start of program.')
logging.info('The main mould is working.')
browser = webdriver.Firefox()
type(browser)

