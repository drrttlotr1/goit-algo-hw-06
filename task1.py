from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)              

class Phone(Field):
    def __init__(self, value):
        if self._validate(value):
            super().__init__(value)
        else:
            raise ValueError("Phone number must contain ten characters and only digits.")

    def _validate(self, value):
        if str(value).isdigit() and len(str(value)) == 10:
            return True
        else:
            return False

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, value):
        phone = Phone(value)
        self.phones.append(phone)

    def find_phone(self, target_phone):
        for phone in self.phones:
         if phone.value == target_phone:
          return phone

    def remove_phone(self, target_phone):
        phone = self.find_phone(target_phone)
        if phone:
            self.phones.remove(phone)
        else:
            raise ValueError(f"Phone number '{target_phone}' not found.")

    def edit_phone(self, target_phone, new_phone):
        if self.find_phone(target_phone):
            self.add_phone(new_phone)
            self.remove_phone(target_phone)
        else:
            raise ValueError(f"Phone number '{target_phone}' not found.")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def __str__(self):
        return '\n'.join(f"{key}: {value}" for key, value in self.data.items())
      
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def find_record(self, name: str):
        return self.data.get(name) 
        
    def delete_record(self, name: str):
        del self.data[name]

book = AddressBook()


oleksandr_record = Record("Oleksandr")
oleksandr_record.add_phone("1234567890")
oleksandr_record.add_phone("6666666666")
book.add_record(oleksandr_record)

svitlana_record = Record("Svitlana")
svitlana_record.add_phone("9876543210")
book.add_record(svitlana_record)
     
print(book)

oleksandr = book.find_record("Oleksandr")
oleksandr.edit_phone("1234567890", "1112223333")

print(oleksandr)

found_phone = oleksandr.find_phone("6666666666")
print(f"{oleksandr.name}: {found_phone}")

book.delete_record("Svitlana")

print(book)