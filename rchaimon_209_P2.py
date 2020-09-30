#-------------------------------------------------------------------------------
# Name: Ramil Chaimongkolbutr
# Project 2
# Due Date: 12/31/1999
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: (list resources used - remember, projects are individual effort!)
#-------------------------------------------------------------------------------
# Comments and assumptions: A note to the grader as to any problems or 
# uncompleted aspects of the assignment, as well as any assumptions about the
# meaning of the specification.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#       10        20        30        40        50        60        70        80
#-------------------------------------------------------------------------------

# this time, the template does not have as much guidance - please
# look at at the actual project specification for the rules and
# meanings of each function. You can modify any part of the template
# code to get the job done (abiding by the project's rules). For
# instance, you might want a different start value, or to use multiple
# return statements. This template is only offered in order to help
# you get started, it is not truly required in any sense for the 
# project. The function and parameter names must remain the same (e.g.,
# discount and age/major/is_in_military/gpa), but you can use any names you want
# inside of the functions (indented).

def discount(age, major, is_in_military, gpa):
	ans = False
	
	if str(major) == "Computer Science" and float(gpa) >= 3.5:
		ans = True
		
	elif int(age) >= 65: 
		ans = True
		
	elif bool(is_in_military): 
		ans = True
	else:
		ans = False
		
	return ans

def calculate_cost(plan, num_minutes, num_text):
	ans = 0
	
	if str(plan) == "basic":
		add_minutes = 0
		add_text = 0
		
		if num_minutes > 100:
			add_minutes = (num_minutes - 100) * 1.5
		if num_text > 1000:
			add_text = (num_text - 1000) * 0.75
		
		ans = float(15 + add_minutes + add_text)
	
	elif str(plan) == "standard":
		add_minutes = 0
		add_text = 0
		
		if num_minutes > 175:
			add_minutes = (num_minutes - 175) * 1.25
		if num_text > 1500:
			add_text = (num_text - 1500) * 0.5
		
		ans = float(20 + add_minutes + add_text)
	
	elif str(plan) == "premium":
		add_minutes = 0
		add_text = 0
		
		if num_minutes > 250:
			add_minutes = (num_minutes - 250) * 1
		if num_text > 2000:
			add_text = (num_text - 2000) * 0.25
		
		ans = float(25 + add_minutes + add_text)	
	
	return ans

def cost_efficient_plan(age, major, is_in_military, gpa, num_minutes, num_text):
	ans = ""
	cost_basic = 0
	cost_standard = 0
	cost_premium = 0
	discount_basic = discount(age, major, is_in_military, gpa)
	
	if discount_basic == True:
		cost_basic = 0.8 * calculate_cost("basic", num_minutes, num_text)
	else:
		cost_basic = calculate_cost("basic", num_minutes, num_text)
	
		
	cost_standard = calculate_cost("standard", num_minutes, num_text)
	cost_premium = calculate_cost("premium", num_minutes, num_text)
	
	#print(discount_basic)
	#print(cost_basic, cost_standard, cost_premium)
	
	if cost_basic < cost_standard < cost_premium:
		ans = "basic"
	elif cost_basic < cost_premium < cost_standard:
		ans = "basic"
	elif cost_standard < cost_basic < cost_premium:
		ans = "standard"
	elif cost_standard < cost_premium < cost_basic:
		ans = "standard"
	elif cost_premium < cost_standard < cost_basic:
		ans = "premium"
	elif cost_premium < cost_basic < cost_standard:
		ans = "premium"
	elif cost_basic == cost_standard and cost_basic < cost_premium:
		ans = "standard"
	elif cost_basic == cost_premium and cost_basic < cost_standard:
		ans = "premium"
	elif cost_basic == cost_standard and cost_basic > cost_premium:
		ans = "premium"
	elif cost_basic == cost_premium and cost_basic > cost_standard:
		ans = "standard"
	elif cost_standard == cost_premium and cost_standard < cost_basic:
		ans = "premium"
	elif cost_standard == cost_premium and cost_standard > cost_basic:
		ans = "basic"
	elif cost_basic == cost_standard == cost_premium:
		ans = "premium"
	
	return ans

def plan_range(num_minutes):
	chart = ""
	
	if num_minutes < 0 or (num_minutes % 1) != 0:
		print("error")
		pass
	else:
		head = "Mins\tBasic\tStd\tPremium\n"
		
		count = 0
		sum_chart = ""
		while count < 10:
			cost_basic = 0.8 * calculate_cost("basic", num_minutes, 1000)
			cost_standard = calculate_cost("standard", num_minutes, 1000)
			cost_premium = calculate_cost("premium", num_minutes, 1000)
			#print(str(num_minutes) + "\t" + str(num_minutes))
			
			add_chart = str(num_minutes) + "\t" + str(cost_basic) + "\t" + str(cost_standard) +"\t" + str(cost_premium) + "\n"	
			sum_chart = sum_chart + add_chart
			
			count += 1
			num_minutes += 10
			
		chart = head + sum_chart	
	
	return chart