def factorial(x):
	if x == 1:
		return x
	else:
		return x*factorial(x-1)


if __name__ == "__main__":
    print(factorial(3))
