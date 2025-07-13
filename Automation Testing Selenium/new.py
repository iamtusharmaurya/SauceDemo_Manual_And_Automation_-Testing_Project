import os
import csv
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setup screenshot folder
timestamp_folder = datetime.now().strftime("screenshots_%Y%m%d_%H%M%S")
os.makedirs(timestamp_folder, exist_ok=True)

# Users list
usernames = [
    "standard_user", "locked_out_user", "problem_user",
    "performance_glitch_user", "error_user", "visual_user"
]
password = "secret_sauce"

# Setup driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)

# Create CSV file
with open("login_results.csv", mode="w", newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Username", "Status", "Message"])

    for user in usernames:
        try:
            driver.get("https://www.saucedemo.com/")
            time.sleep(3)  # Delay before login

            # Login
            wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).clear()
            driver.find_element(By.ID, "user-name").send_keys(user)
            driver.find_element(By.ID, "password").clear()
            driver.find_element(By.ID, "password").send_keys(password)
            driver.find_element(By.ID, "login-button").click()
            time.sleep(3)

            if "inventory" in driver.current_url:
                print(f"[✅] Login successful for: {user}")
                csv_writer.writerow([user, "Success", "Logged in successfully"])

                # Add products to cart
                driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
                driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
                time.sleep(3)

                # Cart management
                driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
                assert "Your Cart" in driver.page_source
                time.sleep(3)

                # Checkout
                driver.find_element(By.ID, "checkout").click()
                time.sleep(3)
                driver.find_element(By.ID, "first-name").send_keys("Tushar")
                driver.find_element(By.ID, "last-name").send_keys("Maurya")
                driver.find_element(By.ID, "postal-code").send_keys("123456")
                time.sleep(3)
                driver.find_element(By.ID, "continue").click()
                time.sleep(3)

                # Order confirmation
                driver.find_element(By.ID, "finish").click()
                assert "Thank you for your order!" in driver.page_source
                print(f"[📦] Order placed for: {user}")
                time.sleep(3)

                # Logout
                wait.until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))).click()
                time.sleep(1)
                wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))).click()
                print(f"[🔓] Logged out for: {user}")
                time.sleep(3)

            else:
                try:
                    error_msg = driver.find_element(By.CLASS_NAME, "error-message-container").text
                except:
                    error_msg = "Unknown login error"
                print(f"[❌] Login failed for: {user} — {error_msg}")
                csv_writer.writerow([user, "Failure", error_msg])
                screenshot_path = os.path.join(timestamp_folder, f"{user}.png")
                driver.save_screenshot(screenshot_path)
                print(f"[📸] Screenshot saved: {screenshot_path}")
                time.sleep(3)

        except Exception as e:
            print(f"[⚠️] Unexpected error for {user}: {e}")
            csv_writer.writerow([user, "Failure", str(e)])
            screenshot_path = os.path.join(timestamp_folder, f"{user}_unexpected.png")
            driver.save_screenshot(screenshot_path)
            time.sleep(3)

driver.quit()
print("✅ Full task completed for all users.")
