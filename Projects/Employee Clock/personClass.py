#! python3

# personClass.py
import time

people = list()
tempName = " "
class person:
	def __init__(self):
		self.name = 'blank'
		self.clockin = time.time()
		self.clockout = 00
		# self.workDuration = self.clockout - self.clockin
	def set_age(self, n):
		self.age = n 
		print('Age now set to %d' % self.age)

	def set_name(self, str):
		self.name = str
		print('Name updated to: %s' % self.name)

	def setWorkDuration(self, n):
		self.workDuration = n - self.clockin

	def clockOut(self, n):
		self.clockout = n	

# test = person(28, "tyler")
# print(test.age)
# print(test.name)

# print('\n\n ******')

# test.set_name('trev')
# test.set_age(99)
# time.sleep(6) # To verify that the clock is working
# clockedOut = time.time()
# # print('clockedout = %d' % clockedOut) verification 
# test.clockOut(clockedOut)
# test.setWorkDuration(test.clockout)
# print(test.age)
# print(test.name)
# print(round(test.workDuration))



#TODO Enable clocking in/out on command
def ask_user():
	global people
	global tempName
	print('What is the employee name?')
	employeeName = input()
	check = str(input("Employee = %s. Is this correct? Y/N" % employeeName)).lower().strip()
	try:
		if check[0] == 'y':
			temp = person()
			temp.set_name(employeeName)
			people.append(temp)
			print('%s has now clocked in. Beginning shift timer. (%d)' % (employeeName, temp.clockin))
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
	global people
	global tempname 
	check = str(input("Would you like to clockout a current employee? Y/N" )).lower()
	try:
		if check[0] == 'y':
			tempName = str(input('What is the employees name?')).lower()
			print('Searching active employees for %s' % tempName)
			stopTime = time.time()
			for val in people:
				if val.name == tempName:
					print('%s has clocked out. They worked for %d seconds' % (val.name, (time.time() - val.clockin)))
					people.remove(val)
				else:
					print('No employee found with that name')
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

def beginning_config():
	checkInput = str(input('To clock-in press 1. To clockout press 2. CTRL-C will exit.'))

	try: 
		if checkInput[0] == '1':
			print('Beginning new employee config...\n\n')
			ask_user()
		elif checkInput[0] == '2':
			print('Entering clock out config...\n\n')
			ask_user_clockOut()
		else:
			print('Invalid input...')
			return beginning_config()
	except Exception as error:
		print('Plese enter a valid input (1/2).')
		print(error)
		return beginning_config()

print('Press Enter to get started...')

input()


while True:
	beginning_config()








