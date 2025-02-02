
#example 1
class StringManipulator:
    def __init__(self):
        self.input_string = ""
    
    def getString(self):
        self.input_string = input()
    
    def printString(self):
        print(self.input_string.upper())


string_obj = StringManipulator()
string_obj.getString()
string_obj.printString()

#example 2
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length * self.length


shape = Shape()
print("Area of Shape:", shape.area())       # Output: 0

square = Square(4)
print("Area of Square:", square.area())     # Output: 16

#example 3
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

shape = Shape()
print("Area of Shape:", shape.area())  # Output: 0

rectangle = Rectangle(4, 5)
print("Area of Rectangle:", rectangle.area())  # Output: 20

#example 4
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)


point1 = Point(1, 2)
point2 = Point(4, 6)

point1.show()  # Output: Point coordinates: (1, 2)
point2.show()  # Output: Point coordinates: (4, 6)

point1.move(3, 4)  # Move point1 by (3, 4)
point1.show()  # Output: Point coordinates: (4, 6)

distance = point1.dist(point2)  # Distance between point1 and point2
print("Distance between points:", distance)  # Output: 0.0

#example 5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. Current balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. Current balance: ${self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

account = Account("John", 1000)

account.deposit(500)  # Deposits $500, current balance: $1500
account.withdraw(300)  # Withdraws $300, current balance: $1200
account.withdraw(2000)  # Attempt to withdraw $2000, should give "Insufficient funds."
account.deposit(-100)  # Invalid deposit, should give a warning
account.withdraw(-50)  # Invalid withdrawal, should give a warning

# example 6
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15]

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print(prime_numbers)