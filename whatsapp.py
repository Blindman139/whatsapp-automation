import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def msg_obj(recipient_list, message_list):
    return {
        "recipients": recipient_list,
        "messages": message_list
    }


all_messages = [
    msg_obj(["97269 ------"], ["Hi There", "This message is automated",
            "Please don't block me", "This is for learning purpose only"])
]


def automate():
    driver_location = os.environ['driver_location']

    chrome_options = Options()
    chrome_options.add_argument(
        "--user-data-dir="+os.environ["profile_data_location"])
    chrome_options.add_argument(
        "--profile-directory="+os.environ["profile_folder"])

    driver = webdriver.Chrome(
        executable_path=driver_location, chrome_options=chrome_options)

    # open whatsapp
    # driver.get("https://www.google.com/")
    driver.get("https://web.whatsapp.com/")

    target = "9638710375"
    message = "This is an automated message for testing"

    wait = WebDriverWait(driver, 600)

    # loop through each and every objects in messages list
    for message_group in all_messages:
        recipients = message_group["recipients"]
        messages = message_group["messages"]

        for recipient in recipients:
            # go to that recipient's page
            search_box = wait.until(EC.presence_of_element_located(
                (By.XPATH, "//div[@title='Search input textbox']")))
            search_box.click()
            search_box.send_keys(recipient)
            press_enter(search_box)

            # find Type a message box and type message
            message_box = wait.until(EC.presence_of_element_located(
                (By.XPATH, "//div[@title='Type a message']")))
            for msg in messages:
                message_box.click()
                message_box.send_keys(msg)
                press_enter(message_box)

    # # div title = Search input textbox --> click -> write name
    # search_box = wait.until(EC.presence_of_element_located(
    #     (By.XPATH, "//div[@title='Search input textbox']")))
    # search_box.click()
    # search_box.send_keys(target)
    # press_enter(search_box)

    # # find Type a message box and type message
    # message_box = wait.until(EC.presence_of_element_located(
    #     (By.XPATH, "//div[@title='Type a message']")))

    # message_box.click()
    # message_box.send_keys(message)
    # press_enter(message_box)

    input()
    driver.quit()


def press_enter(element):
    element.send_keys(Keys.ENTER)
