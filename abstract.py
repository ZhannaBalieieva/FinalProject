from abc import abstractmethod, ABC
import AddressBook
import Bot #?
import info 

class Abstract(ABC):

    @abstractmethod
    def name(self):
        pass
    @abstractmethod
    def phone(self):
        pass
    @abstractmethod
    def birth(self):
        pass
    @abstractmethod
    def email(self):
        pass
    @abstractmethod
    def status(self):
        pass
    @abstractmethod
    def note(self):
        pass

class info(ABC):
    def name(self):
        #self.name = Name
        Name = (input("Name: ")).value.strip()
        return Name
    def birth(self):
        return birth
       
        email = Email().value.strip()
        status = Status().value.strip()
        note = Note(input("Note: ")).value

        


class Report(Abstract):
    def name(self):
        

    def phones(self):

    def birth(self):

    def email(self):

    def status(self):

    def note(self):
                        

from abc import ABC, abstractmethod, abstractproperty

class AbstractBase(ABC):

    @abstractmethod
    def foo(self):
        pass

    @abstractproperty
    def baz(self):
        pass

>>> AbstractBase()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't instantiate abstract class AbstractBase with abstract methods baz, foo

class Base(AbstractBase):
    def foo(self):
        print('foo')
    @property
    def baz(self):
        return 'baz'

>>> base = Base()
>>> base.foo()
foo
>>> base.baz
'baz'