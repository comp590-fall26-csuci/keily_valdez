def iterative_fib(n):
	a,b = 0,1
	sequence = []

	for _ in range(n):
		sequence.append(a)
		a,b = b, a+b

	return sequence

if __name__ == "__main__":
	sequence = iterative_fib(25)
	with open("output/fibonacci.txt", "w") as f:
		for num in sequence:
			f.write(str(num) + "\n")

