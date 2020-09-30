#-------------------------------------------------------------------------------
# Name: Ramil Chaimongkolbutr
# Project: 4
# Section: 209
# Due Date: 10/28/2018
#------------------------------------------------------------------------------
def show(map):
	def str_maxlen(xs): #create function to find the highest number in array "map"
		max_len = 0
	
		for i in xs:
			for j in range(len(i)):
			
				if j == 0 and i[0] >= max_len:
					max_len = i[0]
			
				elif i[j] >= max_len:
					max_len = i[j]
			
				else:
					continue
		return str(max_len) #return in string
	
	spacer = len(str_maxlen(map)) #set the space of each member in the array
	#print(spacer)
	
	stringmap = ""
	finalstring = ""
	
	for i in map:
		listmap = [] #create a list that receives numbers in map and turns them into strings
		for j in i:
			string_j = " " * (spacer - len(str(j))) + str(j) #space between each number
			#print(string_j)
			listmap.append(string_j)	#append a list of string to listmap
		stringmap = " ".join(listmap) + "\n"	#add space between each member
		finalstring += stringmap
		
	return finalstring

def	highest_point(map):
	def find_zero(xs): #create a function to check if all of the member is equal 0
		count = 0
		for i in range(len(xs)):
			for j in range(len(xs[i])):
				if xs[i][j] == 0:
					count += 1	#count all zeroes
					#print(count)
				else:
					continue
			#print(i, j)
		return count == (i+1)*(j+1) #return True or False if they are all zero, a number of count should be equal a size of map
	
	if find_zero(map):	#if True, then return "None"
		return "None"
	
	else:
		max_height = 0
		row = 0
		column = 0
	
		for i in range(len(map)):
			for j in range(len(map[i])):
				if map[i][j] > max_height:	 #find maximun height in map
					max_height = map[i][j]		#store maximum height values 
					#print(max_height)
					row = i				#locate maximum height
					column = j			#locate maximum height
				else:
					continue
		return tuple([row, column])		#return in a tuple
		
def	on_map(map,	r,	c):
	
	if (r > len(map)-1) or (c > len(map[0])-1) or (r < 0) or (c < 0): #if r is higher than map's row or c is higher than map's column or either or both of them are negative numbers
		
		return False
	else:
		onmap = map[r][c] 	#find an on-map point as located in row r and column c
		#print(onmap)
		return onmap >= 0	#return True if found

def is_map(map):
	def find_positive_integer(xs):	#create a function to find that all number in map is postive integer
		
		for i in xs:
			for j in i:
				if (type(j) != int) or j < 0:	#if the type of a member isn't integer and negative, return False
					return False
					break
				else:
					continue
		
		return True
	
	def check_len(xs):				#create a function to measure each length of each column in map
		if len(xs) == 0:			#row must be greater than 0
			return False
		else:
			len_col = len(xs[0])	#set default column length to the first row then compare it with other rows  
			for i in range(len(xs)):
				if len(xs[i]) != len_col:	#if it's not equal, then return False
					return False
					break
				else:
					continue
		return True
	
	if find_positive_integer(map) and check_len(map):	#two results from these functions have to hold True
		return True
	else:
		return False
		
def	neighbors(map, r, c):
	neighbors_list = []
	for i in range((r-1),(r+2)):	#create a loop between an upper and lower row of the given point
		for j in range((c-1),(c+2)):	#create a loop between a left and right colum of the given point
			if on_map(map, i, j) and [i, j] != [r, c]:	#send the value to check with function on_map--if it is outside the map, then return False--no tuple of the point
				tuple_point = tuple([i, j])				#create a tuple of location 
				neighbors_list.append(tuple_point)
			
			else:
				continue
		
	return neighbors_list

def	water_adjacent(map,	r, c):
	if on_map(map, r, c):		#check if map[r][c] is on the map
		xs = neighbors(map, r, c)		#store a list of neighbors of the point in xs
		for m, n in xs:
			if map[m][n] == 0:			# if the neighbor point is zero, then the point's adjacent to water
				return True
				break					#It's not necessary to continue after the result
			else:
				continue				#If it's not zero, keep continuing until all of neighbor points are checked
		return False
	else:
		return False

def	count_coastline(map):
	count = 0
	xss = True
	for i in range(len(map)):							#create a loop for rows of a given map
		for j in range(len(map[i])):					#create a loop for columns of a given map
			#print([i, j])
			#print("point on map is ", map[i][j])
			xss = water_adjacent(map, i, j)				#send to check if the point is adjacent to water
			#print(xss)
			if xss and (map[i][j] != 0):				#count if the point is adjacent to water AND it is not water (the point can't be zero)
				count += 1
				p#rint("count is ", count)
			
			else:
				continue
	
	return count
			
