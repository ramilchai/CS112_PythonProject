def checkout(num_hats, num_tels, num_creams):
	#print("num_hats is", num_hats)
	#print("num_tels is", num_tels)
	#print("num_creams is", num_creams)
	
	knots_hats = (2 * 17 * 29) * num_hats
	knots_tels = ((12 * 29) + 26) * num_tels
	knots_creams = (7 * 29) * num_creams
	total_knots = knots_hats + knots_tels + knots_creams
	
	return(total_knots)

def timing(minutes):
	num_forts = minutes // (14 * 24 * 60)
	res_forts = minutes % (14 * 24 * 60)
	#print("num_forts is", num_forts)
	#print("res_forts is", res_forts)
	num_days = res_forts // (24 * 60)
	res_days = res_forts % (24 * 60)
	num_hours = res_days // 60
	num_mins = res_days % 60
	
	
	return(num_forts, num_days, num_hours, num_mins)
	
	
#extra credits

def catch_bus(dist, time, k):
	int_dist = int(dist)
	int_time = int(time)
	int_k = int(k)
		
	travel = int_dist / int_time 
		
	x = 0
	while travel > k * x:
		x += 1
		#print(x)
		
	multi = x	
	ans = k * multi
	
	return(ans)