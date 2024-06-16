#from vision import trash
#from servos import servorun
#from distance import distanceSensor


#imagepath = "/home/mich/smieci/1.jpg"
#vision = trash(imagepath)
#print(vision)

#hiPrompt = open("prompts/hi.txt", "r")
#print(hiPrompt.read())

from distance import sensor
from vision import trash
from picamera import PiCamera
from time import sleep
from gpiozero import DistanceSensor
from voice import talk
from vision import trash
from servos import I2C_Controller


sensor = DistanceSensor(trigger=18, echo=24)
while True:
    # Wait 2 seconds
    sleep(2)
        
    # Get the distance in metres
    distance = sensor.distance

    # But we want it in centimetres
    distance = sensor.distance * 100

    # We would get a large decimal number so we will round it to 2 places
    distance = round(sensor.distance, 2)

    if distance <= 0.1:
        camera = PiCamera()
        camera.start_preview()
        sleep(3)
        camera.capture('photos/photo.jpg')
        camera.stop_preview()
        trash_type = trash('photos/photo.jpg')
        controller = I2C_Controller(0x40, debug=False)
        controller.setPWMFreq(50)
        if trash_type == 'Plastic':
            controller.Set_Pulse(15, 500) # 0 degrees
        elif trash_type == 'Paper':
            controller.Set_Pulse(15, 1500) # 120 degrees
        elif trash_type == 'Glass':
            controller.Set_Pulse(15, 2500) # 240 degrees

    elif distance > 0.1 and distance <= 0.5:
        talk('voice/hello.mp3')
    
