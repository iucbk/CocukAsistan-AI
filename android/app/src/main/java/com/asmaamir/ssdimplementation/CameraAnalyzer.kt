package com.asmaamir.ssdimplementation

import android.graphics.*
import android.media.Image
import android.util.Log
import androidx.camera.core.ImageAnalysis
import androidx.camera.core.ImageProxy
import com.google.firebase.ml.custom.FirebaseModelDataType
import com.google.firebase.ml.custom.FirebaseModelInputOutputOptions
import com.google.firebase.ml.custom.FirebaseModelInputs
import com.google.firebase.ml.custom.FirebaseModelInterpreter
import java.io.ByteArrayOutputStream

class CameraAnalyzer(remoteInterpreter: FirebaseModelInterpreter) : ImageAnalysis.Analyzer {
    private val TAG = "CameraAnalyzer"
    private val DIM_HEIGHT = 300
    private val DIM_WIDTH = 300
    private val DIM_COLOR = 3
    private val BATCH = 1
    private val OUTPUT_DIM_1 = 10
    private val OUTPUT_DIM_2 = 4

    private var interpreter: FirebaseModelInterpreter = remoteInterpreter

    override fun analyze(imageProxy: ImageProxy?, rotationDegrees: Int) {
        var image = imageProxy!!.image
        val bitmap = Bitmap.createScaledBitmap(image!!.toBitmap(), DIM_WIDTH, DIM_HEIGHT, true)
        val batchNum = 0
        val input = Array(1) { Array(DIM_WIDTH) { Array(DIM_HEIGHT) { FloatArray(DIM_COLOR) } } }
        for (x in 0 until DIM_WIDTH) {
            for (y in 0 until DIM_HEIGHT) {
                val pixel = bitmap.getPixel(x, y)
                // Normalize channel values to [-1.0, 1.0]. This requirement varies by
                // model. For example, some models might require values to be normalized
                // to the range [0.0, 1.0] instead.
                input[batchNum][x][y][0] = (Color.red(pixel) - 127) / 255.0f
                input[batchNum][x][y][1] = (Color.green(pixel) - 127) / 255.0f
                input[batchNum][x][y][2] = (Color.blue(pixel) - 127) / 255.0f
            }
        }

        val inputs = FirebaseModelInputs.Builder()
            .add(input) // add() as many input arrays as your model requires
            .build()

        val inputOutputOptions = FirebaseModelInputOutputOptions.Builder()
            .setInputFormat(
                0,
                FirebaseModelDataType.FLOAT32,
                intArrayOf(1, DIM_WIDTH, DIM_HEIGHT, DIM_COLOR)
            )
            .setOutputFormat(
                0,
                FirebaseModelDataType.FLOAT32,
                intArrayOf(BATCH, OUTPUT_DIM_1, OUTPUT_DIM_2)
            )
            .build()

        interpreter.run(inputs, inputOutputOptions)
            .addOnSuccessListener { result ->
                val output = result.getOutput<Array<Array<FloatArray>>>(0)
                val probabilities = output[0][0][0]
                Log.i(TAG, probabilities.toString())
            }
            .addOnFailureListener { e ->
                Log.e(TAG, "Failed to inference")
            }

    }

    private fun Image.toBitmap(): Bitmap {
        val yBuffer = planes[0].buffer // Y
        val uBuffer = planes[1].buffer // U
        val vBuffer = planes[2].buffer // V

        val ySize = yBuffer.remaining()
        val uSize = uBuffer.remaining()
        val vSize = vBuffer.remaining()

        val nv21 = ByteArray(ySize + uSize + vSize)

        //U and V are swapped
        yBuffer.get(nv21, 0, ySize)
        vBuffer.get(nv21, ySize, vSize)
        uBuffer.get(nv21, ySize + vSize, uSize)

        val yuvImage = YuvImage(nv21, ImageFormat.NV21, this.width, this.height, null)
        val out = ByteArrayOutputStream()
        yuvImage.compressToJpeg(Rect(0, 0, yuvImage.width, yuvImage.height), 50, out)
        val imageBytes = out.toByteArray()
        return BitmapFactory.decodeByteArray(imageBytes, 0, imageBytes.size)
    }
}