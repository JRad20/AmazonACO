'''


    This is an open sourced amazon full checkout script created to help people check out neccicities please do not use this script to later resell the items.

    Scripted Made By J_Rad20#0001

'''


from selenium import webdriver
import json
import os
import time

path = os.path.dirname(os.path.abspath(__file__))
with open(path + '\\config.txt', 'r') as f:
    config = json.load(f)
    email = config['email']
    password = config['password']
    url = config['url']

driver = webdriver.Chrome()
def main():
    driver.get('https://www.amazon.com/ap/signin?_encoding=UTF8&ignoreAuthState=1&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&switch_account=')
    driver.find_element_by_xpath('//*[@id="ap_email"]').send_keys(str(email))
    driver.find_element_by_xpath('//*[@id="continue"]').click()
    driver.find_element_by_xpath('//*[@id="ap_password"]').send_keys(str(password))
    driver.find_element_by_xpath('//*[@id="signInSubmit"]').click()
    driver.get(str(url))
    while True:
        try:
            driver.find_element_by_xpath('//*[@id="buy-now-button"]').click()
        except:
            time.sleep(1)
            print('OOS retrying...')
main()