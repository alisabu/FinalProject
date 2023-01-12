import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_log_in(logging_in_with_email):
    WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[1]/h3[1]')))

def test_log_in_with_phone(logging_in_with_phone):
    WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[1]/h3[1]')))

def test_log_in_with_login(logging_in_with_login):
    WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[1]/h3[1]')))

def test_double_reg_with_email(double_reg_with_email):
    WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]' )))

def test_double_reg_with_phone(double_reg_with_phone):
    WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]' )))

def test_change_patronymic(logging_in_with_email, changing_patronymic):
    WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[1]/h3[1]')))

def test_change_eng_patronymic(logging_in_with_email, changing_eng_patronymic):
    WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/span[1]')))

def test_name_change(logging_in_with_email, name_change):
    WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[1]/h3[1]')))

def test_surname_change(logging_in_with_email, surname_change):
    WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[1]/h3[1]')))

def test_max_lengh_name(logging_in_with_email, max_lengh_name):
    WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]')))

def test_min_lengh_name(logging_in_with_email, min_lengh_name):
    WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]')))

def test_log_out(logging_in_with_email, logging_out):
    WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/h1[1]')))


def test_confidential_policy(logging_in_with_email, confidential_policy):
    pytest.driver.get('https://b2c.passport.rt.ru/sso-static/agreement/agreement.html')
    WebDriverWait(pytest.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/ol[1]/li[1]')))

def test_agreement(logging_in_with_email, agreement):
    pytest.driver.get('https://b2c.passport.rt.ru/sso-static/agreement/agreement.html')
    WebDriverWait(pytest.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/ol[1]/li[1]')))

def test_action_history(logging_in_with_email, action_history):
    WebDriverWait(pytest.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/h1[1]')))

def test_password_change(logging_in_with_email, changing_password):
    WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[1]/h3[1]')))

def test_worng_password_change(logging_in_with_email, changing_wrong_password):
    WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '// *[ @ id = "app"] / main[1] / div[1] / div[2] / div[1] / div[4] / div[1] / div[1] / div[1] / div[2] / span[1]')))

def test_log_in_with_wrong_email(logging_in_with_wrong_email):
    WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="form-error-message"]')))

def test_log_in_with_wrong_phone(logging_in_with_wrong_phone):
    WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="form-error-message"]')))

def test_log_in_with_wrong_password(logging_in_with_wrong_password):
    WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="form-error-message"]')))

















