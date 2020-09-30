#-------------------------------------------------------------------------------
# Name: Ramil Chaimongkolbutr
# Project: 6
# Section: 209
# Due Date: 12/8/2018
#------------------------------------------------------------------------------

class Line:
	def __init__(self, name, area_code, number, is_active=True):
		self.name = name
		self.area_code = area_code
		self.number = number
		self.is_active = is_active
		
	def __str__(self):
		return ("%d-%d(%s)" %(self.area_code, self.number, self.name,))
	
	def __repr__(self):
		return ("Line('%s', %d, %d)" %(self.name, self.area_code, self.number))
		
	def __eq__(self, other):
		if (self.area_code == other.area_code) and (self.number == other.number):
			return True
		else:
			return False
			
	def activate(self):
		self.is_active = True
		return None
	#change value of is_active to True
	def deactivate(self):
		self.is_active = False
		return None
	#change value of is_active to False	
	
class Call:
	def __init__(self, caller, callee, length):
		try:	
			self.caller = caller
			self.callee = callee
			self.length = length
			if (self.caller.is_active == False) or (self.callee.is_active == False):
				if (self.caller.is_active == self.callee.is_active):
					raise CallError("line {} not active".format(str(self.caller)))
	#error if both are False. The error raises for caller. 
				elif (self.caller.is_active == False):
					raise CallError("line {} not active".format(str(self.caller)))
	#error if caller is inactive.
				else:
					raise CallError("line {} not active".format(str(self.callee)))
	#error if callee is inactive.
			elif self.caller.__eq__(self.callee) ==True:
				raise CallError("line {} cannot call itself".format(str(self.caller)))
	#error if caller and callee are the same in area code and number
			elif self.length < 0:
				raise CallError("negative call length: {}".format(self.length)) 
	#error if the argument contains negative number. 
		except CallError:
			raise
	#except code and print the error massage.
	def __str__(self):
		return ("Call(%s, %s, %d)" % (repr(self.caller), repr(self.callee), self.length))
	
	def __repr__(self):
		return str(self)
	
	def is_local(self):
		if self.caller.area_code == self.callee.area_code:
			return True
		else:
			return False
			
class CallError(Exception):
	def __init__(self, msg):
		self.msg = msg
	
	def __str__(self):
		return ("CallError: %s" % self.msg)
	
	def __repr__(self):
		return ("CallError('%s')" % self.msg)
	#class of CallError.
	
class PhonePlanError(Exception):
	def __init__(self, msg):
		self.msg = msg
		
	def __str__(self):
		return ("PhonePlanError: %s" % self.msg)
		
	def __repr__(self):
		return ("PhonePlanError('%s')" % self.msg)
	#class of PhonePlanError.	

class PlanType:
	def __init__(self, basic_rate, default_mins, rate_per_min, has_rollover=True):
		self.basic_rate = basic_rate
		self.default_mins = default_mins
		self.rate_per_min = rate_per_min
		self.has_rollover = has_rollover
	
	def __str__(self):
		return ("PlanType(%.2f, %.2f, %.2f, %r)" %(self.basic_rate, self.default_mins, self.rate_per_min, self.has_rollover))
		
	def __repr__(self):
		return str(self)
		
