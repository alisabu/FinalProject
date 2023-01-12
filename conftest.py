import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from settings import email,invalid_email, password, new_password, invalid_password, phone, invalid_phone


@pytest.fixture(autouse=True)
def driverChrome():
    pytest.driver = webdriver.Chrome(r"D:\chromedriver.exe")
    pytest.driver.implicitly_wait(10)
    pytest.driver.maximize_window()
    pytest.driver.get('https://b2c.passport.rt.ru')
    yield driverChrome
    pytest.driver.quit()

@pytest.fixture()
def logging_in_with_email():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
    pytest.driver.find_element(By.ID, 'username').send_keys(email)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]')))
    pytest.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="kc-login"]')))
    pytest.driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()

@pytest.fixture()
def logging_in_with_login():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="t-btn-tab-login"]')))
    pytest.driver.find_element(By.XPATH, '//*[@id="t-btn-tab-login"]').click()
    pytest.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(email)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]')))
    pytest.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="kc-login"]')))
    pytest.driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()
@pytest.fixture()
def logging_in_with_phone():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
    pytest.driver.find_element(By.ID, 'username').send_keys(phone)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]')))
    pytest.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="kc-login"]')))
    pytest.driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()

@pytest.fixture()
def double_reg_with_email():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="kc-register"]')))
    pytest.driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '// *[ @ id = "page-right"] / div[1] / div[1] / div[1] / form[1] / div[1] / div[1] / div[1] / input[1]')))
    pytest.driver.find_element(By.XPATH, '// *[ @ id = "page-right"] / div[1] / div[1] / div[1] / form[1] / div[1] / div[1] / div[1] / input[1]').send_keys('Алиса')
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH,'// *[ @ id = "page-right"] / div[1] / div[1] / div[1] / form[1] / div[1] / div[2] / div[1] / input[1]')))
    pytest.driver.find_element(By.XPATH, '// *[ @ id = "page-right"] / div[1] / div[1] / div[1] / form[1] / div[1] / div[2] / div[1] / input[1]').send_keys('Булдакова')
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '// *[ @ id = "address"]')))
    pytest.driver.find_element(By.XPATH, '// *[ @ id = "address"]').send_keys(email)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '// *[ @ id = "password"]')))
    pytest.driver.find_element(By.XPATH, '// *[ @ id = "password"]').send_keys(password)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '// *[ @ id = "page-right"] / div[1] / div[1] / div[1] / form[1] / button[1]')))
    pytest.driver.find_element(By.XPATH, '// *[ @ id = "page-right"] / div[1] / div[1] / div[1] / form[1] / button[1]').click()


@pytest.fixture()
def double_reg_with_phone():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="kc-register"]')))
    pytest.driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '// *[ @ id = "page-right"] / div[1] / div[1] / div[1] / form[1] / div[1] / div[1] / div[1] / input[1]')))
    pytest.driver.find_element(By.XPATH, '// *[ @ id = "page-right"] / div[1] / div[1] / div[1] / form[1] / div[1] / div[1] / div[1] / input[1]').send_keys('Алиса')
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH,'// *[ @ id = "page-right"] / div[1] / div[1] / div[1] / form[1] / div[1] / div[2] / div[1] / input[1]')))
    pytest.driver.find_element(By.XPATH, '// *[ @ id = "page-right"] / div[1] / div[1] / div[1] / form[1] / div[1] / div[2] / div[1] / input[1]').send_keys('Булдакова')
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '// *[ @ id = "address"]')))
    pytest.driver.find_element(By.XPATH, '// *[ @ id = "address"]').send_keys(phone)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '// *[ @ id = "password"]')))
    pytest.driver.find_element(By.XPATH, '// *[ @ id = "password"]').send_keys(password)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '// *[ @ id = "page-right"] / div[1] / div[1] / div[1] / form[1] / button[1]')))
    pytest.driver.find_element(By.XPATH, '// *[ @ id = "page-right"] / div[1] / div[1] / div[1] / form[1] / button[1]').click()


@pytest.fixture()
def logging_in_with_wrong_email():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
    pytest.driver.find_element(By.ID, 'username').send_keys(invalid_email)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]')))
    pytest.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="kc-login"]')))
    pytest.driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()

@pytest.fixture()
def logging_in_with_wrong_phone():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
    pytest.driver.find_element(By.ID, 'username').send_keys(invalid_phone)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]')))
    pytest.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="kc-login"]')))
    pytest.driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()

@pytest.fixture()
def logging_in_with_wrong_password():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
    pytest.driver.find_element(By.ID, 'username').send_keys(email)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]')))
    pytest.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(invalid_password)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="kc-login"]')))
    pytest.driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()

