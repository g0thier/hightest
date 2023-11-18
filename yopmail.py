from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

def format_time(timestamp):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))

def create_random_email():
    GENERATOR_BUTTON_XPATH = '/html/body/div/div[2]/main/div/div[2]/div/div[1]/div[2]/button[1]'
    IDENTIFIANT_XPATH = '//*[@id="geny"]/span[1]'
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
            
            time_end = time.time()
            return {'status': 'error',
                    'error_message': 'impossible to generate email, check XPath of "Nouveau" button.',
                    'execution_time': {'start_time': format_time(time_start),
                                       'end_time': format_time(time_end),
                                       'duration': round(time_end - time_start, 2)}}

        try:
            # Get the mail generated.
            identifiant = driver.find_element(By.XPATH, IDENTIFIANT_XPATH)
            domaine = driver.find_element(By.XPATH, DOMAINE_XPATH)
        except:
            driver.close()
            
            time_end = time.time()
            return {'status': 'error',
                    'error_message': 'impossible to get identifiant and/or domain email, check XPath of "geny" span.',
                    'execution_time': {'start_time': format_time(time_start),
                                       'end_time': format_time(time_end),
                                       'duration': round(time_end - time_start, 2)}}
        
        if identifiant.text and domaine.text :
            # Reconstitute email.
            email = f'{identifiant.text}@{domaine.text}'
        else:
            driver.close()

            time_end = time.time()
            return {'status': 'error',
                    'error_message': 'identifiant or domaine is empty.',
                    'execution_time': {'start_time': format_time(time_start),
                                       'end_time': format_time(time_end),
                                       'duration': round(time_end - time_start, 2)}}

        driver.close()

        time_end = time.time()
        return {'status': 'success',
                'generated_email': email,
                'execution_time': {'start_time': format_time(time_start),
                                   'end_time': format_time(time_end),
                                   'duration': round(time_end - time_start, 2)}}
    except:
        driver.close()
            
        time_end = time.time()
        return {'status': 'error',
                'error_message': 'impossible to access to yopmail email generator.',
                'execution_time': {'start_time': format_time(time_start),
                                   'end_time': format_time(time_end),
                                   'duration': round(time_end - time_start, 2)}}
    

def get_cookies_of(email):
    time_start = time.time()
    try:
        driver = webdriver.Chrome()
        driver.get("https://yopmail.com/fr/")

        try:
            # Enter email in the placeholder.
            input_email = driver.find_element(By.XPATH, '//*[@id="login"]')
            input_email.send_keys(email)
        except:
            driver.close()
            
            time_end = time.time()
            return {'status': 'error',
                    'error_message': 'impossible to enter email in placeholder, check XPath of "login" placeholder.',
                    'execution_time': {'start_time': format_time(time_start),
                                       'end_time': format_time(time_end),
                                       'duration': round(time_end - time_start, 2)}}

        try:
            # Clic on the "➔".
            send_button = driver.find_element(By.XPATH, '//*[@id="refreshbut"]/button')
            send_button.click()
        except:
            driver.close()
            
            time_end = time.time()
            return {'status': 'error',
                    'error_message': 'impossible to launch email, check XPath of "➔" button.',
                    'execution_time': {'start_time': format_time(time_start),
                                       'end_time': format_time(time_end),
                                       'duration': round(time_end - time_start, 2)}}
        try:
            cookies = driver.get_cookies()
        except:
            driver.close()

            time_end = time.time()
            return {'status': 'error',
                    'error_message': 'impossible to get cookies, check driver.',
                    'execution_time': {'start_time': format_time(time_start),
                                       'end_time': format_time(time_end),
                                       'duration': round(time_end - time_start, 2)}}
        
        driver.close()

        time_end = time.time()
        return {'status': 'success',
                'generated_cookies': cookies,
                'execution_time': {'start_time': format_time(time_start),
                                   'end_time': format_time(time_end),
                                   'duration': round(time_end - time_start, 2)}}
    except:
        driver.close()

        time_end = time.time()
        return {'status': 'error',
                'error_message': 'impossible to access to yopmail.',
                'execution_time': {'start_time': format_time(time_start),
                                   'end_time': format_time(time_end),
                                   'duration': round(time_end - time_start, 2)}}

 
def last_message_of(email):
    print(email)
    return 'some html text'