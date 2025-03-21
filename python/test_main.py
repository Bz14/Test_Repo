# test_main.py
from main import main  # Assumes the function is in fizz_buzz.py

def test_fizz_buzz():
    # Test multiples of both 3 and 5 (FizzBuzz)
    assert main(15) == "FizzBuzz"
    assert main(30) == "FizzBuzz"
    assert main(45) == "FizzBuzz"

   

def test_fizz():
    # Test multiples of 3 only (Fizz)
    assert main(3) == "Fizz"
    assert main(6) == "Fizz"
    assert main(9) == "Fizz"

def test_buzz():
    # Test multiples of 5 only (Buzz)
    assert main(1) == "Buzz"
    assert main(10) == "Buzz"
    assert main(20) == "Buzz"

def test_numbers():
    # Test numbers that aren't multiples of 3 or 5
    assert main(1) == "1"
    assert main(2) == "2"
    assert main(4) == "4"

def test_zero():
    # Test edge case with zero
    assert main(0) == "FizzBuzz"  # 0 is a multiple of both 3 and 5