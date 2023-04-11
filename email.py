import re
class EmailExtractor:

    def __init__(self, email):
        self.email = email
        self.regex = r"(?P<imie>[a-z]*)\.(?P<nazwisko>[a-z]*[0-9]*)@(?P<rozszerzenie>[a-z]*)"

    def is_student(self):
        m = re.compile(self.regex)
        res = m.findall(self.email)

        ax0 = res[0][2]
        if ax0 == "student":
            return True
        else:
            return False

    def is_male(self):
        m = re.compile(self.regex)
        res = m.findall(self.email)

        ax1 = res[0][0][len(res[0]) - 1]

        if ax1 == 'a':
            return False
        else:
            return True

    def get_name(self):
        m = re.compile(self.regex)
        res = m.findall(self.email)

        #print("res", res)
        #print("res[0]", res[0])
        #print("res[0][0]", res[0][0])
        ax2 = res[0][0].capitalize()

        return ax2

    def get_surname(self):
        m = re.compile(self.regex)
        res = m.findall(self.email)

        output_str = ""
        for char in res[0][1]:
            if not char.isnumeric():
                output_str += char
        ax3 = output_str.capitalize()
        return ax3

