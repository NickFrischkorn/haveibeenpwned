import pandas as pd
import requests
import time

key = "" # -- Insert HIBP APIv3 key here --
email_file = "" # -- Insert path to file containing email list --

master_output = []
head = {"User-Agent": "HIBP-Email-Checker", "hibp-api-key": key}
email_list = open(email_file)

for email in email_list:
    email = email.replace('\n', '') # remove trailing carriage return
    time.sleep(1.7) # rate limiting for APIv3 is 1500 milliseconds, so 1700 to avoid triggering
    try:
        hibp_check = requests.get(url='https://haveibeenpwned.com/api/v3/breachedaccount/' + email, headers=head)
        if len(hibp_check.text > 3: # if response is not empty
               response = hibp_check.text
               response = hibp_check.replace('Name', '')
               response = hibp_check.replace('{', '')
               response = hibp_check.replace('}', '')
               response = hibp_check.replace('[', '')
               response = hibp_check.replace(']', '')
               response = hibp_check.replace(':', '')
               response = hibp_check.replace('"', '')
               loop_output = []
               loop_output.append(email)
               loop_output.append(response)
               master_output.append(loop_output)
    except:
        pass
     
df = pd.DataFrame(master_output)
df.to_excel('HIBP-Emails-Output.xlsx', sheet_name='1. HIBP Emails', headers=['Email', 'HIBP Data Breaches Found In'])
