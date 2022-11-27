'''
This script will convert annotations in an XML format as downloaded from the
Kaggle sources in 'sources.txt'.

All sources must be downloaded to the 'all_data' folder:

all_data/*.xml >>> labels/*.txt

'''

import xml.etree.ElementTree as ET
from pathlib import Path

pathlist = Path('all_data').glob('*.xml')
for path in pathlist:
    # path = 'all_data/N99.xml'
    tree = ET.parse(path)

    labelPath = 'labels/' + path.stem + '.txt'
    labelFile = open(labelPath, 'w')

    root = tree.getroot()
    image_width = float(root.find('size').find('width').text)
    image_height = float(root.find('size').find('height').text)

    # There might be multiple licence plates on the same image
    for annotation in root.findall('object'):
        bndbox = annotation.find('bndbox')
        xmin, ymin = float(bndbox[0].text), float(bndbox[1].text)
        xmax, ymax = float(bndbox[2].text), float(bndbox[3].text)

        bbwidth = xmax - xmin
        bbheight = ymax - ymin
        # We want the following format:
        # <object-class-id> <x> <y> <width> <height>
        # sizes in range 0..1
        labelFile.write(
            "0 {} {} {} {}".format(xmin/image_width, ymin/image_height,
                                   bbwidth/image_width, bbheight/image_height)
        )

    labelFile.close()


