import argparse
import os
import shutil

import numpy as np


def copy_random_files(proportion, src, dst):
    """
    Copia uma proporcao dos arquivos de arquivos da pasta src para a pasta dst.

    Arguments:
        :param proportion: proporcao de arquivos que serao copiados
        :type proportion: float
        :param src: pasta fonte dos arquivos
        :type src: str
        :param dst: pasta de destino
        :type dst: str
    """
    proportion = float(proportion)
    assert 0 < proportion <= 1, 'A proporcao deve ser um valor entre 0 e 1.'
    src_files = os.listdir(src)
    n = int(proportion * len(src_files))
    selected_files = np.random.choice(src_files, n, replace=False)
    for files in selected_files:
        file_name = os.path.join(src, files)
        if os.path.isfile(file_name) and files not in os.listdir(dst):
            shutil.copy(file_name, dst)


def compare_and_copy(dst, compared):
    """
    Compara e copia os arquivos que sao diferentes em duas pastas, somente os arquivos do primeiro argumento de compared
    serao copiados.

    Arguments:
        :param compared: pastas a serem comparadas.
        :type compared: tuple
        :param dst: pasta destino.
        :type dst: str
    """
    (folder_1, folder_2) = compared
    contents_1 = os.listdir(folder_1)
    contents_2 = os.listdir(folder_2)
    diff = list(set(contents_1) - set(contents_2))
    for files in diff:
        file_name = os.path.join(folder_1, files)
        if os.path.isfile(file_name) and files not in os.listdir(dst):
            shutil.copy(file_name, dst)


def main(args):
    assert args.source is not None, 'You must set a source folder.'
    if args.rnd_dst is not None:
        assert args.proportion is not None, 'You must set a number of files with -p.'
    elif args.proportion is not None:
        assert args.rnd_dst is not None, 'You must set a destination folder with -r.'

    if args.compare is not None:
        assert args.cmp_dst is not None, 'You must set a destination folder for comparation with -d.'
    elif args.cmp_dst is not None:
        assert args.compare is not None, 'You must set a folder to be compared with source with -c.'

    if args.rnd_dst is not None and args.proportion is not None:
        copy_random_files(args.proportion, args.source, args.rnd_dst)

    if args.compare is not None and args.cmp_dst is not None:
        compare_and_copy(args.cmp_dst, (args.source, args.compare))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sorter script for getting random files from folder and copying'
                                                 'to destination, or getting the files that are not in another folder.')

    parser.add_argument('-s', '--source', help='Source folder', required=True)
    parser.add_argument('-r', '--rnd_dst', help='Destination for random files', required=False)
    parser.add_argument('-p', '--proportion', help='Proportion of files to be copied', required=False)
    parser.add_argument('-c', '--compare', help='Folder to be compared with source', required=False)
    parser.add_argument('-d', '--cmp_dst', help='Destination for compared files', required=False)

    args = parser.parse_args()
    print(args)
    main(args)
