#! python3

# stopwatch.py - simple stopwatch program

import time

# Display the program's instructions.
print("Press enter to begin - pressing enter again will 'Click' the watch. Press CTRL-C to kill program.")

input()

print("Started...")

startTime = time.time()
lastTime = startTime
lapNum = 1

#TODO: Start tracking lap time.

try:
	while True:
		input()
		lapTime = round(time.time() - lastTime, 2)
		totalTime = round(time.time() - startTime, 2)
		print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
		lapNum += 1
		lastTime = time.time() # resets the last lap time

except KeyboardInterrupt:
	#CTRL-C exception will not be displayed
	print('\nDone')
