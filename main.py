# this works on python 2
import urllib
import sys
import time
import csv
import os
from datetime import datetime

tbList = ["Posts", "Users", "Comments", "Badges",
          "CloseAsOffTopicReasonTypes",
          "CloseReasonTypes",
          "FlagTypes",
          "PendingFlags",
          "PostFeedback",
          "PostHistory",
          "PostHistoryTypes",
          "PostLinks",
          "PostsWithDeleted",
          "PostTags",
          "PostTypes",
          "ReviewRejectionReasons",
          "ReviewTaskResults",
          "ReviewTaskResultTypes",
          "ReviewTasks",
          "ReviewTaskStates",
          "ReviewTaskTypes",
          "SuggestedEdits",
          "SuggestedEditVotes",
          "Tags",
          "TagSynonyms",
          "Votes",
          "VoteTypes"]
urlRegex = "http://data.stackexchange.com/stackoverflow/csv/781501?TableName=%s&beginId=%s"
urlSizeRegex = "http://data.stackexchange.com/stackoverflow/csv/781507?tbname=%s"
directoryRegex = ''


# progress
def reporthook(count, block_size, total_size):
    try:
        global start_time
        if count == 0:
            start_time = time.time()
            return
        duration = time.time() - start_time
        progress_size = int(count * block_size)
        speed = int(progress_size / (1024 * duration))
        # avoiding overflow 100%
        percent = min(int(count * block_size * 100 / total_size), 100)
        sys.stdout.write("\r...%d%%, %d MB, %d KB/s, %d seconds passed" %
                         (percent, progress_size / (1024 * 1024), speed, duration))
        sys.stdout.flush()
    except:
        pass


def donwload(tb, rg):
    print(str(datetime.now()) + '\033[1m' + " Id " + str(rg) + " Download start." + '\033[0m')
    url = urlRegex % (tb, rg)
    dst = directoryRegex % (tb + str(rg))
    urllib.urlretrieve(url, dst, reporthook)
    print("\n" + str(datetime.now()) + '\033[1m' + " File " + str(tb+str(rg)) + ".csv Success!" + '\033[0m')


def process(tb, max):
    cur = 0
    while cur <= max:
        donwload(tb, cur)
        cur += 50000


def getSize(tb):
    response = urllib.urlopen(urlSizeRegex % (tb))
    cr = csv.reader(response)
    next(cr)
    return next(cr)[0]


def detDst(dst):
    if os.path.isdir(dst):
        return dst + '/%s.csv'
    else:
        sys.exit("Directory not exist.")


if __name__ == '__main__':
    tb = raw_input("TableName: ")
    if tb in tbList:
        dst = raw_input('Directory: ')
        directoryRegex = detDst(dst)
        size = getSize(tb)
        print "Start download table " + '\033[1m' + tb + '\033[0m' + ' to ' + '\033[1m' + dst + '\033[0m' \
              + " contains " + '\033[1m' + size + '\033[0m' + " results."
        process(tb, int(size))
    else:
        sys.exit("Table Name is invalid.")
