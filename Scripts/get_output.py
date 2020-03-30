"""
👀 https://stackoverflow.com/a/57257786/12784629
"""
import tensorflow as tf
Graph = tf.GraphDef()   
File = open("E:/training_demo/inference/output_ssd_tflite/tflite_graph.pb","rb")
Graph.ParseFromString(File.read())
"""
# bütün katmanların girişini gör
for Layer in Graph.node:
    print(Layer.name)
"""
# son katman
print(Graph.node[-1].name)