
for num in range(1,101):
    if num % 5 == 0 and num % 3 ==0:  # we need to take this line up so that it checks this logic first
					# or else you will find the this logic is not getting triggered 
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)