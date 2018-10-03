import time
import urllib.request
import ssl
import re

from time import strftime
#Cory Cranford
#Python HW 2 - 9/25

#2.2

url = "https://tycho.usno.navy.mil/timer.html"

def getTimes(url):
    try:
        context = ssl._create_unverified_context()
        page = urllib.request.urlopen(url, context=context)
        page_text = page.read().decode("utf8")
    except:
        print("Connection failed! Please make sure you're connected to the Internet!")
        return False

    mdt = re.search(r'\d\d\:\d\d\:\d\d\s\wM\sMDT', page_text)
    edt = re.search(r'\d\d\:\d\d\:\d\d\s\wM\sEDT', page_text)
    akdt = re.search(r'\d\d\:\d\d\:\d\d\s\wM\sAKDT', page_text)
    localTime = strftime("%M")

    mdtMinutes = re.split(r':', mdt.group(0))

    print("MDT is: " + mdt.group(0))
    print("EDT is: "+edt.group(0))
    print("AKDT is: "+akdt.group(0))
    if(localTime != str(mdtMinutes[1])):
        print("Local Computer time is off, Local time in minutes is: "+localTime)

time = getTimes(url)