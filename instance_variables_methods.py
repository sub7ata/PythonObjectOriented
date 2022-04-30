import types
class Parent:
    def __init__(self):
        self.state = 'West Bengal'

class Child(Parent):
    def __init__(self, first_name, last_name, zipcode):     # <- Constructor
        self.first_name = first_name                        # <- Instance variable
        self.last_name = last_name
        self.email = first_name.lower() + '.' + last_name.lower() + '@email.com'
        self.country = 'India'
        super().__init__()                                  # <- Call parent class constructor
        self.zipcode = zipcode


    def fullname(self):                                     # <- Instance method access instance variable
        return 'Name: {} {}'.format(self.first_name, self.last_name)

    def address(self):                                      # <- Instance method access instance variable
        return 'Email: {}\nCountry: {}\nState: {}\nZipcode: {}'.format(self.email, self.country, self.state, self.zipcode)

    def add(self, age):                                     # <- Instance method to add instance variable
        self.agg = age                                      # <- Add new attribute to current object

    def update(self, zipcode):                              # <- Instance method to modify instance variable
        self.zipcode = zipcode

    def details(self):                                      # <- Call two method from another within the same class
        fullname = self.fullname()
        address = self.address()
        return fullname + "\n" + address


obj = Child('Subrata', 'Das', 721445)                       # <- Create object
print(obj.__dict__)

for key_value in obj.__dict__.items():                      # <- Get each instance variable
    print(key_value[0], '=', key_value[1])

print(obj.fullname())                                       # <- Call instance method
print(obj.address())                                        # <- Call instance method

print("\n")
print(obj.details())                                        # <- Call instance method
print(obj.first_name)                                       # <- Access instance variable

obj.city = 'Kolkata'                                        # <- Add new instance variable 'age' to obj
obj.zipcode = 700006                                        # <- Modify instance variable
print(obj.__dict__)


print('Name:', getattr(obj, 'first_name'))                  # <- Use getattr instead of stud.name
print('Email:', getattr(obj, 'email'))

obj.update(713206)                                          # Modify instance variables

del obj.city                                                # <- Delete instance variable using del
delattr(obj, 'last_name')                                   # <-  Delete instance variable using delattr()
print(obj.__dict__)

obj.add(29)                                                 # <- call instance method
print(obj.__dict__)


def end(self):
    print("Good Bye {}".format(self.first_name))

obj.end = types.MethodType(end, obj)                        # <- Add instance method to object
obj.end()                                                   # <- Call newly added method