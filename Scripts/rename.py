'''
Python Code to rename corresponded images and label files of OpenImages dataset
'''

import os
from pathlib import Path
from shutil import move
import argparse

parser = argparse.ArgumentParser(
    description='Rename images and label files of OpenImages dataset')
parser.add_argument('--sourcepath', type=str,
                    default='dataset/', help='Path of class to convert')
parser.add_argument('--id', type=str, required=True, help='ID of object')
args = parser.parse_args()

ids = []
for file in os.listdir(args.sourcepath):  # Save all images in a list
    filename = os.fsdecode(file)
    if filename.endswith('.jpg'):
        ids.append(filename[:-4])

counter = 0
for counter, fname in enumerate(ids):
    os.rename(os.path.join(args.sourcepath, fname + '.jpg'),
              os.path.join(args.sourcepath, args.id + '_' + str(counter) + '.jpg'))
    os.rename(os.path.join(args.sourcepath, 'Label', fname + '.txt'),
              os.path.join(args.sourcepath, 'Label', args.id + '_' + str(counter) + '.txt'))
