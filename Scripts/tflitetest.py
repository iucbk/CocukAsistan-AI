import numpy as np
import tensorflow as tf
from cv2 import imread, resize
from numpy import expand_dims

# Load TFLite model and allocate tensors.
interpreter = tf.lite.Interpreter(model_path="ssd_mobilenet_v1.tflite")
interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()


try :

    image = imread('dog.jpg' )
    image_cc = image.copy( )

    assert len( image.shape ) == 3
    image = image.astype( 'float32' )

    image = resize( image, ( 300, 300  ) )
    image = expand_dims( image, 0 )

    interpreter.set_tensor( input_details[0][ 'index' ], image )
    interpreter.invoke( )

except AssertionError :
  print( '[ INFO ] Expecting image to have 3 dimensions but found image with dimension(s) {}'.format( image.shape ) )

output_data = interpreter.get_tensor( output_details[ 2 ][ 'index' ] )

print(output_data)
