import os
import argparse

parser = argparse.ArgumentParser(
    description='Rename images and label files of OpenImages dataset')
parser.add_argument('--sourcepath', type=str,
                    default='dataset/', help='Path of folder that contains files')
parser.add_argument('--old_string', type=str, required=True, help='String to be replaced')
parser.add_argument('--new_string', type=str, required=True, help='New string\'s value')
args = parser.parse_args()

for filename in os.listdir(args.sourcepath):
   with open(os.path.join(args.sourcepath, filename), 'r+') as f:
        content = f.read()
        f.seek(0)
        f.truncate()
        f.write(content.replace(args.old_string, args.new_string))