import argparse
import glob
import xml.etree.ElementTree as ET

import pandas as pd


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main(args):
    xml_df = xml_to_csv(args.source)
    xml_df.to_csv(args.dst, index=None)
    print('Successfully converted xml to csv.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert xml file to csv.')

    parser.add_argument('-d', '--dst', help='Destination file')
    parser.add_argument('-s', '--source', help='Source folder.')

    args = parser.parse_args()

    main(args)
