import string

class CeasarDescriptor:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = f"_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+=-?'
        hashed_value = getattr(self, self.private_name, "")
        orig = ''
        for char in hashed_value:
            pos = (alphabet.find(char) - 10) % len(alphabet)
            orig += alphabet[pos]
        return orig

    def __set__(self, instance, value):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+=-?'
        hash = ''
        for char in value:
            pos = (alphabet.find(char) + 10) % len(alphabet)
            hash += alphabet[pos]
        setattr(self, self.private_name, hash)

class AtbashDescriptor:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = f"_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+=-? '
        hashed_value = getattr(self, self.private_name, "")
        orig = ''
        for char in hashed_value:
            pos = (len(alphabet) - alphabet.find(char) - 1) % len(alphabet)
            orig += alphabet[pos]
        return orig

    def __set__(self, instance, value):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+=-? '
        hash = ''
        for char in value:
            pos = (len(alphabet) - alphabet.find(char) - 1) % len(alphabet)
            hash += alphabet[pos]
        setattr(self, self.private_name, hash)

class User:
    log_ces = CeasarDescriptor()
    pswd_atbash = AtbashDescriptor()
    def __init__(self, log_ces, pswd_atbash):
        self.log_ces = log_ces
        self.pswd_atbash = pswd_atbash

us = User('Irina', 'Tvoy Mat')
print(us.log_ces)
print(us.pswd_atbash)

