# this works on python 2
import urllib, sys, time
from datetime import datetime

urlRegex = "http://data.stackexchange.com/stackoverflow/csv/780780?beginId=%s"
# change directoryRegex plz!
# Mac
directoryRegex = '/Users/maxinewell/Downloads/SO/%s.csv'
# Win
# directoryRegex = 'D:\CSV\%s.csv'


# progress
def reporthook(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        return
    duration = time.time() - start_time
    progress_size = int(count * block_size)
    speed = int(progress_size / (1024 * duration))
    percent = min(int(count * block_size * 100 / total_size), 100)
    sys.stdout.write("\r...%d%%, %d MB, %d KB/s, %d seconds passed" %
                    (percent, progress_size / (1024 * 1024), speed, duration))
    sys.stdout.flush()


def donwload(rg):
    file = urllib.URLopener()
    print(str(datetime.now()) + " Download start.")
    url = urlRegex % (rg)
    dst = directoryRegex % (rg)
    #file.retrieve(url, dst)
    urllib.urlretrieve(url,dst, reporthook)
    print("\n" + str(datetime.now()) + " File " + str(rg) + ".csv Success!")


def process(max):
    cur = 0
    while cur <= max:
        donwload(cur)
        cur += 50000


if __name__ == '__main__':
    # table size 42014360
    # calculated size 33.2 GB total
    process(42014360)
