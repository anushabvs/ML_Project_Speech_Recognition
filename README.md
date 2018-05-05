# ML_Project_Speech_Recognition

1. B V S ANUSHA - 173076001
2. K LAKSHMI PHALGUNI – 173070007

As a part of **EE769: Introduction to Machine learning course** we have done **Tensorflow Speech Recognition Challenge which is a kaggle competition.**

## Objective of the project

Tensorflow Speech Recognition Challenge was a Kaggle competition organised by Google Brain to use the Speech Commands Dataset to build an algorithm that understands simple spoken commands. https://www.kaggle.com/c/tensorflow-speech-recognition-challenge

## Architecture of the project

A typical Speech recognition system consists of a feature extractor and a neural network based classifier as shown in the figure below:
![speech Recognition system](../master/pic.png)

source: *https: //arxiv.org/pdf/1711.07128.pdf*

First, the input speech signal of length L is framed into overlapping frames of length l with a stride s, giving a total of T = (L−l)/s + 1 frames.  From each frame, F speech features are extracted, generating a total of T× F features for the entire input speech signal of length L. Log-mel filter bank energies (LFBE) and Mel-frequency cepstral coefficients (MFCC) are the commonly used human-engineered speech features in deep learning based speech-recognition, that are adapted from traditional speech processing techniques. 
Once the speech features are extracted, we train them using a neural network for classification as shown in the figure above.


**Model Used**

In our project we use a Convolutional Recurrent Neural Network(CRNN) classifier for this purpose.
C-RNN (https://arxiv.org/pdf/1711.07128.pdf)

**Code Architecture**

-Download the data for tensorflow speech commands and store it as train/audio and test/audio.
-Go to libs/classification and run the python files to prepare the data for training
-run Codes/train_crnn.py to train the CRNN
-The trained model is saved in checkpoints
-To test the trained model run, Codes/predict_test_wav.py

References

-C-RNN (https://arxiv.org/pdf/1711.07128.pdf)
-ML-KWS-for-MCU (https://github.com/ARM-software/ML-KWS-for-MCU) 
-Very Deep Convolutional Neural Network for Robust Speech Recognition (https://arxiv.org/pdf/1610.00277.pdf) 
-Speech Commands Dataset (https://research.googleblog.com/2017/08/launching-speech-commands-dataset.html) 
-ensorflow audio recognition tutorials: https://www.tensorflow.org/versions/master/tutorials/audio_recognition

