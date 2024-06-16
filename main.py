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
# import picamera
from time import sleep
from gpiozero import DistanceSensor
from voice import talk
from vision import trash
from servos import I2C_Controller
import subprocess

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
    print(distance)
    if distance <= 0.3:
        # camera = PiCamera()
        # camera.start_preview()
        # sleep(3)
        # camera.capture('photos/photo.jpg')
        # camera.stop_preview()
        # Define the bash command
        subprocess.run("bash perfect.sh")
        command = ["libcamera-jpeg", "-o", "photos/photo.jpg", "--timeout", "1500"]
    

        # Run the command
        result = subprocess.run(command, capture_output=True, text=True)

        # Print the output and error (if any)
        print("stdout:", result.stdout)
        print("stderr:", result.stderr)
        subprocess.run("bash process.sh")
        trash_type = trash('photos/photo.jpg')
        controller = I2C_Controller(0x40, debug=False)
        controller.setPWMFreq(50)
        if trash_type == 'plastic':
            subprocess.run("bash plastic_in.sh")
            controller.Set_Pulse(15, 500) # 0 degrees
            sleep(3)
            controller.Set_Pulse(11, 2500) # opening 
            sleep(5)
            controller.Set_Pulse(11, 400) # closing
            subprocess.run("bash plastic_out.sh")
        elif trash_type == 'paper':
            subprocess.run("bash paper_in.sh")
            controller.Set_Pulse(15, 1300) # 0 degrees
            sleep(3)
            controller.Set_Pulse(11, 2500) # opening 
            sleep(5)
            controller.Set_Pulse(11, 400) # closing
            subprocess.run("bash paper_out.sh")
        elif trash_type == 'glass':
            subprocess.run("bash glass_in.sh")
            controller.Set_Pulse(15, 2200) # 0 degrees
            sleep(3)
            controller.Set_Pulse(11, 2500) # opening 
            sleep(5)
            controller.Set_Pulse(11, 400) # closing
            subprocess.run("bash glass_out.sh")
        elif trash_type == 'bio':  
            subprocess.run("bash bio_out.sh")
        elif trash_type == 'ewaste':  
            subprocess.run("bash electro_out.sh")
        elif trash_type == 'mutiple':  
            subprocess.run("bash multiple_out.sh")
        elif trash_type == 'no':  
            subprocess.run("bash no_out.sh")

    elif distance > 0.3 and distance <= 0.7:
        command_voice = 'cvlc --play-and-exit voice/hello.mp3'
        username = 'binaily'
        full_command =["su -c cvlc --play-and-exit voice/hello.mp3 binaily"]
        subprocess.run(full_command)
    
