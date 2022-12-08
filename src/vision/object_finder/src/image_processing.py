# coding=utf-8
import sys
import os
user_name = os.environ.get("HOME")
sys.path.append(user_name + "/edrom/src/vision/object_finder/models/research/object_detection/utils")
sys.path.append(user_name + "/edrom/src/vision/object_finder/models/research/")
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


import numpy as np
import tensorflow.compat.v1 as tf
from object_detection.utils import ops as util_ops
from object_detection.utils import visualization_utils as visual

import src.utils as uts


class ImageProcessing:
    def __init__(self, model="ssd_edrom", labels='label_map.pbtxt'):
        """
        Construtor da classe ImageProcessing.
        :param model: modelo pre treinado usado para deep learning, default é o ssd_v1_coco
        :type model: str
        :param labels: arquivo que descreve as classes do dataset.
        :type labels: str
        """
        self.pb_path = uts.pre_trained_models_dir + model + '/frozen_inference_graph.pb'

        if model is not "ssd_edrom" and model is not "ssd_edrom_v1":
            uts.download_model(model)

        self.category_index = None
        self.tensor_dict = {}
        self.graph = self.load_model()
        self.session = tf.Session(graph=self.graph)

        if labels is not None:
            labels_path = uts.labels_dir + labels
            self.category_index = uts.load_labels(labels_path)

    def __del__(self):
        self.session.close()

    def load_model(self):
        """
                Load frozen TensorFlow model from .pb file into memory. The model loaded is the one set in the constructor.

                    :return: tensorflow graph from loaded model.
                """
        detection_graph = tf.Graph()
        with detection_graph.as_default():
            od_graph_def = tf.GraphDef()
            with tf.gfile.GFile(self.pb_path, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')
        return detection_graph

    def __run_inference_for_frame(self, image):
        """
                Run inference for a single image, detecting the features in the image.

                :param image: image to be processed.
                :type image: numpy array
                :return: output dictionary containing the detection.
                """
        with self.graph.as_default():
            operations = tf.get_default_graph().get_operations()
            all_tensor_names = {output.name for op in operations for output in op.outputs}
            for key in ['num_detections', 'detection_boxes', 'detection_scores', 'detection_classes',
                        'detection_masks']:
                tensor_name = key + ':0'
                if tensor_name in all_tensor_names:
                    self.tensor_dict[key] = tf.get_default_graph().get_tensor_by_name(tensor_name)
            if 'detection_masks' in self.tensor_dict:
                detection_boxes = tf.squeeze(self.tensor_dict['detection_boxes'], [0])
                detection_masks = tf.squeeze(self.tensor_dict['detection_masks'], [0])

                real_num_detection = tf.cast(self.tensor_dict['num_detections'][0], tf.int32)
                detection_boxes = tf.slice(detection_boxes, [0, 0], [real_num_detection, -1])
                detection_masks = tf.slice(detection_masks, [0, 0, 0], [real_num_detection, -1, -1])
                detection_masks_reframed = util_ops.reframe_box_masks_to_image_masks(
                    detection_masks, detection_boxes, image.shape[0], image.shape[1])
                detection_masks_reframed = tf.cast(tf.greater(detection_masks_reframed, 0.5), tf.uint8)
                self.tensor_dict['detection_masks'] = tf.expand_dims(detection_masks_reframed, 0)

            image_tensor = tf.get_default_graph().get_tensor_by_name('image_tensor:0')

            output_dict = self.session.run(self.tensor_dict, feed_dict={image_tensor: np.expand_dims(image, axis=0)})

            # all outputs are float32 numpy arrays, so convert types as appropriate
            output_dict['num_detections'] = int(output_dict['num_detections'][0])
            output_dict['detection_classes'] = output_dict['detection_classes'][0].astype(np.uint8)
            output_dict['detection_boxes'] = output_dict['detection_boxes'][0]
            output_dict['detection_scores'] = output_dict['detection_scores'][0]
            if 'detection_masks' in output_dict:
                output_dict['detection_masks'] = output_dict['detection_masks'][0]

        return output_dict

    def detect(self, images, **kwargs):
        """
        Detect all possible objects in images.
            :param images: list of images or single image to be processed.
            :type images: list[numpy array] or numpy array
            :keyword visualize: (bool) activate visualization of output.
            :return: output dictionary with detections.
        """
        assert type(images) is list or type(images) is np.ndarray, 'Images must be either a list of np.array' \
                                                                   ' or a single np.array.'
        visualize = False
        if kwargs is not None and 'visualize' in kwargs.keys():
            assert type(kwargs['visualize']) is bool, 'Keyword visualize must be of type bool.'
            visualize = kwargs['visualize']

        if type(images) is np.ndarray:
            images = [images]

        outputs = []
        for image in images:
            outputs.append(self.__run_inference_for_frame(image))
            # if visualize is True:
            #     if 'detection_masks' in outputs[-1]:
            #         visual.visualize_boxes_and_labels_on_image_array(image,
            #                                                          outputs[-1]['detection_boxes'],
            #                                                          outputs[-1]['detection_classes'],
            #                                                          outputs[-1]['detection_scores'],
            #                                                          self.category_index,
            #                                                          instance_masks=outputs[-1]['detection_masks'],
            #                                                          use_normalized_coordinates=True,
            #                                                          line_thickness=6)
            #     else:
            #         visual.visualize_boxes_and_labels_on_image_array(image,
            #                                                          outputs[-1]['detection_boxes'],
            #                                                          outputs[-1]['detection_classes'],
            #                                                          outputs[-1]['detection_scores'],
            #                                                          self.category_index,
            #                                                          use_normalized_coordinates=True,
            #                                                          line_thickness=6)
            #     # plt.imshow(image)
                # plt.show()
        return outputs
