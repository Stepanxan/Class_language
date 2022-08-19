class Alphavite:
    def __init__(self, language, letters, number):
        self.language = language
        self.letters  = letters
        self.number = number

    def get_language(self):
        return "Name language" + str(self.language)

    def get_letters(self):
        return "letters" + str(self.letters)

    def get_number(self):
        return "number" + str(self.number)

    def get_full_into(self):
        print("Name language", self.language )
        print("letters", self.letters)
        print("number", self.number)

class ENG_Alphavite(Alphavite):
    def check_palindrome(self):
        reversed_self = self.language[::-1]
        status = 1
        if (self != reversed_self):
            status = 0
        return status

Alphavite_UKR = Alphavite (language = "УКРАЇНСЬКА", letters = "а, б, в, г, д", number = "5")
Alphavite_ENG = Alphavite (language = "English", letters = "а, b, c, d, e", number = "5")