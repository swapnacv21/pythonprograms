'''ABSTRACTION'''
# -----------------
# example 1:

from abc import ABC,abstractmethod
class synnefo(ABC):
    @abstractmethod
    def reg(self):
        pass
    def python(self):
        print('python topics')
    def php(self):
        print('php topics')

class staff(synnefo):
    def reg(self):
        print("Staff details")
    def notes(self):
        print("notes")

class student(synnefo):
    def reg(self):
        print("Student details")
    def exam(self):
        print("exams")


staff1=staff()
# staff1.reg()

swapna=student()
# swapna.reg()