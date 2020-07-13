fibonacciNumbers = [0, 1, 2]
#countOfFibonacci = int(input("please enter the how many Fibonacci numbers you want: "))
countOfFibonacci = 100000000000000
for x in range(countOfFibonacci):
a = int(len(fibonacciNumbers)-1)
b = int(len(fibonacciNumbers)-2)
z = int(fibonacciNumbers[a] + fibonacciNumbers[b])
fibonacciNumbers.append(fibonacciNumbers[a] + fibonacciNumbers[b])
print("here goes your fibonacciNumbers", fibonacciNumbers)