def	on_ridge(map, r, c):
	if on_map(map, r, c):			#check if the point is on the map
		xs = neighbors(map, r, c)	#let xs is a list of neighbors of the point
		count_h_r = 0
		count_v_r = 0
		count_d_r1 = 0
		count_d_r2 = 0
		
		horizontal_ridge = [xs[i] for i in range(len(xs)) if (xs[i][0] == r)]				#find the list of horizontal ridge (same row) in xs
		#print("horizontal_ridge is ", horizontal_ridge)
		for x, y in horizontal_ridge:
			if map[x][y] != 0 and map[x][y] < map[r][c]:									#check if the points in the list are not water and lower than the given point (r, c) 
				count_h_r += 1																
			else:
				continue
		vertical_ridge = [xs[j] for j in range(len(xs)) if (xs[j][-1] == c)]				#find the list of vertical ridge (same column) in xs
		#print("vertical_ridge is ", vertical_ridge)
		for x, y in vertical_ridge:															
			if map[x][y] != 0 and map[x][y] < map[r][c]:									#check if the points in the list are not water and lower than the given point (r, c)
				count_v_r += 1
			else:
				continue
		diagonal_ridge1 = [xs[m] for m in range(len(xs)) if (([xs[m][0], xs[m][-1]] == [r-1,c-1]) or ([xs[m][0], xs[m][-1]] == [r+1,c+1]))]			#find the first list of diagonal (from left to right)
		#print("diagonal_ridge1 is ", diagonal_ridge1)
		for x, y in diagonal_ridge1:
			if map[x][y] != 0 and map[x][y] < map[r][c]:									#check if the points in the list are not water and lower than the given point (r, c)
				count_d_r1 += 1
			else:
				continue
		diagonal_ridge2 = [xs[n] for n in range(len(xs)) if (([xs[n][0], xs[n][-1]] == [r-1,c+1]) or ([xs[n][0], xs[n][-1]] == [r+1,c-1]))]			#find the second list of diagonal (from right to left)
		#print("diagonal_ridge2 is ", diagonal_ridge2)
		for x, y in diagonal_ridge2:
			if map[x][y] != 0 and map[x][y] < map[r][c]:									#check if the points in the list are not water and lower than the given point (r, c)
				count_d_r2 += 1
			else:
				continue
		if (count_h_r == 2) or (count_v_r == 2) or (count_d_r1 == 2) or (count_d_r2 == 2):	#how many points passed the condition? (we need at least 2 points in each list to be considered as a ridge
			return True
		else:
			return False
	else:
		return False
			
def is_peak(map, r, c):
	if on_map(map, r, c) and map[r][c] != 0:			#the point must be a land and on the map
		xs = neighbors(map, r , c)						#let xs is a list of neighbors of the point
		for i, j in xs:
			if map[i][j] > map[r][c]:					#all members in xs must be lower than the point 
				return False							#if any point in xs is greater than the point, then return False 
				break
			else:
				continue
		return True										#if the loop doesn't break, then it's peak
	else:
		return False

def	join_map_side(map1,	map2):
	xs = []
	map_side = []
	if len(map1) == len(map2):					#check if their rows are equal
		for i in range(len(map1)):
			xs = map1[i] + map2[i]				#let xs is a sum of each row in map1 and map2
			map_side.append(xs)					#store xs in a list called map_side
		return map_side	
	else:
		return None

def	join_map_below(map1, map2):
	map_below = []
	if is_map(map1) and is_map(map2) and len(map1[0]) == len(map2[0]):			#check if, first: both of map1 and map2 are legit maps; second, a column in map1 and map2 must be equal  		
		map_below = map1 + map2													#joining maps from below is basically adding 2 maps together 
		return map_below
	else:
		return None
		
def	crop(map, r1, c1, r2, c2):
	xs = []
	crop_map = []
	#print([r1,r2, c1, c2])
	
	if (r2 >= r1) and (c2 >= c1) and on_map(map, r1, c1):			#check if point r2,c2 is greater than point r1,c1 and point r1,c1 must be on the map; return [] otherwise
		
		x = r2+1
		y = c2+1
		if r2 > len(map):						#in case given r2 is greater than the number of rows in the map
			x = len(map)						#let the maximum x is equal the length of rows in the map
		if c2 > len(map[0]):					#in case given c2 is greater than the number of columns in the map
			y = None							#let y is None because when slicing the column, the result gives a whole column
		for i in range(r1, x):					#for each given row r1 to row r2 in the map 
			xs = map[i][c1:y]					#copy all member from c1 to c2 and store them in a list xs
			#print(xs)
			crop_map.append(xs)					#append xs list to a final list called crop_map
		return crop_map
	else:
		return []
		
