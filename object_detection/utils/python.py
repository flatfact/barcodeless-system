import tensorflow as tf
from object_detection.utils import dataset_util


flags = tf.app.flags
flags.DEFINE_string('output_path', '', 'Path to output TFRecord')
FLAGS = flags.FLAGS

def rec(encoded_cat_image_data):
    height = 1032.0
    width = 1200.0
    filename = 'example_cat.jpg'
    image_format = b'jpg'
    xmins = [322.0 / 1200.0]
    xmaxs = [1062.0 / 1200.0]
    ymins = [174.0 / 1032.0]
    ymaxs = [761.0 / 1032.0]
    classes_text = ['Cat']
    classes = [1]
    tf_example = tf.train.Example(features=tf.train.Features(feature={
        'image/height': dataset_util.int64_feature(height),
        'image/width': dataset_util.int64_feature(width),
        'image/filename': dataset_util.bytes_feature(filename),
        'image/source_id': dataset_util.bytes_feature(filename),
        'image/encoded': dataset_util.bytes_feature(encoded_image_data),
        'image/format': dataset_util.bytes_feature(image_format),
        'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
        'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
        'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
        'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
        'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
        'image/object/class/label': dataset_util.int64_list_feature(classes),
    }))
    return tf_example

import base64 
image = open('c:/Users/big_2/Desktop/cat.jpg', 'rb') #open binary file in read mode
image_read = image.read()
encode = base64.encodestring(image_read)
rec(encode)