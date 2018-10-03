import Adafruit_DHT
import requests
import os
import datetime
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

#moisture sensor 1
m1pin = 14
GPIO.setup(m1pin, GPIO.IN)

#moisture sensor 2
m2pin = 15
GPIO.setup(m2pin, GPIO.IN)

#temperature sensor
sensor = 22
pin = 4


while 1 == 1:

        print("Moisture Sensor 1: " + str(GPIO.input(m1pin)))
        r = requests.get("http://www.yourwebsite.com/YourService/Service.asmx/LogMoisture?sensorID=m1&reading=" + str(GPIO.input(m1pin)))
        print "Mositure 1 status: " + str(r.status_code)

        print("Moisture Sensor 2: " + str(GPIO.input(m2pin)))
        r = requests.get("http://www.yourwebsite.com/YourService/Service.asmx/LogMoisture?sensorID=m2&reading=" + str(GPIO.input(m2pin)))
        print "Moisture 2 status: " + str(r.status_code)


        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

        temperature = temperature * 9/5.0 + 32
        print humidity
        print temperature
        r = requests.get("http://www.yourwebsite.com/YourService/Service.asmx/LogTemp?sensorID=tempsensor1&temp=" + str(temperature) + "&humidity=" + str(humidity))
        print "http://www.yourwebsite.com/YourService/Service.asmx/LogTemp?sensorID=tempsensor1&temp=" + str(temperature) + "&humidity=" + str(humidity)

        print r.status_code

        t = datetime.datetime.now()
        os.system('kill fswebcam')
        os.system('fswebcam -r 800x600 /home/pi/scripts/smartGarden/img/img' + t.strftime("%m-%d-%Y_%H_%M_%S") + '.jpg')
        os.system('/home/pi/scripts/smartGarden/ftpUpload.sh')

        time.sleep(300)
