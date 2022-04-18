import os
from whatsapp import *

if __name__ == "__main__":
    print("Starting Whatsapp automation")

    # setting environment veriables
    os.environ['driver_location'] = "../resource/chromedriver.exe"
    os.environ['profile_data_location'] = "C:/Users/parth/AppData/Local/Google/Chrome/User Data/CustomProfiles"
    os.environ['profile_folder'] = 'Profile 1'
    automate()
    print("Ending Whatsapp automation")
