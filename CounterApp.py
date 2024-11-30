import shutil
import subprocess
import time
import unittest
import os
from datetime import datetime

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class EnhancedCounterAppTests(unittest.TestCase):
    report = []

    @classmethod
    def setUpClass(cls):
        # Find the Appium executable
        appium_executable = shutil.which('appium')
        # Start the Appium server
        try:
            cls.appium_process = subprocess.Popen(
                [appium_executable],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=False
            )
            print("Appium server started.")
        except Exception:
            #  print(f"An error occurred while starting Appium: {e}")
            return

        # Wait for a moment to ensure the server is up
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'appium_process'):
            cls.appium_process.terminate()
            print("Appium server stopped.")

    def setUp(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "moto g84 5G",
            "automationName": "UiAutomator2",
            "appPackage": "com.example.testapp",
            "appActivity": "com.example.testapp.MainActivity",
            "noReset": True,
            "autoGrantPermissions": True,
        }

        options = UiAutomator2Options().load_capabilities(desired_caps)
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options)

    def tearDown(self):
        if hasattr(self, 'driver'):
            self.driver.quit()

    def capture_screenshot(self, test_name):
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f"{test_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
        self.driver.save_screenshot(screenshot_path)
        return screenshot_path

    def log_error(self, test_name, message):
        self.report.append({
            'test_case': test_name,
            'result': 'FAIL',
            'message': message
        })

    def test_initial_value(self):
        try:
            current_value_element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "0"))
            )
            assert current_value_element.get_attribute("contentDescription") == "0", \
                f"Expected counter to display 0, but got: {current_value_element.get_attribute('contentDescription')}"
            print("Test passed: Counter shows 0 on app launch.")
            self.report.append({'test_case': 'test_initial_value', 'result': 'PASS'})
        except Exception as e:
            screenshot_path = self.capture_screenshot('test_initial_value')
            self.log_error('test_initial_value', f"{str(e)}. Screenshot saved at: {screenshot_path}")

    def test_increment(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "+1"))
            )
            element.click()
            self.report.append({'test_case': 'test_increment', 'result': 'PASS'})
        except Exception as e:
            screenshot_path = self.capture_screenshot('test_increment')
            self.log_error('test_increment', f"{str(e)}. Screenshot saved at: {screenshot_path}")

    def test_reset(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "+1"))
            )
            element.click()

            reset_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Reset"))
            )
            reset_button.click()
            print("Reset button clicked successfully.")
            self.report.append({'test_case': 'test_reset', 'result': 'PASS'})
        except Exception as e:
            screenshot_path = self.capture_screenshot('test_reset')
            self.log_error('test_reset', f"{str(e)}. Screenshot saved at: {screenshot_path}")

    def test_select_date(self):
        try:
            select_date_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Pick a Date"))
            )
            select_date_button.click()
            self.report.append({'test_case': 'test_select_date', 'result': 'PASS'})
        except Exception as e:
            screenshot_path = self.capture_screenshot('test_select_date')
            self.log_error('test_select_date', f"{str(e)}. Screenshot saved at: {screenshot_path}")

    def test_select_date_display(self):
        try:
            select_date_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Pick a Date"))
            )
            select_date_button.click()

            date_xpath = "//*[@class='android.widget.Button' and @content-desc='14, Thursday, November 14, 2024' and @index='25']"
            date_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, date_xpath))
            )
            date_element.click()

            ok_button_xpath = "//*[@class='android.widget.Button' and @content-desc='OK']"
            ok_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, ok_button_xpath))
            )
            ok_button.click()
            self.report.append({'test_case': 'test_select_date_display', 'result': 'PASS'})
        except Exception as e:
            screenshot_path = self.capture_screenshot('test_select_date_display')
            self.log_error('test_select_date_display', f"{str(e)}. Screenshot saved at: {screenshot_path}")

    def test_select_date_display_cancel(self):
        try:
            select_date_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Pick a Date"))
            )
            select_date_button.click()

            date_xpath = "//*[@class='android.widget.Button' and @content-desc='14, Thursday, November 14, 2024' and @index='25']"
            date_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, date_xpath))
            )
            date_element.click()

            cancel_button_xpath = "//*[@class='android.widget.Button' and @content-desc='Cancel']"
            cancel_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, cancel_button_xpath))
            )
            cancel_button.click()
            self.report.append({'test_case': 'test_select_date_display_cancel', 'result': 'PASS'})
        except Exception as e:
            screenshot_path = self.capture_screenshot('test_select_date_display_cancel')
            self.log_error('test_select_date_display_cancel', f"{str(e)}. Screenshot saved at: {screenshot_path}")

    def test_invalid_action(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "+1"))
            )
            element.click()
            self.report.append({'test_case': 'test_invalid_action ', 'result': 'PASS'})
        except Exception as e:
            screenshot_path = self.capture_screenshot('test_invalid_action')
            self.log_error('test_invalid_action', f"{str(e)}. Screenshot saved at: {screenshot_path}")

    @classmethod
    def tearedDownClass(cls):
        # Print the test report
        print("\nTest Report:")
        for entry in cls.report:
            print(f"Test Case: {entry['test_case']}, Result: {entry['result']}, Message: {entry.get('message', '')}")


if __name__ == '__main__':
    unittest.main()

    # Use xmlrunner to generate XML reports for CI/CD
    runner = xmlrunner.XMLTestRunner(output=EnhancedCounterAppTests.output_dir)
    unittest.main(testRunner=runner)
