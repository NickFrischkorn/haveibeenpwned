# HIBP APIv3 Email Checker

Quick python script to interact with the HIBP APIv3 and check if emails are involved in any data breaches, and if so return which.

emailcheck.py requires a valid HIBP APIv3 key and takes a list of emails (one per line in a text file) as input. The output is an Excel file containing all emails from the list that were found to be part of a databreach accompanied by which data breaches they were found in.
