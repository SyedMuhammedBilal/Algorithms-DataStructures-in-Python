list_1 = ["cat", "dog", "rabit"]
list_2 = []

for aword in list_1:
    for alist in aword:
        list_2.append(alist)

print(list_2)

# gcd function
def gcd(n, m):
    while m % n != 0:
        old_m = m
        old_n = n
        
        m = old_m
        n = old_m % old_n
    return n

# Fraction class
# Implements: addition and equality
# To do: multiplication, division, subtraction and comparison operators (< , >)

class Fraction:
    def __init__ (self, top, bottom):
        
        self.num = top
        self.den = bottom
    
    def __str__(self):
        return str(self.num) + "/" + str(self.den)
    
    def show(self):
        print(self.num, "/", self.den)
    
    def __add__ (self, other_fraction):
        
        new_num = self.num * other_fraction.den + \
                  self.den * other_fraction.num
        new_den = self.den * other_fraction.den 
        common =  gcd(new_num, new_den)
    
        return Fraction(new_num // common, new_den // common)
    
    def __eq__(self, other):
        first_num  = self.num * other.den
        second_num = other.num * self.den
        
        return first_num == second_num

x = Fraction(1, 2)
y = Fraction(2, 3)

print(x + y)
print(x == y) 