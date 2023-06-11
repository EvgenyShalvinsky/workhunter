from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch the browser
browser = webdriver.Chrome()

# Navigate to the login page
browser.get("https://hh.ru/account/login")

# Wait for the login form to load
login_form = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, "loginform"))
)

# Fill in the login credentials
email_field = login_form.find_element_by_name("username")
email_field.send_keys("your_email@example.com")

password_field = login_form.find_element_by_name("password")
password_field.send_keys("your_password")

# Submit the login form
login_button = login_form.find_element_by_css_selector("button[data-qa='account-login-submit']")
login_button.click()

# Wait for the user account page to load
WebDriverWait(browser, 10).until(
    EC.url_matches("https://hh.ru/applicant/resumes")
)

# Do something on the user account page
# ...

# Close the browser
browser.quit()