def flooded_map(map, rise):
	
	flooded = 0
	
	map_flooded = []
	for i in range(len(map)):
		xs = []
		for j in range(len(map[i])):
			if map[i][j] - rise < 0:			#in case negative numbers appear, substitute them with zero
				xs.append(flooded)				#store the number in a list xs
			else:
				xs.append(map[i][j] - rise)		#in case results are zeroes or greater, go ahead and store them in xs 
			#print(xs)
		map_flooded.append(xs)					#append xs to a final list called map_flooded
	
	return map_flooded
	
def flood_map(map, rise):
	mirror = flooded_map(map, rise)				#create a flooded map as a mirror map
	for i in range(len(map)):
		for j in range(len(map[i])):
			map[i][j] = mirror[i][j]			#substitute each member in a given map by each member in a mirror map, now the map is modified
			
	return None									#question requires to return None
	
def find_land(map, r, c, dir):
	x = r										#assign row to a new variable (in case modification is needed)
	y = c										#assign column to a new variable (same reason as row)
	count = 0
	
	if on_map(map, r, c) == False:				#if r, c is not on the map, return None
		return None
	

	while map[x][y] == 0:						#create a loop that the starting point remains 0
		directory_dict = {						#create dictionary assigning each direction to an operation on x and y, for example, moving north is the same as moving from [x,y] to [x-1,y]
			"NW": [x-1, y-1],
			"N" : [x-1, y],
			"NE": [x-1, y+1],
			"W" : [x, y-1],
			"E" : [x, y+1],
			"SW": [x+1, y-1],
			"S" : [x+1, y],
			"SE": [x+1, y+1]
		}
		x = directory_dict[dir][0]				#operation on x based on given direction (dir)
		y = directory_dict[dir][1]				#operation on y based on given direction (dir)
		#print(x)
		#print(y)
		count += 1								#keep counting until a new x, y is land or not equal 0
		if on_map(map, x, y) == False:			#However, if the point (new x,y) is not on the map, None is returned then the loop is broken
			return None
			break
		else: 
			continue
	return count
		
def reorient(map):
	m = 0
	reorient_map = []
	
	for i in range(len(map[0])):
		xs = []
		for j in range(len(map)-1,-1,-1):	#the first column starting from bottom to top becomes first row of the new list
			m = map[j][i]
			xs.append(m)					#store each point in a new list xs
		reorient_map.append(xs)
			
	return reorient_map	
	
#Extra credit 
def get_island_spots(map, r , c):
	if (on_map(map, r ,c) == False) or map[r][c] == 0:		#First filter: to see if the point (r,c) is on the map and not water
		return []
	to_do = []
	answer = []
	to_do.append((r,c))										#add initial point (r,c) to to_do list 
	
	while len(to_do) != 0:
		x = to_do.pop()										#pop one to_do member and assign it to x
		if (map[x[0]][x[1]] != 0) and (not(x in answer)):	#check if point x is a land and isn't in answer
			answer.append(x)								#add x to answer
			xs = neighbors(map, x[0], x[1])					#find neighbors of the point x and assign them to xs list
			for i in xs:
				if (not(i in answer)) and (map[i[0]][i[1]] != 0):	#check if each member isn't water and in answer
					to_do.append(i)							#add them to to_do list to repeat the loop until to_do list is empty then stop
				else:
					continue
	
	answer.sort()											#sort answer list as asked
	return answer

def connected_spots(map, r1, c1, r2, c2):
	if (on_map(map, r1,c1)) and (on_map(map, r2, c2)):		#First filter as usual: both points should be on the map
		xs = get_island_spots(map, r1, c1)					#Let (r1,c1) be an initial point, then find an island around the point
		if (r2,c2) in xs:									#if (r2,c2) is in the same island, this means that they are connected by land
			return True
		else:
			return False
	else:
		return False
		
def remove_island(map, r, c):
	if (on_map(map, r, c)):									#check if (r,c) is on the map
		xs = get_island_spots(map, r, c)					#find an island around the point (r,c), then store it in xs
		for i in xs:				
			map[i[0]][i[1]] = 0								#modify every land point in the island to water 
	else:
		print("out of map's range")
	return None