class Calc:
    res: float = 0
    sign: str = ""

    def set_sing(self, sign: str):
        self.sign = sign

    def summa(self, s: str, si: str):
        number: str = ""
        for i in s[::-1]:
            if i == " " or not i.isdigit():
                break
            else:
                number += i

        num : float = float(number[::-1])
        if si == "+":
            self.res += num
        elif si == "-":
            if self.res == 0:
                self.res = num
            else:
                self.res -= num
        elif si == "*":
            if self.res == 0:
                self.res = num
            else:
                self.res *= num
        elif si == "/":
            if self.res == 0:
                self.res = num
            else:
                self.res /= num

    def result(self, n: str, si: str):
        n = float(n)
        if si == "+":
            self.res += n
        elif si == "-":
            self.res -= n
        elif si == "*":
            self.res *= n
        elif si == "/":
            self.res /= n

        s = str(self.res)
        if s[-1] != "0":
            self.res = float(self.res)
        else:
            self.res = int(self.res)
        self.sign = ""
        return self.res

    def clean_res(self):
        self.res = 0
