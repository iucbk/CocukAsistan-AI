"""
Python code to replace xml tag from all files in a folder
"""

import os
import argparse
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser(
    description='Rename images and label files of OpenImages dataset')
parser.add_argument('--path', type=str,
                    help='Path of folder that contains XML files')
parser.add_argument('--tag', type=str, required=True,
                    help='Tag that its value will be changed')
parser.add_argument('--value', type=str, required=True,
                    help='New value of the tag')
args = parser.parse_args()


for filename in os.listdir(args.path):
    if not filename.endswith('.xml'):
        continue
    fullname = os.path.join(args.path, filename)
    tree = ET.parse(fullname)

    # TODO: kullanışlılığı artıtmak için path için ayrı herhangi tag
    # için ayrı seçenek sunarak full CLI olarak çalışsın
    # tree.find('path').text = os.path.join(args.path, filename.replace('.xml', '.jpg'))
    tree.find(args.tag).text = args.value
    tree.write(fullname)
