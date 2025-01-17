#import RPi.GPIO as GPIO
from time import sleep

notes = {
  8 : { 'q' : 261.63, 'h' : False }, # c4
 10 : { 'q' : 277.18, 'h' : False }, # c4#
 12 : { 'q' : 293.66, 'h' : False }, # d4
 16 : { 'q' : 311.13, 'h' : False }, # d4#
 18 : { 'q' : 329.63, 'h' : False }, # e4
 22 : { 'q' : 349.23, 'h' : False }, # f4
 24 : { 'q' : 369.99, 'h' : False }, # f4#
 26 : { 'q' : 392.00, 'h' : False }, # g4
 28 : { 'q' : 415.30, 'h' : False }, # g4#
 32 : { 'q' : 440.00, 'h' : False }, # a4
 36 : { 'q' : 466.16, 'h' : False }, # a4#
 38 : { 'q' : 493.88, 'h' : False }, # b4
 40 : { 'q' : 523.25, 'h' : False }  # c5
}

#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)

for pin in notes.keys():
  print(f'GPIO.setup({pin}, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)')
#  GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#out = GPIO.PWM(3, 100)
#GPIO.setup(3, GPIO.OUT)
#out.start(50)
#GPIO.output(3, GPIO.LOW)

while True:
  for pin in notes.keys():
    print(f'Querying {pin}')
    if False != notes[pin]['h']:
      print(f"{notes[pin]['h']} = False")
#    if GPIO.input(pin) != notes[pin]['h']:
#      notes[pin]['h'] = GPIO.input(pin)
#      out.ChangeFrequency(notes[pin]['q'])
#      GPIO.output(3, GPIO.input(pin))
  sleep(0.1)
