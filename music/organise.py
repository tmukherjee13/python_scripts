"""
A Python script to move mp3 files from one directory to a
flat structure in another directory
Uses path.py module
"""

import sys
import eyed3
import argparse
import os
from shutil import copyfile

DIRECTORY = '/media/tarun/Dump/Music'  # music source Directory
COPY_DIRECTORY = '/media/tarun/Dump/Music/organised'  # Destination directory


def transfer():
    print "Copying Files from %s to %s" % (DIRECTORY, COPY_DIRECTORY)
    file_count = 0
    for folderName, _, filenames in os.walk(DIRECTORY):
        print('The current folder is ' + folderName)

        for filename in filenames:
            if filename.endswith('mp3'):
                filePath = os.path.join(folderName, filename)
                try:
                    file = eyed3.load(filePath)
                    bitrate = file.info.bit_rate[1]
                    file_count += 1
                    print "Copying %s " % filename
                    target = os.path.join(
                        COPY_DIRECTORY, str(bitrate), filename)
                    ensure_dir(target)
                    copyfile(filePath, target)
                    # print os.path.join(folderName, filename)
                    # print('FILE INSIDE ' + folderName + ': ' + filename)
                except:
                    pass

    print 'Transferred %s files' % file_count


def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)


if __name__ == "__main__":
    transfer()
