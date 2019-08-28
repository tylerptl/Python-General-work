#! python3

import time

# employeeClock.py - This will record the duration from when an employee clocks in to when
# they clock out
employeeName = ""
global startTime
startTime = 0

def ask_user():
	print('What is the employee name?')
	employeeName = input()
	check = str(input("Employee = %s. Is this correct? Y/N" % employeeName)).lower().strip()
	try:
		if check[0] == 'y':
			global startTime
			startTIme = time.time()
			print('%s has now clocked in. Beginning shift timer. (%d)' % (employeeName, startTime))
			return True
		elif check[0] == 'n':
			return False
		else:
			print('Invalid input...')
			return ask_user()
	except Exception as error:
		print("Please enter valid inputs.")
		print(error)
		return ask_user()

def ask_user_clockOut():
	# print('Would you like to clockout the current employee (%s)? Y/N' % employeeName)
	global startTime
	check = str(input("Would you like to clockout the current employee (%s)? Y/N" % employeeName)).lower()
	try:
		if check[0] == 'y':
			stopTime = time.time()
			print('%s has clocked out. They worked for %d seconds' % (employeeName, (time.time() - startTime)))
			return True
		elif check[0] == 'n':
			return False
		else:
			print('Invalid input...')
			return ask_user_clockOut()
	except Exception as error:
		print("Please enter valid inputs...")
		print(error)
		return ask_user_clockOut()


print('Press Enter to get started...')

input()

ask_user()
# print('%s has now clocked in. Beginning shift timer.' % employeeName)
# startTIme = time.time()

while True:
	print('\n\nClock running... Press enter to access clock. Exit program with CTRL-C.')
	if input() == '':
		ask_user_clockOut()

# input()

# print('Would you like to	 clock out the current employee (%s)? Y/N' %employeeName)

# if input() == 'Y' or 'y':
# 	stopTime = time.time()
# 	print('%s has been clocked out. They worked for %d seconds' %(employeeName, (stopTime - startTime)))



