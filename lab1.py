def recursive_fib(n):
	if n <= 1:
		return n
	return recursive_fib(n-1) + recursive_fib(n-2)

def sequence_generator(n):
	sequence = []

	for i in range(n):
		sequence.append(recursive_fib(i))

	return sequence

if __name__ == "__main__":
	sequence = sequence_generator(25)
	with open("output/recursive_fibonacci.txt", "w") as f:
		for num in sequence:
			f.write(str(num) + "\n")

