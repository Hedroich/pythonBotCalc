class Click:
    st: str = ""
    num: str = ""

    def click_num(self, s: str, n: str):
        self.st += s
        self.num += n
        return self.st

    def set_st(self, s: str):
        self.st += s

    def set_num(self, n: str):
        self.num += n

    def clean_all(self):
        self.st = ""
        self.num = ""

    def clean_st(self):
        self.st = ""

    def clean_num(self):
        self.num = ""