class PhonePlan:
	def __init__(self, type, lines=None):
		self.type = type
		self.calls = []
		if lines == None:
			self.lines = []
		#When lines is not given, we use [] as a value of lines.
		else:
			self.lines = lines 
		self.balance = 0
		self.rollover_mins = 0
		self.mins_to_pay = 0
		
	def __str__(self):
		return ("PhonePlan(%s, %r, %r)" % (str(self.type), self.lines, self.calls))
		
	def __repr__(self):
		return str(self)
		
	def activate_all(self):
		for i in self.lines:
			i.activate()
		#use activate function to activate line one by one
		return None
		
	def deactivate_all(self):
		for i in self.lines:
			i.deactivate()
		#use activate function to deactivate line one by one
		return None
	
	def add_call(self, call):
		self.call = call
		try:
			if (self.call.caller in self.lines) or (self.call.callee in self.lines):
				self.calls.append(self.call)
				if not self.call.is_local():
					self.mins_to_pay += self.call.length
		#if the line is local, no need to add length
				else:
					pass	
				
			else:
				raise PhonePlanError("call cannot be added")
				
			return None
			
		except PhonePlanError:
			raise
		#use blank raise to handle exception in later add_call
	def remove_call(self, call):
		self.call = call
		try:
			if self.call in self.calls:
				self.calls.remove(self.call)
			else:
				raise PhonePlanError("no such call to remove")
		#error raises when call doesn't exist in calls	
			return None
		
		except PhonePlanError:
			raise
			
	def add_calls(self, calls):
		count = 0
		for i in calls:
			try:
				self.add_call(i)
				count += 1
			except:
				count += 0
				continue
		#use error handling to interupt the loop 	
		return count
		
	def make_call(self, caller, callee, length):
		try:
			x = Call(caller, callee, length)
			self.add_call(x)
		#create a call using given caller and callee
			return True
		except:
			return False
		#if error occurs, considers it as fall, return False.
	def mins_by_line(self, line):
		count = 0
		for i in self.calls:
			if i.caller.__eq__(line) or i.callee.__eq__(line):
				count += i.length
		#count the minutes associates with the line using __eq__ function.		
		return count 
	
	def calls_by_line(self, line):
		count = 0
		for i in self.calls:
			if i.caller.__eq__(line) or i.callee.__eq__(line):
				count += 1
		#count how many call associates with the line using __eq__ function.		
		return count 
	
	def add_line(self, line):
		for i in self.lines:
			try:
				if i.__eq__(line):
					raise PhonePlanError("duplicated_line_to_add")
		#error raises when we try to add a dupicated line
				else:
					continue
			except PhonePlanError:
				raise 
		self.lines.append(line)
		
		return None
		
	def remove_line(self, line):
		try:
			if line not in self.lines:
				raise PhonePlanError("no such line to remove")
		#error rasies when line is not present in list of lines
			else:
				self.lines.remove(line)
				
				for i in self.calls:
					if i.caller.__eq__(line) or i.callee.__eq__(line):
						self.calls.remove(i)
		#remove any call that associates with line 
			return None
					
		except PhonePlanError:
			raise
		
	def calculate_bill(self):
	#calculate the amount to pay based on the billing activity
		incoming_balance = 0
		#under-used
		if self.mins_to_pay <= self.type.default_mins:
			incoming_balance = self.type.basic_rate
			
			#update rollover_mins in case munites are unused
			if self.type.has_rollover == True:
				self.rollover_mins += (self.type.default_mins - self.mins_to_pay)
			else:
				self.rollover_mins = 0
		#over-used
		else:
			x = self.mins_to_pay - self.type.default_mins
			if (x - self.rollover_mins) > 0:
				incoming_balance = self.type.basic_rate + ((x - self.rollover_mins) * self.type.rate_per_min)
			#update rollover_mins in case it's all spent	
				self.rollover_mins = 0
			else:
				incoming_balance = self.type.basic_rate
			#update rollover_mins in case it's left
				self.rollover_mins += self.rollover_mins - x
				
	
		#update balance, mins_to_pay and call list	
		self.balance += incoming_balance
		xs = self.calls[:]
		for i in xs:
			self.remove_call(i)
		self.mins_to_pay = 0
		if self.balance >= 4*self.type.basic_rate:
			self.deactivate_all()
			
		return None
	
	def pay_bill(self, amount=None):
		
		try:
		#pay all balance
			if amount == None:
				self.balance = 0
			
			elif amount <= 0:
				raise ValueError("amount to pay cannot be negative")
				
			else:
				self.balance +- amount
			
		except ValueError:
			raise 
		#updated balance lower than 4 times of basic_rate, activate all lines 	
		if self.balance < 4*self.type.basic_rate:
			self.activate_all()	