# import
import time


class Card:
    def __init__(self, mojodi) -> None:
        self.mojodi = mojodi
        self.start_sefr = None
    
    def check_mojodi(self):
        self.sefr_hast = True if self.mojodi == 0 else False

        if self.sefr_hast:
            self.start_sefr = time.time()
        else:
            self.start_sefr = None

    def besoze(self):
        if self.start_sefr:
            alan = time.time()
            baze_sefr = alan - self.start_sefr
            # print(baze_sefr)
            if baze_sefr > 6:
                print("sokht!")


a = Card(0)

t1 = time.time()

while True:
    t2 = time.time() 

    if int(t2 -t1) % 7 == 0:
        a.check_mojodi()

    a.besoze()

    time.sleep(1)
