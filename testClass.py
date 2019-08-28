#! python3

# personClass.py
import time
class person:
	
	def __init__(self, age, name):
		self.age = age
		self.name = name
		self.clockin = time.time()
		self.clockout = 00
		
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

test = person(28, "tyler")
print(test.age)
print(test.name)

print('\n\n ******')

test.set_name('trev')
test.set_age(99)
time.sleep(6) # To verify that the clock is working
clockedOut = time.time()
# print('clockedout = %d' % clockedOut) verification 
test.clockOut(clockedOut)
test.setWorkDuration(test.clockout)
print(test.age)
print(test.name)
print(round(test.workDuration))
