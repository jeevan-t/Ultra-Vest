#Libraries
import RPi.GPIO as GPIO
import time
import threading

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
GPIO_TRIGGER1 = 17
GPIO_ECHO1 = 27
GPIO_VIB1 = 19

GPIO_TRIGGER2 = 15
GPIO_ECHO2 = 18
GPIO_VIB2 = 13

GPIO_TRIGGER3 = 9
GPIO_ECHO3 = 11
GPIO_VIB3 = 26

GPIO_TRIGGER4 = 25
GPIO_ECHO4 = 8
GPIO_VIB4 = 6

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER1, GPIO.OUT)
GPIO.setup(GPIO_ECHO1, GPIO.IN)
GPIO.setup(GPIO_VIB1, GPIO.OUT)

GPIO.setup(GPIO_TRIGGER2, GPIO.OUT)
GPIO.setup(GPIO_ECHO2, GPIO.IN)
GPIO.setup(GPIO_VIB2, GPIO.OUT)

GPIO.setup(GPIO_TRIGGER3, GPIO.OUT)
GPIO.setup(GPIO_ECHO3, GPIO.IN)
GPIO.setup(GPIO_VIB3, GPIO.OUT)

GPIO.setup(GPIO_TRIGGER4, GPIO.OUT)
GPIO.setup(GPIO_ECHO4, GPIO.IN)
GPIO.setup(GPIO_VIB4, GPIO.OUT)


def distance(GPIO_TRIGGER, GPIO_ECHO):
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 	
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance




if __name__ == '__main__':


    try:
        while True:
            dist1 = distance(GPIO_TRIGGER1, GPIO_ECHO1)
            print ("Measured Distance 1 = %.1f cm" % dist1)
            time.sleep(.25)

            dist2 = distance(GPIO_TRIGGER2, GPIO_ECHO2)
            print ("Measured Distance 2 = %.1f cm" % dist2)
            time.sleep(.25)

            dist3 = distance(GPIO_TRIGGER3, GPIO_ECHO3)
            print ("Measured Distance 3 = %.1f cm" % dist3)
            time.sleep(.25)

            dist4 = distance(GPIO_TRIGGER4, GPIO_ECHO4)
            print ("Measured Distance 4 = %.1f cm" % dist4)
            time.sleep(.25)

            if dist1 <  100:
                GPIO.output(GPIO_VIB1, True)
            else:
                GPIO.output(GPIO_VIB1, False)

            if dist2 <  100:
                GPIO.output(GPIO_VIB2, True)
            else:
                GPIO.output(GPIO_VIB2, False)

            if dist3 <  100:
                GPIO.output(GPIO_VIB3, True)
            else:
                GPIO.output(GPIO_VIB3, False)

            if dist4 <  100:
                GPIO.output(GPIO_VIB4, True)
            else:
                GPIO.output(GPIO_VIB4, False)

 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