@pytest.fixture()
def changing_patronymic():
    WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[1]/div[1]/button[1]')))
    pytest.driver.find_element(By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[1]/div[1]/button[1]').click()
    WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[1]/div[1]/button[1]')))
    pytest.driver.find_element(By.ID, 'user_patronymic').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
    pytest.driver.find_element(By.ID, 'user_patronymic').send_keys('Александровна')
    pytest.driver.find_element(By.XPATH, '//*[@id="user_contacts_editor_save"]').click()

@pytest.fixture()
def changing_eng_patronymic():
    WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[1]/div[1]/button[1]')))
    pytest.driver.find_element(By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[1]/div[1]/button[1]').click()
    WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[1]/div[1]/button[1]')))
    pytest.driver.find_element(By.ID, 'user_patronymic').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
    pytest.driver.find_element(By.ID, 'user_patronymic').send_keys('Smith')
    pytest.driver.find_element(By.XPATH, '//*[@id="user_contacts_editor_save"]').click()

@pytest.fixture()
def changing_password():
    WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '// *[ @ id = "password_change"]')))
    pytest.driver.find_element(By.XPATH, '// *[ @ id = "password_change"]').click()
    pytest.driver.find_element(By.XPATH, '// *[ @ id = "current_password"]').send_keys(password)
    pytest.driver.find_element(By.XPATH, '// *[ @ id = "new_password"]').send_keys(new_password)
    pytest.driver.find_element(By.XPATH, '// *[ @ id = "confirm_password"]').send_keys(new_password)
    pytest.driver.find_element(By.XPATH, '//*[@id="password_save"]').click()

@pytest.fixture()
def changing_wrong_password():
    WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '// *[ @ id = "password_change"]')))
    pytest.driver.find_element(By.XPATH, '// *[ @ id = "password_change"]').click()
    pytest.driver.find_element(By.XPATH, '// *[ @ id = "current_password"]').send_keys(password)
    pytest.driver.find_element(By.XPATH, '// *[ @ id = "new_password"]').send_keys(invalid_password)
    pytest.driver.find_element(By.XPATH, '// *[ @ id = "confirm_password"]').send_keys(invalid_password)
    pytest.driver.find_element(By.XPATH, '//*[@id="password_save"]').click()


@pytest.fixture()
def logging_out():
    WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.ID, 'logout-btn'))).click()

@pytest.fixture()
def going_rstl_site():
    WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.ID, 'rt-btn'))).click()

@pytest.fixture()
def confidential_policy():
    WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="rt-footer-agreement-link"]/span[1]'))).click()

@pytest.fixture()
def agreement():
    WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="rt-footer-agreement-link"]/span[2]'))).click()

@pytest.fixture()
def action_history():
    WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[2]/div[1]/button[1]'))).click()

@pytest.fixture()
def name_change():
    WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[1]/div[1]/button[1]')))
    pytest.driver.find_element(By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[1]/div[1]/button[1]').click()
    WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[1]/div[1]/button[1]')))
    pytest.driver.find_element(By.ID, 'user_firstname').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
    pytest.driver.find_element(By.ID, 'user_firstname').send_keys('Апрель')
    pytest.driver.find_element(By.XPATH, '//*[@id="user_contacts_editor_save"]').click()

@pytest.fixture()
def surname_change():
    WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[1]/div[1]/button[1]')))
    pytest.driver.find_element(By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[1]/div[1]/button[1]').click()
    WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[1]/div[1]/button[1]')))
    pytest.driver.find_element(By.ID, 'user_lastname').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
    pytest.driver.find_element(By.ID, 'user_lastname').send_keys('Май')
    pytest.driver.find_element(By.XPATH, '//*[@id="user_contacts_editor_save"]').click()

@pytest.fixture()
def max_lengh_name():
    WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[1]/div[1]/button[1]')))
    pytest.driver.find_element(By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[1]/div[1]/button[1]').click()
    WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[1]/div[1]/button[1]')))
    pytest.driver.find_element(By.ID, 'user_firstname').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
    pytest.driver.find_element(By.ID, 'user_firstname').send_keys('Йцукенгшщзхъфывапвролджэячсмить')
    pytest.driver.find_element(By.XPATH, '//*[@id="user_contacts_editor_save"]').click()

@pytest.fixture()
def min_lengh_name():
    WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[1]/div[1]/button[1]')))
    pytest.driver.find_element(By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[1]/div[1]/button[1]').click()
    WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[1]/div[1]/button[1]')))
    pytest.driver.find_element(By.ID, 'user_firstname').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
    pytest.driver.find_element(By.ID, 'user_firstname').send_keys('А')
    pytest.driver.find_element(By.XPATH, '//*[@id="user_contacts_editor_save"]').click()













