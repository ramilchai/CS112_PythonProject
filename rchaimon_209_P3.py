#-------------------------------------------------------------------------------
# Name: Ramil Chaimongkolbutr
# Project 3
# Due Date: 10/07/2018
#------------------------------------------------------------------------------


def sum_divisors(n):
	i = 1
	divisors_list = []
	sum = 0
	
	while i <= int(n):
		if int(n) % i == 0:
			divisors_list.append(i)
		
		else:
			pass
		i += 1
	
	for divisor in divisors_list:
		sum = sum + divisor
	
	return sum
	#print(divisors_list)

def pi(precision):
	k = 0
	leibniz = 0
	
	
	while float(precision) < (4)/(2*k + 1):
		k += 2
	
	j = k + 1
	
	for n in range(j):
		leibniz = leibniz + (4*(-1)**n)/(2*n + 1)
		#print(leibniz)
	
	return leibniz

def span(nums):
	if nums == []:
		difmaxmin = 0
		return difmaxmin
	else:
		x = nums[0]
		y = nums[0]
		i = 0
		for i in range(len(nums)):
			if x < nums[i]:
				x = nums[i]
			else:
				pass
		for i in range(len(nums)):
			if y > nums[i]:
				y = nums[i]
			else:
				pass
	#print(x)
	#print(y)
		difmaxmin = x - y
	
	return difmaxmin

def single_steps(nums):
	if nums == []:
		singlestep = 0
		return singlestep
	else:
		x = 0
		i = 0
		j = 0
		count = 0
		for i in (range(len(nums)-1)):
			x = nums[i]
			#print(x)
			j = i + 1
			if (x - nums[j] == -1) or (x - nums[j]) == 1:
				count += 1
			else:
				pass
	
	return count

def remove_echo(xs):
	echo = []
	
	if xs == []:
		return echo
	else:
		i = 1
		echo.append(xs[0])
		
		#print(echo)
		
		for i in range(len(xs)):
			x = xs[i]
			
			if x != echo[-1]:
				echo.append(x)
				#print(echo)
			else:
				pass
	
	return echo
	
def even_product_2d(grid):
	
	multisum = 1
	product = []
	
	if grid == []:
		return multisum
	else:
		for group in grid:
			if group == []:
				pass
			for i in group:
				if i % 2 == 0:
					product.append(i)
				elif i == []:
					pass
				else:
					pass
	
		for j in product: 
			multisum = multisum * j
	
		return multisum
		
#extra credit
def count_isolated(grid):
	
	m = len(grid[0])
	n = len(grid)
	mat = []
	count = 0
	
	for i in range(0, n+2):
		
		mat.append([])
		for j in range(0, m+2):
			mat[-1].append('.')
	
	
	for a in range(0, n):
		for b in range(0, m):
			if grid[a][b] != '.':
				mat[a+1][b+1] = grid[a][b]
			else:
				pass
	
	for c in range(0, len(mat)):
		for d in range(0, len(mat[c])):
			if (mat[c][d] != '.') and ([mat[c-1][d-1], mat[c-1][d], mat[c-1][d+1]] == ['.','.','.']) and ([mat[c][d-1], mat[c][d+1]] == ['.','.']) and ([mat[c+1][d-1], mat[c+1][d], mat[c+1][d+1]] == ['.', '.', '.']):
					count += 1
			else:
				pass
	
	return count
	
	
