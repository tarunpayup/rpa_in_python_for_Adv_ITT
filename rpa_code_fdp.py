from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


form_url = 'https://forms.gle/qgUHSZpDT82sV4af6'
form_data = {
    "name": "Tarun Bansal",
    "email": "devs.tarunbansal@gmail.com",
    "city": "Meerut",
    "gender": "Male" 
}


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 15)

try:
    driver.get(form_url)


    name_field = wait.until(EC.element_to_be_clickable((By.XPATH, '(//input[@type="text"])[1]')))
    name_field.send_keys(form_data["name"])
    time.sleep(0.5)


    email_field = wait.until(EC.element_to_be_clickable((By.XPATH, '(//input[@type="text"])[2]')))
    email_field.send_keys(form_data["email"])
    time.sleep(0.5)

    
    city_field = wait.until(EC.element_to_be_clickable((By.XPATH, '(//input[@type="text"])[3]')))
    city_field.send_keys(form_data["city"])
    time.sleep(0.5)

    
    gender_options = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[role="radio"]')))
    for option in gender_options:
        label = option.get_attribute("aria-label")
        if label and form_data["gender"].lower() in label.lower():
            driver.execute_script("arguments[0].scrollIntoView(true);", option)
            wait.until(EC.element_to_be_clickable(option)).click()
            break
    time.sleep(0.5)

    
    submit_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//div[@role="button"][.//span[contains(text(), "Submit")]]')
    ))
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()

    
    time.sleep(2)
    print("Google Form submitted successfully!")

    input("Press Enter to close the browser...")

except Exception as e:
    print(f"Error occurred: {e}")

finally:
    driver.quit()
