#-------------------------------------------------------------------------------
# Name: Ramil Chaimongkolbutr
# Project: 5
# Section: 209
# Due Date: 11/11/2018
#------------------------------------------------------------------------------
	
#The first function I create it for sorting purpose since sort() fucntion is not allowed
def sort_alph(xs):
	xss = []
	
	while xs != []:
		m = min(xs)
		xs.remove(m) 
		xss.append(m)
	return xss
#For sorting alphabetically purpose
	
def read_votes(filename):
	try:
		raw_file = open(filename)			#open and read a file
		lines = raw_file.readlines()		#keep the read file in 'lines' variable
		raw_file.close()
		a = ""
		b = ""
		c = {}
		e = {}
		xs = []
		xss = {}
		spliter_1 = ','
	
		for i in range(1,len(lines)):		#This loop is for slicing the data in the file. We exclude the head so it starts at 1 to slice each data 
			a = lines[i][0:len(lines[i])-1]		#Cut \n out first
			b = a.split(spliter_1)				#Seperate each data from ','. The result we get is a list of each type of data.
			b[-1] = int(b[-1])
			b[-2] = int(b[-2])
			xs.append(b)					#Store all data in a list 'xs'. 
		#print(xs)
		
		
		for i in range(len(xs)):				#In this loop, we manage to convert our list to dictionary.
		
			if not xs[i][0] in xss.keys():			#Check if the key has already add in the dictionary--if not, add it.
				
				c = {xs[i][0]:[tuple(xs[i][1:]),]}	#Create a dictionary variable and add it to the dictionary xss. 
				xss.update(c)
			else:
				d = xss.get(xs[i][0])		#This is a case when the key already exists. We grab the existing value from the dictionary and recreate it. 
				d.append(tuple(xs[i][1:]))	#Add a new value to the existing list.
				e = {xs[i][0]:d}			#Create a new dict variable then add to the dictionary
				xss.update(e)
		
		
		
		for key in xss.keys():
			xss[key] = sort_alph(xss[key])					#Sort alphabetically for candidate's names
			for i in range(len(xss[key])):				#Remove candidate that has negative number of popular_votes
				if int(xss[key][i][2]) < 0:
					xss[key].pop(i)
				else:
					continue
		
		#print(xss)
		return xss
	
	except ValueError:									#Collecting error and return False 
		return False

def write_votes(db, filename):
	try:
		xs = ['state,name,party,popular_votes,electoral_votes\n']			#Create a list variable 'xs' by putting the head of columns at the start.
		gap = ','							
		
		for state, result in db.items():									#Doing the first function backward.
			
			#print(state)
			#print(result)
			for i in result:
				data = []													#create a list to represent each row in excel data
				a = ""
				b = ""
				data.append(state)											#Append the state alphabet first. 
				for j in i:													
					data.append(j)											#Append all remaining value from the dictionary.
				
				#print(data)
				a = gap.join(data)											#join them with ','
				b = a + '\n'												#Add '\n' at the end of each data in excel
				xs.append(b)												#Store each of finishing data in the list 'xs'
		#print(xs)
		
		raw_file = open(filename, 'w')										#Open the file for writing.
		for k in xs:														#Write each menber in the list on excel sheet
			raw_file.write(k)
		raw_file.close()
		

	except:
		return False
		
def read_abbreviations(filename):
	try:
		raw_file = open(filename)			#open and read a file
		lines = raw_file.readlines()		#keep the read file in 'lines' variable
		raw_file.close()
	
		#print(lines)
	
		a = ""
		b = ""
		spliter_1 = ","
		xs = []
		for i in range(1,len(lines)):			#This loop is for slicing the data in the file the same way we did in the first function.
			a = lines[i][0:len(lines[i])-1]		#Cut \n out first
			b = a.split(spliter_1)				#Seperate each data from ','. The result we get is a list of each type of data.  
			xs.append(b)
		xss = dict(xs)							#Create a dictionary out of the list 'xs' 
		return xss
	except:
		return False
		
def add_candidate(db, state, name, party, popular_votes, electoral_votes):
	entry = (name, party, popular_votes, electoral_votes)						#Set up the entry
	dict_entry = {state: [entry]}												#Set up Dictionary entry
	update_check = True															#Use to check if the name can be found in the value
	if state in db.keys():
		for i in range(len(db[state])):
			if db[state][i][0] == name:											#Update entry when the name is found
				db[state][i] = entry
				update_check = False											#Update value switches to False
			else:
				continue
		if update_check:														#When the name can't be found, it'll trigger this if-condition. Then we add the new value to the list.
			db[state].append(entry)
			db[state] = sort_alph(db[state])									#Use defined function to sort name alphabetically.
		else:
			pass	
		
	else:
		db.update(dict_entry)													#Update the whole key if the given state hasn't been in the dictionary.
		
	return None
	
