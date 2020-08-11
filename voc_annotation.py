import xml.etree.ElementTree as ET
from os import getcwd
import os

sets=[('2007', 'train'), ('2007', 'val'), ('2007', 'test')]

# classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]


def convert_annotation(year, image_id, list_file):
    print(image_id)
    in_file = open('./xml/%s.xml'%(image_id))
    # print(in_file)
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        # difficult = obj.find('difficult').text
        # cls = obj.find('name').text
        # if int(difficult)==1:
        #     continue
        cls_id =0
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

wd = getcwd()

for year, image_set in sets:
    # image_ids = open('VOCdevkit/VOC%s/ImageSets/Main/%s.txt'%(year, image_set)).read().strip().split()
    list_file = open('%s_%s.txt'%(year, image_set), 'w')
    for image_id in  os.listdir("./xml"):
        image_id=image_id.replace(".xml","")
        list_file.write('img/%s.png' % (image_id))
        convert_annotation(year, image_id, list_file)
        list_file.write('\n')
    list_file.close()
