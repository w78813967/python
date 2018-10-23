
class BMITest:
    def __init__(self, h=0, w=0, name=""):
        self.name = name
        self.height = h
        self.weight = w

    def BMI(self):
        print('hello,', self.name , ' your bmi: ', self.weight / ((self.height/100)**2))
        return self.weight / ((self.height/100)**2)