def remove_candidate(db, name, state=None):
	
	if state == None:														#Case 1: state = None, we look for all state in the dictionary
		for key, value in db.items():
			for i in range(len(value)):
				if value[i][0] == name:										#When we find the name, we remove the tuple from the list
					value.remove(value[i])
					break													#break because each name can be presented once in each state.
			if db[key] == []:
				db.pop(key)													#If we found that value of the key is empty, we remove the key from the dictionary.
			else:
				pass
		return None
	
	elif state not in db.keys():											#Cases extra: given state doesn't exist in the dictionary, we return False.
		return False
	
	else:
		for i in range(len(db[state])):										#Cases 2: state is known, we look for a certain given state.
			if db[state][i][0] == name:										#Do exactly the same as case 1 but on;y in particular state.
				db[state].remove(db[state][i])
				break
		if db[state] == []:
			db.pop(state)
		else:
			pass
		
		return None
		
def incorporate_precinct(db, name, state , popular_votes_increment):
	update_check = True													#Set up the update value	
	if state in db.keys():												
		for i in range(len(db[state])):
			if db[state][i][0] == name:									#look for the given name in given state.
				list_a = list(db[state][i])								#Since value in the database1 is a tuple, we copy it and turn into a list because it is mutable.
				list_a[2] = list_a[2] + popular_votes_increment			#Add the increment to the original
				db[state][i] = tuple(list_a)							#Turn it back to a tuple and replace the old tuple
				update_check = False									#Update the update value
				break
			else:
				continue
		if update_check:												#If the update value has been updated, this means that name cannot be found.
			return False
		else:
			return None
	else:
		return False
		
def merge_votes(db, name1, name2, new_name, new_party, state=None):
	if state == None:												#Case 1: we look for all state in the database.
		for key, value in db.items():
			name1_pop = ("","",0,0)
			name2_pop = ("","",0,0)
			
			for i in range(len(value)):				
				if value[i][0] == name1:							#We try to pop data of given name1 from the list value and store it in the variable 'name1_pop'
					name1_pop = value.pop(i)
					break
				else:
					continue
			for j in range(len(value)):								#We try to pop data of given name2 from the list value and store it in the variable 'name2_pop'
				if value[j][0] == name2:
					name2_pop = value.pop(j)
					break
				else:
					continue
			new_votes = name1_pop[2]+name2_pop[2]					#We combine values of 2 popular votes 
			new_electoral = name1_pop[3]+name2_pop[3]				#We combine values of 2 electoral votes
			combination = (new_name, new_party, new_votes, new_electoral)			#Create a new tuple representing as a candidate named "combination," which stores all combined data (new name and party as well)
			add_candidate(db, key, combination[0], combination[1], combination[2], combination[3]) #Use function add_candidate to add 'combination' to the dictionary
			#value.append(combination)
			#value = sort_alph(value)
			#print(combination) 
		return None
	
	elif state not in db.keys():
		return False
	
	else:															#Case 2: state is known, we do exactlythe same as the first part of this function but we look at a specific state. 
		name1_pop = ("","",0,0)
		name2_pop = ("","",0,0)
		for i in range(len(db[state])):
			if db[state][i][0] == name1:
				name1_pop = db[state].pop(i)
				break
			else:
				continue
		for j in range(len(db[state])):
			if db[state][j][0] == name2:
				name2_pop = db[state].pop(j)
				break
			else:
				continue
		new_votes = name1_pop[2]+name2_pop[2]
		new_electoral = name1_pop[3]+name2_pop[3]
		combination = (new_name, new_party, new_votes, new_electoral)
		add_candidate(db, state, combination[0], combination[1], combination[2], combination[3])
		
		return None
		
def number_of_votes(db, name, category='popular',numbering='tally', state=None):
	if category not in ('popular','electoral'):									#Check value of varible "category"
		return False
	elif numbering not in ('tally','percent'):									#Check value of varible "numbering"
		return False
	elif state == None:															#Case 1: State is unknown, we look for all state.
		if category == 'popular':												#Subecase: we only add the popular votes
			count = 0															#Set up initial value "count" for given specific name's votes 
			total = 0
			name_check = True													
			for key, value in db.items():										
				for i in range(len(value)):
					total += value[i][2]										#Every votes will be added in total
					if value[i][0] == name:										#Only votes of the given name will be added in count  
						count += value[i][2]
						name_check = False
					else:
						continue
		elif category == 'electoral':											#Subecase: we only add the electoral votes. Same logic as popular votes
			count = 0
			total = 0
			name_check = True
			for key, value in db.items():
				for i in range(len(value)):
					total += value[i][3]
					if value[i][0] == name:
						count += value[i][3]
						name_check = False
					else:
						continue
		if name_check:
			return False
		ans = round((count/total)*100, 2)										#This is for a requested answer of percent: 2 digits float. 					
		if numbering == 'tally':												#If we want "tally", we return "count" but if we want "percent", we have to calculate it from total, then return "ans" 
			return count
		if numbering == 'percent':
			return ans
		#print(count, total)
		
	elif state != None:															#Case 2: state is known. Everything is almost exactlythe same as Case 1 but we calculate everything based on the given state.
		if category == 'popular':
			count = 0
			total = 0
			name_check = True
			for i in range(len(db[state])):
				total += db[state][i][2]
				if db[state][i][0] == name:
					count += db[state][i][2]
					name_check = False
				else:
					continue
		elif category == 'electoral':
			count = 0
			total = 0
			
			for i in range(len(db[state])):
				total += db[state][i][3]
				if db[state][i][0] == name:
					count += db[state][i][3]
					name_check = False
				else:
					continue
		if name_check:
			return False
		ans = round((count/total)*100, 2)
		if numbering == 'tally':
			return count
		if numbering == 'percent':
			return ans
		#print(count, total)
		
