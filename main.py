#1-misol
from datetime import datetime

class Hisob:
    def __init__(self, balans):
        self.balans = balans

    def foiz_hisoblash(self):
        raise NotImplementedError

    def pul_chiqarish(self, summa):
        raise NotImplementedError


class OmonatHisobi(Hisob):
    minimal_qoldiq = 10000

    def foiz_hisoblash(self):
        return self.balans * 0.05

    def pul_chiqarish(self, summa):
        if self.balans - summa < self.minimal_qoldiq:
            return "Xatolik: Minimal qoldiq talab qilinadi!"
        self.balans -= summa
        return f"Pul berildi: {summa}, Qoldiq: {self.balans}"


class KreditHisobi(Hisob):
    def foiz_hisoblash(self):
        return self.balans * 0.15

    def pul_chiqarish(self, summa):
        komissiya = summa * 0.02
        jami = summa + komissiya
        self.balans -= jami
        return f"Pul berildi: {summa}, Komissiya: {komissiya}, Qoldiq: {self.balans}"


class InvestitsiyaHisobi(Hisob):
    def foiz_hisoblash(self):
        return self.balans * 0.20

    def _ish_kuni(self):
        return datetime.today().weekday() < 5  # 0-4 = ish kuni

    def pul_chiqarish(self, summa):
        if not self._ish_kuni():
            return "Bugun ish kuni emas, pul chiqarish taqiqlangan!"
        self.balans -= summa
        return f"Pul berildi: {summa}, Qoldiq: {self.balans}"
