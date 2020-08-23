import time
from selenium import webdriver
import Locators as locator
import functions as function
# navigate to website

#driver = webdriver.Chrome('./chromedriver')  # change as per your location

print('Select from the following')
print('1. Log in')
print('2. Create User')
print('3. Create Vendor')
print('4. Delete Vendor')
print('5. Associate Client and Vendor')
print('')
switch = int(input())
function.start()
if switch == 1:
#log_in
    function.login()

elif switch == 2:
#create user
    if function.login():

elif switch == 3:
# create vendor
   if function.login():
        function.CreateVendor()

elif switch == 4: # delete Vendor

elif switch == 5:   # Associate client and vendor

elif switch == 6:

else
    print('nothing')
# create user
    exit()
#function.login()


