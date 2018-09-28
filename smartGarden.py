import Adafruit_DHT
import requests
import os
import datetime
import time

#temperature sensor
sensor = 22
pin = 4

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

temperature = temperature * 9/5.0 + 32

r = requests.get("http://www.thejoestory.com/SmartGarden/Service.asmx/LogTemp?sensorID=tempsensor1&temp=" + str(temperature) + "&humidity=" + str(humidity))
print r.status_code

t = datetime.datetime.now()
os.system('fswebcam -r 800x600 /home/pi/scripts/smartGarden/img/img' + t.strftime("%m-%d-%Y_%H_%M_%S") + '.jpg')