def popular_votes_performance(db, name, numbering, order='max'):
	if numbering not in ('tally','percent'):										#Check both numbering and order variables 
		return False
	elif order not in ('min', 'max'):
		return False
	else:
		if order == 'max':															#Case 1: Maximum votes.
			number = 0																
			max_votes = 0															#Set up initial varibles (For max, we use 0)
			max_state = ''
			for key in db.keys():
				number = number_of_votes(db, name, category='popular', numbering=numbering, state=key) 		#Use function number_of_votes to fine votes.
				if number > max_votes:												#We replace current maximum number if the number we found is greater than the current number (start at 0)
					max_votes = number
					max_state = key													#We collect the current maximum state
				else:
					continue
			#print(max_votes, max_state)
			xss = read_abbreviations('abbreviations.csv')							#Use read_abbreviations function to find what our abbreviations stand for.
			ans = xss[max_state]								
			return ans																#Return the result
			
		elif order == 'min':														#Case 2: Minimum votes.
			number = 0
			min_votes = 10000000000000000000000										#Set up initial variable (For min, we use an extra large number)
			min_state = ''
			for key in db.keys():
				number = number_of_votes(db, name, category='popular', numbering=numbering, state=key)			#Everything else is the same as Max case.
				if number < min_votes:
					min_votes = number
					min_state = key
				else:
					continue
			#print(min_votes, min_state)
			
			xss = read_abbreviations('abbreviations.csv')
			ans = xss[min_state]
			return ans
			
def candidate_difference(db, name1, name2, order='smallest'):
	if order not in ('smallest','largest'):
		return False
	else:
		if order == 'largest':											#Case 1: Largest difference.
			number_dif = 0												#Set up initial variables
			max_dif = 0
			max_dif_state = ""
			for key, value in db.items():								#Create a list containing names in each state
				xs = []
				for i in range(len(value)):
					xs.append(value[i][0])
				#print(xs)
				x1 = 0
				x2 = 0
				if (name1 in xs) and (name2 in xs):						#We use the created list to find if we have 2 given candidates presented in the state
					x1 = number_of_votes(db, name1, category='popular', numbering='percent', state=key)			#Votes of name1 is stored in varible x1 while of name2 is store in variablex2
					x2 = number_of_votes(db, name2, category='popular', numbering='percent', state=key)
					number_dif = max(x1,x2) - min(x1,x2)														#We use max() and min() in this case because we don't want a negative difference
					if number_dif > max_dif:							#Same logic as earlier function--replacing with a new greater value
						max_dif = number_dif
						max_dif_state = key
					else:
						pass
				else:
					continue
			#print(max_dif, max_dif_state)
			xss = read_abbreviations('abbreviations.csv')				#Use read_abbreviations to find what our answer stands for.
			ans = xss[max_dif_state]
			return ans
			
		if order == 'smallest':											#Case 2: Smallest difference
			number_dif = 0												#Everything is almost the same as 'Largest' but the initial min_dif we set and an extra large value
			min_dif = 100000000000000000000
			min_dif_state = ""
			for key, value in db.items():
				xs = []
				for i in range(len(value)):
					xs.append(value[i][0])
				#print(xs)
				x1 = 0
				x2 = 0
				if (name1 in xs) and (name2 in xs):
					x1 = number_of_votes(db, name1, category='popular', numbering='percent', state=key)
					x2 = number_of_votes(db, name2, category='popular', numbering='percent', state=key)
					number_dif = max(x1,x2) - min(x1,x2)
					if number_dif < min_dif:							#Keep replacing with a new smaller number while updating min_dif_state.
						min_dif = number_dif
						min_dif_state = key
					else:
						pass
				else:
					continue
			#print(min_dif, min_dif_state)
			xss = read_abbreviations('abbreviations.csv')				
			ans = xss[min_dif_state]
			return ans
			

	
	
	
	
	
	
	