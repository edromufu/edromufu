# coding=utf-8
"""
Use este script quando tiver que importar anotações de outro computador, pela maneira que o labelimg funciona, o elemento
path seria setado para o computador de quem setou os parametros, esse script corrige essa variavel em todos os pcs.

Ex:
    python solve_annotations.py ~/edrom/ros/py_vision/annotations/all
"""

import argparse
import os
import xml.etree.ElementTree as ET

from src.finder_package import utils as uts


def set_right_path(path):
    if not path.endswith('/'):
        path = path + '/'
    files_in_path = os.listdir(path)
    files = [path + res for res in files_in_path]
    for file in files:
        tree = ET.parse(file)
        root = tree.getroot()
        for path in root.iter('path'):
            if uts.root_dir != tree.findtext('path').split('vision')[0] + 'vision/':
                path.text = uts.root_dir + 'annotations/all'
        tree.write(file)


def main(args):
    set_right_path(args.path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', help='Set path of annotations folder.')
    args = parser.parse_args()
    main(args)
