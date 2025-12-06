class Person:
    def __init__(self, name, type_) -> None:
        self.type = type_
        self.name = name

    
    def greet(self):
        print(f"Good Morning... {self.name} !")



class Employee(Person):
    def __init__(self, name, type_, emp_no) -> None:
        super().__init__(name, type_)
        self.emp_no = emp_no


class God:
    person = Person

    def __init__(self) -> None:
        self.name = self.person("Jesus", "god")

    def grant_wish(self):
        print(f"grant wisht to {self.name}")    


john = Person("John", "human")

manager = Employee("Jane", "human", 12345)

manager.greet()