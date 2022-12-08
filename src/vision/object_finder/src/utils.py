import os
import tarfile
from os import listdir
from os.path import isfile, join

import cv2
import numpy as np
import six.moves.urllib as urllib
import label_map_util
# import src

# Verificando se esta rodando em um conteiner do Docker ou nao
## Se nao for um conteiner, o diretorio root_dir eh o seguinte
root_dir = os.path.expanduser('~') + '/edrom_2020/src/vision/object_finder/'

## Se for um conteiner, o diretorio root_dir eh o definido dentro do for
arq = open('/proc/self/cgroup', 'r')
linhas = arq.readlines()

for linha in linhas:
    if 'docker' in linha:
        root_dir = '/home/edrom_user/edrom/src/vision/object_finder/'
        break

pre_trained_models_dir = root_dir + 'pre_trained_models/'
labels_dir = root_dir + 'data/'


def read_image_from_file(path):
    """
    Read an image from file.

        :param path: path to file.
        :type path: str
        :returns: an image (np.ndarray).
    """
    image = cv2.imread(path)
    assert type(image) is np.ndarray, 'Could not open file' + str(path) + ', verify extension.'
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image


def read_images_from_folder(path):
    """
    Read all images from folder.

        :param path: path to folder.
        :type path: str
        :returns: list of images(np.ndarray) available in folder.
    """
    files = [join(path, f) for f in listdir(path) if isfile(join(path, f)) if
             (f.endswith(".png") or f.endswith(".jpeg") or f.endswith(".jpg"))]
    return [read_image_from_file(file) for file in files]


def download_model(model):
    """
    Downloads model from tensorflow object.py detection api.

        :param model: name of the model to be downloaded.
        :type model: str
    """

    try:
        os.chdir(pre_trained_models_dir)
    except OSError:
        print('pre_trained_models folder not found at repository root. Creating...')
        os.mkdir(pre_trained_models_dir)
        os.chdir(pre_trained_models_dir)

    model_file = model + ".tar.gz"
    download_base = 'http://download.tensorflow.org/models/object_detection/'

    if model_file not in os.listdir(pre_trained_models_dir):
        print('Downloading model ' + model)
        opener = urllib.request.URLopener()
        opener.retrieve(download_base + model_file, model_file)
    __extract_pb(model)


def __extract_pb(model):
    """
    Extract pb file from tar file.

    Arguments:
        :param model: model tar file name.
        :type model: str
    """
    model_file = model + ".tar.gz"
    if model not in os.listdir(pre_trained_models_dir):
        has_graph = False
        tar_file = tarfile.open(model_file)
        for file in tar_file.getmembers():
            file_name = os.path.basename(file.name)
            if 'frozen_inference_graph.pb' in file_name:
                has_graph = True
                tar_file.extract(file, pre_trained_models_dir)
        if has_graph is False:
            raise OSError('Frozen_inference_graph.pb not found in tar file.')


def load_labels(labels_path, num_classes=90):
    """
    Load labels from .pbtxt file.

        :param labels_path: path to labels file(.pbtxt).
        :type labels_path: str
        :param num_classes: number of classes in the labels file.
        :type num_classes: int
    """
    try:
        label_map = label_map_util.load_labelmap(labels_path)
    except OSError:
        raise OSError('Provided labels_path does not exist.')

    categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=num_classes,
                                                                use_display_name=True)
    categories = label_map_util.create_category_index(categories)
    for ids in categories.values():
        categories[ids['id']] = ids['name']
    return categories
