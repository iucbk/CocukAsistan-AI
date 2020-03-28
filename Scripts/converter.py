import tensorflow as tf
import argparse

parser = argparse.ArgumentParser(
    description='Rename images and label files of OpenImages dataset')
parser.add_argument('--pb_path', type=str,
                     help='Path to .pb file')
parser.add_argument('--tflite_out', type=str, required=True, help='Path to tflite as output, e.g.: /out/model.tflite')
args = parser.parse_args()


input_arrays=["image_tensor"]

output_arrays=["detection_boxes","detection_classes","detection_scores","num_detections"]

converter= tf.lite.TocoConverter.from_frozen_graph(args.pb_path, input_arrays, output_arrays)

model = converter.convert()
open(args.tflite_out, "wb").write(model)