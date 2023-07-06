from decouple import config
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# service = Service(ChromeDriverManager().install())


main_url = 'https://weather.com/'

def get_source_code(url, city):
    try:
        service = Service(executable_path=config('EXEC_PATH'))

        options = Options()
        options.page_load_strategy = 'normal'
        options.add_argument('--no-sandbox')
        options.add_argument(f'user-data-dir={config("SELENIUM_PROFILE")}')
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(url)

        driver.maximize_window()
        time.sleep(5)

        language_button = driver.find_element(By.CSS_SELECTOR, 'div[data-testid="languageSelectorSection"]')
        language_button.click()
        time.sleep(2)
        
        degree_button = driver.find_element(By.CSS_SELECTOR, 'li[data-testid="degreesCbutton"]')
        degree_button.click()
        time.sleep(3)
        
        city_input = driver.find_element(By.ID, 'LocationSearch_input')
        city_input.clear()
        city_input.send_keys(city)
        time.sleep(3)

        # city_input.send_keys(Keys.ARROW_DOWN, Keys.ENTER)

        choose = driver.find_element(By.XPATH, '//*[@id="LocationSearch_listbox-0"]')
        choose.click()
        time.sleep(2)
        
        
        with open('forecast.html', 'w') as f:
            f.write(driver.page_source)
        time.sleep(1)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


# def main():
#     get_source_code(url=main_url, city='oslo')

# if __name__ == '__main__':
#     main()