def find_reverse(numbers):
   return list(reversed(numbers))

def find_max(numbers):
    return max(numbers)

def find_min(numbers):
    return min(numbers)

def find_sum(numbers):
    return sum(numbers)

def find_average(numbers):
    return (sum(numbers) / len(numbers))

def find_descending(numbers):
    return list(reversed(sorted(numbers)))

def second_smallest(numbers):
	numbers.sort()
	i = 0
	while numbers[i] == numbers[0]:
		i += 1

	return numbers[i]



'''
 bonus task:
 a function that takes in a list of numbers, and an index 'k' 
 and prints the kth smallest number in the list
'''
def kth_smallest(numbers, k):
	numbers.sort()
	i = 0
	num = numbers[0]
	counter = 1
	j = 0
	while i < len(numbers) and counter != k:
		if numbers[i] != num:
			num = numbers[i]
			counter += 1
			if counter == k:
				j = i
		i += 1

	#print (numbers[j])
	return numbers[j]
