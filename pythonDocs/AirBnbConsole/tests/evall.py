class Person():
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex


# person1 = Person('brian', 'male')

# print(person1.name)
# print(person1.sex)
# print(person1.__class__)
# print(person1.__dict__)
# print(person1.__repr__)
# print(person1.__str__)

# class_obj = eval(Person)

# print(class_obj)

class_name = "Person"

obj_dict = {'name': 'Brian',
            'sex': 'male'}
class_obj = eval(class_name)

instance = class_obj(**obj_dict)

print(instance.name)
print(instance.sex)

instance2 = Person(**obj_dict)

print(instance2.name)
print(instance2.sex)