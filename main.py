# this works on python 2
import urllib
from datetime import datetime

urlRegex = "http://data.stackexchange.com/stackoverflow/csv/780780?beginId=%s"
# change directoryRegex plz!
directoryRegex = 'D:\CSV\%s.csv'


def donwload(rg):
    file = urllib.URLopener()
    print(str(datetime.now()) + " Download start.")
    file.retrieve(urlRegex % (rg), directoryRegex % (rg))
    print(str(datetime.now()) + " File " + str(rg) + ".csv Success!")


def process(max):
    cur = 0
    while cur <= max:
        donwload(cur)
        cur += 50000


if __name__ == '__main__':
    # table size 42014360
    # calculated size 33.2 GB total
    process(42014360)
