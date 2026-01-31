from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
import random
import sys
import logging
import sys

# Configurazione del logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)] # Invia i log alla console di GitHub
)
# Poiché il file .yml lo lancia ogni 20 minuti:
# Se vogliamo che giri mediamente ogni 3 ore (180 min),
# deve attivarsi 1 volta su 9 tentativi (180/20 = 9).

def filtro_probabilita():
    # Generiamo un numero tra 0 e 100
    # Più tieni basso questo numero, più raramente lo script partirà.
    soglia = 50
    estrazione = random.randint(1, 100)
    logging.info(f"{estrazione} vs. {soglia}")
    return estrazione <= soglia

if __name__ == "__main__":
    try:
        if not filtro_probabilita():
            logging.warning("Estrazione negativa. Lo script si chiude per rispettare la frequenza.")
            sys.exit(0)
        
        # Se passa il filtro, il codice continua...
        logging.info("Log: Estrazione positiva! Eseguo Selenium...")
            
        with open('database_scuole.json', 'r') as f:
            database_scuole = json.load(f)
        with open('database_nomi.json', 'r') as f:
            database_nomi = json.load(f)
        with open('database_problemi_scuola.json', 'r') as f:
            database_problemi_scuola = json.load(f)
        with open('database_motivazioni_gita.json', 'r') as f:
            database_motivazioni_gita = json.load(f)    
        with open('database_avvenimento.json', 'r') as f:
            database_avvenimento = json.load(f)

        email_domains = [
            # Global providers
            "gmail.com","outlook.com","gmail.com","outlook.com","gmail.com","outlook.com","gmail.com","outlook.com","gmail.com","outlook.com","gmail.com","outlook.com","gmail.com","outlook.com","hotmail.com","hotmail.it",
            "live.com","msn.com","yahoo.com","yahoo.it","icloud.com",
            # Privacy / alternative
            "proton.me","protonmail.com",
            # Italian providers
            "libero.it","virgilio.it",
            # Middle East / general
            "ymail.com","rocketmail.com"
        ]

        TESTO_NOME_COGNOME = random.choice(list(database_nomi.keys()))
        TESTO_MAIL = random.choice(database_nomi[TESTO_NOME_COGNOME]) + '@' + random.choice(list(email_domains))
        TESTO_PROVINCIA = random.choice(list(database_scuole.keys()))
        TESTO_ISTITUTO = random.choice(database_scuole[TESTO_PROVINCIA])
        TESTO_CLASSE = f"{str(random.randint(1,5))}{random.choice(list(["","","","","","","",""," "," "," "," ","°","a","^"]))}{random.choice(list(["A","A","A","A","A","A","A","B","B","B","B","B","C","C","C","D","D","D","E","E","F"]))}"
        TESTO_PROBLEMATICHE_SCUOLA = random.choice(list(database_problemi_scuola))
        TESTO_COSA_FATTO_PROF = random.choice(list(database_avvenimento))
        TESTO_COMMENTO_GITA = random.choice(list(database_motivazioni_gita))

        # 1. Setup Chrome options (Optional: add '--headless' to run without a window)
        chrome_options = Options()
        chrome_options.add_argument("--headless=new") 
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        # 2. Initialize the Driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        ##### Pagina 1 #######
        logging.info("Lo script è partito...")
        
        url = "https://docs.google.com/forms/d/e/1FAIpQLScaFaiaOkPTptrOk2BEKvnqZCmjhbFREbLY8qlOTVD_BgE12w/viewform?pli=1&pli=1"
        driver.get(url)

        # Wait until the input field is visible
        mail_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/input')))
        time.sleep(random.choice([1, 0.5, 2, 2.5, 5, 1.5, 3, 4, 9, 3.2, 0.6]))
        mail_field.clear()
        mail_field.send_keys(f"{TESTO_MAIL}")
        time.sleep(random.choice([1, 0.5, 2, 2.5, 5, 1.5, 3, 4, 9, 3.2, 0.6]))
        # Click the 'Next' button
        next_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
        next_button.click()


        ####### Pagina 2 #########
        # Nome e Cognome
        logging.info("Nome e Cognome...")
        first_name_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
        first_name_field.clear()
        first_name_field.send_keys(f"{TESTO_NOME_COGNOME}")

        time.sleep(random.choice([1, 0.5, 2, 2.5, 5, 1.5, 3, 4, 9, 3.2, 0.6]))
        # Provincia
        first_name_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
        first_name_field.clear()
        first_name_field.send_keys(F"{TESTO_PROVINCIA}")

        time.sleep(random.choice([1, 0.5, 2, 2.5, 5, 1.5, 3, 4, 9, 3.2, 0.6]))
        # Istituto
        first_name_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')))
        first_name_field.clear()
        first_name_field.send_keys(f"{TESTO_ISTITUTO}")

        time.sleep(random.choice([1, 0.5, 2, 2.5, 5, 1.5, 3, 4, 9, 3.2, 0.6]))

        # Classe
        first_name_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')))
        first_name_field.clear()
        first_name_field.send_keys(f"{TESTO_CLASSE}")

        time.sleep(random.choice([1, 0.5, 2, 2.5, 5, 1.5, 3, 4, 9, 3.2, 0.6]))

        # Click the 'Next' button
        next_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
        next_button.click()

        ########### Pagina 3 ############
        logging.info("Condizioni Scolastiche...")
        # Condizioni scolastiche
        time.sleep(random.choice([1, 0.5, 2, 2.5, 5, 1.5, 3, 4, 9, 3.2, 0.6]))

        condizioni_options = [
            '//*[@id="i12"]/div[3]/div',
            '//*[@id="i6"]/div[3]/div',
            '//*[@id="i9"]/div[3]/div'
        ]

        chosen_xpath = random.choice(condizioni_options)
        choice_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, chosen_xpath)))
        choice_element.click()

        time.sleep(random.choice([1, 0.5, 2, 2.5, 5, 1.5, 3, 4, 9, 3.2, 0.6]))

        problematiche_options = [
        '//*[@id="i20"]/div[3]/div','//*[@id="i23"]/div[3]/div','//*[@id="i26"]/div[3]/div',
        '//*[@id="i20"]/div[3]/div','//*[@id="i23"]/div[3]/div','//*[@id="i26"]/div[3]/div',
        '//*[@id="i20"]/div[3]/div','//*[@id="i23"]/div[3]/div','//*[@id="i26"]/div[3]/div',
        '//*[@id="i20"]/div[3]/div','//*[@id="i23"]/div[3]/div','//*[@id="i26"]/div[3]/div',
        '//*[@id="i20"]/div[3]/div','//*[@id="i23"]/div[3]/div','//*[@id="i26"]/div[3]/div',
        '//*[@id="i20"]/div[3]/div','//*[@id="i23"]/div[3]/div','//*[@id="i26"]/div[3]/div',
        '//*[@id="i20"]/div[3]/div','//*[@id="i23"]/div[3]/div','//*[@id="i26"]/div[3]/div',
        '//*[@id="i29"]/div[3]/div' 
        ]

        chosen_xpath = random.choice(problematiche_options)
        choice_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, chosen_xpath)))
        choice_element.click()

        input_field_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[4]/div/span/div/div/div[1]/input'
        # Wait for the input field to become interactable
        extra_input = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, input_field_xpath))
            )

        # 3. Check if the chosen option is the one requiring text input
        if chosen_xpath == problematiche_options[len(problematiche_options)-1]:
            # Commento aggiuntivo
            extra_input.send_keys(f"{TESTO_PROBLEMATICHE_SCUOLA}")
        else:
            extra_input.clear()
            
        time.sleep(random.choice([1, 0.5, 2, 2.5, 5, 1.5, 3, 4, 9, 3.2, 0.6]))
        # Click the 'Next' button
        next_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
        next_button.click()
            
            
        ########### Pagina 4 ############
        logging.info("Il prof comunista...")
        # Avere professore comunista
        time.sleep(random.choice([1, 0.5, 2, 2.5, 5, 1.5, 3, 4, 9, 3.2, 0.6]))

        prof_comunista = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i6"]/div[3]')))
        prof_comunista.click()


        testo_evento = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea'))
            )
        testo_evento.clear()

        time.sleep(random.choice([8,2,3,4,5,10]))
        testo_evento.send_keys(F"{TESTO_COSA_FATTO_PROF}")

        # Click the 'Next' button
        next_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
        next_button.click()

        ########### Pagina 5 ############
        logging.info("Le gite...")
        # Gite Scolastiche
        time.sleep(random.choice([1, 0.5, 2, 2.5, 5, 1.5, 3, 4, 9, 3.2, 0.6]))
        si_no = [
        '//*[@id="i6"]/div[3]',
        '//*[@id="i9"]/div[3]'
        ]

        chosen_xpath = random.choice(si_no)
        choice_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, chosen_xpath)))
        choice_element.click()

        time.sleep(random.choice([1, 0.5, 2, 2.5, 5, 1.5, 3, 4, 9, 3.2, 0.6]))

        # 3. Check if the chosen option is the one requiring text input
        if chosen_xpath == si_no[1]:

            commento_gita_options = [
            '//*[@id="i17"]/div[3]','//*[@id="i20"]/div[3]','//*[@id="i23"]/div[3]',
            '//*[@id="i17"]/div[3]','//*[@id="i20"]/div[3]','//*[@id="i23"]/div[3]',
            '//*[@id="i17"]/div[3]','//*[@id="i20"]/div[3]','//*[@id="i23"]/div[3]',
            '//*[@id="i17"]/div[3]','//*[@id="i20"]/div[3]','//*[@id="i23"]/div[3]',
            '//*[@id="i17"]/div[3]','//*[@id="i20"]/div[3]','//*[@id="i23"]/div[3]',
            '//*[@id="i17"]/div[3]','//*[@id="i20"]/div[3]','//*[@id="i23"]/div[3]',
            '//*[@id="i17"]/div[3]','//*[@id="i20"]/div[3]','//*[@id="i23"]/div[3]',
            '//*[@id="i17"]/div[3]','//*[@id="i20"]/div[3]','//*[@id="i23"]/div[3]',
            '//*[@id="i26"]/div[3]'
            ]

            chosen_xpath = random.choice(commento_gita_options)
            choice_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, chosen_xpath)))
            choice_element.click()

            time.sleep(random.choice([1, 0.5, 2, 2.5, 5, 1.5, 3, 4, 9, 3.2, 0.6]))
            
            input_field_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[4]/div/span/div/div/div[1]/input'
            extra_input = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, input_field_xpath))
                )
            # 3. Check if the chosen option is the one requiring text input
            if chosen_xpath == commento_gita_options[len(commento_gita_options)-1]:

                # Commento gita
                time.sleep(random.choice([8, 9, 7, 13, 10, 20, 6]))
                extra_input.clear()
                extra_input.send_keys(f"{TESTO_COMMENTO_GITA}")
                
            else:
                extra_input.clear()
            
        else:
            input_field_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[4]/div/span/div/div/div[1]/input'
            extra_input = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, input_field_xpath))
                )
            extra_input.clear()
        
        # Click the 'Invia' button
        next_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
        next_button.click()
        time.sleep(3)
        
        driver.quit()
        
        report = f"""
******************************************
Script eseguito!
Nome e Cognome: {TESTO_NOME_COGNOME}
Mail: {TESTO_MAIL}
Provincia: {TESTO_PROVINCIA}
Istituto: {TESTO_ISTITUTO}
Classe: {TESTO_CLASSE}
Problematiche: {TESTO_PROBLEMATICHE_SCUOLA}
Gita: {TESTO_COMMENTO_GITA}
Azione Prof: {TESTO_COSA_FATTO_PROF}
******************************************
"""
        logging.info(report)
        
    except Exception as e:
        logging.error(f"Errore:\n {e}")
            