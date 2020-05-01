'''

Update Logs

- Fixed issues with logging in includes recaptchas and 2fa

- Added comments

If you are a dev and would like to add to the repo please do as well if you want me to continue supporting this repo donations are appericated and can be send to PayPal jaredrego1@hotmail.ocm 


'''


# Importing Other libaries
from selenium import webdriver
import json
import os
import time




# Loading data from config.txt
path = os.path.dirname(os.path.abspath(__file__))
with open(path + '\\config.txt', 'r') as f:
    config = json.load(f)

    email = config['email']
    password = config['password']

    url = config['url']

# initilzing selenium
driver = webdriver.Chrome()


def main():
    driver.get('https://www.amazon.com/ap/signin?_encoding=UTF8&ignoreAuthState=1&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&switch_account=') # login url
    print('Manual Sign in Enabled\nPlease Sign in within 20 seconds !')
    time.sleep(20)

    '''
    Removed Auto Sign in So Users Are Able to Manually do it incase of captchas ( Feel free to un comment the lines below and it will enable it)


    #driver.find_element_by_xpath('//*[@id="ap_email"]').send_keys(str(email))
    #driver.find_element_by_xpath('//*[@id="continue"]').click()
    #driver.find_element_by_xpath('//*[@id="ap_password"]').send_keys(str(password))
    #driver.find_element_by_xpath('//*[@id="signInSubmit"]').click()


	'''

    driver.get(str(url)) # getting url from txt file

    while True: # Creating a loop

        try: # Allows us to pass errors through

            driver.find_element_by_xpath('//*[@id="buy-now-button"]').click() # Attempts to click buy now on item
            print('Product in stock checking out...')
            time.sleep(.1) # sleeping for 100 ms to avoid loading errors
            driver.find_element_by_xpath('//*[@id="address-book-entry-0"]/div[2]/span/a').click()
            print('Default Card Selected!')
            driver.find_element_by_xpath('//*[@id="pp-bwShWI-82"]/span/input').click() # Clicking continue button

            # Try your best to follow along here
            prime_sucks = driver.current_url


            if 'primeinterstitial' in prime_sucks: # Amazon has a bunch of annoying popups in this code we are checking if they want us to join prime and saying NO!

            	driver.find_element_by_xpath('//*[@id="primeAutomaticPopoverAdContent"]/div/div[1]/div[1]/a').click()
            	driver.find_element_by_xpath('//*[@id="placeYourOrder"]/span/input').click()
            	print('Order Placed !')

            else:
            	# This statment if if the popup isnt there
            	driver.find_element_by_xpath('//*[@id="placeYourOrder"]/span/input').click()
            	print('Order Placed !')

            	# Default Shipping method is always choosen please becareful of this

        except:

            time.sleep(2.5) # Takes a 2 second break before refreshing page
            driver.refresh()
            print('OOS retrying...') # prints OOS

            # loop repeats

main()
