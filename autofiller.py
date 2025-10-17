import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#remember that bruin email needs g.ucla.edu
def autofill_library_reservation(first_name,last_name,bruin_email,bruin_id):
    #Option 1: Keep browser open (testing purposes)
    #options = webdriver.ChromeOptions()
    #options.add_experimental_option("detach", True)
    #driver = webdriver.Chrome(options=options)

    #Option 2: Close browser after script execution
    driver = webdriver.Chrome()

    driver.get('https://libbooking.law.ucla.edu/reserve/study')
    driver.implicitly_wait(0.5)

    #select earliest open 8AM time slot
    element = driver.find_element(By.XPATH, "//div[@class='s-lc-eq-period s-lc-eq-period-available'][contains(@data-period-display,'8:00am')]")
    element.click()
    driver.implicitly_wait(0.5)

    #find and click submit button
    submit = driver.find_element(By.NAME, "submit_times")
    submit.click()
    driver.implicitly_wait(0.5)

    #find and fill out fName, lName, email, bruinID input
    fName = driver.find_element(By.NAME, "fname")
    fName.send_keys(first_name)

    lName = driver.find_element(By.NAME, "lname")
    lName.send_keys(last_name)

    email = driver.find_element(By.NAME, "email")
    email.send_keys(bruin_email)

    bruinID = driver.find_element(By.ID, "q11933")
    bruinID.send_keys(bruin_id)

    #find and click submit bookings button
    submitBooking = driver.find_element(By.ID, "btn-form-submit")
    submitBooking.click()

    #if testing, comment out
    driver.quit()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python3 scrape.py <first_name> <last_name> <bruin_email> <bruin_id>")
        sys.exit(1)
    _, first_name, last_name, bruin_email, bruin_id = sys.argv
    autofill_library_reservation(first_name, last_name, bruin_email, bruin_id)