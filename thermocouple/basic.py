from max31855 import MAX31855, MAX31855Error
from time import sleep

cs = 24
clk = 23
data = 22
units = "f"
thermocouple = MAX31855(cs, clk, data, units)


try:
	while True:
		print(thermocouple.get())
		sleep(0.5)

except:
	thermocouple.cleanup()

