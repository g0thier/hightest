import reporting

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import time

def create_random_email():
    GENERATOR_BUTTON_XPATH = '/html/body/div/div[2]/main/div/div[2]/div/div[1]/div[2]/button[1]'
    IDENTIFIER_XPATH = '//*[@id="geny"]/span[1]'
    DOMAINE_XPATH = '//*[@id="geny"]/span[2]'

    time_start = time.time()
    try:
        driver = webdriver.Chrome()
        driver.get("https://yopmail.com/fr/email-generator")

        try:
            # Clic on the "Nouveau".
            generator_button = driver.find_element(By.XPATH, GENERATOR_BUTTON_XPATH)
            generator_button.click()
        except:
            driver.close()
            return reporting.error_message(time_start, 'impossible to generate email, check XPath of "Nouveau" button.')

        try:
            # Get the mail generated.
            identifier = driver.find_element(By.XPATH, IDENTIFIER_XPATH)
            domaine = driver.find_element(By.XPATH, DOMAINE_XPATH)
        except:
            driver.close()
            return reporting.error_message(time_start, 'impossible to get identifiant and/or domain email, check XPath of "geny" span.')
        
        if identifier.text and domaine.text :
            # Reconstitute email.
            identifier_email = identifier.text
            domaine_email = domaine.text
            email = f'{identifier_email}@{domaine_email}'
        else:
            driver.close()
            return reporting.error_message(time_start, 'identifier or domaine is empty.')

        driver.close()
        return {'status': 'success',
                'generated_email': email,
                'identifier_email': identifier_email,
                'domaine_email': domaine_email,
                'execution_time': reporting.execution_time(time_start)}
    
    except:
        driver.close()
        return reporting.error_message(time_start, 'impossible to access to yopmail email generator.')

def last_message_of(identifier):
    EXPEDITOR_PATH = '/html/body/header/div[3]/div[2]/span'
    DATE_TIME_PATH = '/html/body/header/div[3]/div[3]/span'
    SUBJECT_PATH = '/html/body/header/div[3]/div[1]'
    CONTENT_PATH = '//*[@id="mail"]/div/div'

    time_start = time.time()
    try:
        driver = webdriver.Chrome()
        driver.get(f'https://yopmail.com?{identifier}')

        try:
            # Wait and move to the iframe.
            iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ifmail")))
            driver.switch_to.frame(iframe)
        except:
            driver.close()
            return reporting.error_message(time_start, 'impossible to detect the iframe, check XPath of "ifmail" ID.')
            
        try:
            # Get the message.
            expeditor = driver.find_element(By.XPATH, EXPEDITOR_PATH)
            date = driver.find_element(By.XPATH, DATE_TIME_PATH)
            subject = driver.find_element(By.XPATH, SUBJECT_PATH)
            content = driver.find_element(By.XPATH, CONTENT_PATH)

            expeditor_email = expeditor.text
            date_email = date.text
            subject_email = subject.text
            content_email = content.text
        except:
            driver.close()
            return reporting.error_message(time_start, 'impossible to copy the last mail, check XPaths of expeditor, date, subject and content.')

        driver.close()
        return {'status': 'success',
                'expeditor': expeditor_email,
                'date': date_email,
                'subject': subject_email,
                'content': content_email,
                'execution_time': reporting.execution_time(time_start)}
    
    except:
        driver.close()
        return reporting.error_message(time_start, 'impossible to access to yopmail mailbox.')