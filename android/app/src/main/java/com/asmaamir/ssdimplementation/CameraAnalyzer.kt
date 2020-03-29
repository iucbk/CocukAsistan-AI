package com.asmaamir.ssdimplementation

import android.util.Log
import androidx.camera.core.ImageAnalysis
import androidx.camera.core.ImageProxy

class CameraAnalyzer : ImageAnalysis.Analyzer {
    private val TAG = "CameraAnalyzer"
    override fun analyze(image: ImageProxy?, rotationDegrees: Int) {
        Log.i(TAG, "Camera analyzer is linked")
    }
}