class MyClass:
    my_attribute = 0

    def my_method(self):
        MyClass.my_attribute = 42


my_object1 = MyClass()
my_object2 = MyClass()

print(my_object1.my_attribute)

my_object2.my_method()

print(my_object1.my_attribute)
