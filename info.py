from datetime import datetime as dt
import re
from abc import ABC, abstractmethod


class Record:

    def __init__(self, name, phones='', birthday='', email='', status='', note=''):

        @abstractmethod   
        def birthday(self):
            self.birthday = birthday
        def name(self):
            self.name = name
        def phones(self):
            self.phones = phones
        def email(self):
            self.email = email
        def status(self):
            self.status = status
        def note(self):
            self.note = note

    def days_to_birthday(self):
        current_datetime = dt.now()
        self.birthday = self.birthday.replace(year=current_datetime.year)
        if self.birthday >= current_datetime:
            result = self.birthday - current_datetime
        else:
            self.birthday = self.birthday.replace(year=current_datetime.year + 1)
            result = self.birthday - current_datetime
        return result.days


class Field(ABC):                #АБСТРАКТНЫЙ КЛАСС

    @abstractmethod
    def __getitem__(self):
        pass


class Name(Field):                 #НАСЛЕДОВАНИЕ ОТ АБСТРАКТНОГО КЛАССА
    def __init__(self, value):
        self.value = value

    def __getitem__(self):
        return self.value


class Phone(Field):      #НАСЛЕДОВАНИЕ ОТ АБСТРАКТНОГО КЛАССА

    def __init__(self, value=''):
        while True:
            self.value = []
            if value:
                self.values = value
            else:
                self.values = input("Phones(+48......... or +38..........) (multiple phones can be added with space between them. +48 pattern has 9 symbols after code): ")
            try:
                for number in self.values.split(' '):
                    if re.match('^\+48\d{9}$', number) or re.match('^\\+38\d{10}$', number) or number == '':
                        self.value.append(number)
                    else:
                        raise ValueError
            except ValueError:
                print('Incorrect phone number format! Please provide correct phone number format.')
            else:
                break

    def __getitem__(self):
        return self.value


class Birthday(Field):   #НАСЛЕДОВАНИЕ ОТ АБСТРАКТНОГО КЛАССА

    def __init__(self, value=''):
        while True:
            if value:
                self.value = value
            else:
                self.value = input("Birthday date(dd/mm/YYYY): ")
            try:
                if re.match('^\d{2}/\d{2}/\d{4}$', self.value):
                    self.value = dt.strptime(self.value.strip(), "%d/%m/%Y")
                    break
                elif self.value == '':
                    break
                else:
                    raise ValueError
            except ValueError:
                print('Incorrect date! Please provide correct date format.')

    def __getitem__(self):
        return self.value


class Email(Field):           #НАСЛЕДОВАНИЕ ОТ АБСТРАКТНОГО КЛАССА
    def __init__(self, value=''):
        while True:

            if value:
                self.value = value
            else:
                self.value = input("Email: ")
            try:
                if re.match('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$', self.value) or self.value == '':
                    break
                else:
                    raise ValueError
            except ValueError:
                print('Incorrect email! Please provide correct email.')

    def __getitem__(self):
        return self.value


class Status(Field):           #НАСЛЕДОВАНИЕ ОТ АБСТРАКТНОГО КЛАССА

    def __init__(self, value=''):
        while True:
            self.status_types = ['', 'family', 'friend', 'work']
            if value:
                self.value = value
            else:
                self.value = input("Type of relationship (family, friend, work): ")
            try:
                if self.value in self.status_types:
                    break
                else:
                    raise ValueError
            except ValueError:
                print('There is no such status!')

    def __getitem__(self):
        return self.value


class Note(Field):
    def __init__(self, value):
        self.value = value

    def __getitem__(self):
        return self.value


class UserdataReport(Field):
    
    def name(self):
        return UserdataReport()

    def birthday(self):
        return UserdataReport()

    def phones(self):
        return UserdataReport()

    def email(self):
        return UserdataReport()

    def status(self):
        return UserdataReport()

    def note(self):
        return UserdataReport()

