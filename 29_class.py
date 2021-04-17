import termcolor2


class Fraction:
    def __init__(self):
        self.s1 = int(input("Enter S1: "))
        self.m1 = int(input("Enter m1: "))
        self.s2 = int(input("Enter S2: "))
        self.m2 = int(input("Enter m2: "))

    def sum(self):
        return f"Fraction Sum: {(self.s1 * self.m2) + (self.s2 * self.m1)} / {self.m1 * self.m2} "

    def show_sum(self):
        print(self.sum())

    def multi(self):
        return f"Fraction Multiplication: {(self.s1 * self.s2)} / {self.m1 * self.m2} "

    def show_multi(self):
        print(self.multi())

    def minus(self):
        m = self.m1 * self.m2
        return f"Fraction Minus: {(m // self.m1) * self.s1 - (m // self.m2) * self.s2} / {m} "

    def show_minus(self):
        print(self.minus())

    def divide(self):
        return f"Fraction Divide: {self.s1 * self.m2} / {self.s2 * self.m1} "

    def show_divide(self):
        print(self.divide())


res = Fraction()

res.sum()
res.show_sum()

res.multi()
res.show_multi()

res.minus()
res.show_minus()

res.divide()
res.show_divide()

print(termcolor2.colored("--------------------------------------------", color="red"))
print(termcolor2.colored("--------------------------------------------", color="blue"))


class Time:
    def __init__(self):
        self.hour1 = int(input("Enter Hour1: "))
        self.minutes1 = int(input("Enter Minutes1: "))
        if 0 > self.minutes1 or self.minutes1 > 60:
            print(termcolor2.colored("TryAgain", color="red"))
            exit()
        self.seconds1 = int(input("Enter Seconds1: "))
        if 0 > self.seconds1 or self.seconds1 > 60:
            print(termcolor2.colored("TryAgain", color="red"))
            exit()
        self.hour2 = int(input("Enter Hour2: "))
        self.minutes2 = int(input("Enter Minutes2: "))
        if 0 > self.minutes2 or self.minutes2 > 60:
            print(termcolor2.colored("TryAgain", color="red"))
            exit()
        self.seconds2 = int(input("Enter Seconds2: "))
        if 0 > self.seconds2 or self.seconds2 > 60:
            print(termcolor2.colored("TryAgain", color="red"))
            exit()

    def sum(self):
        return f"{self.hour1 + self.hour2} : {self.minutes1 + self.minutes2} : {self.seconds1 + self.seconds2}"

    def show_sum(self):
        print(self.sum())

    def minus(self):
        return f"{self.hour1 - self.hour2} : {self.minutes1 - self.minutes2} : {self.seconds1 - self.seconds2}"

    def show_minus(self):
        print(self.minus())


res = Time()

res.sum()
res.show_sum()

res.minus()
res.show_minus()

print(termcolor2.colored("--------------------------------------------", color="red"))
print(termcolor2.colored("--------------------------------------------", color="blue"))


class Convert:
    def __init__(self):
        self.h = int(input("Enter Hour: "))
        self.m = int(input("Enter Minutes: "))
        self.s = int(input("Enter Seconds: "))
        print(f"{self.h} : {self.m} : {self.s}")

    def convert_to_seconds(self):
        self.hour = self.h * 3600
        self.minute = self.m * 60
        result = f"Seconds: {self.hour + self.minute + self.s}"
        return result

    def show_time(self):
        print(self.convert_to_seconds())


res = Convert()
res.convert_to_seconds()
res.show_time()
