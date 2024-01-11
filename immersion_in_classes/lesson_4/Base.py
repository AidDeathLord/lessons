class Base:
    def is_instance_of(self, name):
        class_list = []
        for __class in type(self).__mro__:
            class_list.append(__class.__name__)
        return name in class_list


class Child(Base):
    pass


class ChildOfChild(Child):
    pass


a = Base()
print(a.is_instance_of('aaa'))
b = Child()
print(b.is_instance_of('Child'))
