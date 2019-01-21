
import RPi.GPIO as GPIO
import time
import urllib

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)


try :
    url = "https://www.bbc.co.uk"
    urllib.urlopen(url)
    status = "Connected"
    GPIO.output(18,GPIO.HIGH)
except :
    status = "Not connect"
    GPIO.output(18,GPIO.LOW)
print (status)
