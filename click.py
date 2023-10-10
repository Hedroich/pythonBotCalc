class Click:
    st: str = ""
    num: str = ""

    def click_num(self, s: str, n: str) -> str:
        self.st += s
        self.num += n
        return self.st

    def set_st(self, s: str) -> None:
        self.st += s

    def set_num(self, n: str) -> None:
        self.num += n

    def clean_all(self) -> None:
        self.st = ""
        self.num = ""

    def clean_st(self) -> None:
        self.st = ""

    def clean_num(self) -> None:
        self.num = ""
