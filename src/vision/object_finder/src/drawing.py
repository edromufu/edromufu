# coding=utf-8
import cv2
import numpy as np


def get_data(detections, score_threshold=0.3, category_dict=None):
    """
    Pegar dados do dicionário de detecções.
    Arguments:
        :param detections: output do processo de execução do model do tensorflow.
        :type detections: dict
        :param score_threshold: limiar de avaliação para resultar em objeto encontrado.
        :type score_threshold: float
        :param category_dict: dicionário para dar nome as classes encontradas.
        :type category_dict: dict
        :return: tuple com (score, label, bounding_box)
        :rtype: tuple
    """
    data = []
    for detection in detections:
        for score, det_class, box in zip(detection['detection_scores'], detection['detection_classes'],
                                         detection['detection_boxes']):
            if score > score_threshold:
                if category_dict is None:
                    data.append((score, det_class, box))
                else:
                    data.append((score, category_dict[det_class], box))
    return data


def draw(image, detections, **kwargs):
    """
    Desenha as bounding boxes.
    Arguments:
        :param image: frame da filmagem.
        :type image: np.ndarray
        :param detections: detecções da.
        :type detections: dict
    Keywords:
        :param label_and_score: flag para desenhar label e score na imagem.
        :type label_and_score: bool
        :param bounding_box: flag para desenhar bouding box na imagem.
        :type bounding_box: bool
    """
    assert type(image) is np.ndarray, 'Images must be a single image.'
    if isinstance(image, list):
        assert len(image) <= len(detections), 'Size of images must be lesser or equal size of detections. Make sure the' \
                                              'detections are equivalent to the images provided.'
    label_and_score = None
    bounding_box = None
    if 'label_and_score' in kwargs.keys():
        assert type(kwargs['label_and_score']) is bool, 'label_and_score must be a boolean.'
        label_and_score = kwargs['label_and_score']
    if 'bounding_box' in kwargs.keys():
        assert type(kwargs['bounding_box']) is bool, 'bounding_box must be a boolean.'
        bounding_box = kwargs['bounding_box']

    score = None
    label = None
    temp_image = image.copy()
    for detection in detections:
        if label_and_score:
            score = detection[0]
            label = detection[1]
        if bounding_box:
            upper_left_point = (int(detection[2][1] * image.shape[1]),
                                int(detection[2][0] * image.shape[0]))
            bottom_right_point = (int(detection[2][3] * image.shape[1]),
                                  int(detection[2][2] * image.shape[0]))
            cv2.rectangle(temp_image, upper_left_point, bottom_right_point, (255, 0, 0), 3)
        cv2.putText(temp_image, label + ': ' + str(score), (upper_left_point[0] + 5, upper_left_point[1] + 15),
                    cv2.FONT_HERSHEY_COMPLEX, .5, color=(0, 255, 0))
    output = temp_image
    return output
