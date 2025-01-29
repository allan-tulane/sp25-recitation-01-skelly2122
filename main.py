"""
CMPS 2200 Recitation 1
"""

# Import necessary libraries
import tabulate  # Used for displaying results in a table format
import time  # Used for measuring the execution time of functions


def linear_search(mylist, key):
	"""
		Performs a linear search to find the position of a given key in a list.

		Parameters:
				mylist.....The list to search within
				key........The value to locate in the list

		Returns:
				The index of the key if found; otherwise, returns -1.
		"""
	for i, v in enumerate(mylist):  # Loop through each element in the list
		if v == key:  # If the current element matches the key
			return i  # Return the index where the key is found
	return -1  # If the key isn't found, return -1


def binary_search(mylist, key):
	"""
		A wrapper function for binary search that initializes the recursive search.

		Parameters:
				mylist.....A sorted list in which to search
				key........The value to locate in the list

		Returns:
				The index of the key if found; otherwise, returns -1.
		"""
	return _binary_search(mylist, key, 0, len(mylist) - 1)


def _binary_search(mylist, key, left, right):
	"""
		A recursive implementation of binary search.

		Parameters:
				mylist.....A sorted list in which to search
				key........The value to locate in the list
				left.......The starting index of the search range
				right......The ending index of the search range

		Returns:
				The index where the key is found, or -1 if the key is not in the list.
		"""
	if left > right:  # If the search range is invalid, the key isn't present
		return -1

	mid = (left + right) // 2  # Find the middle index of the current range
	if mylist[mid] == key:  # If the key is at the middle index, return it
		return mid
	elif mylist[
	    mid] > key:  # If the key is smaller, continue searching in the left half
		return _binary_search(mylist, key, left, mid - 1)
	else:  # If the key is larger, continue searching in the right half
		return _binary_search(mylist, key, mid + 1, right)


def time_search(search_fn, mylist, key):
	"""
		Measures how long a search function takes to execute.

		Parameters:
				search_fn...The search function to measure (linear_search or binary_search)
				mylist......The list to search in
				key.........The target value to find

		Returns:
				The execution time in milliseconds.
		"""
	start_time = time.time()  # Record the start time
	search_fn(mylist, key)  # Run the search function
	end_time = time.time()  # Record the end time
	return (end_time - start_time) * 1000  # Convert time to milliseconds


def compare_search(sizes=[10, 100, 1000, 10000, 100000, 1000000, 10000000]):
	"""
		Compares the performance of linear_search and binary_search for different input sizes.

		The key being searched (-1) is not in the list, ensuring a worst-case scenario.

		Parameters:
				sizes...A list of different list sizes to test the searches on

		Returns:
				A list of tuples (n, linear_search_time, binary_search_time),
				where `n` is the size of the list and times are measured in milliseconds.
		"""
	results = []  # Store results for each list size

	for n in sizes:
		mylist = list(range(n))  # Generate a sorted list from 0 to n-1
		key = -1  # Use a key that is guaranteed to be absent

		linear_time = time_search(linear_search, mylist,
		                          key)  # Measure linear search time
		binary_time = time_search(binary_search, mylist,
		                          key)  # Measure binary search time

		results.append((n, linear_time, binary_time))  # Store results as a tuple

	return results  # Return all collected results


def print_results(results):
	"""
		Displays search performance results in a well-structured table.

		Parameters:
				results...A list of tuples containing execution times for searches.
		"""
	print(
	    tabulate.tabulate(
	        results,
	        headers=['n', 'linear', 'binary'],  # Column labels
	        floatfmt=".3f",  # Show values with three decimal places
	        tablefmt="github"))  # Use GitHub-style table formatting


if __name__ == "__main__":
	"""
		If this script is executed directly, perform the search comparison and print the results.
		"""
	results = compare_search()  # Run the performance comparison
	print_results(results)  # Display the results in a table
