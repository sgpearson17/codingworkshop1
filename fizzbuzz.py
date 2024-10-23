def fizzbuzz(yourNum):
	if yourNum < 1:
		return "Fail!"
	if yourNum % 3 == 0 and yourNum % 5 != 0:
		return "Fizz"
	if yourNum % 3 != 0 and yourNum % 5 == 0:
		return "Buzz"
	if yourNum % 3 == 0 and yourNum % 5 == 0:
		return "FizzBuzz"
	return input
	
def test_fizzbuzz():
	assert fizzbuzz(0) == "Fail!"
	assert fizzbuzz(-1) == "Fail!"
	assert fizzbuzz(3) == "Fizz"
	assert fizzbuzz(6) == "Fizz"
	assert fizzbuzz(5) == "Buzz"
	assert fizzbuzz(10) == "Buzz"
	assert fizzbuzz(15) == "FizzBuzz"
	assert fizzbuzz(30) == "FizzBuzz"

