# Write your code here :-)
import time
import board
import analogio
import digitalio
import adafruit_dht
import adafruit_scd30
from rgbled import ChainableLED

# Humidity and Temperature
# D2 auf Shield, D5 auf Feather
D2 = adafruit_dht.DHT11(board.D5)

# CO2, Humidity and Temperature
# I2C-1 auf Shield, D23 auf Feather
I2C1 = adafruit_scd30.SCD30(board.I2C())

# Motion
# D4 auf Shield, D9 auf Feather
D4 = digitalio.DigitalInOut(board.D9)
D4.direction = digitalio.Direction.INPUT

# Light
# A0 auf Shield und Feather
A0 = analogio.AnalogIn(board.A0)

# RGB LED
# A2(D16) auf Shield und Feather
A2 = ChainableLED(board.A2, board.A3, 1)

counter = 1
while True:
    print(" -- Loop " + str(counter) + " -- ")
    print("D2 Temperature: " + str(D2.temperature) + " °C")
    print("D2 Humidity: " + str(D2.humidity) + " %%rH")
    print()
    print("I2C1 Temperature: " + str(I2C1.temperature) + " °C")
    print("I2C1 Humidity: " + str(I2C1.relative_humidity) + " %%rH")
    print("I2C1 CO2: " + str(I2C1.CO2) + " PPM")
    print()
    print("D4 Motion: " + str(D4.value))
    print()
    print("A0 Light: " + str(A0.value)) # Wertebereich: 0 - ca. 46500
    print()
    print("Lightshow!!!")
    steps = 5 # longer steps -> shorter cycles
    for i in range(0, 256, steps):   A2.setColorRGB(  i, 255,   0)
    for i in range(255, -1, -steps): A2.setColorRGB(255,   i,   0)
    for i in range(0 ,256, steps):   A2.setColorRGB(255,   0,   i)
    for i in range(255, -1, -steps): A2.setColorRGB(  i,   0, 255)
    for i in range(0, 256, steps):   A2.setColorRGB(  0,   i, 255)
    for i in range(255, -1, -steps): A2.setColorRGB(  0, 255,   i)
    counter +=1
    print()
