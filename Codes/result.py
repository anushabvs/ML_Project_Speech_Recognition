Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
============= RESTART: F:\ML_Project\notebooks\Training_CRNN.py =============
WARNING:tensorflow:From C:\Users\ADMIN\AppData\Local\Programs\Python\Python36\lib\site-packages\tensorflow\contrib\learn\python\learn\datasets\base.py:198: retry (from tensorflow.contrib.learn.python.learn.datasets.base) is deprecated and will be removed in a future version.
Instructions for updating:
Use the retry module or similar alternatives.
[name: "/device:CPU:0"
device_type: "CPU"
memory_limit: 268435456
locality {
}
incarnation: 3367256102908305598
, name: "/device:GPU:0"
device_type: "GPU"
memory_limit: 1500636774
locality {
  bus_id: 1
  links {
  }
}
incarnation: 7773563022904453660
physical_device_desc: "device: 0, name: GeForce 840M, pci bus id: 0000:08:00.0, compute capability: 5.0"
]
Traceback (most recent call last):
  File "F:\ML_Project\notebooks\Training_CRNN.py", line 14, in <module>
    K.tensorflow_backend._get_available_gpus()
NameError: name 'K' is not defined
>>> with tf.device('/gpu:0')
SyntaxError: invalid syntax
>>> tf.device('/gpu:0')
<contextlib._GeneratorContextManager object at 0x000001CE48406160>
>>> tf.device
<function device at 0x000001CE4FC44EA0>
>>> print tf.device('/gpu:0')
SyntaxError: invalid syntax
>>> print(tf.device('/gpu:0'))
<contextlib._GeneratorContextManager object at 0x000001CE48406160>
>>> 
============= RESTART: F:\ML_Project\notebooks\Training_CRNN.py =============
WARNING:tensorflow:From C:\Users\ADMIN\AppData\Local\Programs\Python\Python36\lib\site-packages\tensorflow\contrib\learn\python\learn\datasets\base.py:198: retry (from tensorflow.contrib.learn.python.learn.datasets.base) is deprecated and will be removed in a future version.
Instructions for updating:
Use the retry module or similar alternatives.
[name: "/device:CPU:0"
device_type: "CPU"
memory_limit: 268435456
locality {
}
incarnation: 3495665183333056257
, name: "/device:GPU:0"
device_type: "GPU"
memory_limit: 1500636774
locality {
  bus_id: 1
  links {
  }
}
incarnation: 14633455872739350885
physical_device_desc: "device: 0, name: GeForce 840M, pci bus id: 0000:08:00.0, compute capability: 5.0"
]
F:\ML_Project\Data\train\audio\*\*.wav
F:\ML_Project\Data\train\audio\_background_noise_\doing_the_dishes.wav
F:\ML_Project\Data\train\audio\_background_noise_\dude_miaowing.wav
F:\ML_Project\Data\train\audio\_background_noise_\exercise_bike.wav
F:\ML_Project\Data\train\audio\_background_noise_\pink_noise.wav
F:\ML_Project\Data\train\audio\_background_noise_\running_tap.wav
F:\ML_Project\Data\train\audio\_background_noise_\white_noise.wav
Tensor("AudioSpectrogram:0", shape=(?, 49, 513), dtype=float32)
WARNING:tensorflow:From ..\libs\classification\trainer.py:60: softmax_cross_entropy_with_logits (from tensorflow.python.ops.nn_ops) is deprecated and will be removed in a future version.
Instructions for updating:

Future major versions of TensorFlow will allow gradients to flow
into the labels input on backprop by default.

See tf.nn.softmax_cross_entropy_with_logits_v2.

WARNING:tensorflow:From ..\libs\classification\trainer.py:74: get_or_create_global_step (from tensorflow.contrib.framework.python.ops.variables) is deprecated and will be removed in a future version.
Instructions for updating:
Please switch to tf.train.get_or_create_global_step
INFO:tensorflow:Training from step: 1 
INFO:tensorflow:Step #10: rate 0.000500, accuracy 7.4%, cross entropy 2.471514
INFO:tensorflow:Step #20: rate 0.000500, accuracy 14.5%, cross entropy 2.445806
INFO:tensorflow:Step #30: rate 0.000500, accuracy 12.1%, cross entropy 2.424612
INFO:tensorflow:Step #40: rate 0.000500, accuracy 16.0%, cross entropy 2.395563
INFO:tensorflow:Step #50: rate 0.000500, accuracy 16.4%, cross entropy 2.342727
INFO:tensorflow:Step #60: rate 0.000500, accuracy 21.9%, cross entropy 2.264127
INFO:tensorflow:Step #70: rate 0.000500, accuracy 22.3%, cross entropy 2.144122
INFO:tensorflow:Step #80: rate 0.000500, accuracy 20.7%, cross entropy 2.104248
INFO:tensorflow:Step #90: rate 0.000500, accuracy 25.4%, cross entropy 1.986801
INFO:tensorflow:Step #100: rate 0.000500, accuracy 24.6%, cross entropy 1.989562
INFO:tensorflow:Step #110: rate 0.000500, accuracy 26.6%, cross entropy 1.911603
INFO:tensorflow:Step #120: rate 0.000500, accuracy 26.2%, cross entropy 1.797597
INFO:tensorflow:Step #130: rate 0.000500, accuracy 29.7%, cross entropy 1.922492
INFO:tensorflow:Step #140: rate 0.000500, accuracy 28.5%, cross entropy 1.890504
INFO:tensorflow:Step #150: rate 0.000500, accuracy 31.6%, cross entropy 1.798714
INFO:tensorflow:Step #160: rate 0.000500, accuracy 32.8%, cross entropy 1.692816
INFO:tensorflow:Step #170: rate 0.000500, accuracy 37.1%, cross entropy 1.676234
INFO:tensorflow:Step #180: rate 0.000500, accuracy 34.4%, cross entropy 1.691938
INFO:tensorflow:Step #190: rate 0.000500, accuracy 36.3%, cross entropy 1.683062
INFO:tensorflow:Step #200: rate 0.000500, accuracy 35.9%, cross entropy 1.672312
INFO:tensorflow:Step #210: rate 0.000500, accuracy 38.7%, cross entropy 1.606414
INFO:tensorflow:Step #220: rate 0.000500, accuracy 39.8%, cross entropy 1.575878
INFO:tensorflow:Step #230: rate 0.000500, accuracy 35.9%, cross entropy 1.633143
INFO:tensorflow:Step #240: rate 0.000500, accuracy 38.7%, cross entropy 1.592931
INFO:tensorflow:Step #250: rate 0.000500, accuracy 46.1%, cross entropy 1.483034
INFO:tensorflow:Step #260: rate 0.000500, accuracy 37.5%, cross entropy 1.578260
INFO:tensorflow:Step #270: rate 0.000500, accuracy 41.4%, cross entropy 1.571039
INFO:tensorflow:Step #280: rate 0.000500, accuracy 45.7%, cross entropy 1.437389
INFO:tensorflow:Step #290: rate 0.000500, accuracy 43.4%, cross entropy 1.546887
INFO:tensorflow:Step #300: rate 0.000500, accuracy 48.4%, cross entropy 1.408759
INFO:tensorflow:Step #310: rate 0.000500, accuracy 46.5%, cross entropy 1.464761
INFO:tensorflow:Step #320: rate 0.000500, accuracy 48.8%, cross entropy 1.381488
INFO:tensorflow:Step #330: rate 0.000500, accuracy 53.1%, cross entropy 1.316842
INFO:tensorflow:Step #340: rate 0.000500, accuracy 51.6%, cross entropy 1.430447
INFO:tensorflow:Step #350: rate 0.000500, accuracy 51.2%, cross entropy 1.306969
INFO:tensorflow:Step #360: rate 0.000500, accuracy 55.1%, cross entropy 1.265547
INFO:tensorflow:Step #370: rate 0.000500, accuracy 52.3%, cross entropy 1.372509
INFO:tensorflow:Step #380: rate 0.000500, accuracy 52.7%, cross entropy 1.262455
INFO:tensorflow:Step #390: rate 0.000500, accuracy 60.5%, cross entropy 1.188506
INFO:tensorflow:Step #400: rate 0.000500, accuracy 54.3%, cross entropy 1.240172
INFO:tensorflow:Step #410: rate 0.000500, accuracy 58.6%, cross entropy 1.205467
INFO:tensorflow:Step #420: rate 0.000500, accuracy 56.6%, cross entropy 1.247920
INFO:tensorflow:Step #430: rate 0.000500, accuracy 59.0%, cross entropy 1.122763
INFO:tensorflow:Step #440: rate 0.000500, accuracy 57.8%, cross entropy 1.182712
INFO:tensorflow:Step #450: rate 0.000500, accuracy 63.7%, cross entropy 1.119436
INFO:tensorflow:Step #460: rate 0.000500, accuracy 63.3%, cross entropy 1.169107
INFO:tensorflow:Step #470: rate 0.000500, accuracy 62.5%, cross entropy 1.150117
INFO:tensorflow:Step #480: rate 0.000500, accuracy 63.3%, cross entropy 1.087967
INFO:tensorflow:Step #490: rate 0.000500, accuracy 62.9%, cross entropy 1.065712
INFO:tensorflow:Step #500: rate 0.000500, accuracy 64.1%, cross entropy 1.104290
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0  74  19  29  10  27   9  43  19   5  12  11]
 [  0   4 242   3   1   0  10   1   0   0   0   0]
 [  0   3   7 230   0   7   2   1   0   0   7  13]
 [  0   4   0   1 201   0   1   2   1  21  29   0]
 [  0   0   2  29   0 202   1   0   0   0   2  28]
 [  0   3  40   0   3   0 197   4   0   0   0   0]
 [  0  11   1   1   2   0   9 230   2   0   0   0]
 [  0   9   0   0   2   1   1   3 235   5   1   0]
 [  0   1   0   0  29   1   0   0  11 211   3   0]
 [  0   4   0   1  33   1   2   0   0   3 196   6]
 [  0   7   2  62   4  21   3   2   2   1  16 140]]
INFO:tensorflow:Step 500: Validation accuracy = 76.1% (N=2835)
INFO:tensorflow:Step #510: rate 0.000500, accuracy 59.8%, cross entropy 1.043521
INFO:tensorflow:Step #520: rate 0.000500, accuracy 64.5%, cross entropy 1.071813
INFO:tensorflow:Step #530: rate 0.000500, accuracy 62.9%, cross entropy 1.066072
INFO:tensorflow:Step #540: rate 0.000500, accuracy 62.9%, cross entropy 1.050199
INFO:tensorflow:Step #550: rate 0.000500, accuracy 67.2%, cross entropy 1.052099
INFO:tensorflow:Step #560: rate 0.000500, accuracy 65.2%, cross entropy 0.993710
INFO:tensorflow:Step #570: rate 0.000500, accuracy 63.3%, cross entropy 1.019499
INFO:tensorflow:Step #580: rate 0.000500, accuracy 66.4%, cross entropy 0.984213
INFO:tensorflow:Step #590: rate 0.000500, accuracy 69.1%, cross entropy 1.008450
INFO:tensorflow:Step #600: rate 0.000500, accuracy 69.5%, cross entropy 0.913361
INFO:tensorflow:Step #610: rate 0.000500, accuracy 70.7%, cross entropy 0.830305
INFO:tensorflow:Step #620: rate 0.000500, accuracy 67.2%, cross entropy 0.921733
INFO:tensorflow:Step #630: rate 0.000500, accuracy 71.5%, cross entropy 0.853920
INFO:tensorflow:Step #640: rate 0.000500, accuracy 69.1%, cross entropy 0.920393
INFO:tensorflow:Step #650: rate 0.000500, accuracy 69.1%, cross entropy 0.917135
INFO:tensorflow:Step #660: rate 0.000500, accuracy 72.7%, cross entropy 0.859675
INFO:tensorflow:Step #670: rate 0.000500, accuracy 69.1%, cross entropy 0.965394
INFO:tensorflow:Step #680: rate 0.000500, accuracy 71.1%, cross entropy 0.919541
INFO:tensorflow:Step #690: rate 0.000500, accuracy 71.5%, cross entropy 0.910799
INFO:tensorflow:Step #700: rate 0.000500, accuracy 71.9%, cross entropy 0.816543
INFO:tensorflow:Step #710: rate 0.000500, accuracy 77.0%, cross entropy 0.771597
INFO:tensorflow:Step #720: rate 0.000500, accuracy 74.2%, cross entropy 0.866097
INFO:tensorflow:Step #730: rate 0.000500, accuracy 76.6%, cross entropy 0.629374
INFO:tensorflow:Step #740: rate 0.000500, accuracy 73.0%, cross entropy 0.842213
INFO:tensorflow:Step #750: rate 0.000500, accuracy 79.3%, cross entropy 0.663132
INFO:tensorflow:Step #760: rate 0.000500, accuracy 69.5%, cross entropy 0.935924
INFO:tensorflow:Step #770: rate 0.000500, accuracy 74.6%, cross entropy 0.860145
INFO:tensorflow:Step #780: rate 0.000500, accuracy 75.8%, cross entropy 0.777732
INFO:tensorflow:Step #790: rate 0.000500, accuracy 77.0%, cross entropy 0.710029
INFO:tensorflow:Step #800: rate 0.000500, accuracy 73.4%, cross entropy 0.749168
INFO:tensorflow:Step #810: rate 0.000500, accuracy 74.2%, cross entropy 0.778223
INFO:tensorflow:Step #820: rate 0.000500, accuracy 66.0%, cross entropy 0.961410
INFO:tensorflow:Step #830: rate 0.000500, accuracy 73.4%, cross entropy 0.844839
INFO:tensorflow:Step #840: rate 0.000500, accuracy 75.8%, cross entropy 0.718276
INFO:tensorflow:Step #850: rate 0.000500, accuracy 78.5%, cross entropy 0.684199
INFO:tensorflow:Step #860: rate 0.000500, accuracy 76.2%, cross entropy 0.731373
INFO:tensorflow:Step #870: rate 0.000500, accuracy 74.2%, cross entropy 0.757235
INFO:tensorflow:Step #880: rate 0.000500, accuracy 77.3%, cross entropy 0.718468
INFO:tensorflow:Step #890: rate 0.000500, accuracy 73.0%, cross entropy 0.819456
INFO:tensorflow:Step #900: rate 0.000500, accuracy 74.2%, cross entropy 0.773355
INFO:tensorflow:Step #910: rate 0.000500, accuracy 69.9%, cross entropy 0.886162
INFO:tensorflow:Step #920: rate 0.000500, accuracy 80.9%, cross entropy 0.628369
INFO:tensorflow:Step #930: rate 0.000500, accuracy 77.0%, cross entropy 0.725264
INFO:tensorflow:Step #940: rate 0.000500, accuracy 75.8%, cross entropy 0.715845
INFO:tensorflow:Step #950: rate 0.000500, accuracy 73.4%, cross entropy 0.773077
INFO:tensorflow:Step #960: rate 0.000500, accuracy 78.1%, cross entropy 0.632515
INFO:tensorflow:Step #970: rate 0.000500, accuracy 73.8%, cross entropy 0.827167
INFO:tensorflow:Step #980: rate 0.000500, accuracy 77.0%, cross entropy 0.763046
INFO:tensorflow:Step #990: rate 0.000500, accuracy 76.2%, cross entropy 0.757982
INFO:tensorflow:Step #1000: rate 0.000500, accuracy 82.0%, cross entropy 0.554462
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 136  10  11  11  14  15  20  13   2   8  18]
 [  0   1 248   2   3   0   7   0   0   0   0   0]
 [  0   5   8 238   0   4   0   0   0   0   4  11]
 [  0   5   0   0 243   0   0   1   1   7   3   0]
 [  0   2   2  10   0 235   0   0   0   0   2  13]
 [  0   2  26   0   2   0 216   1   0   0   0   0]
 [  0  10   1   0   2   0   6 236   1   0   0   0]
 [  0   7   0   0   5   0   1   0 238   5   1   0]
 [  0   0   0   0  24   0   0   0   8 223   0   1]
 [  0   1   0   1  22   0   1   0   0   3 214   4]
 [  0   8   1  20   9   7   3   0   2   1   3 206]]
INFO:tensorflow:Step 1000: Validation accuracy = 85.8% (N=2835)
INFO:tensorflow:Step #1010: rate 0.000500, accuracy 77.0%, cross entropy 0.787006
INFO:tensorflow:Step #1020: rate 0.000500, accuracy 83.2%, cross entropy 0.607213
INFO:tensorflow:Step #1030: rate 0.000500, accuracy 76.2%, cross entropy 0.744203
INFO:tensorflow:Step #1040: rate 0.000500, accuracy 78.5%, cross entropy 0.689395
INFO:tensorflow:Step #1050: rate 0.000500, accuracy 75.8%, cross entropy 0.710653
INFO:tensorflow:Step #1060: rate 0.000500, accuracy 79.7%, cross entropy 0.656738
INFO:tensorflow:Step #1070: rate 0.000500, accuracy 75.4%, cross entropy 0.773389
INFO:tensorflow:Step #1080: rate 0.000500, accuracy 78.1%, cross entropy 0.696653
INFO:tensorflow:Step #1090: rate 0.000500, accuracy 78.9%, cross entropy 0.707980
INFO:tensorflow:Step #1100: rate 0.000500, accuracy 78.9%, cross entropy 0.655459
INFO:tensorflow:Step #1110: rate 0.000500, accuracy 80.9%, cross entropy 0.637904
INFO:tensorflow:Step #1120: rate 0.000500, accuracy 80.5%, cross entropy 0.607262
INFO:tensorflow:Step #1130: rate 0.000500, accuracy 80.5%, cross entropy 0.631078
INFO:tensorflow:Step #1140: rate 0.000500, accuracy 78.5%, cross entropy 0.750983
INFO:tensorflow:Step #1150: rate 0.000500, accuracy 80.5%, cross entropy 0.614332
INFO:tensorflow:Step #1160: rate 0.000500, accuracy 81.2%, cross entropy 0.586971
INFO:tensorflow:Step #1170: rate 0.000500, accuracy 78.1%, cross entropy 0.663341
INFO:tensorflow:Step #1180: rate 0.000500, accuracy 77.3%, cross entropy 0.672477
INFO:tensorflow:Step #1190: rate 0.000500, accuracy 77.3%, cross entropy 0.641489
INFO:tensorflow:Step #1200: rate 0.000500, accuracy 83.6%, cross entropy 0.544367
INFO:tensorflow:Step #1210: rate 0.000500, accuracy 81.2%, cross entropy 0.577797
INFO:tensorflow:Step #1220: rate 0.000500, accuracy 81.2%, cross entropy 0.556749
INFO:tensorflow:Step #1230: rate 0.000500, accuracy 78.9%, cross entropy 0.639563
INFO:tensorflow:Step #1240: rate 0.000500, accuracy 83.2%, cross entropy 0.657756
INFO:tensorflow:Step #1250: rate 0.000500, accuracy 79.7%, cross entropy 0.566757
INFO:tensorflow:Step #1260: rate 0.000500, accuracy 79.3%, cross entropy 0.681768
INFO:tensorflow:Step #1270: rate 0.000500, accuracy 82.0%, cross entropy 0.565341
INFO:tensorflow:Step #1280: rate 0.000500, accuracy 80.1%, cross entropy 0.532579
INFO:tensorflow:Step #1290: rate 0.000500, accuracy 78.9%, cross entropy 0.642666
INFO:tensorflow:Step #1300: rate 0.000500, accuracy 83.2%, cross entropy 0.518003
INFO:tensorflow:Step #1310: rate 0.000500, accuracy 84.8%, cross entropy 0.510160
INFO:tensorflow:Step #1320: rate 0.000500, accuracy 77.7%, cross entropy 0.705795
INFO:tensorflow:Step #1330: rate 0.000500, accuracy 81.2%, cross entropy 0.697800
INFO:tensorflow:Step #1340: rate 0.000500, accuracy 81.2%, cross entropy 0.594282
INFO:tensorflow:Step #1350: rate 0.000500, accuracy 84.0%, cross entropy 0.543139
INFO:tensorflow:Step #1360: rate 0.000500, accuracy 83.2%, cross entropy 0.504834
INFO:tensorflow:Step #1370: rate 0.000500, accuracy 78.1%, cross entropy 0.698911
INFO:tensorflow:Step #1380: rate 0.000500, accuracy 81.2%, cross entropy 0.541243
INFO:tensorflow:Step #1390: rate 0.000500, accuracy 83.6%, cross entropy 0.538517
INFO:tensorflow:Step #1400: rate 0.000500, accuracy 75.4%, cross entropy 0.694715
INFO:tensorflow:Step #1410: rate 0.000500, accuracy 84.8%, cross entropy 0.541208
INFO:tensorflow:Step #1420: rate 0.000500, accuracy 81.6%, cross entropy 0.595827
INFO:tensorflow:Step #1430: rate 0.000500, accuracy 79.7%, cross entropy 0.653886
INFO:tensorflow:Step #1440: rate 0.000500, accuracy 82.0%, cross entropy 0.569621
INFO:tensorflow:Step #1450: rate 0.000500, accuracy 80.1%, cross entropy 0.568550
INFO:tensorflow:Step #1460: rate 0.000500, accuracy 78.1%, cross entropy 0.605756
INFO:tensorflow:Step #1470: rate 0.000500, accuracy 87.5%, cross entropy 0.485717
INFO:tensorflow:Step #1480: rate 0.000500, accuracy 83.2%, cross entropy 0.531316
INFO:tensorflow:Step #1490: rate 0.000500, accuracy 80.1%, cross entropy 0.675710
INFO:tensorflow:Step #1500: rate 0.000500, accuracy 79.7%, cross entropy 0.579213
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 182   5   5   7   7   2  14   7   3   8  18]
 [  0   3 249   5   3   0   1   0   0   0   0   0]
 [  0   6   6 239   0   2   1   1   0   0   3  12]
 [  0   4   0   0 246   0   0   1   1   5   3   0]
 [  0   6   1  11   0 236   0   1   0   0   1   8]
 [  0   6  21   0   2   0 217   1   0   0   0   0]
 [  0   8   0   0   2   0   5 241   0   0   0   0]
 [  0   6   0   0   4   0   1   0 242   4   0   0]
 [  0   2   0   0  19   0   0   0   6 228   0   1]
 [  0   2   0   0  14   1   0   0   0   3 224   2]
 [  0  11   1   8   8   4   2   1   1   2   3 219]]
INFO:tensorflow:Step 1500: Validation accuracy = 89.0% (N=2835)
INFO:tensorflow:Step #1510: rate 0.000500, accuracy 88.3%, cross entropy 0.391304
INFO:tensorflow:Step #1520: rate 0.000500, accuracy 78.1%, cross entropy 0.620185
INFO:tensorflow:Step #1530: rate 0.000500, accuracy 80.9%, cross entropy 0.567301
INFO:tensorflow:Step #1540: rate 0.000500, accuracy 82.4%, cross entropy 0.505718
INFO:tensorflow:Step #1550: rate 0.000500, accuracy 76.2%, cross entropy 0.637884
INFO:tensorflow:Step #1560: rate 0.000500, accuracy 79.3%, cross entropy 0.576468
INFO:tensorflow:Step #1570: rate 0.000500, accuracy 78.1%, cross entropy 0.559952
INFO:tensorflow:Step #1580: rate 0.000500, accuracy 77.7%, cross entropy 0.670969
INFO:tensorflow:Step #1590: rate 0.000500, accuracy 83.2%, cross entropy 0.585954
INFO:tensorflow:Step #1600: rate 0.000500, accuracy 81.2%, cross entropy 0.575482
INFO:tensorflow:Step #1610: rate 0.000500, accuracy 82.4%, cross entropy 0.559632
INFO:tensorflow:Step #1620: rate 0.000500, accuracy 83.6%, cross entropy 0.482323
INFO:tensorflow:Step #1630: rate 0.000500, accuracy 80.9%, cross entropy 0.599668
INFO:tensorflow:Step #1640: rate 0.000500, accuracy 86.3%, cross entropy 0.469521
INFO:tensorflow:Step #1650: rate 0.000500, accuracy 84.8%, cross entropy 0.451911
INFO:tensorflow:Step #1660: rate 0.000500, accuracy 80.1%, cross entropy 0.591946
INFO:tensorflow:Step #1670: rate 0.000500, accuracy 82.8%, cross entropy 0.581727
INFO:tensorflow:Step #1680: rate 0.000500, accuracy 81.2%, cross entropy 0.577210
INFO:tensorflow:Step #1690: rate 0.000500, accuracy 85.2%, cross entropy 0.511735
INFO:tensorflow:Step #1700: rate 0.000500, accuracy 82.4%, cross entropy 0.623228
INFO:tensorflow:Step #1710: rate 0.000500, accuracy 84.8%, cross entropy 0.474137
INFO:tensorflow:Step #1720: rate 0.000500, accuracy 82.0%, cross entropy 0.577980
INFO:tensorflow:Step #1730: rate 0.000500, accuracy 82.0%, cross entropy 0.587925
INFO:tensorflow:Step #1740: rate 0.000500, accuracy 82.8%, cross entropy 0.562270
INFO:tensorflow:Step #1750: rate 0.000500, accuracy 84.0%, cross entropy 0.519159
INFO:tensorflow:Step #1760: rate 0.000500, accuracy 84.4%, cross entropy 0.600033
INFO:tensorflow:Step #1770: rate 0.000500, accuracy 83.2%, cross entropy 0.515647
INFO:tensorflow:Step #1780: rate 0.000500, accuracy 85.2%, cross entropy 0.495377
INFO:tensorflow:Step #1790: rate 0.000500, accuracy 84.0%, cross entropy 0.533693
INFO:tensorflow:Step #1800: rate 0.000500, accuracy 79.7%, cross entropy 0.594498
INFO:tensorflow:Step #1810: rate 0.000500, accuracy 85.2%, cross entropy 0.456035
INFO:tensorflow:Step #1820: rate 0.000500, accuracy 82.0%, cross entropy 0.571904
INFO:tensorflow:Step #1830: rate 0.000500, accuracy 87.1%, cross entropy 0.413348
INFO:tensorflow:Step #1840: rate 0.000500, accuracy 85.2%, cross entropy 0.460530
INFO:tensorflow:Step #1850: rate 0.000500, accuracy 87.5%, cross entropy 0.460434
INFO:tensorflow:Step #1860: rate 0.000500, accuracy 85.5%, cross entropy 0.492533
INFO:tensorflow:Step #1870: rate 0.000500, accuracy 85.5%, cross entropy 0.554990
INFO:tensorflow:Step #1880: rate 0.000500, accuracy 87.5%, cross entropy 0.395221
INFO:tensorflow:Step #1890: rate 0.000500, accuracy 86.3%, cross entropy 0.443456
INFO:tensorflow:Step #1900: rate 0.000500, accuracy 82.4%, cross entropy 0.554329
INFO:tensorflow:Step #1910: rate 0.000500, accuracy 85.5%, cross entropy 0.432937
INFO:tensorflow:Step #1920: rate 0.000500, accuracy 82.0%, cross entropy 0.505321
INFO:tensorflow:Step #1930: rate 0.000500, accuracy 81.6%, cross entropy 0.570794
INFO:tensorflow:Step #1940: rate 0.000500, accuracy 84.0%, cross entropy 0.525927
INFO:tensorflow:Step #1950: rate 0.000500, accuracy 85.9%, cross entropy 0.442751
INFO:tensorflow:Step #1960: rate 0.000500, accuracy 83.6%, cross entropy 0.495140
INFO:tensorflow:Step #1970: rate 0.000500, accuracy 85.5%, cross entropy 0.450487
INFO:tensorflow:Step #1980: rate 0.000500, accuracy 84.8%, cross entropy 0.426999
INFO:tensorflow:Step #1990: rate 0.000500, accuracy 83.6%, cross entropy 0.480717
INFO:tensorflow:Step #2000: rate 0.000500, accuracy 82.0%, cross entropy 0.582993
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 192   8   6   7   3  11  10   4   3   8   6]
 [  0   0 251   1   3   0   6   0   0   0   0   0]
 [  0   7   5 246   0   0   1   1   0   0   3   7]
 [  0   5   2   0 246   0   0   0   0   6   1   0]
 [  0   7   2  10   0 237   0   0   0   0   2   6]
 [  0   2  19   0   3   0 223   0   0   0   0   0]
 [  0   5   0   0   2   0   9 240   0   0   0   0]
 [  0   6   0   0   4   0   1   2 237   7   0   0]
 [  0   2   1   0  21   0   0   0   3 227   2   0]
 [  0   2   0   0  15   0   1   0   0   1 225   2]
 [  0  17   1  12   8   2   2   0   0   1   2 215]]
INFO:tensorflow:Step 2000: Validation accuracy = 89.6% (N=2835)
INFO:tensorflow:Saving to "F:\ML_Project\Data\logs&checkpoint\c_rnn\ckpt-2000"
INFO:tensorflow:Step #2010: rate 0.000500, accuracy 83.2%, cross entropy 0.511936
INFO:tensorflow:Step #2020: rate 0.000500, accuracy 85.9%, cross entropy 0.479363
INFO:tensorflow:Step #2030: rate 0.000500, accuracy 81.6%, cross entropy 0.584820
INFO:tensorflow:Step #2040: rate 0.000500, accuracy 82.4%, cross entropy 0.507888
INFO:tensorflow:Step #2050: rate 0.000500, accuracy 85.2%, cross entropy 0.429502
INFO:tensorflow:Step #2060: rate 0.000500, accuracy 86.3%, cross entropy 0.417539
INFO:tensorflow:Step #2070: rate 0.000500, accuracy 85.2%, cross entropy 0.459523
INFO:tensorflow:Step #2080: rate 0.000500, accuracy 86.7%, cross entropy 0.529517
INFO:tensorflow:Step #2090: rate 0.000500, accuracy 85.2%, cross entropy 0.463981
INFO:tensorflow:Step #2100: rate 0.000500, accuracy 84.4%, cross entropy 0.407829
INFO:tensorflow:Step #2110: rate 0.000500, accuracy 84.4%, cross entropy 0.468519
INFO:tensorflow:Step #2120: rate 0.000500, accuracy 82.0%, cross entropy 0.565939
INFO:tensorflow:Step #2130: rate 0.000500, accuracy 85.9%, cross entropy 0.469378
INFO:tensorflow:Step #2140: rate 0.000500, accuracy 85.9%, cross entropy 0.421187
INFO:tensorflow:Step #2150: rate 0.000500, accuracy 82.8%, cross entropy 0.412269
INFO:tensorflow:Step #2160: rate 0.000500, accuracy 85.9%, cross entropy 0.493054
INFO:tensorflow:Step #2170: rate 0.000500, accuracy 82.8%, cross entropy 0.471382
INFO:tensorflow:Step #2180: rate 0.000500, accuracy 84.4%, cross entropy 0.515954
INFO:tensorflow:Step #2190: rate 0.000500, accuracy 85.5%, cross entropy 0.433802
INFO:tensorflow:Step #2200: rate 0.000500, accuracy 85.5%, cross entropy 0.483023
INFO:tensorflow:Step #2210: rate 0.000500, accuracy 86.3%, cross entropy 0.412811
INFO:tensorflow:Step #2220: rate 0.000500, accuracy 88.7%, cross entropy 0.400349
INFO:tensorflow:Step #2230: rate 0.000500, accuracy 81.6%, cross entropy 0.511098
INFO:tensorflow:Step #2240: rate 0.000500, accuracy 85.2%, cross entropy 0.416836
INFO:tensorflow:Step #2250: rate 0.000500, accuracy 85.2%, cross entropy 0.470837
INFO:tensorflow:Step #2260: rate 0.000500, accuracy 86.3%, cross entropy 0.432383
INFO:tensorflow:Step #2270: rate 0.000500, accuracy 81.6%, cross entropy 0.507255
INFO:tensorflow:Step #2280: rate 0.000500, accuracy 82.8%, cross entropy 0.590739
INFO:tensorflow:Step #2290: rate 0.000500, accuracy 83.2%, cross entropy 0.515542
INFO:tensorflow:Step #2300: rate 0.000500, accuracy 86.7%, cross entropy 0.406395
INFO:tensorflow:Step #2310: rate 0.000500, accuracy 83.6%, cross entropy 0.564574
INFO:tensorflow:Step #2320: rate 0.000500, accuracy 80.5%, cross entropy 0.579729
INFO:tensorflow:Step #2330: rate 0.000500, accuracy 86.7%, cross entropy 0.478860
INFO:tensorflow:Step #2340: rate 0.000500, accuracy 84.8%, cross entropy 0.464287
INFO:tensorflow:Step #2350: rate 0.000500, accuracy 83.6%, cross entropy 0.575581
INFO:tensorflow:Step #2360: rate 0.000500, accuracy 88.7%, cross entropy 0.388281
INFO:tensorflow:Step #2370: rate 0.000500, accuracy 89.1%, cross entropy 0.367554
INFO:tensorflow:Step #2380: rate 0.000500, accuracy 84.4%, cross entropy 0.487919
INFO:tensorflow:Step #2390: rate 0.000500, accuracy 82.0%, cross entropy 0.512815
INFO:tensorflow:Step #2400: rate 0.000500, accuracy 85.5%, cross entropy 0.454609
INFO:tensorflow:Step #2410: rate 0.000500, accuracy 84.8%, cross entropy 0.437852
INFO:tensorflow:Step #2420: rate 0.000500, accuracy 86.3%, cross entropy 0.457456
INFO:tensorflow:Step #2430: rate 0.000500, accuracy 84.8%, cross entropy 0.463488
INFO:tensorflow:Step #2440: rate 0.000500, accuracy 83.6%, cross entropy 0.431821
INFO:tensorflow:Step #2450: rate 0.000500, accuracy 89.8%, cross entropy 0.367619
INFO:tensorflow:Step #2460: rate 0.000500, accuracy 82.0%, cross entropy 0.527000
INFO:tensorflow:Step #2470: rate 0.000500, accuracy 88.3%, cross entropy 0.362784
INFO:tensorflow:Step #2480: rate 0.000500, accuracy 84.4%, cross entropy 0.484080
INFO:tensorflow:Step #2490: rate 0.000500, accuracy 85.9%, cross entropy 0.439907
INFO:tensorflow:Step #2500: rate 0.000500, accuracy 83.6%, cross entropy 0.480167
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 193   5   6   8   6   3   8   8   2   5  14]
 [  0   0 253   3   3   0   2   0   0   0   0   0]
 [  0   5   1 251   0   1   1   0   1   0   3   7]
 [  0   5   0   0 248   0   0   0   1   5   1   0]
 [  0   4   0  10   0 243   0   1   0   0   1   5]
 [  0   2  19   2   3   0 220   1   0   0   0   0]
 [  0  12   0   0   2   0   3 238   0   0   1   0]
 [  0   4   0   0   5   0   0   0 243   5   0   0]
 [  0   0   0   0  18   0   0   0   4 231   2   1]
 [  0   3   0   0  10   0   1   0   0   3 226   3]
 [  0   9   0   8   9   2   1   0   0   3   2 226]]
INFO:tensorflow:Step 2500: Validation accuracy = 90.7% (N=2835)
INFO:tensorflow:Step #2510: rate 0.000500, accuracy 89.8%, cross entropy 0.386339
INFO:tensorflow:Step #2520: rate 0.000500, accuracy 87.9%, cross entropy 0.339034
INFO:tensorflow:Step #2530: rate 0.000500, accuracy 87.1%, cross entropy 0.444707
INFO:tensorflow:Step #2540: rate 0.000500, accuracy 87.1%, cross entropy 0.409820
INFO:tensorflow:Step #2550: rate 0.000500, accuracy 83.6%, cross entropy 0.501085
INFO:tensorflow:Step #2560: rate 0.000500, accuracy 85.2%, cross entropy 0.541926
INFO:tensorflow:Step #2570: rate 0.000500, accuracy 86.7%, cross entropy 0.362234
INFO:tensorflow:Step #2580: rate 0.000500, accuracy 84.0%, cross entropy 0.498806
INFO:tensorflow:Step #2590: rate 0.000500, accuracy 85.2%, cross entropy 0.482549
INFO:tensorflow:Step #2600: rate 0.000500, accuracy 85.2%, cross entropy 0.453617
INFO:tensorflow:Step #2610: rate 0.000500, accuracy 85.9%, cross entropy 0.436982
INFO:tensorflow:Step #2620: rate 0.000500, accuracy 83.6%, cross entropy 0.506340
INFO:tensorflow:Step #2630: rate 0.000500, accuracy 85.2%, cross entropy 0.503695
INFO:tensorflow:Step #2640: rate 0.000500, accuracy 85.2%, cross entropy 0.424578
INFO:tensorflow:Step #2650: rate 0.000500, accuracy 86.3%, cross entropy 0.392153
INFO:tensorflow:Step #2660: rate 0.000500, accuracy 85.5%, cross entropy 0.407393
INFO:tensorflow:Step #2670: rate 0.000500, accuracy 90.2%, cross entropy 0.323724
INFO:tensorflow:Step #2680: rate 0.000500, accuracy 84.0%, cross entropy 0.468850
INFO:tensorflow:Step #2690: rate 0.000500, accuracy 86.7%, cross entropy 0.392692
INFO:tensorflow:Step #2700: rate 0.000500, accuracy 85.9%, cross entropy 0.420848
INFO:tensorflow:Step #2710: rate 0.000500, accuracy 84.8%, cross entropy 0.481478
INFO:tensorflow:Step #2720: rate 0.000500, accuracy 84.0%, cross entropy 0.492684
INFO:tensorflow:Step #2730: rate 0.000500, accuracy 88.7%, cross entropy 0.379127
INFO:tensorflow:Step #2740: rate 0.000500, accuracy 85.5%, cross entropy 0.443141
INFO:tensorflow:Step #2750: rate 0.000500, accuracy 87.5%, cross entropy 0.406855
INFO:tensorflow:Step #2760: rate 0.000500, accuracy 84.4%, cross entropy 0.422289
INFO:tensorflow:Step #2770: rate 0.000500, accuracy 85.5%, cross entropy 0.402388
INFO:tensorflow:Step #2780: rate 0.000500, accuracy 83.2%, cross entropy 0.500217
INFO:tensorflow:Step #2790: rate 0.000500, accuracy 84.0%, cross entropy 0.431251
INFO:tensorflow:Step #2800: rate 0.000500, accuracy 87.5%, cross entropy 0.389778
INFO:tensorflow:Step #2810: rate 0.000500, accuracy 83.6%, cross entropy 0.438980
INFO:tensorflow:Step #2820: rate 0.000500, accuracy 88.3%, cross entropy 0.315431
INFO:tensorflow:Step #2830: rate 0.000500, accuracy 86.3%, cross entropy 0.433982
INFO:tensorflow:Step #2840: rate 0.000500, accuracy 89.5%, cross entropy 0.357712
INFO:tensorflow:Step #2850: rate 0.000500, accuracy 86.7%, cross entropy 0.341547
INFO:tensorflow:Step #2860: rate 0.000500, accuracy 89.1%, cross entropy 0.321895
INFO:tensorflow:Step #2870: rate 0.000500, accuracy 85.5%, cross entropy 0.442080
INFO:tensorflow:Step #2880: rate 0.000500, accuracy 86.3%, cross entropy 0.472063
INFO:tensorflow:Step #2890: rate 0.000500, accuracy 87.5%, cross entropy 0.403095
INFO:tensorflow:Step #2900: rate 0.000500, accuracy 87.1%, cross entropy 0.512178
INFO:tensorflow:Step #2910: rate 0.000500, accuracy 85.2%, cross entropy 0.441948
INFO:tensorflow:Step #2920: rate 0.000500, accuracy 89.1%, cross entropy 0.367912
INFO:tensorflow:Step #2930: rate 0.000500, accuracy 84.4%, cross entropy 0.431071
INFO:tensorflow:Step #2940: rate 0.000500, accuracy 87.5%, cross entropy 0.395738
INFO:tensorflow:Step #2950: rate 0.000500, accuracy 83.2%, cross entropy 0.532180
INFO:tensorflow:Step #2960: rate 0.000500, accuracy 83.2%, cross entropy 0.494427
INFO:tensorflow:Step #2970: rate 0.000500, accuracy 85.2%, cross entropy 0.443232
INFO:tensorflow:Step #2980: rate 0.000500, accuracy 86.3%, cross entropy 0.369120
INFO:tensorflow:Step #2990: rate 0.000500, accuracy 88.7%, cross entropy 0.404911
INFO:tensorflow:Step #3000: rate 0.000500, accuracy 86.3%, cross entropy 0.426249
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 201   4  10   5   4   5   8   4   2   3  12]
 [  0   0 250   5   3   0   3   0   0   0   0   0]
 [  0   5   1 257   0   0   1   0   0   0   0   6]
 [  0   5   0   0 246   0   0   0   1   6   2   0]
 [  0   3   0  15   0 241   0   0   1   0   1   3]
 [  0   2  18   4   1   0 221   1   0   0   0   0]
 [  0   5   0   1   1   0   4 244   0   0   1   0]
 [  0   8   0   0   5   0   0   0 240   4   0   0]
 [  0   2   0   1  15   0   0   0   8 227   2   1]
 [  0   3   0   0  10   1   1   0   0   3 225   3]
 [  0  11   0  14   8   2   1   0   0   0   2 222]]
INFO:tensorflow:Step 3000: Validation accuracy = 90.8% (N=2835)
INFO:tensorflow:Step #3010: rate 0.000500, accuracy 84.8%, cross entropy 0.468867
INFO:tensorflow:Step #3020: rate 0.000500, accuracy 87.9%, cross entropy 0.388872
INFO:tensorflow:Step #3030: rate 0.000500, accuracy 85.2%, cross entropy 0.410872
INFO:tensorflow:Step #3040: rate 0.000500, accuracy 87.5%, cross entropy 0.400882
INFO:tensorflow:Step #3050: rate 0.000500, accuracy 90.6%, cross entropy 0.389997
INFO:tensorflow:Step #3060: rate 0.000500, accuracy 86.3%, cross entropy 0.461838
INFO:tensorflow:Step #3070: rate 0.000500, accuracy 85.9%, cross entropy 0.448229
INFO:tensorflow:Step #3080: rate 0.000500, accuracy 84.0%, cross entropy 0.444499
INFO:tensorflow:Step #3090: rate 0.000500, accuracy 86.3%, cross entropy 0.427137
INFO:tensorflow:Step #3100: rate 0.000500, accuracy 86.7%, cross entropy 0.400469
INFO:tensorflow:Step #3110: rate 0.000500, accuracy 85.2%, cross entropy 0.508235
INFO:tensorflow:Step #3120: rate 0.000500, accuracy 89.8%, cross entropy 0.290184
INFO:tensorflow:Step #3130: rate 0.000500, accuracy 87.1%, cross entropy 0.345030
INFO:tensorflow:Step #3140: rate 0.000500, accuracy 85.9%, cross entropy 0.465893
INFO:tensorflow:Step #3150: rate 0.000500, accuracy 90.6%, cross entropy 0.299061
INFO:tensorflow:Step #3160: rate 0.000500, accuracy 85.5%, cross entropy 0.408765
INFO:tensorflow:Step #3170: rate 0.000500, accuracy 88.7%, cross entropy 0.409808
INFO:tensorflow:Step #3180: rate 0.000500, accuracy 86.7%, cross entropy 0.394820
INFO:tensorflow:Step #3190: rate 0.000500, accuracy 85.5%, cross entropy 0.454309
INFO:tensorflow:Step #3200: rate 0.000500, accuracy 89.1%, cross entropy 0.412859
INFO:tensorflow:Step #3210: rate 0.000500, accuracy 87.1%, cross entropy 0.432134
INFO:tensorflow:Step #3220: rate 0.000500, accuracy 89.1%, cross entropy 0.337387
INFO:tensorflow:Step #3230: rate 0.000500, accuracy 90.2%, cross entropy 0.349988
INFO:tensorflow:Step #3240: rate 0.000500, accuracy 86.3%, cross entropy 0.423445
INFO:tensorflow:Step #3250: rate 0.000500, accuracy 84.0%, cross entropy 0.453535
INFO:tensorflow:Step #3260: rate 0.000500, accuracy 87.1%, cross entropy 0.385875
INFO:tensorflow:Step #3270: rate 0.000500, accuracy 86.7%, cross entropy 0.460386
INFO:tensorflow:Step #3280: rate 0.000500, accuracy 83.2%, cross entropy 0.492691
INFO:tensorflow:Step #3290: rate 0.000500, accuracy 87.9%, cross entropy 0.386040
INFO:tensorflow:Step #3300: rate 0.000500, accuracy 84.0%, cross entropy 0.474537
INFO:tensorflow:Step #3310: rate 0.000500, accuracy 84.8%, cross entropy 0.433447
INFO:tensorflow:Step #3320: rate 0.000500, accuracy 91.0%, cross entropy 0.286754
INFO:tensorflow:Step #3330: rate 0.000500, accuracy 85.9%, cross entropy 0.443754
INFO:tensorflow:Step #3340: rate 0.000500, accuracy 89.1%, cross entropy 0.356437
INFO:tensorflow:Step #3350: rate 0.000500, accuracy 85.9%, cross entropy 0.512180
INFO:tensorflow:Step #3360: rate 0.000500, accuracy 87.5%, cross entropy 0.408524
INFO:tensorflow:Step #3370: rate 0.000500, accuracy 85.5%, cross entropy 0.414978
INFO:tensorflow:Step #3380: rate 0.000500, accuracy 84.0%, cross entropy 0.471099
INFO:tensorflow:Step #3390: rate 0.000500, accuracy 87.5%, cross entropy 0.366218
INFO:tensorflow:Step #3400: rate 0.000500, accuracy 89.8%, cross entropy 0.390371
INFO:tensorflow:Step #3410: rate 0.000500, accuracy 88.7%, cross entropy 0.364717
INFO:tensorflow:Step #3420: rate 0.000500, accuracy 88.3%, cross entropy 0.318675
INFO:tensorflow:Step #3430: rate 0.000500, accuracy 87.9%, cross entropy 0.452947
INFO:tensorflow:Step #3440: rate 0.000500, accuracy 89.5%, cross entropy 0.365162
INFO:tensorflow:Step #3450: rate 0.000500, accuracy 85.9%, cross entropy 0.448463
INFO:tensorflow:Step #3460: rate 0.000500, accuracy 88.3%, cross entropy 0.344077
INFO:tensorflow:Step #3470: rate 0.000500, accuracy 87.1%, cross entropy 0.422693
INFO:tensorflow:Step #3480: rate 0.000500, accuracy 86.3%, cross entropy 0.400211
INFO:tensorflow:Step #3490: rate 0.000500, accuracy 86.7%, cross entropy 0.369145
INFO:tensorflow:Step #3500: rate 0.000500, accuracy 86.3%, cross entropy 0.405704
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 201   4   7   3   3   3  11   7   3   4  12]
 [  0   0 247   6   0   0   5   0   1   2   0   0]
 [  0   3   1 256   0   1   1   0   1   0   1   6]
 [  0   5   0   0 244   0   0   1   0   9   1   0]
 [  0   2   1  15   0 237   0   0   1   0   2   6]
 [  0   5  11   4   0   0 225   1   0   1   0   0]
 [  0   5   0   0   1   0   3 246   0   0   1   0]
 [  0   4   0   0   1   0   0   0 246   6   0   0]
 [  0   1   0   0  13   0   0   0   4 235   2   1]
 [  0   3   0   0   9   0   0   1   1   3 227   2]
 [  0   9   1   6   6   3   0   0   0   7   2 226]]
INFO:tensorflow:Step 3500: Validation accuracy = 91.4% (N=2835)
INFO:tensorflow:Step #3510: rate 0.000500, accuracy 90.6%, cross entropy 0.305940
INFO:tensorflow:Step #3520: rate 0.000500, accuracy 89.5%, cross entropy 0.361303
INFO:tensorflow:Step #3530: rate 0.000500, accuracy 89.8%, cross entropy 0.326221
INFO:tensorflow:Step #3540: rate 0.000500, accuracy 85.9%, cross entropy 0.468815
INFO:tensorflow:Step #3550: rate 0.000500, accuracy 87.5%, cross entropy 0.441473
INFO:tensorflow:Step #3560: rate 0.000500, accuracy 87.9%, cross entropy 0.384872
INFO:tensorflow:Step #3570: rate 0.000500, accuracy 87.9%, cross entropy 0.360737
INFO:tensorflow:Step #3580: rate 0.000500, accuracy 85.2%, cross entropy 0.508482
INFO:tensorflow:Step #3590: rate 0.000500, accuracy 86.3%, cross entropy 0.391657
INFO:tensorflow:Step #3600: rate 0.000500, accuracy 87.5%, cross entropy 0.359462
INFO:tensorflow:Step #3610: rate 0.000500, accuracy 85.2%, cross entropy 0.476063
INFO:tensorflow:Step #3620: rate 0.000500, accuracy 87.9%, cross entropy 0.359297
INFO:tensorflow:Step #3630: rate 0.000500, accuracy 88.3%, cross entropy 0.376513
INFO:tensorflow:Step #3640: rate 0.000500, accuracy 89.5%, cross entropy 0.274448
INFO:tensorflow:Step #3650: rate 0.000500, accuracy 91.8%, cross entropy 0.296135
INFO:tensorflow:Step #3660: rate 0.000500, accuracy 90.6%, cross entropy 0.342277
INFO:tensorflow:Step #3670: rate 0.000500, accuracy 88.3%, cross entropy 0.397650
INFO:tensorflow:Step #3680: rate 0.000500, accuracy 88.7%, cross entropy 0.332015
INFO:tensorflow:Step #3690: rate 0.000500, accuracy 89.5%, cross entropy 0.324586
INFO:tensorflow:Step #3700: rate 0.000500, accuracy 88.7%, cross entropy 0.325755
INFO:tensorflow:Step #3710: rate 0.000500, accuracy 87.5%, cross entropy 0.373317
INFO:tensorflow:Step #3720: rate 0.000500, accuracy 91.0%, cross entropy 0.298176
INFO:tensorflow:Step #3730: rate 0.000500, accuracy 84.4%, cross entropy 0.449593
INFO:tensorflow:Step #3740: rate 0.000500, accuracy 89.8%, cross entropy 0.388342
INFO:tensorflow:Step #3750: rate 0.000500, accuracy 84.0%, cross entropy 0.474946
INFO:tensorflow:Step #3760: rate 0.000500, accuracy 87.1%, cross entropy 0.427509
INFO:tensorflow:Step #3770: rate 0.000500, accuracy 92.6%, cross entropy 0.282885
INFO:tensorflow:Step #3780: rate 0.000500, accuracy 86.7%, cross entropy 0.386531
INFO:tensorflow:Step #3790: rate 0.000500, accuracy 90.6%, cross entropy 0.325512
INFO:tensorflow:Step #3800: rate 0.000500, accuracy 90.2%, cross entropy 0.270569
INFO:tensorflow:Step #3810: rate 0.000500, accuracy 91.0%, cross entropy 0.303982
INFO:tensorflow:Step #3820: rate 0.000500, accuracy 89.8%, cross entropy 0.299308
INFO:tensorflow:Step #3830: rate 0.000500, accuracy 89.5%, cross entropy 0.365609
INFO:tensorflow:Step #3840: rate 0.000500, accuracy 86.7%, cross entropy 0.414023
INFO:tensorflow:Step #3850: rate 0.000500, accuracy 89.5%, cross entropy 0.335214
INFO:tensorflow:Step #3860: rate 0.000500, accuracy 88.7%, cross entropy 0.318595
INFO:tensorflow:Step #3870: rate 0.000500, accuracy 86.3%, cross entropy 0.368796
INFO:tensorflow:Step #3880: rate 0.000500, accuracy 91.0%, cross entropy 0.294293
INFO:tensorflow:Step #3890: rate 0.000500, accuracy 90.6%, cross entropy 0.351969
INFO:tensorflow:Step #3900: rate 0.000500, accuracy 91.0%, cross entropy 0.296255
INFO:tensorflow:Step #3910: rate 0.000500, accuracy 88.3%, cross entropy 0.360013
INFO:tensorflow:Step #3920: rate 0.000500, accuracy 90.6%, cross entropy 0.298568
INFO:tensorflow:Step #3930: rate 0.000500, accuracy 89.8%, cross entropy 0.317824
INFO:tensorflow:Step #3940: rate 0.000500, accuracy 91.8%, cross entropy 0.279352
INFO:tensorflow:Step #3950: rate 0.000500, accuracy 85.2%, cross entropy 0.458238
INFO:tensorflow:Step #3960: rate 0.000500, accuracy 87.9%, cross entropy 0.361265
INFO:tensorflow:Step #3970: rate 0.000500, accuracy 89.5%, cross entropy 0.292457
INFO:tensorflow:Step #3980: rate 0.000500, accuracy 89.8%, cross entropy 0.354284
INFO:tensorflow:Step #3990: rate 0.000500, accuracy 87.9%, cross entropy 0.437357
INFO:tensorflow:Step #4000: rate 0.000500, accuracy 87.5%, cross entropy 0.420581
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 194   5   9   2   3   4   9   6   5   6  15]
 [  0   0 250   6   0   0   2   0   1   2   0   0]
 [  0   5   1 253   0   1   0   0   1   0   1   8]
 [  0   4   0   1 242   0   0   0   2  10   1   0]
 [  0   1   1   9   0 247   0   0   1   0   0   5]
 [  0   2  16   4   1   0 222   1   0   1   0   0]
 [  0   3   0   1   1   1   5 244   0   0   1   0]
 [  0   3   0   0   1   1   0   1 246   5   0   0]
 [  0   0   0   1  12   0   0   0   4 235   3   1]
 [  0   1   0   0   7   0   0   1   0   5 230   2]
 [  0   6   1   7   4   3   0   0   0   7   3 229]]
INFO:tensorflow:Step 4000: Validation accuracy = 91.4% (N=2835)
INFO:tensorflow:Saving to "F:\ML_Project\Data\logs&checkpoint\c_rnn\ckpt-4000"
INFO:tensorflow:Step #4010: rate 0.000500, accuracy 87.5%, cross entropy 0.308459
INFO:tensorflow:Step #4020: rate 0.000500, accuracy 87.5%, cross entropy 0.362005
INFO:tensorflow:Step #4030: rate 0.000500, accuracy 90.6%, cross entropy 0.281556
INFO:tensorflow:Step #4040: rate 0.000500, accuracy 89.5%, cross entropy 0.326473
INFO:tensorflow:Step #4050: rate 0.000500, accuracy 86.3%, cross entropy 0.413386
INFO:tensorflow:Step #4060: rate 0.000500, accuracy 87.1%, cross entropy 0.390385
INFO:tensorflow:Step #4070: rate 0.000500, accuracy 92.6%, cross entropy 0.269613
INFO:tensorflow:Step #4080: rate 0.000500, accuracy 91.8%, cross entropy 0.274848
INFO:tensorflow:Step #4090: rate 0.000500, accuracy 87.1%, cross entropy 0.345521
INFO:tensorflow:Step #4100: rate 0.000500, accuracy 89.8%, cross entropy 0.360163
INFO:tensorflow:Step #4110: rate 0.000500, accuracy 91.4%, cross entropy 0.246066
INFO:tensorflow:Step #4120: rate 0.000500, accuracy 87.1%, cross entropy 0.390284
INFO:tensorflow:Step #4130: rate 0.000500, accuracy 85.9%, cross entropy 0.452793
INFO:tensorflow:Step #4140: rate 0.000500, accuracy 93.4%, cross entropy 0.246637
INFO:tensorflow:Step #4150: rate 0.000500, accuracy 86.3%, cross entropy 0.449668
INFO:tensorflow:Step #4160: rate 0.000500, accuracy 90.6%, cross entropy 0.344896
INFO:tensorflow:Step #4170: rate 0.000500, accuracy 87.9%, cross entropy 0.342717
INFO:tensorflow:Step #4180: rate 0.000500, accuracy 89.5%, cross entropy 0.341795
INFO:tensorflow:Step #4190: rate 0.000500, accuracy 88.3%, cross entropy 0.296947
INFO:tensorflow:Step #4200: rate 0.000500, accuracy 87.9%, cross entropy 0.341933
INFO:tensorflow:Step #4210: rate 0.000500, accuracy 87.1%, cross entropy 0.356127
INFO:tensorflow:Step #4220: rate 0.000500, accuracy 85.9%, cross entropy 0.393405
INFO:tensorflow:Step #4230: rate 0.000500, accuracy 89.8%, cross entropy 0.343528
INFO:tensorflow:Step #4240: rate 0.000500, accuracy 89.5%, cross entropy 0.372577
INFO:tensorflow:Step #4250: rate 0.000500, accuracy 88.3%, cross entropy 0.360171
INFO:tensorflow:Step #4260: rate 0.000500, accuracy 89.1%, cross entropy 0.309271
INFO:tensorflow:Step #4270: rate 0.000500, accuracy 91.8%, cross entropy 0.258104
INFO:tensorflow:Step #4280: rate 0.000500, accuracy 86.7%, cross entropy 0.456809
INFO:tensorflow:Step #4290: rate 0.000500, accuracy 88.7%, cross entropy 0.358663
INFO:tensorflow:Step #4300: rate 0.000500, accuracy 87.9%, cross entropy 0.318802
INFO:tensorflow:Step #4310: rate 0.000500, accuracy 89.8%, cross entropy 0.344558
INFO:tensorflow:Step #4320: rate 0.000500, accuracy 86.7%, cross entropy 0.427727
INFO:tensorflow:Step #4330: rate 0.000500, accuracy 89.5%, cross entropy 0.322834
INFO:tensorflow:Step #4340: rate 0.000500, accuracy 90.6%, cross entropy 0.340049
INFO:tensorflow:Step #4350: rate 0.000500, accuracy 87.1%, cross entropy 0.418508
INFO:tensorflow:Step #4360: rate 0.000500, accuracy 85.9%, cross entropy 0.419404
INFO:tensorflow:Step #4370: rate 0.000500, accuracy 88.7%, cross entropy 0.370722
INFO:tensorflow:Step #4380: rate 0.000500, accuracy 89.1%, cross entropy 0.346160
INFO:tensorflow:Step #4390: rate 0.000500, accuracy 87.1%, cross entropy 0.360399
INFO:tensorflow:Step #4400: rate 0.000500, accuracy 86.7%, cross entropy 0.391263
INFO:tensorflow:Step #4410: rate 0.000500, accuracy 91.0%, cross entropy 0.261398
INFO:tensorflow:Step #4420: rate 0.000500, accuracy 89.1%, cross entropy 0.333212
INFO:tensorflow:Step #4430: rate 0.000500, accuracy 87.9%, cross entropy 0.406781
INFO:tensorflow:Step #4440: rate 0.000500, accuracy 87.9%, cross entropy 0.353110
INFO:tensorflow:Step #4450: rate 0.000500, accuracy 85.5%, cross entropy 0.407368
INFO:tensorflow:Step #4460: rate 0.000500, accuracy 88.3%, cross entropy 0.347990
INFO:tensorflow:Step #4470: rate 0.000500, accuracy 89.8%, cross entropy 0.318014
INFO:tensorflow:Step #4480: rate 0.000500, accuracy 88.3%, cross entropy 0.364213
INFO:tensorflow:Step #4490: rate 0.000500, accuracy 89.5%, cross entropy 0.362950
INFO:tensorflow:Step #4500: rate 0.000500, accuracy 87.5%, cross entropy 0.328850
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 217   6   8   4   3   3   8   3   2   1   3]
 [  0   0 251   5   3   0   2   0   0   0   0   0]
 [  0   3   1 261   1   2   0   0   0   0   0   2]
 [  0   6   0   0 245   0   0   1   0   7   0   1]
 [  0   2   2   5   0 254   0   1   0   0   0   0]
 [  0   3  18   2   1   0 222   1   0   0   0   0]
 [  0   6   0   1   1   0   3 245   0   0   0   0]
 [  0   8   0   0   4   1   0   0 241   3   0   0]
 [  0   3   0   1  14   0   0   0   7 229   1   1]
 [  0   5   0   1   8   0   3   0   0   3 225   1]
 [  0  10   1  18   8   3   1   0   0   2   2 215]]
INFO:tensorflow:Step 4500: Validation accuracy = 91.9% (N=2835)
INFO:tensorflow:Step #4510: rate 0.000500, accuracy 87.1%, cross entropy 0.444502
INFO:tensorflow:Step #4520: rate 0.000500, accuracy 86.3%, cross entropy 0.458446
INFO:tensorflow:Step #4530: rate 0.000500, accuracy 88.7%, cross entropy 0.406964
INFO:tensorflow:Step #4540: rate 0.000500, accuracy 91.4%, cross entropy 0.330418
INFO:tensorflow:Step #4550: rate 0.000500, accuracy 93.0%, cross entropy 0.273898
INFO:tensorflow:Step #4560: rate 0.000500, accuracy 91.4%, cross entropy 0.258074
INFO:tensorflow:Step #4570: rate 0.000500, accuracy 89.8%, cross entropy 0.304285
INFO:tensorflow:Step #4580: rate 0.000500, accuracy 87.9%, cross entropy 0.377503
INFO:tensorflow:Step #4590: rate 0.000500, accuracy 88.7%, cross entropy 0.342841
INFO:tensorflow:Step #4600: rate 0.000500, accuracy 87.5%, cross entropy 0.386662
INFO:tensorflow:Step #4610: rate 0.000500, accuracy 88.3%, cross entropy 0.369806
INFO:tensorflow:Step #4620: rate 0.000500, accuracy 90.2%, cross entropy 0.301004
INFO:tensorflow:Step #4630: rate 0.000500, accuracy 87.5%, cross entropy 0.472190
INFO:tensorflow:Step #4640: rate 0.000500, accuracy 91.0%, cross entropy 0.299479
INFO:tensorflow:Step #4650: rate 0.000500, accuracy 89.5%, cross entropy 0.304626
INFO:tensorflow:Step #4660: rate 0.000500, accuracy 87.5%, cross entropy 0.335942
INFO:tensorflow:Step #4670: rate 0.000500, accuracy 83.6%, cross entropy 0.472690
INFO:tensorflow:Step #4680: rate 0.000500, accuracy 89.1%, cross entropy 0.353432
INFO:tensorflow:Step #4690: rate 0.000500, accuracy 87.5%, cross entropy 0.353298
INFO:tensorflow:Step #4700: rate 0.000500, accuracy 90.2%, cross entropy 0.306382
INFO:tensorflow:Step #4710: rate 0.000500, accuracy 89.5%, cross entropy 0.278031
INFO:tensorflow:Step #4720: rate 0.000500, accuracy 89.5%, cross entropy 0.326149
INFO:tensorflow:Step #4730: rate 0.000500, accuracy 88.3%, cross entropy 0.332772
INFO:tensorflow:Step #4740: rate 0.000500, accuracy 89.1%, cross entropy 0.366915
INFO:tensorflow:Step #4750: rate 0.000500, accuracy 92.6%, cross entropy 0.324480
INFO:tensorflow:Step #4760: rate 0.000500, accuracy 87.5%, cross entropy 0.306366
INFO:tensorflow:Step #4770: rate 0.000500, accuracy 92.2%, cross entropy 0.299917
INFO:tensorflow:Step #4780: rate 0.000500, accuracy 91.8%, cross entropy 0.231837
INFO:tensorflow:Step #4790: rate 0.000500, accuracy 88.3%, cross entropy 0.353910
INFO:tensorflow:Step #4800: rate 0.000500, accuracy 91.0%, cross entropy 0.266797
INFO:tensorflow:Step #4810: rate 0.000500, accuracy 88.7%, cross entropy 0.382624
INFO:tensorflow:Step #4820: rate 0.000500, accuracy 89.8%, cross entropy 0.324165
INFO:tensorflow:Step #4830: rate 0.000500, accuracy 91.0%, cross entropy 0.276924
INFO:tensorflow:Step #4840: rate 0.000500, accuracy 87.1%, cross entropy 0.361685
INFO:tensorflow:Step #4850: rate 0.000500, accuracy 89.5%, cross entropy 0.324310
INFO:tensorflow:Step #4860: rate 0.000500, accuracy 87.5%, cross entropy 0.370133
INFO:tensorflow:Step #4870: rate 0.000500, accuracy 89.1%, cross entropy 0.300080
INFO:tensorflow:Step #4880: rate 0.000500, accuracy 87.5%, cross entropy 0.380825
INFO:tensorflow:Step #4890: rate 0.000500, accuracy 90.2%, cross entropy 0.312387
INFO:tensorflow:Step #4900: rate 0.000500, accuracy 85.9%, cross entropy 0.434703
INFO:tensorflow:Step #4910: rate 0.000500, accuracy 89.5%, cross entropy 0.355920
INFO:tensorflow:Step #4920: rate 0.000500, accuracy 87.5%, cross entropy 0.488677
INFO:tensorflow:Step #4930: rate 0.000500, accuracy 93.0%, cross entropy 0.209043
INFO:tensorflow:Step #4940: rate 0.000500, accuracy 89.8%, cross entropy 0.296169
INFO:tensorflow:Step #4950: rate 0.000500, accuracy 85.9%, cross entropy 0.434145
INFO:tensorflow:Step #4960: rate 0.000500, accuracy 90.6%, cross entropy 0.291364
INFO:tensorflow:Step #4970: rate 0.000500, accuracy 91.4%, cross entropy 0.295152
INFO:tensorflow:Step #4980: rate 0.000500, accuracy 91.0%, cross entropy 0.311455
INFO:tensorflow:Step #4990: rate 0.000500, accuracy 89.1%, cross entropy 0.343520
INFO:tensorflow:Step #5000: rate 0.000500, accuracy 85.5%, cross entropy 0.396210
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 210   5   4   1   4   5  12   3   3   1  10]
 [  0   0 250   6   1   0   2   2   0   0   0   0]
 [  0   3   1 257   1   1   1   1   0   0   0   5]
 [  0   5   0   0 248   0   0   2   0   5   0   0]
 [  0   2   0   7   0 250   0   1   0   0   0   4]
 [  0   1  15   1   0   0 229   1   0   0   0   0]
 [  0   3   0   1   1   0   6 245   0   0   0   0]
 [  0   6   0   0   1   1   1   5 240   3   0   0]
 [  0   2   0   0  18   0   1   0   5 229   1   0]
 [  0   4   0   0   9   0   1   2   0   2 227   1]
 [  0   8   1   7   8   3   0   1   0   1   3 228]]
INFO:tensorflow:Step 5000: Validation accuracy = 92.2% (N=2835)
INFO:tensorflow:Step #5010: rate 0.000500, accuracy 89.5%, cross entropy 0.308749
INFO:tensorflow:Step #5020: rate 0.000500, accuracy 90.6%, cross entropy 0.329912
INFO:tensorflow:Step #5030: rate 0.000500, accuracy 91.4%, cross entropy 0.244347
INFO:tensorflow:Step #5040: rate 0.000500, accuracy 86.7%, cross entropy 0.350190
INFO:tensorflow:Step #5050: rate 0.000500, accuracy 87.9%, cross entropy 0.413012
INFO:tensorflow:Step #5060: rate 0.000500, accuracy 89.1%, cross entropy 0.306774
INFO:tensorflow:Step #5070: rate 0.000500, accuracy 89.1%, cross entropy 0.347735
INFO:tensorflow:Step #5080: rate 0.000500, accuracy 84.4%, cross entropy 0.407240
INFO:tensorflow:Step #5090: rate 0.000500, accuracy 91.4%, cross entropy 0.289529
INFO:tensorflow:Step #5100: rate 0.000500, accuracy 87.1%, cross entropy 0.383356
INFO:tensorflow:Step #5110: rate 0.000500, accuracy 84.0%, cross entropy 0.396444
INFO:tensorflow:Step #5120: rate 0.000500, accuracy 85.9%, cross entropy 0.465849
INFO:tensorflow:Step #5130: rate 0.000500, accuracy 86.7%, cross entropy 0.383145
INFO:tensorflow:Step #5140: rate 0.000500, accuracy 89.1%, cross entropy 0.343463
INFO:tensorflow:Step #5150: rate 0.000500, accuracy 87.1%, cross entropy 0.354119
INFO:tensorflow:Step #5160: rate 0.000500, accuracy 89.8%, cross entropy 0.328351
INFO:tensorflow:Step #5170: rate 0.000500, accuracy 89.8%, cross entropy 0.323139
INFO:tensorflow:Step #5180: rate 0.000500, accuracy 87.9%, cross entropy 0.350307
INFO:tensorflow:Step #5190: rate 0.000500, accuracy 91.4%, cross entropy 0.311983
INFO:tensorflow:Step #5200: rate 0.000500, accuracy 87.9%, cross entropy 0.333792
INFO:tensorflow:Step #5210: rate 0.000500, accuracy 85.9%, cross entropy 0.411883
INFO:tensorflow:Step #5220: rate 0.000500, accuracy 86.3%, cross entropy 0.375853
INFO:tensorflow:Step #5230: rate 0.000500, accuracy 87.1%, cross entropy 0.368259
INFO:tensorflow:Step #5240: rate 0.000500, accuracy 87.5%, cross entropy 0.398417
INFO:tensorflow:Step #5250: rate 0.000500, accuracy 88.7%, cross entropy 0.336342
INFO:tensorflow:Step #5260: rate 0.000500, accuracy 88.3%, cross entropy 0.406511
INFO:tensorflow:Step #5270: rate 0.000500, accuracy 90.6%, cross entropy 0.261800
INFO:tensorflow:Step #5280: rate 0.000500, accuracy 85.9%, cross entropy 0.438626
INFO:tensorflow:Step #5290: rate 0.000500, accuracy 93.0%, cross entropy 0.214758
INFO:tensorflow:Step #5300: rate 0.000500, accuracy 89.8%, cross entropy 0.272311
INFO:tensorflow:Step #5310: rate 0.000500, accuracy 90.2%, cross entropy 0.328232
INFO:tensorflow:Step #5320: rate 0.000500, accuracy 89.5%, cross entropy 0.294206
INFO:tensorflow:Step #5330: rate 0.000500, accuracy 88.3%, cross entropy 0.335040
INFO:tensorflow:Step #5340: rate 0.000500, accuracy 91.0%, cross entropy 0.307902
INFO:tensorflow:Step #5350: rate 0.000500, accuracy 85.9%, cross entropy 0.333964
INFO:tensorflow:Step #5360: rate 0.000500, accuracy 92.2%, cross entropy 0.271473
INFO:tensorflow:Step #5370: rate 0.000500, accuracy 86.3%, cross entropy 0.319066
INFO:tensorflow:Step #5380: rate 0.000500, accuracy 90.2%, cross entropy 0.313706
INFO:tensorflow:Step #5390: rate 0.000500, accuracy 91.0%, cross entropy 0.296157
INFO:tensorflow:Step #5400: rate 0.000500, accuracy 89.8%, cross entropy 0.289737
INFO:tensorflow:Step #5410: rate 0.000500, accuracy 88.3%, cross entropy 0.399400
INFO:tensorflow:Step #5420: rate 0.000500, accuracy 90.6%, cross entropy 0.286189
INFO:tensorflow:Step #5430: rate 0.000500, accuracy 91.0%, cross entropy 0.297516
INFO:tensorflow:Step #5440: rate 0.000500, accuracy 87.9%, cross entropy 0.371978
INFO:tensorflow:Step #5450: rate 0.000500, accuracy 87.1%, cross entropy 0.383793
INFO:tensorflow:Step #5460: rate 0.000500, accuracy 87.5%, cross entropy 0.426296
INFO:tensorflow:Step #5470: rate 0.000500, accuracy 91.8%, cross entropy 0.259501
INFO:tensorflow:Step #5480: rate 0.000500, accuracy 89.1%, cross entropy 0.299043
INFO:tensorflow:Step #5490: rate 0.000500, accuracy 91.0%, cross entropy 0.252116
INFO:tensorflow:Step #5500: rate 0.000500, accuracy 90.2%, cross entropy 0.300063
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 222   4   5   3   4   0   6   4   3   4   3]
 [  0   0 252   4   2   0   2   0   0   1   0   0]
 [  0   6   1 255   1   2   0   0   0   0   0   5]
 [  0   7   0   0 242   0   0   1   1   9   0   0]
 [  0   1   1   4   0 255   0   0   1   0   1   1]
 [  0   3  14   2   1   0 227   0   0   0   0   0]
 [  0   8   0   0   2   0   2 244   0   0   0   0]
 [  0   6   0   0   4   1   0   0 242   4   0   0]
 [  0   2   0   1  16   0   0   0   4 230   2   1]
 [  0   4   0   0  11   0   0   0   0   2 228   1]
 [  0  12   0   9   8   3   0   0   0   3   3 222]]
INFO:tensorflow:Step 5500: Validation accuracy = 92.4% (N=2835)
INFO:tensorflow:Step #5510: rate 0.000500, accuracy 88.7%, cross entropy 0.332636
INFO:tensorflow:Step #5520: rate 0.000500, accuracy 89.1%, cross entropy 0.423423
INFO:tensorflow:Step #5530: rate 0.000500, accuracy 85.9%, cross entropy 0.375690
INFO:tensorflow:Step #5540: rate 0.000500, accuracy 89.1%, cross entropy 0.332917
INFO:tensorflow:Step #5550: rate 0.000500, accuracy 90.6%, cross entropy 0.277183
INFO:tensorflow:Step #5560: rate 0.000500, accuracy 91.0%, cross entropy 0.279390
INFO:tensorflow:Step #5570: rate 0.000500, accuracy 89.5%, cross entropy 0.316857
INFO:tensorflow:Step #5580: rate 0.000500, accuracy 87.5%, cross entropy 0.386745
INFO:tensorflow:Step #5590: rate 0.000500, accuracy 83.6%, cross entropy 0.466684
INFO:tensorflow:Step #5600: rate 0.000500, accuracy 88.7%, cross entropy 0.332678
INFO:tensorflow:Step #5610: rate 0.000500, accuracy 85.9%, cross entropy 0.449624
INFO:tensorflow:Step #5620: rate 0.000500, accuracy 88.3%, cross entropy 0.342951
INFO:tensorflow:Step #5630: rate 0.000500, accuracy 91.4%, cross entropy 0.295598
INFO:tensorflow:Step #5640: rate 0.000500, accuracy 89.8%, cross entropy 0.303002
INFO:tensorflow:Step #5650: rate 0.000500, accuracy 89.5%, cross entropy 0.317840
INFO:tensorflow:Step #5660: rate 0.000500, accuracy 90.2%, cross entropy 0.270608
INFO:tensorflow:Step #5670: rate 0.000500, accuracy 89.1%, cross entropy 0.343251
INFO:tensorflow:Step #5680: rate 0.000500, accuracy 90.2%, cross entropy 0.311065
INFO:tensorflow:Step #5690: rate 0.000500, accuracy 87.9%, cross entropy 0.406215
INFO:tensorflow:Step #5700: rate 0.000500, accuracy 93.4%, cross entropy 0.231460
INFO:tensorflow:Step #5710: rate 0.000500, accuracy 92.6%, cross entropy 0.265185
INFO:tensorflow:Step #5720: rate 0.000500, accuracy 89.8%, cross entropy 0.302274
INFO:tensorflow:Step #5730: rate 0.000500, accuracy 87.1%, cross entropy 0.414974
INFO:tensorflow:Step #5740: rate 0.000500, accuracy 86.7%, cross entropy 0.408544
INFO:tensorflow:Step #5750: rate 0.000500, accuracy 87.9%, cross entropy 0.323666
INFO:tensorflow:Step #5760: rate 0.000500, accuracy 91.8%, cross entropy 0.259159
INFO:tensorflow:Step #5770: rate 0.000500, accuracy 91.8%, cross entropy 0.255347
INFO:tensorflow:Step #5780: rate 0.000500, accuracy 89.8%, cross entropy 0.296252
INFO:tensorflow:Step #5790: rate 0.000500, accuracy 90.6%, cross entropy 0.284048
INFO:tensorflow:Step #5800: rate 0.000500, accuracy 89.8%, cross entropy 0.335012
INFO:tensorflow:Step #5810: rate 0.000500, accuracy 88.7%, cross entropy 0.333214
INFO:tensorflow:Step #5820: rate 0.000500, accuracy 90.2%, cross entropy 0.314977
INFO:tensorflow:Step #5830: rate 0.000500, accuracy 90.6%, cross entropy 0.257647
INFO:tensorflow:Step #5840: rate 0.000500, accuracy 87.5%, cross entropy 0.345190
INFO:tensorflow:Step #5850: rate 0.000500, accuracy 88.3%, cross entropy 0.333094
INFO:tensorflow:Step #5860: rate 0.000500, accuracy 88.7%, cross entropy 0.321103
INFO:tensorflow:Step #5870: rate 0.000500, accuracy 92.2%, cross entropy 0.228565
INFO:tensorflow:Step #5880: rate 0.000500, accuracy 88.7%, cross entropy 0.299062
INFO:tensorflow:Step #5890: rate 0.000500, accuracy 87.5%, cross entropy 0.369565
INFO:tensorflow:Step #5900: rate 0.000500, accuracy 86.7%, cross entropy 0.383406
INFO:tensorflow:Step #5910: rate 0.000500, accuracy 90.6%, cross entropy 0.237871
INFO:tensorflow:Step #5920: rate 0.000500, accuracy 91.8%, cross entropy 0.245392
INFO:tensorflow:Step #5930: rate 0.000500, accuracy 89.8%, cross entropy 0.333667
INFO:tensorflow:Step #5940: rate 0.000500, accuracy 88.7%, cross entropy 0.305469
INFO:tensorflow:Step #5950: rate 0.000500, accuracy 90.6%, cross entropy 0.328393
INFO:tensorflow:Step #5960: rate 0.000500, accuracy 91.0%, cross entropy 0.320856
INFO:tensorflow:Step #5970: rate 0.000500, accuracy 93.0%, cross entropy 0.258863
INFO:tensorflow:Step #5980: rate 0.000500, accuracy 92.2%, cross entropy 0.233132
INFO:tensorflow:Step #5990: rate 0.000500, accuracy 89.5%, cross entropy 0.299928
INFO:tensorflow:Step #6000: rate 0.000500, accuracy 87.1%, cross entropy 0.375219
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 212   4   5   7   7   0   8   6   1   3   5]
 [  0   0 249   6   3   0   3   0   0   0   0   0]
 [  0   4   1 253   1   2   1   0   1   0   0   7]
 [  0   5   0   0 250   0   0   0   0   5   0   0]
 [  0   0   1   5   0 257   0   0   1   0   0   0]
 [  0   1  13   3   1   0 228   1   0   0   0   0]
 [  0   6   0   0   2   0   1 247   0   0   0   0]
 [  0   3   0   0   5   1   0   0 245   3   0   0]
 [  0   1   0   0  17   0   0   0   3 233   2   0]
 [  0   3   0   0  10   0   0   0   0   1 232   0]
 [  0   7   0   8   7   7   0   0   0   4   3 224]]
INFO:tensorflow:Step 6000: Validation accuracy = 92.8% (N=2835)
INFO:tensorflow:Saving to "F:\ML_Project\Data\logs&checkpoint\c_rnn\ckpt-6000"
INFO:tensorflow:Step #6010: rate 0.000500, accuracy 88.3%, cross entropy 0.344217
INFO:tensorflow:Step #6020: rate 0.000500, accuracy 87.5%, cross entropy 0.361920
INFO:tensorflow:Step #6030: rate 0.000500, accuracy 89.5%, cross entropy 0.280158
INFO:tensorflow:Step #6040: rate 0.000500, accuracy 87.9%, cross entropy 0.340663
INFO:tensorflow:Step #6050: rate 0.000500, accuracy 90.2%, cross entropy 0.284335
INFO:tensorflow:Step #6060: rate 0.000500, accuracy 86.3%, cross entropy 0.441283
INFO:tensorflow:Step #6070: rate 0.000500, accuracy 93.0%, cross entropy 0.266032
INFO:tensorflow:Step #6080: rate 0.000500, accuracy 89.8%, cross entropy 0.300059
INFO:tensorflow:Step #6090: rate 0.000500, accuracy 87.9%, cross entropy 0.365075
INFO:tensorflow:Step #6100: rate 0.000500, accuracy 91.0%, cross entropy 0.338309
INFO:tensorflow:Step #6110: rate 0.000500, accuracy 88.3%, cross entropy 0.356726
INFO:tensorflow:Step #6120: rate 0.000500, accuracy 93.0%, cross entropy 0.219533
INFO:tensorflow:Step #6130: rate 0.000500, accuracy 88.3%, cross entropy 0.304394
INFO:tensorflow:Step #6140: rate 0.000500, accuracy 90.2%, cross entropy 0.365632
INFO:tensorflow:Step #6150: rate 0.000500, accuracy 91.4%, cross entropy 0.260496
INFO:tensorflow:Step #6160: rate 0.000500, accuracy 90.2%, cross entropy 0.254115
INFO:tensorflow:Step #6170: rate 0.000500, accuracy 92.6%, cross entropy 0.247277
INFO:tensorflow:Step #6180: rate 0.000500, accuracy 90.2%, cross entropy 0.320980
INFO:tensorflow:Step #6190: rate 0.000500, accuracy 91.0%, cross entropy 0.260430
INFO:tensorflow:Step #6200: rate 0.000500, accuracy 89.5%, cross entropy 0.323842
INFO:tensorflow:Step #6210: rate 0.000500, accuracy 89.5%, cross entropy 0.299951
INFO:tensorflow:Step #6220: rate 0.000500, accuracy 86.3%, cross entropy 0.380261
INFO:tensorflow:Step #6230: rate 0.000500, accuracy 89.5%, cross entropy 0.334411
INFO:tensorflow:Step #6240: rate 0.000500, accuracy 90.2%, cross entropy 0.322004
INFO:tensorflow:Step #6250: rate 0.000500, accuracy 89.5%, cross entropy 0.328895
INFO:tensorflow:Step #6260: rate 0.000500, accuracy 87.9%, cross entropy 0.312274
INFO:tensorflow:Step #6270: rate 0.000500, accuracy 91.4%, cross entropy 0.261240
INFO:tensorflow:Step #6280: rate 0.000500, accuracy 89.5%, cross entropy 0.307972
INFO:tensorflow:Step #6290: rate 0.000500, accuracy 90.6%, cross entropy 0.328686
INFO:tensorflow:Step #6300: rate 0.000500, accuracy 87.1%, cross entropy 0.349745
INFO:tensorflow:Step #6310: rate 0.000500, accuracy 92.6%, cross entropy 0.222230
INFO:tensorflow:Step #6320: rate 0.000500, accuracy 92.2%, cross entropy 0.302028
INFO:tensorflow:Step #6330: rate 0.000500, accuracy 88.7%, cross entropy 0.293840
INFO:tensorflow:Step #6340: rate 0.000500, accuracy 92.2%, cross entropy 0.246216
INFO:tensorflow:Step #6350: rate 0.000500, accuracy 93.0%, cross entropy 0.212597
INFO:tensorflow:Step #6360: rate 0.000500, accuracy 87.9%, cross entropy 0.386710
INFO:tensorflow:Step #6370: rate 0.000500, accuracy 88.3%, cross entropy 0.354742
INFO:tensorflow:Step #6380: rate 0.000500, accuracy 90.2%, cross entropy 0.345696
INFO:tensorflow:Step #6390: rate 0.000500, accuracy 92.6%, cross entropy 0.212739
INFO:tensorflow:Step #6400: rate 0.000500, accuracy 91.4%, cross entropy 0.258576
INFO:tensorflow:Step #6410: rate 0.000500, accuracy 91.4%, cross entropy 0.270071
INFO:tensorflow:Step #6420: rate 0.000500, accuracy 91.4%, cross entropy 0.302596
INFO:tensorflow:Step #6430: rate 0.000500, accuracy 88.3%, cross entropy 0.358995
INFO:tensorflow:Step #6440: rate 0.000500, accuracy 91.0%, cross entropy 0.289454
INFO:tensorflow:Step #6450: rate 0.000500, accuracy 90.6%, cross entropy 0.307457
INFO:tensorflow:Step #6460: rate 0.000500, accuracy 91.4%, cross entropy 0.287606
INFO:tensorflow:Step #6470: rate 0.000500, accuracy 90.2%, cross entropy 0.296470
INFO:tensorflow:Step #6480: rate 0.000500, accuracy 90.2%, cross entropy 0.294854
INFO:tensorflow:Step #6490: rate 0.000500, accuracy 90.2%, cross entropy 0.376539
INFO:tensorflow:Step #6500: rate 0.000500, accuracy 90.6%, cross entropy 0.308449
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 215   5   8   4   4   0   8   3   2   1   8]
 [  0   0 250   6   3   0   2   0   0   0   0   0]
 [  0   4   1 255   1   2   0   1   0   0   0   6]
 [  0   4   0   0 243   0   0   2   0  11   0   0]
 [  0   0   1   6   0 255   0   1   0   0   0   1]
 [  0   3  17   2   1   0 222   2   0   0   0   0]
 [  0   4   0   0   2   0   1 249   0   0   0   0]
 [  0   4   0   0   5   1   0   0 244   3   0   0]
 [  0   1   0   0  15   1   0   0   4 233   1   1]
 [  0   3   0   1   9   0   1   2   0   3 226   1]
 [  0   6   0  14   9   5   0   0   1   2   2 221]]
INFO:tensorflow:Step 6500: Validation accuracy = 92.2% (N=2835)
INFO:tensorflow:Step #6510: rate 0.000500, accuracy 91.8%, cross entropy 0.238677
INFO:tensorflow:Step #6520: rate 0.000500, accuracy 91.0%, cross entropy 0.283301
INFO:tensorflow:Step #6530: rate 0.000500, accuracy 90.2%, cross entropy 0.280597
INFO:tensorflow:Step #6540: rate 0.000500, accuracy 89.8%, cross entropy 0.316125
INFO:tensorflow:Step #6550: rate 0.000500, accuracy 91.4%, cross entropy 0.251683
INFO:tensorflow:Step #6560: rate 0.000500, accuracy 91.8%, cross entropy 0.266076
INFO:tensorflow:Step #6570: rate 0.000500, accuracy 90.6%, cross entropy 0.259784
INFO:tensorflow:Step #6580: rate 0.000500, accuracy 86.7%, cross entropy 0.461497
INFO:tensorflow:Step #6590: rate 0.000500, accuracy 91.4%, cross entropy 0.275037
INFO:tensorflow:Step #6600: rate 0.000500, accuracy 89.8%, cross entropy 0.339252
INFO:tensorflow:Step #6610: rate 0.000500, accuracy 89.8%, cross entropy 0.262124
INFO:tensorflow:Step #6620: rate 0.000500, accuracy 89.8%, cross entropy 0.351279
INFO:tensorflow:Step #6630: rate 0.000500, accuracy 89.1%, cross entropy 0.340946
INFO:tensorflow:Step #6640: rate 0.000500, accuracy 87.9%, cross entropy 0.354308
INFO:tensorflow:Step #6650: rate 0.000500, accuracy 89.8%, cross entropy 0.308571
INFO:tensorflow:Step #6660: rate 0.000500, accuracy 87.1%, cross entropy 0.368164
INFO:tensorflow:Step #6670: rate 0.000500, accuracy 91.4%, cross entropy 0.274014
INFO:tensorflow:Step #6680: rate 0.000500, accuracy 91.4%, cross entropy 0.244665
INFO:tensorflow:Step #6690: rate 0.000500, accuracy 92.2%, cross entropy 0.255836
INFO:tensorflow:Step #6700: rate 0.000500, accuracy 90.2%, cross entropy 0.307531
INFO:tensorflow:Step #6710: rate 0.000500, accuracy 91.0%, cross entropy 0.233522
INFO:tensorflow:Step #6720: rate 0.000500, accuracy 89.5%, cross entropy 0.341999
INFO:tensorflow:Step #6730: rate 0.000500, accuracy 93.0%, cross entropy 0.257634
INFO:tensorflow:Step #6740: rate 0.000500, accuracy 91.0%, cross entropy 0.323456
INFO:tensorflow:Step #6750: rate 0.000500, accuracy 90.2%, cross entropy 0.262154
INFO:tensorflow:Step #6760: rate 0.000500, accuracy 90.2%, cross entropy 0.326168
INFO:tensorflow:Step #6770: rate 0.000500, accuracy 89.1%, cross entropy 0.305419
INFO:tensorflow:Step #6780: rate 0.000500, accuracy 91.8%, cross entropy 0.229454
INFO:tensorflow:Step #6790: rate 0.000500, accuracy 91.8%, cross entropy 0.287282
INFO:tensorflow:Step #6800: rate 0.000500, accuracy 90.6%, cross entropy 0.268166
INFO:tensorflow:Step #6810: rate 0.000500, accuracy 92.6%, cross entropy 0.250233
INFO:tensorflow:Step #6820: rate 0.000500, accuracy 93.0%, cross entropy 0.214304
INFO:tensorflow:Step #6830: rate 0.000500, accuracy 86.7%, cross entropy 0.387569
INFO:tensorflow:Step #6840: rate 0.000500, accuracy 90.2%, cross entropy 0.296313
INFO:tensorflow:Step #6850: rate 0.000500, accuracy 86.7%, cross entropy 0.427740
INFO:tensorflow:Step #6860: rate 0.000500, accuracy 91.4%, cross entropy 0.248293
INFO:tensorflow:Step #6870: rate 0.000500, accuracy 91.0%, cross entropy 0.224465
INFO:tensorflow:Step #6880: rate 0.000500, accuracy 91.0%, cross entropy 0.250115
INFO:tensorflow:Step #6890: rate 0.000500, accuracy 91.0%, cross entropy 0.267758
INFO:tensorflow:Step #6900: rate 0.000500, accuracy 87.5%, cross entropy 0.452767
INFO:tensorflow:Step #6910: rate 0.000500, accuracy 88.3%, cross entropy 0.406676
INFO:tensorflow:Step #6920: rate 0.000500, accuracy 92.2%, cross entropy 0.244798
INFO:tensorflow:Step #6930: rate 0.000500, accuracy 91.0%, cross entropy 0.277298
INFO:tensorflow:Step #6940: rate 0.000500, accuracy 93.4%, cross entropy 0.269447
INFO:tensorflow:Step #6950: rate 0.000500, accuracy 91.8%, cross entropy 0.250703
INFO:tensorflow:Step #6960: rate 0.000500, accuracy 89.5%, cross entropy 0.273578
INFO:tensorflow:Step #6970: rate 0.000500, accuracy 87.9%, cross entropy 0.356335
INFO:tensorflow:Step #6980: rate 0.000500, accuracy 89.1%, cross entropy 0.312007
INFO:tensorflow:Step #6990: rate 0.000500, accuracy 90.2%, cross entropy 0.303633
INFO:tensorflow:Step #7000: rate 0.000500, accuracy 85.9%, cross entropy 0.375043
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 209   4   8   6   4   1   8   4   3   1  10]
 [  0   0 249   7   3   0   2   0   0   0   0   0]
 [  0   2   1 258   1   1   0   1   0   0   0   6]
 [  0   4   0   0 248   0   0   0   0   8   0   0]
 [  0   0   1   8   0 250   1   0   0   0   1   3]
 [  0   0  13   6   1   0 226   1   0   0   0   0]
 [  0   3   0   1   2   1   2 247   0   0   0   0]
 [  0   3   0   0   5   0   0   0 245   4   0   0]
 [  0   1   0   1  18   0   0   0   2 232   2   0]
 [  0   3   0   0   9   0   0   0   0   3 230   1]
 [  0   6   0  11   8   3   0   0   0   2   3 227]]
INFO:tensorflow:Step 7000: Validation accuracy = 92.5% (N=2835)
INFO:tensorflow:Step #7010: rate 0.000500, accuracy 86.3%, cross entropy 0.394312
INFO:tensorflow:Step #7020: rate 0.000500, accuracy 89.1%, cross entropy 0.305294
INFO:tensorflow:Step #7030: rate 0.000500, accuracy 93.4%, cross entropy 0.271291
INFO:tensorflow:Step #7040: rate 0.000500, accuracy 87.9%, cross entropy 0.331079
INFO:tensorflow:Step #7050: rate 0.000500, accuracy 90.6%, cross entropy 0.329846
INFO:tensorflow:Step #7060: rate 0.000500, accuracy 89.5%, cross entropy 0.331209
INFO:tensorflow:Step #7070: rate 0.000500, accuracy 87.9%, cross entropy 0.353304
INFO:tensorflow:Step #7080: rate 0.000500, accuracy 90.6%, cross entropy 0.292766
INFO:tensorflow:Step #7090: rate 0.000500, accuracy 86.7%, cross entropy 0.420937
INFO:tensorflow:Step #7100: rate 0.000500, accuracy 91.8%, cross entropy 0.276554
INFO:tensorflow:Step #7110: rate 0.000500, accuracy 89.5%, cross entropy 0.315726
INFO:tensorflow:Step #7120: rate 0.000500, accuracy 87.5%, cross entropy 0.357389
INFO:tensorflow:Step #7130: rate 0.000500, accuracy 87.5%, cross entropy 0.396277
INFO:tensorflow:Step #7140: rate 0.000500, accuracy 91.4%, cross entropy 0.245079
INFO:tensorflow:Step #7150: rate 0.000500, accuracy 91.4%, cross entropy 0.276473
INFO:tensorflow:Step #7160: rate 0.000500, accuracy 91.0%, cross entropy 0.268442
INFO:tensorflow:Step #7170: rate 0.000500, accuracy 91.0%, cross entropy 0.264662
INFO:tensorflow:Step #7180: rate 0.000500, accuracy 90.6%, cross entropy 0.281651
INFO:tensorflow:Step #7190: rate 0.000500, accuracy 90.2%, cross entropy 0.313202
INFO:tensorflow:Step #7200: rate 0.000500, accuracy 88.3%, cross entropy 0.322119
INFO:tensorflow:Step #7210: rate 0.000500, accuracy 88.3%, cross entropy 0.301445
INFO:tensorflow:Step #7220: rate 0.000500, accuracy 89.8%, cross entropy 0.298841
INFO:tensorflow:Step #7230: rate 0.000500, accuracy 88.3%, cross entropy 0.308006
INFO:tensorflow:Step #7240: rate 0.000500, accuracy 88.7%, cross entropy 0.328315
INFO:tensorflow:Step #7250: rate 0.000500, accuracy 85.9%, cross entropy 0.366999
INFO:tensorflow:Step #7260: rate 0.000500, accuracy 91.0%, cross entropy 0.345606
INFO:tensorflow:Step #7270: rate 0.000500, accuracy 88.3%, cross entropy 0.399692
INFO:tensorflow:Step #7280: rate 0.000500, accuracy 93.8%, cross entropy 0.184819
INFO:tensorflow:Step #7290: rate 0.000500, accuracy 87.5%, cross entropy 0.371328
INFO:tensorflow:Step #7300: rate 0.000500, accuracy 94.9%, cross entropy 0.160604
INFO:tensorflow:Step #7310: rate 0.000500, accuracy 92.6%, cross entropy 0.268486
INFO:tensorflow:Step #7320: rate 0.000500, accuracy 91.0%, cross entropy 0.246032
INFO:tensorflow:Step #7330: rate 0.000500, accuracy 88.3%, cross entropy 0.349827
INFO:tensorflow:Step #7340: rate 0.000500, accuracy 88.3%, cross entropy 0.342592
INFO:tensorflow:Step #7350: rate 0.000500, accuracy 89.1%, cross entropy 0.335336
INFO:tensorflow:Step #7360: rate 0.000500, accuracy 89.8%, cross entropy 0.291473
INFO:tensorflow:Step #7370: rate 0.000500, accuracy 89.1%, cross entropy 0.364866
INFO:tensorflow:Step #7380: rate 0.000500, accuracy 89.5%, cross entropy 0.258039
INFO:tensorflow:Step #7390: rate 0.000500, accuracy 92.6%, cross entropy 0.254915
INFO:tensorflow:Step #7400: rate 0.000500, accuracy 90.6%, cross entropy 0.284172
INFO:tensorflow:Step #7410: rate 0.000500, accuracy 90.2%, cross entropy 0.287392
INFO:tensorflow:Step #7420: rate 0.000500, accuracy 92.6%, cross entropy 0.225461
INFO:tensorflow:Step #7430: rate 0.000500, accuracy 92.6%, cross entropy 0.221307
INFO:tensorflow:Step #7440: rate 0.000500, accuracy 89.1%, cross entropy 0.289467
INFO:tensorflow:Step #7450: rate 0.000500, accuracy 87.5%, cross entropy 0.340505
INFO:tensorflow:Step #7460: rate 0.000500, accuracy 92.2%, cross entropy 0.282152
INFO:tensorflow:Step #7470: rate 0.000500, accuracy 89.5%, cross entropy 0.296265
INFO:tensorflow:Step #7480: rate 0.000500, accuracy 90.6%, cross entropy 0.304976
INFO:tensorflow:Step #7490: rate 0.000500, accuracy 90.2%, cross entropy 0.304530
INFO:tensorflow:Step #7500: rate 0.000500, accuracy 90.2%, cross entropy 0.362398
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 223   4   7   4   2   0   4   2   4   4   4]
 [  0   0 247   7   2   0   4   0   1   0   0   0]
 [  0   2   1 259   1   1   0   0   0   0   0   6]
 [  0   5   0   0 244   0   0   1   0  10   0   0]
 [  0   1   1   9   0 251   0   0   0   0   0   2]
 [  0   5  10   6   1   0 224   1   0   0   0   0]
 [  0   7   0   1   2   1   1 244   0   0   0   0]
 [  0   7   0   0   5   1   0   0 236   8   0   0]
 [  0   1   0   1  12   0   0   0   2 237   2   1]
 [  0   2   0   0   8   0   0   0   0   2 232   2]
 [  0   9   0  12   8   5   0   0   0   3   2 221]]
INFO:tensorflow:Step 7500: Validation accuracy = 92.3% (N=2835)
INFO:tensorflow:Step #7510: rate 0.000500, accuracy 89.5%, cross entropy 0.287669
INFO:tensorflow:Step #7520: rate 0.000500, accuracy 89.1%, cross entropy 0.328606
INFO:tensorflow:Step #7530: rate 0.000500, accuracy 89.5%, cross entropy 0.312154
INFO:tensorflow:Step #7540: rate 0.000500, accuracy 91.4%, cross entropy 0.248556
INFO:tensorflow:Step #7550: rate 0.000500, accuracy 86.3%, cross entropy 0.356168
INFO:tensorflow:Step #7560: rate 0.000500, accuracy 86.3%, cross entropy 0.354318
INFO:tensorflow:Step #7570: rate 0.000500, accuracy 90.2%, cross entropy 0.336830
INFO:tensorflow:Step #7580: rate 0.000500, accuracy 89.8%, cross entropy 0.269340
INFO:tensorflow:Step #7590: rate 0.000500, accuracy 90.6%, cross entropy 0.268385
INFO:tensorflow:Step #7600: rate 0.000500, accuracy 93.0%, cross entropy 0.256957
INFO:tensorflow:Step #7610: rate 0.000500, accuracy 88.3%, cross entropy 0.327667
INFO:tensorflow:Step #7620: rate 0.000500, accuracy 91.0%, cross entropy 0.241564
INFO:tensorflow:Step #7630: rate 0.000500, accuracy 94.1%, cross entropy 0.207540
INFO:tensorflow:Step #7640: rate 0.000500, accuracy 89.8%, cross entropy 0.323921
INFO:tensorflow:Step #7650: rate 0.000500, accuracy 91.4%, cross entropy 0.274017
INFO:tensorflow:Step #7660: rate 0.000500, accuracy 91.8%, cross entropy 0.269882
INFO:tensorflow:Step #7670: rate 0.000500, accuracy 88.7%, cross entropy 0.333891
INFO:tensorflow:Step #7680: rate 0.000500, accuracy 92.6%, cross entropy 0.265408
INFO:tensorflow:Step #7690: rate 0.000500, accuracy 91.0%, cross entropy 0.306735
INFO:tensorflow:Step #7700: rate 0.000500, accuracy 91.8%, cross entropy 0.254256
INFO:tensorflow:Step #7710: rate 0.000500, accuracy 91.0%, cross entropy 0.294532
INFO:tensorflow:Step #7720: rate 0.000500, accuracy 91.8%, cross entropy 0.258586
INFO:tensorflow:Step #7730: rate 0.000500, accuracy 90.6%, cross entropy 0.289111
INFO:tensorflow:Step #7740: rate 0.000500, accuracy 88.3%, cross entropy 0.347663
INFO:tensorflow:Step #7750: rate 0.000500, accuracy 87.5%, cross entropy 0.342409
INFO:tensorflow:Step #7760: rate 0.000500, accuracy 89.1%, cross entropy 0.306590
INFO:tensorflow:Step #7770: rate 0.000500, accuracy 89.1%, cross entropy 0.283336
INFO:tensorflow:Step #7780: rate 0.000500, accuracy 89.8%, cross entropy 0.297929
INFO:tensorflow:Step #7790: rate 0.000500, accuracy 89.8%, cross entropy 0.313977
INFO:tensorflow:Step #7800: rate 0.000500, accuracy 90.6%, cross entropy 0.266566
INFO:tensorflow:Step #7810: rate 0.000500, accuracy 91.4%, cross entropy 0.240575
INFO:tensorflow:Step #7820: rate 0.000500, accuracy 90.6%, cross entropy 0.298012
INFO:tensorflow:Step #7830: rate 0.000500, accuracy 90.6%, cross entropy 0.293797
INFO:tensorflow:Step #7840: rate 0.000500, accuracy 93.0%, cross entropy 0.242538
INFO:tensorflow:Step #7850: rate 0.000500, accuracy 89.8%, cross entropy 0.291430
INFO:tensorflow:Step #7860: rate 0.000500, accuracy 93.0%, cross entropy 0.230845
INFO:tensorflow:Step #7870: rate 0.000500, accuracy 88.7%, cross entropy 0.334072
INFO:tensorflow:Step #7880: rate 0.000500, accuracy 87.9%, cross entropy 0.347115
INFO:tensorflow:Step #7890: rate 0.000500, accuracy 89.5%, cross entropy 0.320716
INFO:tensorflow:Step #7900: rate 0.000500, accuracy 90.6%, cross entropy 0.275170
INFO:tensorflow:Step #7910: rate 0.000500, accuracy 90.6%, cross entropy 0.306476
INFO:tensorflow:Step #7920: rate 0.000500, accuracy 90.6%, cross entropy 0.362664
INFO:tensorflow:Step #7930: rate 0.000500, accuracy 91.4%, cross entropy 0.254250
INFO:tensorflow:Step #7940: rate 0.000500, accuracy 91.0%, cross entropy 0.285132
INFO:tensorflow:Step #7950: rate 0.000500, accuracy 90.2%, cross entropy 0.245519
INFO:tensorflow:Step #7960: rate 0.000500, accuracy 89.5%, cross entropy 0.342378
INFO:tensorflow:Step #7970: rate 0.000500, accuracy 92.2%, cross entropy 0.245862
INFO:tensorflow:Step #7980: rate 0.000500, accuracy 90.6%, cross entropy 0.317887
INFO:tensorflow:Step #7990: rate 0.000500, accuracy 90.2%, cross entropy 0.317167
INFO:tensorflow:Step #8000: rate 0.000500, accuracy 89.8%, cross entropy 0.294372
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 210   4   6   4   2   1   9   7   4   3   8]
 [  0   0 247   7   3   0   4   0   0   0   0   0]
 [  0   2   1 255   1   1   2   0   0   0   0   8]
 [  0   4   0   0 241   0   0   1   0  14   0   0]
 [  0   0   1   7   0 251   1   0   0   0   1   3]
 [  0   0  13   6   1   0 226   1   0   0   0   0]
 [  0   4   0   1   3   1   4 241   2   0   0   0]
 [  0   3   0   0   5   1   0   0 243   5   0   0]
 [  0   0   0   2  15   0   0   0   2 237   0   0]
 [  0   1   0   0  10   0   0   0   0   3 230   2]
 [  0   4   0   8   7   3   0   0   0   4   2 232]]
INFO:tensorflow:Step 8000: Validation accuracy = 92.2% (N=2835)
INFO:tensorflow:Saving to "F:\ML_Project\Data\logs&checkpoint\c_rnn\ckpt-8000"
INFO:tensorflow:Step #8010: rate 0.000500, accuracy 89.1%, cross entropy 0.354499
INFO:tensorflow:Step #8020: rate 0.000500, accuracy 91.4%, cross entropy 0.275441
INFO:tensorflow:Step #8030: rate 0.000500, accuracy 88.7%, cross entropy 0.296171
INFO:tensorflow:Step #8040: rate 0.000500, accuracy 88.3%, cross entropy 0.329708
INFO:tensorflow:Step #8050: rate 0.000500, accuracy 93.8%, cross entropy 0.226655
INFO:tensorflow:Step #8060: rate 0.000500, accuracy 91.4%, cross entropy 0.251465
INFO:tensorflow:Step #8070: rate 0.000500, accuracy 86.3%, cross entropy 0.355586
INFO:tensorflow:Step #8080: rate 0.000500, accuracy 88.3%, cross entropy 0.310795
INFO:tensorflow:Step #8090: rate 0.000500, accuracy 89.1%, cross entropy 0.319009
INFO:tensorflow:Step #8100: rate 0.000500, accuracy 86.7%, cross entropy 0.335006
INFO:tensorflow:Step #8110: rate 0.000500, accuracy 93.0%, cross entropy 0.266937
INFO:tensorflow:Step #8120: rate 0.000500, accuracy 89.8%, cross entropy 0.314847
INFO:tensorflow:Step #8130: rate 0.000500, accuracy 89.5%, cross entropy 0.285943
INFO:tensorflow:Step #8140: rate 0.000500, accuracy 93.4%, cross entropy 0.224769
INFO:tensorflow:Step #8150: rate 0.000500, accuracy 87.9%, cross entropy 0.387117
INFO:tensorflow:Step #8160: rate 0.000500, accuracy 91.8%, cross entropy 0.272653
INFO:tensorflow:Step #8170: rate 0.000500, accuracy 90.2%, cross entropy 0.287313
INFO:tensorflow:Step #8180: rate 0.000500, accuracy 93.0%, cross entropy 0.235248
INFO:tensorflow:Step #8190: rate 0.000500, accuracy 91.0%, cross entropy 0.276142
INFO:tensorflow:Step #8200: rate 0.000500, accuracy 91.8%, cross entropy 0.263553
INFO:tensorflow:Step #8210: rate 0.000500, accuracy 88.3%, cross entropy 0.353790
INFO:tensorflow:Step #8220: rate 0.000500, accuracy 91.8%, cross entropy 0.242831
INFO:tensorflow:Step #8230: rate 0.000500, accuracy 90.6%, cross entropy 0.247820
INFO:tensorflow:Step #8240: rate 0.000500, accuracy 88.7%, cross entropy 0.341425
INFO:tensorflow:Step #8250: rate 0.000500, accuracy 91.4%, cross entropy 0.282037
INFO:tensorflow:Step #8260: rate 0.000500, accuracy 91.0%, cross entropy 0.251082
INFO:tensorflow:Step #8270: rate 0.000500, accuracy 89.8%, cross entropy 0.290241
INFO:tensorflow:Step #8280: rate 0.000500, accuracy 87.1%, cross entropy 0.337531
INFO:tensorflow:Step #8290: rate 0.000500, accuracy 93.4%, cross entropy 0.231771
INFO:tensorflow:Step #8300: rate 0.000500, accuracy 91.4%, cross entropy 0.296762
INFO:tensorflow:Step #8310: rate 0.000500, accuracy 90.2%, cross entropy 0.262345
INFO:tensorflow:Step #8320: rate 0.000500, accuracy 88.7%, cross entropy 0.305384
INFO:tensorflow:Step #8330: rate 0.000500, accuracy 87.1%, cross entropy 0.307779
INFO:tensorflow:Step #8340: rate 0.000500, accuracy 87.9%, cross entropy 0.317490
INFO:tensorflow:Step #8350: rate 0.000500, accuracy 91.0%, cross entropy 0.243222
INFO:tensorflow:Step #8360: rate 0.000500, accuracy 93.8%, cross entropy 0.239564
INFO:tensorflow:Step #8370: rate 0.000500, accuracy 92.6%, cross entropy 0.235136
INFO:tensorflow:Step #8380: rate 0.000500, accuracy 92.2%, cross entropy 0.288363
INFO:tensorflow:Step #8390: rate 0.000500, accuracy 91.0%, cross entropy 0.226591
INFO:tensorflow:Step #8400: rate 0.000500, accuracy 92.2%, cross entropy 0.266472
INFO:tensorflow:Step #8410: rate 0.000500, accuracy 91.8%, cross entropy 0.228206
INFO:tensorflow:Step #8420: rate 0.000500, accuracy 93.8%, cross entropy 0.235274
INFO:tensorflow:Step #8430: rate 0.000500, accuracy 92.6%, cross entropy 0.247711
INFO:tensorflow:Step #8440: rate 0.000500, accuracy 93.4%, cross entropy 0.205158
INFO:tensorflow:Step #8450: rate 0.000500, accuracy 95.7%, cross entropy 0.160002
INFO:tensorflow:Step #8460: rate 0.000500, accuracy 92.6%, cross entropy 0.227878
INFO:tensorflow:Step #8470: rate 0.000500, accuracy 90.6%, cross entropy 0.293307
INFO:tensorflow:Step #8480: rate 0.000500, accuracy 90.6%, cross entropy 0.293965
INFO:tensorflow:Step #8490: rate 0.000500, accuracy 92.6%, cross entropy 0.276931
INFO:tensorflow:Step #8500: rate 0.000500, accuracy 92.2%, cross entropy 0.249266
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 216   7   6   4   2   1   4   2   3   4   9]
 [  0   0 250   6   3   0   2   0   0   0   0   0]
 [  0   1   0 262   1   1   0   0   0   0   0   5]
 [  0   5   0   0 244   0   0   1   0   9   1   0]
 [  0   0   1  15   0 243   0   0   0   0   1   4]
 [  0   2  13   6   1   0 224   1   0   0   0   0]
 [  0   9   0   1   1   0   3 242   0   0   0   0]
 [  0   5   0   0   3   1   0   2 242   3   0   1]
 [  0   1   0   1  16   0   1   0   7 229   0   1]
 [  0   1   0   0   8   0   1   1   0   3 230   2]
 [  0   6   0  10   7   4   0   1   0   2   2 228]]
INFO:tensorflow:Step 8500: Validation accuracy = 92.1% (N=2835)
INFO:tensorflow:Step #8510: rate 0.000500, accuracy 89.1%, cross entropy 0.303216
INFO:tensorflow:Step #8520: rate 0.000500, accuracy 93.8%, cross entropy 0.205933
INFO:tensorflow:Step #8530: rate 0.000500, accuracy 87.1%, cross entropy 0.308882
INFO:tensorflow:Step #8540: rate 0.000500, accuracy 88.3%, cross entropy 0.324637
INFO:tensorflow:Step #8550: rate 0.000500, accuracy 92.6%, cross entropy 0.254929
INFO:tensorflow:Step #8560: rate 0.000500, accuracy 94.1%, cross entropy 0.188114
INFO:tensorflow:Step #8570: rate 0.000500, accuracy 92.6%, cross entropy 0.303614
INFO:tensorflow:Step #8580: rate 0.000500, accuracy 91.0%, cross entropy 0.282356
INFO:tensorflow:Step #8590: rate 0.000500, accuracy 91.8%, cross entropy 0.246770
INFO:tensorflow:Step #8600: rate 0.000500, accuracy 93.4%, cross entropy 0.241269
INFO:tensorflow:Step #8610: rate 0.000500, accuracy 91.0%, cross entropy 0.262803
INFO:tensorflow:Step #8620: rate 0.000500, accuracy 89.1%, cross entropy 0.279533
INFO:tensorflow:Step #8630: rate 0.000500, accuracy 90.6%, cross entropy 0.257880
INFO:tensorflow:Step #8640: rate 0.000500, accuracy 91.0%, cross entropy 0.269511
INFO:tensorflow:Step #8650: rate 0.000500, accuracy 91.4%, cross entropy 0.249178
INFO:tensorflow:Step #8660: rate 0.000500, accuracy 91.8%, cross entropy 0.238797
INFO:tensorflow:Step #8670: rate 0.000500, accuracy 90.6%, cross entropy 0.254946
INFO:tensorflow:Step #8680: rate 0.000500, accuracy 89.8%, cross entropy 0.299577
INFO:tensorflow:Step #8690: rate 0.000500, accuracy 91.8%, cross entropy 0.252206
INFO:tensorflow:Step #8700: rate 0.000500, accuracy 89.5%, cross entropy 0.246526
INFO:tensorflow:Step #8710: rate 0.000500, accuracy 85.2%, cross entropy 0.451087
INFO:tensorflow:Step #8720: rate 0.000500, accuracy 89.8%, cross entropy 0.299375
INFO:tensorflow:Step #8730: rate 0.000500, accuracy 89.8%, cross entropy 0.372835
INFO:tensorflow:Step #8740: rate 0.000500, accuracy 90.2%, cross entropy 0.308028
INFO:tensorflow:Step #8750: rate 0.000500, accuracy 87.9%, cross entropy 0.365580
INFO:tensorflow:Step #8760: rate 0.000500, accuracy 86.3%, cross entropy 0.429623
INFO:tensorflow:Step #8770: rate 0.000500, accuracy 91.0%, cross entropy 0.299490
INFO:tensorflow:Step #8780: rate 0.000500, accuracy 88.7%, cross entropy 0.305714
INFO:tensorflow:Step #8790: rate 0.000500, accuracy 92.6%, cross entropy 0.223893
INFO:tensorflow:Step #8800: rate 0.000500, accuracy 89.5%, cross entropy 0.259949
INFO:tensorflow:Step #8810: rate 0.000500, accuracy 92.2%, cross entropy 0.284034
INFO:tensorflow:Step #8820: rate 0.000500, accuracy 89.5%, cross entropy 0.267163
INFO:tensorflow:Step #8830: rate 0.000500, accuracy 92.2%, cross entropy 0.231542
INFO:tensorflow:Step #8840: rate 0.000500, accuracy 93.4%, cross entropy 0.235283
INFO:tensorflow:Step #8850: rate 0.000500, accuracy 89.1%, cross entropy 0.331631
INFO:tensorflow:Step #8860: rate 0.000500, accuracy 89.8%, cross entropy 0.313164
INFO:tensorflow:Step #8870: rate 0.000500, accuracy 88.7%, cross entropy 0.374760
INFO:tensorflow:Step #8880: rate 0.000500, accuracy 91.0%, cross entropy 0.369517
INFO:tensorflow:Step #8890: rate 0.000500, accuracy 88.3%, cross entropy 0.347027
INFO:tensorflow:Step #8900: rate 0.000500, accuracy 85.9%, cross entropy 0.382157
INFO:tensorflow:Step #8910: rate 0.000500, accuracy 92.2%, cross entropy 0.304567
INFO:tensorflow:Step #8920: rate 0.000500, accuracy 92.2%, cross entropy 0.232256
INFO:tensorflow:Step #8930: rate 0.000500, accuracy 91.8%, cross entropy 0.318814
INFO:tensorflow:Step #8940: rate 0.000500, accuracy 91.4%, cross entropy 0.227285
INFO:tensorflow:Step #8950: rate 0.000500, accuracy 87.9%, cross entropy 0.327206
INFO:tensorflow:Step #8960: rate 0.000500, accuracy 92.6%, cross entropy 0.215484
INFO:tensorflow:Step #8970: rate 0.000500, accuracy 87.5%, cross entropy 0.424399
INFO:tensorflow:Step #8980: rate 0.000500, accuracy 91.0%, cross entropy 0.273660
INFO:tensorflow:Step #8990: rate 0.000500, accuracy 90.6%, cross entropy 0.281365
INFO:tensorflow:Step #9000: rate 0.000500, accuracy 87.5%, cross entropy 0.361723
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 219   5   4   2   2   0   7   5   2   3   9]
 [  0   1 250   5   2   1   2   0   0   0   0   0]
 [  0   2   1 253   1   2   0   1   0   0   0  10]
 [  0   7   0   0 241   0   0   1   0   8   2   1]
 [  0   1   1   6   0 249   0   1   0   0   1   5]
 [  0   2  13   4   1   0 227   0   0   0   0   0]
 [  0   5   0   1   2   0   3 245   0   0   0   0]
 [  0   6   0   0   2   1   0   0 242   3   3   0]
 [  0   0   0   1  13   0   0   0   6 234   1   1]
 [  0   5   0   1   5   0   0   0   0   4 230   1]
 [  0   7   0   7   6   4   0   1   0   3   3 229]]
INFO:tensorflow:Step 9000: Validation accuracy = 92.4% (N=2835)
INFO:tensorflow:Step #9010: rate 0.000500, accuracy 91.0%, cross entropy 0.260519
INFO:tensorflow:Step #9020: rate 0.000500, accuracy 91.8%, cross entropy 0.261432
INFO:tensorflow:Step #9030: rate 0.000500, accuracy 91.0%, cross entropy 0.277344
INFO:tensorflow:Step #9040: rate 0.000500, accuracy 92.6%, cross entropy 0.182163
INFO:tensorflow:Step #9050: rate 0.000500, accuracy 93.0%, cross entropy 0.271397
INFO:tensorflow:Step #9060: rate 0.000500, accuracy 87.5%, cross entropy 0.322946
INFO:tensorflow:Step #9070: rate 0.000500, accuracy 93.0%, cross entropy 0.229840
INFO:tensorflow:Step #9080: rate 0.000500, accuracy 91.0%, cross entropy 0.259510
INFO:tensorflow:Step #9090: rate 0.000500, accuracy 89.5%, cross entropy 0.291917
INFO:tensorflow:Step #9100: rate 0.000500, accuracy 91.0%, cross entropy 0.251641
INFO:tensorflow:Step #9110: rate 0.000500, accuracy 91.8%, cross entropy 0.207848
INFO:tensorflow:Step #9120: rate 0.000500, accuracy 90.2%, cross entropy 0.334434
INFO:tensorflow:Step #9130: rate 0.000500, accuracy 91.0%, cross entropy 0.291835
INFO:tensorflow:Step #9140: rate 0.000500, accuracy 94.1%, cross entropy 0.150404
INFO:tensorflow:Step #9150: rate 0.000500, accuracy 91.4%, cross entropy 0.282079
INFO:tensorflow:Step #9160: rate 0.000500, accuracy 88.3%, cross entropy 0.346861
INFO:tensorflow:Step #9170: rate 0.000500, accuracy 89.8%, cross entropy 0.293283
INFO:tensorflow:Step #9180: rate 0.000500, accuracy 89.5%, cross entropy 0.272165
INFO:tensorflow:Step #9190: rate 0.000500, accuracy 91.0%, cross entropy 0.273316
INFO:tensorflow:Step #9200: rate 0.000500, accuracy 89.8%, cross entropy 0.246079
INFO:tensorflow:Step #9210: rate 0.000500, accuracy 91.4%, cross entropy 0.260262
INFO:tensorflow:Step #9220: rate 0.000500, accuracy 87.9%, cross entropy 0.329934
INFO:tensorflow:Step #9230: rate 0.000500, accuracy 87.9%, cross entropy 0.328399
INFO:tensorflow:Step #9240: rate 0.000500, accuracy 90.2%, cross entropy 0.251969
INFO:tensorflow:Step #9250: rate 0.000500, accuracy 91.8%, cross entropy 0.232847
INFO:tensorflow:Step #9260: rate 0.000500, accuracy 93.0%, cross entropy 0.205466
INFO:tensorflow:Step #9270: rate 0.000500, accuracy 87.9%, cross entropy 0.388561
INFO:tensorflow:Step #9280: rate 0.000500, accuracy 88.3%, cross entropy 0.327380
INFO:tensorflow:Step #9290: rate 0.000500, accuracy 94.1%, cross entropy 0.188520
INFO:tensorflow:Step #9300: rate 0.000500, accuracy 94.5%, cross entropy 0.171563
INFO:tensorflow:Step #9310: rate 0.000500, accuracy 88.7%, cross entropy 0.319632
INFO:tensorflow:Step #9320: rate 0.000500, accuracy 93.0%, cross entropy 0.235684
INFO:tensorflow:Step #9330: rate 0.000500, accuracy 91.8%, cross entropy 0.218528
INFO:tensorflow:Step #9340: rate 0.000500, accuracy 92.2%, cross entropy 0.247785
INFO:tensorflow:Step #9350: rate 0.000500, accuracy 89.1%, cross entropy 0.260740
INFO:tensorflow:Step #9360: rate 0.000500, accuracy 93.8%, cross entropy 0.200397
INFO:tensorflow:Step #9370: rate 0.000500, accuracy 89.8%, cross entropy 0.310033
INFO:tensorflow:Step #9380: rate 0.000500, accuracy 92.2%, cross entropy 0.246797
INFO:tensorflow:Step #9390: rate 0.000500, accuracy 92.6%, cross entropy 0.226016
INFO:tensorflow:Step #9400: rate 0.000500, accuracy 91.4%, cross entropy 0.244943
INFO:tensorflow:Step #9410: rate 0.000500, accuracy 86.7%, cross entropy 0.324901
INFO:tensorflow:Step #9420: rate 0.000500, accuracy 89.5%, cross entropy 0.265230
INFO:tensorflow:Step #9430: rate 0.000500, accuracy 91.4%, cross entropy 0.293471
INFO:tensorflow:Step #9440: rate 0.000500, accuracy 90.6%, cross entropy 0.272299
INFO:tensorflow:Step #9450: rate 0.000500, accuracy 88.7%, cross entropy 0.304123
INFO:tensorflow:Step #9460: rate 0.000500, accuracy 87.9%, cross entropy 0.342282
INFO:tensorflow:Step #9470: rate 0.000500, accuracy 89.5%, cross entropy 0.365472
INFO:tensorflow:Step #9480: rate 0.000500, accuracy 93.4%, cross entropy 0.176236
INFO:tensorflow:Step #9490: rate 0.000500, accuracy 87.9%, cross entropy 0.347300
INFO:tensorflow:Step #9500: rate 0.000500, accuracy 90.6%, cross entropy 0.330970
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 203   4   9   2   4   0   9   6   6   3  12]
 [  0   0 249   8   0   0   1   0   0   1   2   0]
 [  0   2   0 253   1   2   1   0   0   0   0  11]
 [  0   3   0   0 234   0   0   1   0  19   2   1]
 [  0   0   1   5   0 254   0   0   0   0   0   4]
 [  0   3   9   8   1   0 224   1   0   0   1   0]
 [  0   2   0   1   0   0   2 250   0   0   1   0]
 [  0   2   0   0   0   1   0   2 244   5   3   0]
 [  0   1   0   0   9   0   0   0   9 234   2   1]
 [  0   1   0   0   5   0   0   0   0   4 232   4]
 [  0   4   0   6   5   4   0   1   1   3   3 233]]
INFO:tensorflow:Step 9500: Validation accuracy = 92.1% (N=2835)
INFO:tensorflow:Step #9510: rate 0.000500, accuracy 89.5%, cross entropy 0.324959
INFO:tensorflow:Step #9520: rate 0.000500, accuracy 94.1%, cross entropy 0.166271
INFO:tensorflow:Step #9530: rate 0.000500, accuracy 89.1%, cross entropy 0.316252
INFO:tensorflow:Step #9540: rate 0.000500, accuracy 87.1%, cross entropy 0.361632
INFO:tensorflow:Step #9550: rate 0.000500, accuracy 87.9%, cross entropy 0.306492
INFO:tensorflow:Step #9560: rate 0.000500, accuracy 88.3%, cross entropy 0.352831
INFO:tensorflow:Step #9570: rate 0.000500, accuracy 90.2%, cross entropy 0.309484
INFO:tensorflow:Step #9580: rate 0.000500, accuracy 91.4%, cross entropy 0.306447
INFO:tensorflow:Step #9590: rate 0.000500, accuracy 87.9%, cross entropy 0.392900
INFO:tensorflow:Step #9600: rate 0.000500, accuracy 89.8%, cross entropy 0.288899
INFO:tensorflow:Step #9610: rate 0.000500, accuracy 89.5%, cross entropy 0.326156
INFO:tensorflow:Step #9620: rate 0.000500, accuracy 87.5%, cross entropy 0.325579
INFO:tensorflow:Step #9630: rate 0.000500, accuracy 91.8%, cross entropy 0.288088
INFO:tensorflow:Step #9640: rate 0.000500, accuracy 94.1%, cross entropy 0.197354
INFO:tensorflow:Step #9650: rate 0.000500, accuracy 92.2%, cross entropy 0.240742
INFO:tensorflow:Step #9660: rate 0.000500, accuracy 91.8%, cross entropy 0.241986
INFO:tensorflow:Step #9670: rate 0.000500, accuracy 89.8%, cross entropy 0.281422
INFO:tensorflow:Step #9680: rate 0.000500, accuracy 90.6%, cross entropy 0.287304
INFO:tensorflow:Step #9690: rate 0.000500, accuracy 90.2%, cross entropy 0.266825
INFO:tensorflow:Step #9700: rate 0.000500, accuracy 89.8%, cross entropy 0.250259
INFO:tensorflow:Step #9710: rate 0.000500, accuracy 88.3%, cross entropy 0.324384
INFO:tensorflow:Step #9720: rate 0.000500, accuracy 89.1%, cross entropy 0.329047
INFO:tensorflow:Step #9730: rate 0.000500, accuracy 91.0%, cross entropy 0.234640
INFO:tensorflow:Step #9740: rate 0.000500, accuracy 91.0%, cross entropy 0.276122
INFO:tensorflow:Step #9750: rate 0.000500, accuracy 89.8%, cross entropy 0.322308
INFO:tensorflow:Step #9760: rate 0.000500, accuracy 90.6%, cross entropy 0.257932
INFO:tensorflow:Step #9770: rate 0.000500, accuracy 89.8%, cross entropy 0.300039
INFO:tensorflow:Step #9780: rate 0.000500, accuracy 92.6%, cross entropy 0.229096
INFO:tensorflow:Step #9790: rate 0.000500, accuracy 91.4%, cross entropy 0.258614
INFO:tensorflow:Step #9800: rate 0.000500, accuracy 90.6%, cross entropy 0.273372
INFO:tensorflow:Step #9810: rate 0.000500, accuracy 93.0%, cross entropy 0.206933
INFO:tensorflow:Step #9820: rate 0.000500, accuracy 85.9%, cross entropy 0.348062
INFO:tensorflow:Step #9830: rate 0.000500, accuracy 89.1%, cross entropy 0.292383
INFO:tensorflow:Step #9840: rate 0.000500, accuracy 87.5%, cross entropy 0.354423
INFO:tensorflow:Step #9850: rate 0.000500, accuracy 90.2%, cross entropy 0.249840
INFO:tensorflow:Step #9860: rate 0.000500, accuracy 92.6%, cross entropy 0.189393
INFO:tensorflow:Step #9870: rate 0.000500, accuracy 89.5%, cross entropy 0.291572
INFO:tensorflow:Step #9880: rate 0.000500, accuracy 90.2%, cross entropy 0.257195
INFO:tensorflow:Step #9890: rate 0.000500, accuracy 92.6%, cross entropy 0.223381
INFO:tensorflow:Step #9900: rate 0.000500, accuracy 91.8%, cross entropy 0.272654
INFO:tensorflow:Step #9910: rate 0.000500, accuracy 92.2%, cross entropy 0.215108
INFO:tensorflow:Step #9920: rate 0.000500, accuracy 90.6%, cross entropy 0.303704
INFO:tensorflow:Step #9930: rate 0.000500, accuracy 87.5%, cross entropy 0.336882
INFO:tensorflow:Step #9940: rate 0.000500, accuracy 91.8%, cross entropy 0.270064
INFO:tensorflow:Step #9950: rate 0.000500, accuracy 92.2%, cross entropy 0.265229
INFO:tensorflow:Step #9960: rate 0.000500, accuracy 94.5%, cross entropy 0.219522
INFO:tensorflow:Step #9970: rate 0.000500, accuracy 93.0%, cross entropy 0.243404
INFO:tensorflow:Step #9980: rate 0.000500, accuracy 93.0%, cross entropy 0.228661
INFO:tensorflow:Step #9990: rate 0.000500, accuracy 92.6%, cross entropy 0.251396
INFO:tensorflow:Step #10000: rate 0.000500, accuracy 93.4%, cross entropy 0.213072
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 217   5   6   3   2   0   6   4   4   3   8]
 [  0   0 250   6   2   0   2   0   1   0   0   0]
 [  0   2   1 258   1   1   0   0   0   0   0   7]
 [  0   5   0   0 246   0   0   0   0   9   0   0]
 [  0   3   1  13   0 242   0   0   0   0   0   5]
 [  0   1  10   6   1   0 228   1   0   0   0   0]
 [  0   6   0   1   1   0   3 245   0   0   0   0]
 [  0   5   0   0   3   0   0   2 243   4   0   0]
 [  0   1   0   1  16   0   0   0   4 233   0   1]
 [  0   3   0   1   9   0   0   0   0   2 228   3]
 [  0   7   0   8   6   4   0   2   0   3   1 229]]
INFO:tensorflow:Step 10000: Validation accuracy = 92.4% (N=2835)
INFO:tensorflow:Saving to "F:\ML_Project\Data\logs&checkpoint\c_rnn\ckpt-10000"
INFO:tensorflow:Step #10010: rate 0.000100, accuracy 91.0%, cross entropy 0.247945
INFO:tensorflow:Step #10020: rate 0.000100, accuracy 91.8%, cross entropy 0.284628
INFO:tensorflow:Step #10030: rate 0.000100, accuracy 87.9%, cross entropy 0.349426
INFO:tensorflow:Step #10040: rate 0.000100, accuracy 91.4%, cross entropy 0.271370
INFO:tensorflow:Step #10050: rate 0.000100, accuracy 89.1%, cross entropy 0.340721
INFO:tensorflow:Step #10060: rate 0.000100, accuracy 92.6%, cross entropy 0.275628
INFO:tensorflow:Step #10070: rate 0.000100, accuracy 91.0%, cross entropy 0.285829
INFO:tensorflow:Step #10080: rate 0.000100, accuracy 91.8%, cross entropy 0.249918
INFO:tensorflow:Step #10090: rate 0.000100, accuracy 92.2%, cross entropy 0.227458
INFO:tensorflow:Step #10100: rate 0.000100, accuracy 91.4%, cross entropy 0.229916
INFO:tensorflow:Step #10110: rate 0.000100, accuracy 90.6%, cross entropy 0.258033
INFO:tensorflow:Step #10120: rate 0.000100, accuracy 90.2%, cross entropy 0.260401
INFO:tensorflow:Step #10130: rate 0.000100, accuracy 91.0%, cross entropy 0.280291
INFO:tensorflow:Step #10140: rate 0.000100, accuracy 93.4%, cross entropy 0.213649
INFO:tensorflow:Step #10150: rate 0.000100, accuracy 91.0%, cross entropy 0.267686
INFO:tensorflow:Step #10160: rate 0.000100, accuracy 90.6%, cross entropy 0.206358
INFO:tensorflow:Step #10170: rate 0.000100, accuracy 90.2%, cross entropy 0.315464
INFO:tensorflow:Step #10180: rate 0.000100, accuracy 89.5%, cross entropy 0.247749
INFO:tensorflow:Step #10190: rate 0.000100, accuracy 93.0%, cross entropy 0.204994
INFO:tensorflow:Step #10200: rate 0.000100, accuracy 92.2%, cross entropy 0.245696
INFO:tensorflow:Step #10210: rate 0.000100, accuracy 93.4%, cross entropy 0.150122
INFO:tensorflow:Step #10220: rate 0.000100, accuracy 89.1%, cross entropy 0.267928
INFO:tensorflow:Step #10230: rate 0.000100, accuracy 92.6%, cross entropy 0.261767
INFO:tensorflow:Step #10240: rate 0.000100, accuracy 93.0%, cross entropy 0.219515
INFO:tensorflow:Step #10250: rate 0.000100, accuracy 92.2%, cross entropy 0.269052
INFO:tensorflow:Step #10260: rate 0.000100, accuracy 89.5%, cross entropy 0.354956
INFO:tensorflow:Step #10270: rate 0.000100, accuracy 92.2%, cross entropy 0.224851
INFO:tensorflow:Step #10280: rate 0.000100, accuracy 93.8%, cross entropy 0.214205
INFO:tensorflow:Step #10290: rate 0.000100, accuracy 93.4%, cross entropy 0.240182
INFO:tensorflow:Step #10300: rate 0.000100, accuracy 93.0%, cross entropy 0.218891
INFO:tensorflow:Step #10310: rate 0.000100, accuracy 91.0%, cross entropy 0.235383
INFO:tensorflow:Step #10320: rate 0.000100, accuracy 91.0%, cross entropy 0.269455
INFO:tensorflow:Step #10330: rate 0.000100, accuracy 93.8%, cross entropy 0.200223
INFO:tensorflow:Step #10340: rate 0.000100, accuracy 90.2%, cross entropy 0.291002
INFO:tensorflow:Step #10350: rate 0.000100, accuracy 92.6%, cross entropy 0.202366
INFO:tensorflow:Step #10360: rate 0.000100, accuracy 92.2%, cross entropy 0.237548
INFO:tensorflow:Step #10370: rate 0.000100, accuracy 88.7%, cross entropy 0.278809
INFO:tensorflow:Step #10380: rate 0.000100, accuracy 93.0%, cross entropy 0.267665
INFO:tensorflow:Step #10390: rate 0.000100, accuracy 90.6%, cross entropy 0.264938
INFO:tensorflow:Step #10400: rate 0.000100, accuracy 91.0%, cross entropy 0.235154
INFO:tensorflow:Step #10410: rate 0.000100, accuracy 90.2%, cross entropy 0.307943
INFO:tensorflow:Step #10420: rate 0.000100, accuracy 91.4%, cross entropy 0.246171
INFO:tensorflow:Step #10430: rate 0.000100, accuracy 92.2%, cross entropy 0.260679
INFO:tensorflow:Step #10440: rate 0.000100, accuracy 93.4%, cross entropy 0.234015
INFO:tensorflow:Step #10450: rate 0.000100, accuracy 90.6%, cross entropy 0.305131
INFO:tensorflow:Step #10460: rate 0.000100, accuracy 91.8%, cross entropy 0.284023
INFO:tensorflow:Step #10470: rate 0.000100, accuracy 91.4%, cross entropy 0.238665
INFO:tensorflow:Step #10480: rate 0.000100, accuracy 90.2%, cross entropy 0.279430
INFO:tensorflow:Step #10490: rate 0.000100, accuracy 87.9%, cross entropy 0.333023
INFO:tensorflow:Step #10500: rate 0.000100, accuracy 91.8%, cross entropy 0.257662
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 212   7   6   2   2   1   9   6   3   4   6]
 [  0   0 250   6   2   0   2   0   1   0   0   0]
 [  0   2   1 256   1   2   1   0   0   0   0   7]
 [  0   5   0   0 246   0   0   0   0   9   0   0]
 [  0   0   1   6   0 252   0   0   0   0   1   4]
 [  0   1   9   4   1   0 231   1   0   0   0   0]
 [  0   3   0   1   1   0   4 247   0   0   0   0]
 [  0   4   0   0   3   1   0   3 243   3   0   0]
 [  0   1   0   1  18   0   0   0   3 232   0   1]
 [  0   2   0   0   7   0   0   1   0   3 230   3]
 [  0   5   0   9   6   4   0   2   0   2   2 230]]
INFO:tensorflow:Step 10500: Validation accuracy = 92.7% (N=2835)
INFO:tensorflow:Step #10510: rate 0.000100, accuracy 90.6%, cross entropy 0.240870
INFO:tensorflow:Step #10520: rate 0.000100, accuracy 93.8%, cross entropy 0.181888
INFO:tensorflow:Step #10530: rate 0.000100, accuracy 89.8%, cross entropy 0.282457
INFO:tensorflow:Step #10540: rate 0.000100, accuracy 95.3%, cross entropy 0.189201
INFO:tensorflow:Step #10550: rate 0.000100, accuracy 93.4%, cross entropy 0.218440
INFO:tensorflow:Step #10560: rate 0.000100, accuracy 91.4%, cross entropy 0.258280
INFO:tensorflow:Step #10570: rate 0.000100, accuracy 91.8%, cross entropy 0.262075
INFO:tensorflow:Step #10580: rate 0.000100, accuracy 90.2%, cross entropy 0.300824
INFO:tensorflow:Step #10590: rate 0.000100, accuracy 91.8%, cross entropy 0.228965
INFO:tensorflow:Step #10600: rate 0.000100, accuracy 88.3%, cross entropy 0.325529
INFO:tensorflow:Step #10610: rate 0.000100, accuracy 88.3%, cross entropy 0.330524
INFO:tensorflow:Step #10620: rate 0.000100, accuracy 91.8%, cross entropy 0.262213
INFO:tensorflow:Step #10630: rate 0.000100, accuracy 91.8%, cross entropy 0.268971
INFO:tensorflow:Step #10640: rate 0.000100, accuracy 90.2%, cross entropy 0.295231
INFO:tensorflow:Step #10650: rate 0.000100, accuracy 95.3%, cross entropy 0.166069
INFO:tensorflow:Step #10660: rate 0.000100, accuracy 90.6%, cross entropy 0.309952
INFO:tensorflow:Step #10670: rate 0.000100, accuracy 93.0%, cross entropy 0.217179
INFO:tensorflow:Step #10680: rate 0.000100, accuracy 90.2%, cross entropy 0.301386
INFO:tensorflow:Step #10690: rate 0.000100, accuracy 93.4%, cross entropy 0.205654
INFO:tensorflow:Step #10700: rate 0.000100, accuracy 92.2%, cross entropy 0.253328
INFO:tensorflow:Step #10710: rate 0.000100, accuracy 91.4%, cross entropy 0.281192
INFO:tensorflow:Step #10720: rate 0.000100, accuracy 89.8%, cross entropy 0.277830
INFO:tensorflow:Step #10730: rate 0.000100, accuracy 90.2%, cross entropy 0.234109
INFO:tensorflow:Step #10740: rate 0.000100, accuracy 94.1%, cross entropy 0.168169
INFO:tensorflow:Step #10750: rate 0.000100, accuracy 89.8%, cross entropy 0.250160
INFO:tensorflow:Step #10760: rate 0.000100, accuracy 93.8%, cross entropy 0.179739
INFO:tensorflow:Step #10770: rate 0.000100, accuracy 89.1%, cross entropy 0.344465
INFO:tensorflow:Step #10780: rate 0.000100, accuracy 91.4%, cross entropy 0.253071
INFO:tensorflow:Step #10790: rate 0.000100, accuracy 93.8%, cross entropy 0.204193
INFO:tensorflow:Step #10800: rate 0.000100, accuracy 92.6%, cross entropy 0.222134
INFO:tensorflow:Step #10810: rate 0.000100, accuracy 93.0%, cross entropy 0.185606
INFO:tensorflow:Step #10820: rate 0.000100, accuracy 93.0%, cross entropy 0.222125
INFO:tensorflow:Step #10830: rate 0.000100, accuracy 89.8%, cross entropy 0.241666
INFO:tensorflow:Step #10840: rate 0.000100, accuracy 91.8%, cross entropy 0.233549
INFO:tensorflow:Step #10850: rate 0.000100, accuracy 93.0%, cross entropy 0.203347
INFO:tensorflow:Step #10860: rate 0.000100, accuracy 89.8%, cross entropy 0.254262
INFO:tensorflow:Step #10870: rate 0.000100, accuracy 90.6%, cross entropy 0.262932
INFO:tensorflow:Step #10880: rate 0.000100, accuracy 92.6%, cross entropy 0.250198
INFO:tensorflow:Step #10890: rate 0.000100, accuracy 89.5%, cross entropy 0.300860
INFO:tensorflow:Step #10900: rate 0.000100, accuracy 93.0%, cross entropy 0.218403
INFO:tensorflow:Step #10910: rate 0.000100, accuracy 90.2%, cross entropy 0.249656
INFO:tensorflow:Step #10920: rate 0.000100, accuracy 95.3%, cross entropy 0.152982
INFO:tensorflow:Step #10930: rate 0.000100, accuracy 89.5%, cross entropy 0.301607
INFO:tensorflow:Step #10940: rate 0.000100, accuracy 92.2%, cross entropy 0.241492
INFO:tensorflow:Step #10950: rate 0.000100, accuracy 92.6%, cross entropy 0.235695
INFO:tensorflow:Step #10960: rate 0.000100, accuracy 91.4%, cross entropy 0.246125
INFO:tensorflow:Step #10970: rate 0.000100, accuracy 91.4%, cross entropy 0.403044
INFO:tensorflow:Step #10980: rate 0.000100, accuracy 92.6%, cross entropy 0.218507
INFO:tensorflow:Step #10990: rate 0.000100, accuracy 89.5%, cross entropy 0.304288
INFO:tensorflow:Step #11000: rate 0.000100, accuracy 90.2%, cross entropy 0.266948
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 212   7   7   3   2   0   7   6   2   5   7]
 [  0   0 250   6   2   0   2   0   1   0   0   0]
 [  0   2   1 257   1   1   1   0   0   0   0   7]
 [  0   4   0   0 249   0   0   0   0   7   0   0]
 [  0   0   1   6   0 252   0   0   0   0   1   4]
 [  0   1   9   4   1   0 231   1   0   0   0   0]
 [  0   4   0   1   1   0   3 247   0   0   0   0]
 [  0   4   0   0   5   1   0   1 243   3   0   0]
 [  0   2   0   1  22   0   0   0   2 228   0   1]
 [  0   1   0   0   8   0   0   0   0   2 232   3]
 [  0   5   0   8   7   4   0   1   0   2   2 231]]
INFO:tensorflow:Step 11000: Validation accuracy = 92.8% (N=2835)
INFO:tensorflow:Step #11010: rate 0.000100, accuracy 91.4%, cross entropy 0.309214
INFO:tensorflow:Step #11020: rate 0.000100, accuracy 89.1%, cross entropy 0.282813
INFO:tensorflow:Step #11030: rate 0.000100, accuracy 91.0%, cross entropy 0.293900
INFO:tensorflow:Step #11040: rate 0.000100, accuracy 87.1%, cross entropy 0.357112
INFO:tensorflow:Step #11050: rate 0.000100, accuracy 89.8%, cross entropy 0.259635
INFO:tensorflow:Step #11060: rate 0.000100, accuracy 94.9%, cross entropy 0.133281
INFO:tensorflow:Step #11070: rate 0.000100, accuracy 92.6%, cross entropy 0.218265
INFO:tensorflow:Step #11080: rate 0.000100, accuracy 87.5%, cross entropy 0.331886
INFO:tensorflow:Step #11090: rate 0.000100, accuracy 91.4%, cross entropy 0.247769
INFO:tensorflow:Step #11100: rate 0.000100, accuracy 93.0%, cross entropy 0.207821
INFO:tensorflow:Step #11110: rate 0.000100, accuracy 94.5%, cross entropy 0.157798
INFO:tensorflow:Step #11120: rate 0.000100, accuracy 91.8%, cross entropy 0.231785
INFO:tensorflow:Step #11130: rate 0.000100, accuracy 90.6%, cross entropy 0.291046
INFO:tensorflow:Step #11140: rate 0.000100, accuracy 89.1%, cross entropy 0.329549
INFO:tensorflow:Step #11150: rate 0.000100, accuracy 93.0%, cross entropy 0.227162
INFO:tensorflow:Step #11160: rate 0.000100, accuracy 90.2%, cross entropy 0.321411
INFO:tensorflow:Step #11170: rate 0.000100, accuracy 92.2%, cross entropy 0.248373
INFO:tensorflow:Step #11180: rate 0.000100, accuracy 90.2%, cross entropy 0.305470
INFO:tensorflow:Step #11190: rate 0.000100, accuracy 90.6%, cross entropy 0.330361
INFO:tensorflow:Step #11200: rate 0.000100, accuracy 91.0%, cross entropy 0.279377
INFO:tensorflow:Step #11210: rate 0.000100, accuracy 87.9%, cross entropy 0.361014
INFO:tensorflow:Step #11220: rate 0.000100, accuracy 89.5%, cross entropy 0.273294
INFO:tensorflow:Step #11230: rate 0.000100, accuracy 91.8%, cross entropy 0.262166
INFO:tensorflow:Step #11240: rate 0.000100, accuracy 92.6%, cross entropy 0.249993
INFO:tensorflow:Step #11250: rate 0.000100, accuracy 90.2%, cross entropy 0.286925
INFO:tensorflow:Step #11260: rate 0.000100, accuracy 94.1%, cross entropy 0.224313
INFO:tensorflow:Step #11270: rate 0.000100, accuracy 92.6%, cross entropy 0.247199
INFO:tensorflow:Step #11280: rate 0.000100, accuracy 91.4%, cross entropy 0.263984
INFO:tensorflow:Step #11290: rate 0.000100, accuracy 92.2%, cross entropy 0.307907
INFO:tensorflow:Step #11300: rate 0.000100, accuracy 94.1%, cross entropy 0.169926
INFO:tensorflow:Step #11310: rate 0.000100, accuracy 94.5%, cross entropy 0.208170
INFO:tensorflow:Step #11320: rate 0.000100, accuracy 91.0%, cross entropy 0.281267
INFO:tensorflow:Step #11330: rate 0.000100, accuracy 91.0%, cross entropy 0.241309
INFO:tensorflow:Step #11340: rate 0.000100, accuracy 91.0%, cross entropy 0.355566
INFO:tensorflow:Step #11350: rate 0.000100, accuracy 91.8%, cross entropy 0.257556
INFO:tensorflow:Step #11360: rate 0.000100, accuracy 92.2%, cross entropy 0.227277
INFO:tensorflow:Step #11370: rate 0.000100, accuracy 92.2%, cross entropy 0.219014
INFO:tensorflow:Step #11380: rate 0.000100, accuracy 88.7%, cross entropy 0.280247
INFO:tensorflow:Step #11390: rate 0.000100, accuracy 92.6%, cross entropy 0.225490
INFO:tensorflow:Step #11400: rate 0.000100, accuracy 94.1%, cross entropy 0.199752
INFO:tensorflow:Step #11410: rate 0.000100, accuracy 91.4%, cross entropy 0.246830
INFO:tensorflow:Step #11420: rate 0.000100, accuracy 92.6%, cross entropy 0.272660
INFO:tensorflow:Step #11430: rate 0.000100, accuracy 88.7%, cross entropy 0.318177
INFO:tensorflow:Step #11440: rate 0.000100, accuracy 94.9%, cross entropy 0.214244
INFO:tensorflow:Step #11450: rate 0.000100, accuracy 92.6%, cross entropy 0.194496
INFO:tensorflow:Step #11460: rate 0.000100, accuracy 93.8%, cross entropy 0.210447
INFO:tensorflow:Step #11470: rate 0.000100, accuracy 93.8%, cross entropy 0.212809
INFO:tensorflow:Step #11480: rate 0.000100, accuracy 92.2%, cross entropy 0.278161
INFO:tensorflow:Step #11490: rate 0.000100, accuracy 94.1%, cross entropy 0.195098
INFO:tensorflow:Step #11500: rate 0.000100, accuracy 89.8%, cross entropy 0.376284
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 211   5   8   2   2   0   7   7   4   4   8]
 [  0   0 251   6   2   0   1   0   1   0   0   0]
 [  0   2   1 256   1   1   1   0   0   0   0   8]
 [  0   5   0   0 241   0   0   0   0  14   0   0]
 [  0   0   1   9   0 250   0   0   0   0   1   3]
 [  0   2   9   4   1   0 230   1   0   0   0   0]
 [  0   4   0   1   2   0   3 246   0   0   0   0]
 [  0   4   0   0   2   1   0   1 245   4   0   0]
 [  0   1   0   1  14   0   0   0   4 235   0   1]
 [  0   2   0   0   5   0   0   0   2   3 231   3]
 [  0   4   0   8   6   4   0   1   1   2   1 233]]
INFO:tensorflow:Step 11500: Validation accuracy = 92.7% (N=2835)
INFO:tensorflow:Step #11510: rate 0.000100, accuracy 93.4%, cross entropy 0.217552
INFO:tensorflow:Step #11520: rate 0.000100, accuracy 92.6%, cross entropy 0.205645
INFO:tensorflow:Step #11530: rate 0.000100, accuracy 92.2%, cross entropy 0.234330
INFO:tensorflow:Step #11540: rate 0.000100, accuracy 95.3%, cross entropy 0.152810
INFO:tensorflow:Step #11550: rate 0.000100, accuracy 91.8%, cross entropy 0.234366
INFO:tensorflow:Step #11560: rate 0.000100, accuracy 89.5%, cross entropy 0.287310
INFO:tensorflow:Step #11570: rate 0.000100, accuracy 87.5%, cross entropy 0.327290
INFO:tensorflow:Step #11580: rate 0.000100, accuracy 91.0%, cross entropy 0.235330
INFO:tensorflow:Step #11590: rate 0.000100, accuracy 91.8%, cross entropy 0.276552
INFO:tensorflow:Step #11600: rate 0.000100, accuracy 93.4%, cross entropy 0.224093
INFO:tensorflow:Step #11610: rate 0.000100, accuracy 92.2%, cross entropy 0.283996
INFO:tensorflow:Step #11620: rate 0.000100, accuracy 93.4%, cross entropy 0.226747
INFO:tensorflow:Step #11630: rate 0.000100, accuracy 91.8%, cross entropy 0.260857
INFO:tensorflow:Step #11640: rate 0.000100, accuracy 90.6%, cross entropy 0.316719
INFO:tensorflow:Step #11650: rate 0.000100, accuracy 88.3%, cross entropy 0.372167
INFO:tensorflow:Step #11660: rate 0.000100, accuracy 94.1%, cross entropy 0.212230
INFO:tensorflow:Step #11670: rate 0.000100, accuracy 95.3%, cross entropy 0.164713
INFO:tensorflow:Step #11680: rate 0.000100, accuracy 91.8%, cross entropy 0.252939
INFO:tensorflow:Step #11690: rate 0.000100, accuracy 87.5%, cross entropy 0.324290
INFO:tensorflow:Step #11700: rate 0.000100, accuracy 91.0%, cross entropy 0.256458
INFO:tensorflow:Step #11710: rate 0.000100, accuracy 89.5%, cross entropy 0.319673
INFO:tensorflow:Step #11720: rate 0.000100, accuracy 93.0%, cross entropy 0.224728
INFO:tensorflow:Step #11730: rate 0.000100, accuracy 89.8%, cross entropy 0.289524
INFO:tensorflow:Step #11740: rate 0.000100, accuracy 92.2%, cross entropy 0.236899
INFO:tensorflow:Step #11750: rate 0.000100, accuracy 90.2%, cross entropy 0.289319
INFO:tensorflow:Step #11760: rate 0.000100, accuracy 89.5%, cross entropy 0.294255
INFO:tensorflow:Step #11770: rate 0.000100, accuracy 90.6%, cross entropy 0.261307
INFO:tensorflow:Step #11780: rate 0.000100, accuracy 94.1%, cross entropy 0.213022
INFO:tensorflow:Step #11790: rate 0.000100, accuracy 93.8%, cross entropy 0.211753
INFO:tensorflow:Step #11800: rate 0.000100, accuracy 91.8%, cross entropy 0.224855
INFO:tensorflow:Step #11810: rate 0.000100, accuracy 91.0%, cross entropy 0.263059
INFO:tensorflow:Step #11820: rate 0.000100, accuracy 91.4%, cross entropy 0.233967
INFO:tensorflow:Step #11830: rate 0.000100, accuracy 89.5%, cross entropy 0.299074
INFO:tensorflow:Step #11840: rate 0.000100, accuracy 85.9%, cross entropy 0.357667
INFO:tensorflow:Step #11850: rate 0.000100, accuracy 91.8%, cross entropy 0.228125
INFO:tensorflow:Step #11860: rate 0.000100, accuracy 90.6%, cross entropy 0.238990
INFO:tensorflow:Step #11870: rate 0.000100, accuracy 92.2%, cross entropy 0.269171
INFO:tensorflow:Step #11880: rate 0.000100, accuracy 92.2%, cross entropy 0.215334
INFO:tensorflow:Step #11890: rate 0.000100, accuracy 89.8%, cross entropy 0.312318
INFO:tensorflow:Step #11900: rate 0.000100, accuracy 91.8%, cross entropy 0.223212
INFO:tensorflow:Step #11910: rate 0.000100, accuracy 91.0%, cross entropy 0.261735
INFO:tensorflow:Step #11920: rate 0.000100, accuracy 89.8%, cross entropy 0.296969
INFO:tensorflow:Step #11930: rate 0.000100, accuracy 88.7%, cross entropy 0.358174
INFO:tensorflow:Step #11940: rate 0.000100, accuracy 93.4%, cross entropy 0.202030
INFO:tensorflow:Step #11950: rate 0.000100, accuracy 92.2%, cross entropy 0.206366
INFO:tensorflow:Step #11960: rate 0.000100, accuracy 93.8%, cross entropy 0.225796
INFO:tensorflow:Step #11970: rate 0.000100, accuracy 91.0%, cross entropy 0.278226
INFO:tensorflow:Step #11980: rate 0.000100, accuracy 94.1%, cross entropy 0.201598
INFO:tensorflow:Step #11990: rate 0.000100, accuracy 93.0%, cross entropy 0.250111
INFO:tensorflow:Step #12000: rate 0.000100, accuracy 90.2%, cross entropy 0.268662
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 213   5   6   2   3   1   8   5   3   4   8]
 [  0   0 250   6   2   0   2   0   1   0   0   0]
 [  0   2   1 256   1   2   1   0   0   0   0   7]
 [  0   4   0   0 245   0   0   1   0  10   0   0]
 [  0   0   1   6   0 253   0   0   0   0   1   3]
 [  0   1   9   4   1   0 231   1   0   0   0   0]
 [  0   5   0   1   1   0   2 247   0   0   0   0]
 [  0   4   0   0   2   1   0   4 243   3   0   0]
 [  0   1   0   1  16   0   0   0   5 231   1   1]
 [  0   1   0   0   5   0   0   2   0   2 233   3]
 [  0   5   0   8   6   4   0   2   0   2   2 231]]
INFO:tensorflow:Step 12000: Validation accuracy = 92.9% (N=2835)
INFO:tensorflow:Saving to "F:\ML_Project\Data\logs&checkpoint\c_rnn\ckpt-12000"
INFO:tensorflow:Step #12010: rate 0.000100, accuracy 92.2%, cross entropy 0.222830
INFO:tensorflow:Step #12020: rate 0.000100, accuracy 91.8%, cross entropy 0.203720
INFO:tensorflow:Step #12030: rate 0.000100, accuracy 90.2%, cross entropy 0.330216
INFO:tensorflow:Step #12040: rate 0.000100, accuracy 90.2%, cross entropy 0.283389
INFO:tensorflow:Step #12050: rate 0.000100, accuracy 93.4%, cross entropy 0.189392
INFO:tensorflow:Step #12060: rate 0.000100, accuracy 92.2%, cross entropy 0.204993
INFO:tensorflow:Step #12070: rate 0.000100, accuracy 94.1%, cross entropy 0.199861
INFO:tensorflow:Step #12080: rate 0.000100, accuracy 91.0%, cross entropy 0.253915
INFO:tensorflow:Step #12090: rate 0.000100, accuracy 94.1%, cross entropy 0.212913
INFO:tensorflow:Step #12100: rate 0.000100, accuracy 90.6%, cross entropy 0.264860
INFO:tensorflow:Step #12110: rate 0.000100, accuracy 91.0%, cross entropy 0.320974
INFO:tensorflow:Step #12120: rate 0.000100, accuracy 89.8%, cross entropy 0.261377
INFO:tensorflow:Step #12130: rate 0.000100, accuracy 92.2%, cross entropy 0.242783
INFO:tensorflow:Step #12140: rate 0.000100, accuracy 91.8%, cross entropy 0.218885
INFO:tensorflow:Step #12150: rate 0.000100, accuracy 92.6%, cross entropy 0.205414
INFO:tensorflow:Step #12160: rate 0.000100, accuracy 93.0%, cross entropy 0.218892
INFO:tensorflow:Step #12170: rate 0.000100, accuracy 91.4%, cross entropy 0.232504
INFO:tensorflow:Step #12180: rate 0.000100, accuracy 93.0%, cross entropy 0.201974
INFO:tensorflow:Step #12190: rate 0.000100, accuracy 93.0%, cross entropy 0.230010
INFO:tensorflow:Step #12200: rate 0.000100, accuracy 94.1%, cross entropy 0.236176
INFO:tensorflow:Step #12210: rate 0.000100, accuracy 89.5%, cross entropy 0.322936
INFO:tensorflow:Step #12220: rate 0.000100, accuracy 87.5%, cross entropy 0.352214
INFO:tensorflow:Step #12230: rate 0.000100, accuracy 92.2%, cross entropy 0.218664
INFO:tensorflow:Step #12240: rate 0.000100, accuracy 94.5%, cross entropy 0.197752
INFO:tensorflow:Step #12250: rate 0.000100, accuracy 92.6%, cross entropy 0.204759
INFO:tensorflow:Step #12260: rate 0.000100, accuracy 92.6%, cross entropy 0.217066
INFO:tensorflow:Step #12270: rate 0.000100, accuracy 89.8%, cross entropy 0.265907
INFO:tensorflow:Step #12280: rate 0.000100, accuracy 92.2%, cross entropy 0.224080
INFO:tensorflow:Step #12290: rate 0.000100, accuracy 93.4%, cross entropy 0.199855
INFO:tensorflow:Step #12300: rate 0.000100, accuracy 91.8%, cross entropy 0.303526
INFO:tensorflow:Step #12310: rate 0.000100, accuracy 90.6%, cross entropy 0.243910
INFO:tensorflow:Step #12320: rate 0.000100, accuracy 94.9%, cross entropy 0.140970
INFO:tensorflow:Step #12330: rate 0.000100, accuracy 93.8%, cross entropy 0.190396
INFO:tensorflow:Step #12340: rate 0.000100, accuracy 93.8%, cross entropy 0.173505
INFO:tensorflow:Step #12350: rate 0.000100, accuracy 89.8%, cross entropy 0.290541
INFO:tensorflow:Step #12360: rate 0.000100, accuracy 91.8%, cross entropy 0.248575
INFO:tensorflow:Step #12370: rate 0.000100, accuracy 92.6%, cross entropy 0.251537
INFO:tensorflow:Step #12380: rate 0.000100, accuracy 91.8%, cross entropy 0.274748
INFO:tensorflow:Step #12390: rate 0.000100, accuracy 88.7%, cross entropy 0.313703
INFO:tensorflow:Step #12400: rate 0.000100, accuracy 94.9%, cross entropy 0.157808
INFO:tensorflow:Step #12410: rate 0.000100, accuracy 92.6%, cross entropy 0.254451
INFO:tensorflow:Step #12420: rate 0.000100, accuracy 91.0%, cross entropy 0.225681
INFO:tensorflow:Step #12430: rate 0.000100, accuracy 91.4%, cross entropy 0.283374
INFO:tensorflow:Step #12440: rate 0.000100, accuracy 88.7%, cross entropy 0.342557
INFO:tensorflow:Step #12450: rate 0.000100, accuracy 91.8%, cross entropy 0.265235
INFO:tensorflow:Step #12460: rate 0.000100, accuracy 90.2%, cross entropy 0.282596
INFO:tensorflow:Step #12470: rate 0.000100, accuracy 92.2%, cross entropy 0.284907
INFO:tensorflow:Step #12480: rate 0.000100, accuracy 93.8%, cross entropy 0.196931
INFO:tensorflow:Step #12490: rate 0.000100, accuracy 90.6%, cross entropy 0.247106
INFO:tensorflow:Step #12500: rate 0.000100, accuracy 93.0%, cross entropy 0.238811
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 217   5   6   2   2   1   8   5   2   4   6]
 [  0   0 249   6   2   0   3   0   1   0   0   0]
 [  0   3   1 256   1   1   1   0   0   0   0   7]
 [  0   5   0   0 242   0   0   1   0  12   0   0]
 [  0   1   1   6   0 251   0   1   0   0   1   3]
 [  0   1   8   4   1   0 232   1   0   0   0   0]
 [  0   4   0   0   1   0   2 249   0   0   0   0]
 [  0   5   0   0   3   0   0   3 243   3   0   0]
 [  0   1   0   1  15   0   1   0   4 233   0   1]
 [  0   3   0   0   8   0   0   0   0   3 230   2]
 [  0   5   0   6   6   4   0   2   0   3   2 232]]
INFO:tensorflow:Step 12500: Validation accuracy = 92.9% (N=2835)
INFO:tensorflow:Step #12510: rate 0.000100, accuracy 93.8%, cross entropy 0.220402
INFO:tensorflow:Step #12520: rate 0.000100, accuracy 89.1%, cross entropy 0.280609
INFO:tensorflow:Step #12530: rate 0.000100, accuracy 91.4%, cross entropy 0.284919
INFO:tensorflow:Step #12540: rate 0.000100, accuracy 90.6%, cross entropy 0.303324
INFO:tensorflow:Step #12550: rate 0.000100, accuracy 90.2%, cross entropy 0.258475
INFO:tensorflow:Step #12560: rate 0.000100, accuracy 93.4%, cross entropy 0.175534
INFO:tensorflow:Step #12570: rate 0.000100, accuracy 89.5%, cross entropy 0.242515
INFO:tensorflow:Step #12580: rate 0.000100, accuracy 94.1%, cross entropy 0.222298
INFO:tensorflow:Step #12590: rate 0.000100, accuracy 91.8%, cross entropy 0.272190
INFO:tensorflow:Step #12600: rate 0.000100, accuracy 93.4%, cross entropy 0.210463
INFO:tensorflow:Step #12610: rate 0.000100, accuracy 91.4%, cross entropy 0.277071
INFO:tensorflow:Step #12620: rate 0.000100, accuracy 90.6%, cross entropy 0.268441
INFO:tensorflow:Step #12630: rate 0.000100, accuracy 93.8%, cross entropy 0.230596
INFO:tensorflow:Step #12640: rate 0.000100, accuracy 91.8%, cross entropy 0.197635
INFO:tensorflow:Step #12650: rate 0.000100, accuracy 92.6%, cross entropy 0.256116
INFO:tensorflow:Step #12660: rate 0.000100, accuracy 90.2%, cross entropy 0.287508
INFO:tensorflow:Step #12670: rate 0.000100, accuracy 90.2%, cross entropy 0.300710
INFO:tensorflow:Step #12680: rate 0.000100, accuracy 91.8%, cross entropy 0.250895
INFO:tensorflow:Step #12690: rate 0.000100, accuracy 91.8%, cross entropy 0.213487
INFO:tensorflow:Step #12700: rate 0.000100, accuracy 90.2%, cross entropy 0.310730
INFO:tensorflow:Step #12710: rate 0.000100, accuracy 92.2%, cross entropy 0.238911
INFO:tensorflow:Step #12720: rate 0.000100, accuracy 91.4%, cross entropy 0.241785
INFO:tensorflow:Step #12730: rate 0.000100, accuracy 95.7%, cross entropy 0.175246
INFO:tensorflow:Step #12740: rate 0.000100, accuracy 90.6%, cross entropy 0.254415
INFO:tensorflow:Step #12750: rate 0.000100, accuracy 92.6%, cross entropy 0.254400
INFO:tensorflow:Step #12760: rate 0.000100, accuracy 91.4%, cross entropy 0.224200
INFO:tensorflow:Step #12770: rate 0.000100, accuracy 91.8%, cross entropy 0.267909
INFO:tensorflow:Step #12780: rate 0.000100, accuracy 90.2%, cross entropy 0.303583
INFO:tensorflow:Step #12790: rate 0.000100, accuracy 91.8%, cross entropy 0.231916
INFO:tensorflow:Step #12800: rate 0.000100, accuracy 93.4%, cross entropy 0.253089
INFO:tensorflow:Step #12810: rate 0.000100, accuracy 90.6%, cross entropy 0.275888
INFO:tensorflow:Step #12820: rate 0.000100, accuracy 92.6%, cross entropy 0.262086
INFO:tensorflow:Step #12830: rate 0.000100, accuracy 93.8%, cross entropy 0.186938
INFO:tensorflow:Step #12840: rate 0.000100, accuracy 93.4%, cross entropy 0.161455
INFO:tensorflow:Step #12850: rate 0.000100, accuracy 90.2%, cross entropy 0.278795
INFO:tensorflow:Step #12860: rate 0.000100, accuracy 91.8%, cross entropy 0.272180
INFO:tensorflow:Step #12870: rate 0.000100, accuracy 91.8%, cross entropy 0.249726
INFO:tensorflow:Step #12880: rate 0.000100, accuracy 91.4%, cross entropy 0.267936
INFO:tensorflow:Step #12890: rate 0.000100, accuracy 91.8%, cross entropy 0.261938
INFO:tensorflow:Step #12900: rate 0.000100, accuracy 93.4%, cross entropy 0.199824
INFO:tensorflow:Step #12910: rate 0.000100, accuracy 91.4%, cross entropy 0.264261
INFO:tensorflow:Step #12920: rate 0.000100, accuracy 91.8%, cross entropy 0.251521
INFO:tensorflow:Step #12930: rate 0.000100, accuracy 91.4%, cross entropy 0.277997
INFO:tensorflow:Step #12940: rate 0.000100, accuracy 91.0%, cross entropy 0.206411
INFO:tensorflow:Step #12950: rate 0.000100, accuracy 90.6%, cross entropy 0.270949
INFO:tensorflow:Step #12960: rate 0.000100, accuracy 94.1%, cross entropy 0.177403
INFO:tensorflow:Step #12970: rate 0.000100, accuracy 93.0%, cross entropy 0.213878
INFO:tensorflow:Step #12980: rate 0.000100, accuracy 91.0%, cross entropy 0.288075
INFO:tensorflow:Step #12990: rate 0.000100, accuracy 90.6%, cross entropy 0.278875
INFO:tensorflow:Step #13000: rate 0.000100, accuracy 93.0%, cross entropy 0.225546
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 213   5   5   2   2   1   8   6   3   4   9]
 [  0   0 248   6   2   0   4   0   1   0   0   0]
 [  0   3   1 255   1   2   1   0   0   0   0   7]
 [  0   5   0   0 244   0   0   1   0  10   0   0]
 [  0   0   1   5   0 254   0   1   0   0   1   2]
 [  0   1   8   4   1   0 232   1   0   0   0   0]
 [  0   2   0   0   1   0   2 251   0   0   0   0]
 [  0   5   0   0   3   0   0   3 243   3   0   0]
 [  0   1   0   1  18   0   0   0   5 230   0   1]
 [  0   1   0   0   7   0   0   1   0   2 232   3]
 [  0   6   0   6   6   4   0   2   0   2   2 232]]
INFO:tensorflow:Step 13000: Validation accuracy = 92.9% (N=2835)
INFO:tensorflow:Step #13010: rate 0.000100, accuracy 92.6%, cross entropy 0.211824
INFO:tensorflow:Step #13020: rate 0.000100, accuracy 93.4%, cross entropy 0.196874
INFO:tensorflow:Step #13030: rate 0.000100, accuracy 96.1%, cross entropy 0.162197
INFO:tensorflow:Step #13040: rate 0.000100, accuracy 91.0%, cross entropy 0.261002
INFO:tensorflow:Step #13050: rate 0.000100, accuracy 90.6%, cross entropy 0.257441
INFO:tensorflow:Step #13060: rate 0.000100, accuracy 91.4%, cross entropy 0.286822
INFO:tensorflow:Step #13070: rate 0.000100, accuracy 91.0%, cross entropy 0.292008
INFO:tensorflow:Step #13080: rate 0.000100, accuracy 92.2%, cross entropy 0.238115
INFO:tensorflow:Step #13090: rate 0.000100, accuracy 93.4%, cross entropy 0.231402
INFO:tensorflow:Step #13100: rate 0.000100, accuracy 92.2%, cross entropy 0.220089
INFO:tensorflow:Step #13110: rate 0.000100, accuracy 92.6%, cross entropy 0.291164
INFO:tensorflow:Step #13120: rate 0.000100, accuracy 93.0%, cross entropy 0.205108
INFO:tensorflow:Step #13130: rate 0.000100, accuracy 91.8%, cross entropy 0.262767
INFO:tensorflow:Step #13140: rate 0.000100, accuracy 93.0%, cross entropy 0.253268
INFO:tensorflow:Step #13150: rate 0.000100, accuracy 89.5%, cross entropy 0.290047
INFO:tensorflow:Step #13160: rate 0.000100, accuracy 90.2%, cross entropy 0.281735
INFO:tensorflow:Step #13170: rate 0.000100, accuracy 93.0%, cross entropy 0.208354
INFO:tensorflow:Step #13180: rate 0.000100, accuracy 91.4%, cross entropy 0.299055
INFO:tensorflow:Step #13190: rate 0.000100, accuracy 91.4%, cross entropy 0.238345
INFO:tensorflow:Step #13200: rate 0.000100, accuracy 91.8%, cross entropy 0.234586
INFO:tensorflow:Step #13210: rate 0.000100, accuracy 87.5%, cross entropy 0.283271
INFO:tensorflow:Step #13220: rate 0.000100, accuracy 90.6%, cross entropy 0.268078
INFO:tensorflow:Step #13230: rate 0.000100, accuracy 89.8%, cross entropy 0.325373
INFO:tensorflow:Step #13240: rate 0.000100, accuracy 94.1%, cross entropy 0.207870
INFO:tensorflow:Step #13250: rate 0.000100, accuracy 92.6%, cross entropy 0.255622
INFO:tensorflow:Step #13260: rate 0.000100, accuracy 94.5%, cross entropy 0.183559
INFO:tensorflow:Step #13270: rate 0.000100, accuracy 90.6%, cross entropy 0.289387
INFO:tensorflow:Step #13280: rate 0.000100, accuracy 93.8%, cross entropy 0.238485
INFO:tensorflow:Step #13290: rate 0.000100, accuracy 92.2%, cross entropy 0.236404
INFO:tensorflow:Step #13300: rate 0.000100, accuracy 91.4%, cross entropy 0.219850
INFO:tensorflow:Step #13310: rate 0.000100, accuracy 92.6%, cross entropy 0.216199
INFO:tensorflow:Step #13320: rate 0.000100, accuracy 91.4%, cross entropy 0.264641
INFO:tensorflow:Step #13330: rate 0.000100, accuracy 92.6%, cross entropy 0.221089
INFO:tensorflow:Step #13340: rate 0.000100, accuracy 93.4%, cross entropy 0.213478
INFO:tensorflow:Step #13350: rate 0.000100, accuracy 91.8%, cross entropy 0.246167
INFO:tensorflow:Step #13360: rate 0.000100, accuracy 91.0%, cross entropy 0.281984
INFO:tensorflow:Step #13370: rate 0.000100, accuracy 94.1%, cross entropy 0.176762
INFO:tensorflow:Step #13380: rate 0.000100, accuracy 89.8%, cross entropy 0.326763
INFO:tensorflow:Step #13390: rate 0.000100, accuracy 91.8%, cross entropy 0.268330
INFO:tensorflow:Step #13400: rate 0.000100, accuracy 90.6%, cross entropy 0.290411
INFO:tensorflow:Step #13410: rate 0.000100, accuracy 93.0%, cross entropy 0.242418
INFO:tensorflow:Step #13420: rate 0.000100, accuracy 90.6%, cross entropy 0.269993
INFO:tensorflow:Step #13430: rate 0.000100, accuracy 89.1%, cross entropy 0.278290
INFO:tensorflow:Step #13440: rate 0.000100, accuracy 92.2%, cross entropy 0.224259
INFO:tensorflow:Step #13450: rate 0.000100, accuracy 90.2%, cross entropy 0.270185
INFO:tensorflow:Step #13460: rate 0.000100, accuracy 91.4%, cross entropy 0.310519
INFO:tensorflow:Step #13470: rate 0.000100, accuracy 92.2%, cross entropy 0.250803
INFO:tensorflow:Step #13480: rate 0.000100, accuracy 92.2%, cross entropy 0.280020
INFO:tensorflow:Step #13490: rate 0.000100, accuracy 91.4%, cross entropy 0.240390
INFO:tensorflow:Step #13500: rate 0.000100, accuracy 92.6%, cross entropy 0.214214
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 216   5   4   4   2   0   8   6   2   4   7]
 [  0   0 248   6   3   0   4   0   0   0   0   0]
 [  0   2   1 255   1   2   1   0   0   0   0   8]
 [  0   5   0   0 248   0   0   0   0   7   0   0]
 [  0   1   1   4   0 253   0   1   0   0   1   3]
 [  0   1   9   4   1   0 231   1   0   0   0   0]
 [  0   3   0   0   2   0   2 249   0   0   0   0]
 [  0   4   0   0   5   0   0   1 244   3   0   0]
 [  0   1   0   1  20   0   0   0   3 230   0   1]
 [  0   2   0   0   8   0   0   0   0   2 231   3]
 [  0   5   0   4   7   4   0   1   0   3   2 234]]
INFO:tensorflow:Step 13500: Validation accuracy = 93.1% (N=2835)
INFO:tensorflow:Step #13510: rate 0.000100, accuracy 89.8%, cross entropy 0.315563
INFO:tensorflow:Step #13520: rate 0.000100, accuracy 91.0%, cross entropy 0.282936
INFO:tensorflow:Step #13530: rate 0.000100, accuracy 96.5%, cross entropy 0.145895
INFO:tensorflow:Step #13540: rate 0.000100, accuracy 92.6%, cross entropy 0.216227
INFO:tensorflow:Step #13550: rate 0.000100, accuracy 93.4%, cross entropy 0.219496
INFO:tensorflow:Step #13560: rate 0.000100, accuracy 91.0%, cross entropy 0.255796
INFO:tensorflow:Step #13570: rate 0.000100, accuracy 91.4%, cross entropy 0.272986
INFO:tensorflow:Step #13580: rate 0.000100, accuracy 96.1%, cross entropy 0.157191
INFO:tensorflow:Step #13590: rate 0.000100, accuracy 91.4%, cross entropy 0.199195
INFO:tensorflow:Step #13600: rate 0.000100, accuracy 90.6%, cross entropy 0.281058
INFO:tensorflow:Step #13610: rate 0.000100, accuracy 91.8%, cross entropy 0.231385
INFO:tensorflow:Step #13620: rate 0.000100, accuracy 88.7%, cross entropy 0.349769
INFO:tensorflow:Step #13630: rate 0.000100, accuracy 89.8%, cross entropy 0.263263
INFO:tensorflow:Step #13640: rate 0.000100, accuracy 91.8%, cross entropy 0.230877
INFO:tensorflow:Step #13650: rate 0.000100, accuracy 92.6%, cross entropy 0.221903
INFO:tensorflow:Step #13660: rate 0.000100, accuracy 89.5%, cross entropy 0.271193
INFO:tensorflow:Step #13670: rate 0.000100, accuracy 87.1%, cross entropy 0.368893
INFO:tensorflow:Step #13680: rate 0.000100, accuracy 92.2%, cross entropy 0.226995
INFO:tensorflow:Step #13690: rate 0.000100, accuracy 91.8%, cross entropy 0.244743
INFO:tensorflow:Step #13700: rate 0.000100, accuracy 90.6%, cross entropy 0.277215
INFO:tensorflow:Step #13710: rate 0.000100, accuracy 91.0%, cross entropy 0.260863
INFO:tensorflow:Step #13720: rate 0.000100, accuracy 92.2%, cross entropy 0.209477
INFO:tensorflow:Step #13730: rate 0.000100, accuracy 93.4%, cross entropy 0.209576
INFO:tensorflow:Step #13740: rate 0.000100, accuracy 93.4%, cross entropy 0.181998
INFO:tensorflow:Step #13750: rate 0.000100, accuracy 92.2%, cross entropy 0.222703
INFO:tensorflow:Step #13760: rate 0.000100, accuracy 91.4%, cross entropy 0.282166
INFO:tensorflow:Step #13770: rate 0.000100, accuracy 89.5%, cross entropy 0.298971
INFO:tensorflow:Step #13780: rate 0.000100, accuracy 92.2%, cross entropy 0.220533
INFO:tensorflow:Step #13790: rate 0.000100, accuracy 93.0%, cross entropy 0.210710
INFO:tensorflow:Step #13800: rate 0.000100, accuracy 93.4%, cross entropy 0.216399
INFO:tensorflow:Step #13810: rate 0.000100, accuracy 91.4%, cross entropy 0.256114
INFO:tensorflow:Step #13820: rate 0.000100, accuracy 94.9%, cross entropy 0.152870
INFO:tensorflow:Step #13830: rate 0.000100, accuracy 96.1%, cross entropy 0.164303
INFO:tensorflow:Step #13840: rate 0.000100, accuracy 95.7%, cross entropy 0.123130
INFO:tensorflow:Step #13850: rate 0.000100, accuracy 93.8%, cross entropy 0.177248
INFO:tensorflow:Step #13860: rate 0.000100, accuracy 94.1%, cross entropy 0.191545
INFO:tensorflow:Step #13870: rate 0.000100, accuracy 90.6%, cross entropy 0.241558
INFO:tensorflow:Step #13880: rate 0.000100, accuracy 91.4%, cross entropy 0.236905
INFO:tensorflow:Step #13890: rate 0.000100, accuracy 93.0%, cross entropy 0.243522
INFO:tensorflow:Step #13900: rate 0.000100, accuracy 90.6%, cross entropy 0.323556
INFO:tensorflow:Step #13910: rate 0.000100, accuracy 88.7%, cross entropy 0.362657
INFO:tensorflow:Step #13920: rate 0.000100, accuracy 92.6%, cross entropy 0.197498
INFO:tensorflow:Step #13930: rate 0.000100, accuracy 89.1%, cross entropy 0.248042
INFO:tensorflow:Step #13940: rate 0.000100, accuracy 94.1%, cross entropy 0.230104
INFO:tensorflow:Step #13950: rate 0.000100, accuracy 94.1%, cross entropy 0.206735
INFO:tensorflow:Step #13960: rate 0.000100, accuracy 92.6%, cross entropy 0.260366
INFO:tensorflow:Step #13970: rate 0.000100, accuracy 94.5%, cross entropy 0.207694
INFO:tensorflow:Step #13980: rate 0.000100, accuracy 90.6%, cross entropy 0.310928
INFO:tensorflow:Step #13990: rate 0.000100, accuracy 90.6%, cross entropy 0.241962
INFO:tensorflow:Step #14000: rate 0.000100, accuracy 91.8%, cross entropy 0.224321
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 220   5   5   3   1   1   7   4   3   4   5]
 [  0   0 251   6   2   0   1   0   0   1   0   0]
 [  0   2   1 256   1   2   1   0   0   0   0   7]
 [  0   5   0   0 243   0   0   0   0  12   0   0]
 [  0   0   1   6   0 255   0   0   0   0   0   2]
 [  0   1   9   4   1   0 231   1   0   0   0   0]
 [  0   3   0   0   2   0   2 249   0   0   0   0]
 [  0   5   0   0   5   1   0   1 242   3   0   0]
 [  0   1   0   1  16   0   1   0   4 232   0   1]
 [  0   2   0   0   7   0   0   0   0   3 231   3]
 [  0   6   0   6   7   4   0   1   0   3   2 231]]
INFO:tensorflow:Step 14000: Validation accuracy = 93.2% (N=2835)
INFO:tensorflow:Saving to "F:\ML_Project\Data\logs&checkpoint\c_rnn\ckpt-14000"
INFO:tensorflow:Step #14010: rate 0.000100, accuracy 92.6%, cross entropy 0.239405
INFO:tensorflow:Step #14020: rate 0.000100, accuracy 93.0%, cross entropy 0.250970
INFO:tensorflow:Step #14030: rate 0.000100, accuracy 93.0%, cross entropy 0.196855
INFO:tensorflow:Step #14040: rate 0.000100, accuracy 92.2%, cross entropy 0.300949
INFO:tensorflow:Step #14050: rate 0.000100, accuracy 91.0%, cross entropy 0.277419
INFO:tensorflow:Step #14060: rate 0.000100, accuracy 95.3%, cross entropy 0.198664
INFO:tensorflow:Step #14070: rate 0.000100, accuracy 93.0%, cross entropy 0.227366
INFO:tensorflow:Step #14080: rate 0.000100, accuracy 94.1%, cross entropy 0.158040
INFO:tensorflow:Step #14090: rate 0.000100, accuracy 94.1%, cross entropy 0.205020
INFO:tensorflow:Step #14100: rate 0.000100, accuracy 93.4%, cross entropy 0.200852
INFO:tensorflow:Step #14110: rate 0.000100, accuracy 93.8%, cross entropy 0.241846
INFO:tensorflow:Step #14120: rate 0.000100, accuracy 91.4%, cross entropy 0.270319
INFO:tensorflow:Step #14130: rate 0.000100, accuracy 93.0%, cross entropy 0.212264
INFO:tensorflow:Step #14140: rate 0.000100, accuracy 92.6%, cross entropy 0.272494
INFO:tensorflow:Step #14150: rate 0.000100, accuracy 92.6%, cross entropy 0.199719
INFO:tensorflow:Step #14160: rate 0.000100, accuracy 91.8%, cross entropy 0.262232
INFO:tensorflow:Step #14170: rate 0.000100, accuracy 93.8%, cross entropy 0.211445
INFO:tensorflow:Step #14180: rate 0.000100, accuracy 91.4%, cross entropy 0.267536
INFO:tensorflow:Step #14190: rate 0.000100, accuracy 94.1%, cross entropy 0.196638
INFO:tensorflow:Step #14200: rate 0.000100, accuracy 92.2%, cross entropy 0.272260
INFO:tensorflow:Step #14210: rate 0.000100, accuracy 90.2%, cross entropy 0.276106
INFO:tensorflow:Step #14220: rate 0.000100, accuracy 91.8%, cross entropy 0.260927
INFO:tensorflow:Step #14230: rate 0.000100, accuracy 90.2%, cross entropy 0.261311
INFO:tensorflow:Step #14240: rate 0.000100, accuracy 90.2%, cross entropy 0.264622
INFO:tensorflow:Step #14250: rate 0.000100, accuracy 91.0%, cross entropy 0.259313
INFO:tensorflow:Step #14260: rate 0.000100, accuracy 93.0%, cross entropy 0.200443
INFO:tensorflow:Step #14270: rate 0.000100, accuracy 90.6%, cross entropy 0.296479
INFO:tensorflow:Step #14280: rate 0.000100, accuracy 90.2%, cross entropy 0.301659
INFO:tensorflow:Step #14290: rate 0.000100, accuracy 92.2%, cross entropy 0.260715
INFO:tensorflow:Step #14300: rate 0.000100, accuracy 87.9%, cross entropy 0.342013
INFO:tensorflow:Step #14310: rate 0.000100, accuracy 95.3%, cross entropy 0.136199
INFO:tensorflow:Step #14320: rate 0.000100, accuracy 91.8%, cross entropy 0.270515
INFO:tensorflow:Step #14330: rate 0.000100, accuracy 92.6%, cross entropy 0.222087
INFO:tensorflow:Step #14340: rate 0.000100, accuracy 89.8%, cross entropy 0.264926
INFO:tensorflow:Step #14350: rate 0.000100, accuracy 94.1%, cross entropy 0.161835
INFO:tensorflow:Step #14360: rate 0.000100, accuracy 94.5%, cross entropy 0.213336
INFO:tensorflow:Step #14370: rate 0.000100, accuracy 94.9%, cross entropy 0.219392
INFO:tensorflow:Step #14380: rate 0.000100, accuracy 91.8%, cross entropy 0.280763
INFO:tensorflow:Step #14390: rate 0.000100, accuracy 91.4%, cross entropy 0.297016
INFO:tensorflow:Step #14400: rate 0.000100, accuracy 91.8%, cross entropy 0.246711
INFO:tensorflow:Step #14410: rate 0.000100, accuracy 94.9%, cross entropy 0.193156
INFO:tensorflow:Step #14420: rate 0.000100, accuracy 94.1%, cross entropy 0.150624
INFO:tensorflow:Step #14430: rate 0.000100, accuracy 92.6%, cross entropy 0.211944
INFO:tensorflow:Step #14440: rate 0.000100, accuracy 90.2%, cross entropy 0.286529
INFO:tensorflow:Step #14450: rate 0.000100, accuracy 91.4%, cross entropy 0.243758
INFO:tensorflow:Step #14460: rate 0.000100, accuracy 92.6%, cross entropy 0.230838
INFO:tensorflow:Step #14470: rate 0.000100, accuracy 91.8%, cross entropy 0.229203
INFO:tensorflow:Step #14480: rate 0.000100, accuracy 91.4%, cross entropy 0.229765
INFO:tensorflow:Step #14490: rate 0.000100, accuracy 93.0%, cross entropy 0.208063
INFO:tensorflow:Step #14500: rate 0.000100, accuracy 94.1%, cross entropy 0.194796
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 216   6   5   2   2   1   8   5   3   4   6]
 [  0   0 249   6   2   0   3   0   1   0   0   0]
 [  0   2   1 258   1   2   0   0   0   0   0   6]
 [  0   5   0   0 248   0   0   0   0   7   0   0]
 [  0   1   1   6   0 252   0   0   0   0   1   3]
 [  0   2   7   4   1   0 232   1   0   0   0   0]
 [  0   3   0   0   1   0   2 250   0   0   0   0]
 [  0   5   0   0   4   1   0   1 242   4   0   0]
 [  0   1   0   1  17   0   0   0   4 232   0   1]
 [  0   2   0   0   8   0   0   0   0   1 232   3]
 [  0   5   0   8   6   4   0   1   0   3   2 231]]
INFO:tensorflow:Step 14500: Validation accuracy = 93.2% (N=2835)
INFO:tensorflow:Step #14510: rate 0.000100, accuracy 93.8%, cross entropy 0.184405
INFO:tensorflow:Step #14520: rate 0.000100, accuracy 92.2%, cross entropy 0.240811
INFO:tensorflow:Step #14530: rate 0.000100, accuracy 90.6%, cross entropy 0.303227
INFO:tensorflow:Step #14540: rate 0.000100, accuracy 93.4%, cross entropy 0.195436
INFO:tensorflow:Step #14550: rate 0.000100, accuracy 91.4%, cross entropy 0.247822
INFO:tensorflow:Step #14560: rate 0.000100, accuracy 93.8%, cross entropy 0.205146
INFO:tensorflow:Step #14570: rate 0.000100, accuracy 90.2%, cross entropy 0.292927
INFO:tensorflow:Step #14580: rate 0.000100, accuracy 91.0%, cross entropy 0.242560
INFO:tensorflow:Step #14590: rate 0.000100, accuracy 92.6%, cross entropy 0.247427
INFO:tensorflow:Step #14600: rate 0.000100, accuracy 92.2%, cross entropy 0.194743
INFO:tensorflow:Step #14610: rate 0.000100, accuracy 88.3%, cross entropy 0.312447
INFO:tensorflow:Step #14620: rate 0.000100, accuracy 93.0%, cross entropy 0.200063
INFO:tensorflow:Step #14630: rate 0.000100, accuracy 92.6%, cross entropy 0.218615
INFO:tensorflow:Step #14640: rate 0.000100, accuracy 87.5%, cross entropy 0.358889
INFO:tensorflow:Step #14650: rate 0.000100, accuracy 89.8%, cross entropy 0.281955
INFO:tensorflow:Step #14660: rate 0.000100, accuracy 90.6%, cross entropy 0.274736
INFO:tensorflow:Step #14670: rate 0.000100, accuracy 91.4%, cross entropy 0.305282
INFO:tensorflow:Step #14680: rate 0.000100, accuracy 91.8%, cross entropy 0.254835
INFO:tensorflow:Step #14690: rate 0.000100, accuracy 93.8%, cross entropy 0.210784
INFO:tensorflow:Step #14700: rate 0.000100, accuracy 93.0%, cross entropy 0.228787
INFO:tensorflow:Step #14710: rate 0.000100, accuracy 92.6%, cross entropy 0.244230
INFO:tensorflow:Step #14720: rate 0.000100, accuracy 95.3%, cross entropy 0.162811
INFO:tensorflow:Step #14730: rate 0.000100, accuracy 90.2%, cross entropy 0.255394
INFO:tensorflow:Step #14740: rate 0.000100, accuracy 89.5%, cross entropy 0.310361
INFO:tensorflow:Step #14750: rate 0.000100, accuracy 93.0%, cross entropy 0.204647
INFO:tensorflow:Step #14760: rate 0.000100, accuracy 89.8%, cross entropy 0.293084
INFO:tensorflow:Step #14770: rate 0.000100, accuracy 91.0%, cross entropy 0.250498
INFO:tensorflow:Step #14780: rate 0.000100, accuracy 93.0%, cross entropy 0.208708
INFO:tensorflow:Step #14790: rate 0.000100, accuracy 92.2%, cross entropy 0.245581
INFO:tensorflow:Step #14800: rate 0.000100, accuracy 89.1%, cross entropy 0.349332
INFO:tensorflow:Step #14810: rate 0.000100, accuracy 90.6%, cross entropy 0.322809
INFO:tensorflow:Step #14820: rate 0.000100, accuracy 89.1%, cross entropy 0.303854
INFO:tensorflow:Step #14830: rate 0.000100, accuracy 93.8%, cross entropy 0.212763
INFO:tensorflow:Step #14840: rate 0.000100, accuracy 93.4%, cross entropy 0.190029
INFO:tensorflow:Step #14850: rate 0.000100, accuracy 93.0%, cross entropy 0.201567
INFO:tensorflow:Step #14860: rate 0.000100, accuracy 91.0%, cross entropy 0.267960
INFO:tensorflow:Step #14870: rate 0.000100, accuracy 91.8%, cross entropy 0.249452
INFO:tensorflow:Step #14880: rate 0.000100, accuracy 92.6%, cross entropy 0.221348
INFO:tensorflow:Step #14890: rate 0.000100, accuracy 89.8%, cross entropy 0.285263
INFO:tensorflow:Step #14900: rate 0.000100, accuracy 92.6%, cross entropy 0.280474
INFO:tensorflow:Step #14910: rate 0.000100, accuracy 89.8%, cross entropy 0.324932
INFO:tensorflow:Step #14920: rate 0.000100, accuracy 93.0%, cross entropy 0.198117
INFO:tensorflow:Step #14930: rate 0.000100, accuracy 92.6%, cross entropy 0.222565
INFO:tensorflow:Step #14940: rate 0.000100, accuracy 90.2%, cross entropy 0.257381
INFO:tensorflow:Step #14950: rate 0.000100, accuracy 93.4%, cross entropy 0.245257
INFO:tensorflow:Step #14960: rate 0.000100, accuracy 91.0%, cross entropy 0.271198
INFO:tensorflow:Step #14970: rate 0.000100, accuracy 88.3%, cross entropy 0.317487
INFO:tensorflow:Step #14980: rate 0.000100, accuracy 92.6%, cross entropy 0.251198
INFO:tensorflow:Step #14990: rate 0.000100, accuracy 89.5%, cross entropy 0.301714
INFO:tensorflow:Step #15000: rate 0.000100, accuracy 91.8%, cross entropy 0.240437
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 205   6   8   3   3   1   7   6   4   4  11]
 [  0   0 248   6   2   0   4   0   0   1   0   0]
 [  0   2   1 257   1   1   1   0   0   0   0   7]
 [  0   5   0   0 244   0   0   0   0  11   0   0]
 [  0   0   1   5   0 253   0   0   0   0   1   4]
 [  0   1   7   4   1   0 233   1   0   0   0   0]
 [  0   4   0   1   1   0   2 248   0   0   0   0]
 [  0   4   0   0   5   0   0   1 244   3   0   0]
 [  0   1   0   1  16   0   0   0   6 231   0   1]
 [  0   1   0   0   7   1   0   0   0   3 231   3]
 [  0   3   0   6   7   4   0   1   0   3   2 234]]
INFO:tensorflow:Step 15000: Validation accuracy = 92.7% (N=2835)
INFO:tensorflow:Step #15010: rate 0.000100, accuracy 93.8%, cross entropy 0.216028
INFO:tensorflow:Step #15020: rate 0.000100, accuracy 92.6%, cross entropy 0.217522
INFO:tensorflow:Step #15030: rate 0.000100, accuracy 93.0%, cross entropy 0.220190
INFO:tensorflow:Step #15040: rate 0.000100, accuracy 91.4%, cross entropy 0.206444
INFO:tensorflow:Step #15050: rate 0.000100, accuracy 90.6%, cross entropy 0.255100
INFO:tensorflow:Step #15060: rate 0.000100, accuracy 92.2%, cross entropy 0.206454
INFO:tensorflow:Step #15070: rate 0.000100, accuracy 92.2%, cross entropy 0.291511
INFO:tensorflow:Step #15080: rate 0.000100, accuracy 93.8%, cross entropy 0.198626
INFO:tensorflow:Step #15090: rate 0.000100, accuracy 88.7%, cross entropy 0.345909
INFO:tensorflow:Step #15100: rate 0.000100, accuracy 91.4%, cross entropy 0.267429
INFO:tensorflow:Step #15110: rate 0.000100, accuracy 91.4%, cross entropy 0.232044
INFO:tensorflow:Step #15120: rate 0.000100, accuracy 91.4%, cross entropy 0.242169
INFO:tensorflow:Step #15130: rate 0.000100, accuracy 89.5%, cross entropy 0.320727
INFO:tensorflow:Step #15140: rate 0.000100, accuracy 91.8%, cross entropy 0.237339
INFO:tensorflow:Step #15150: rate 0.000100, accuracy 94.1%, cross entropy 0.231002
INFO:tensorflow:Step #15160: rate 0.000100, accuracy 90.2%, cross entropy 0.305604
INFO:tensorflow:Step #15170: rate 0.000100, accuracy 93.0%, cross entropy 0.214083
INFO:tensorflow:Step #15180: rate 0.000100, accuracy 91.8%, cross entropy 0.232435
INFO:tensorflow:Step #15190: rate 0.000100, accuracy 91.4%, cross entropy 0.226908
INFO:tensorflow:Step #15200: rate 0.000100, accuracy 92.6%, cross entropy 0.239458
INFO:tensorflow:Step #15210: rate 0.000100, accuracy 91.8%, cross entropy 0.262823
INFO:tensorflow:Step #15220: rate 0.000100, accuracy 92.2%, cross entropy 0.216220
INFO:tensorflow:Step #15230: rate 0.000100, accuracy 94.9%, cross entropy 0.169325
INFO:tensorflow:Step #15240: rate 0.000100, accuracy 93.4%, cross entropy 0.188419
INFO:tensorflow:Step #15250: rate 0.000100, accuracy 89.8%, cross entropy 0.299557
INFO:tensorflow:Step #15260: rate 0.000100, accuracy 92.6%, cross entropy 0.231014
INFO:tensorflow:Step #15270: rate 0.000100, accuracy 91.0%, cross entropy 0.319880
INFO:tensorflow:Step #15280: rate 0.000100, accuracy 93.0%, cross entropy 0.202994
INFO:tensorflow:Step #15290: rate 0.000100, accuracy 93.0%, cross entropy 0.240779
INFO:tensorflow:Step #15300: rate 0.000100, accuracy 92.2%, cross entropy 0.279004
INFO:tensorflow:Step #15310: rate 0.000100, accuracy 94.1%, cross entropy 0.180642
INFO:tensorflow:Step #15320: rate 0.000100, accuracy 92.2%, cross entropy 0.205489
INFO:tensorflow:Step #15330: rate 0.000100, accuracy 90.2%, cross entropy 0.275993
INFO:tensorflow:Step #15340: rate 0.000100, accuracy 94.1%, cross entropy 0.150184
INFO:tensorflow:Step #15350: rate 0.000100, accuracy 89.8%, cross entropy 0.287901
INFO:tensorflow:Step #15360: rate 0.000100, accuracy 94.9%, cross entropy 0.170615
INFO:tensorflow:Step #15370: rate 0.000100, accuracy 92.2%, cross entropy 0.244188
INFO:tensorflow:Step #15380: rate 0.000100, accuracy 92.2%, cross entropy 0.225668
INFO:tensorflow:Step #15390: rate 0.000100, accuracy 92.6%, cross entropy 0.244177
INFO:tensorflow:Step #15400: rate 0.000100, accuracy 90.2%, cross entropy 0.316746
INFO:tensorflow:Step #15410: rate 0.000100, accuracy 92.6%, cross entropy 0.241078
INFO:tensorflow:Step #15420: rate 0.000100, accuracy 91.8%, cross entropy 0.233490
INFO:tensorflow:Step #15430: rate 0.000100, accuracy 91.4%, cross entropy 0.244346
INFO:tensorflow:Step #15440: rate 0.000100, accuracy 93.8%, cross entropy 0.162146
INFO:tensorflow:Step #15450: rate 0.000100, accuracy 90.6%, cross entropy 0.305663
INFO:tensorflow:Step #15460: rate 0.000100, accuracy 93.4%, cross entropy 0.215291
INFO:tensorflow:Step #15470: rate 0.000100, accuracy 92.2%, cross entropy 0.223826
INFO:tensorflow:Step #15480: rate 0.000100, accuracy 93.8%, cross entropy 0.184732
INFO:tensorflow:Step #15490: rate 0.000100, accuracy 94.1%, cross entropy 0.224944
INFO:tensorflow:Step #15500: rate 0.000100, accuracy 89.8%, cross entropy 0.339920
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 213   6   7   2   2   2   7   6   4   3   6]
 [  0   0 249   6   2   0   3   0   0   1   0   0]
 [  0   2   1 257   1   1   1   0   0   0   0   7]
 [  0   4   0   0 246   0   0   0   0  10   0   0]
 [  0   1   1   7   0 252   0   0   0   0   0   3]
 [  0   1   8   4   1   0 232   1   0   0   0   0]
 [  0   4   0   0   1   0   2 249   0   0   0   0]
 [  0   4   0   0   4   1   0   1 243   4   0   0]
 [  0   1   0   1  20   0   0   0   6 227   0   1]
 [  0   2   0   0   7   0   0   0   0   4 230   3]
 [  0   7   0   6   6   4   0   1   0   3   2 231]]
INFO:tensorflow:Step 15500: Validation accuracy = 92.7% (N=2835)
INFO:tensorflow:Step #15510: rate 0.000100, accuracy 91.0%, cross entropy 0.285249
INFO:tensorflow:Step #15520: rate 0.000100, accuracy 92.6%, cross entropy 0.203223
INFO:tensorflow:Step #15530: rate 0.000100, accuracy 91.0%, cross entropy 0.279730
INFO:tensorflow:Step #15540: rate 0.000100, accuracy 92.6%, cross entropy 0.219841
INFO:tensorflow:Step #15550: rate 0.000100, accuracy 93.4%, cross entropy 0.171394
INFO:tensorflow:Step #15560: rate 0.000100, accuracy 91.4%, cross entropy 0.248497
INFO:tensorflow:Step #15570: rate 0.000100, accuracy 91.8%, cross entropy 0.268160
INFO:tensorflow:Step #15580: rate 0.000100, accuracy 87.9%, cross entropy 0.290988
INFO:tensorflow:Step #15590: rate 0.000100, accuracy 92.2%, cross entropy 0.264935
INFO:tensorflow:Step #15600: rate 0.000100, accuracy 93.4%, cross entropy 0.202197
INFO:tensorflow:Step #15610: rate 0.000100, accuracy 92.2%, cross entropy 0.216922
INFO:tensorflow:Step #15620: rate 0.000100, accuracy 89.8%, cross entropy 0.290714
INFO:tensorflow:Step #15630: rate 0.000100, accuracy 91.8%, cross entropy 0.291239
INFO:tensorflow:Step #15640: rate 0.000100, accuracy 92.2%, cross entropy 0.247549
INFO:tensorflow:Step #15650: rate 0.000100, accuracy 91.4%, cross entropy 0.278592
INFO:tensorflow:Step #15660: rate 0.000100, accuracy 93.8%, cross entropy 0.187373
INFO:tensorflow:Step #15670: rate 0.000100, accuracy 88.7%, cross entropy 0.293907
INFO:tensorflow:Step #15680: rate 0.000100, accuracy 91.0%, cross entropy 0.250976
INFO:tensorflow:Step #15690: rate 0.000100, accuracy 88.7%, cross entropy 0.272802
INFO:tensorflow:Step #15700: rate 0.000100, accuracy 93.8%, cross entropy 0.182358
INFO:tensorflow:Step #15710: rate 0.000100, accuracy 91.8%, cross entropy 0.265343
INFO:tensorflow:Step #15720: rate 0.000100, accuracy 91.0%, cross entropy 0.257316
INFO:tensorflow:Step #15730: rate 0.000100, accuracy 93.4%, cross entropy 0.195428
INFO:tensorflow:Step #15740: rate 0.000100, accuracy 91.0%, cross entropy 0.210849
INFO:tensorflow:Step #15750: rate 0.000100, accuracy 94.5%, cross entropy 0.253282
INFO:tensorflow:Step #15760: rate 0.000100, accuracy 93.4%, cross entropy 0.206988
INFO:tensorflow:Step #15770: rate 0.000100, accuracy 93.8%, cross entropy 0.217473
INFO:tensorflow:Step #15780: rate 0.000100, accuracy 90.6%, cross entropy 0.258732
INFO:tensorflow:Step #15790: rate 0.000100, accuracy 93.4%, cross entropy 0.169422
INFO:tensorflow:Step #15800: rate 0.000100, accuracy 93.4%, cross entropy 0.191931
INFO:tensorflow:Step #15810: rate 0.000100, accuracy 90.2%, cross entropy 0.298680
INFO:tensorflow:Step #15820: rate 0.000100, accuracy 90.2%, cross entropy 0.293388
INFO:tensorflow:Step #15830: rate 0.000100, accuracy 91.4%, cross entropy 0.249061
INFO:tensorflow:Step #15840: rate 0.000100, accuracy 92.2%, cross entropy 0.233469
INFO:tensorflow:Step #15850: rate 0.000100, accuracy 94.5%, cross entropy 0.156993
INFO:tensorflow:Step #15860: rate 0.000100, accuracy 91.4%, cross entropy 0.252723
INFO:tensorflow:Step #15870: rate 0.000100, accuracy 91.0%, cross entropy 0.264160
INFO:tensorflow:Step #15880: rate 0.000100, accuracy 93.0%, cross entropy 0.184015
INFO:tensorflow:Step #15890: rate 0.000100, accuracy 94.1%, cross entropy 0.220883
INFO:tensorflow:Step #15900: rate 0.000100, accuracy 95.7%, cross entropy 0.135418
INFO:tensorflow:Step #15910: rate 0.000100, accuracy 90.6%, cross entropy 0.256622
INFO:tensorflow:Step #15920: rate 0.000100, accuracy 89.5%, cross entropy 0.303060
INFO:tensorflow:Step #15930: rate 0.000100, accuracy 94.9%, cross entropy 0.188013
INFO:tensorflow:Step #15940: rate 0.000100, accuracy 90.2%, cross entropy 0.282821
INFO:tensorflow:Step #15950: rate 0.000100, accuracy 91.0%, cross entropy 0.258346
INFO:tensorflow:Step #15960: rate 0.000100, accuracy 91.8%, cross entropy 0.242873
INFO:tensorflow:Step #15970: rate 0.000100, accuracy 93.4%, cross entropy 0.200021
INFO:tensorflow:Step #15980: rate 0.000100, accuracy 89.5%, cross entropy 0.306789
INFO:tensorflow:Step #15990: rate 0.000100, accuracy 91.4%, cross entropy 0.250346
INFO:tensorflow:Step #16000: rate 0.000100, accuracy 91.8%, cross entropy 0.296233
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 217   7   5   3   2   0   6   6   2   4   6]
 [  0   0 250   6   2   0   2   0   0   1   0   0]
 [  0   2   1 257   1   2   1   0   0   0   0   6]
 [  0   5   0   0 244   0   0   0   0  11   0   0]
 [  0   1   1   6   0 250   0   1   0   0   1   4]
 [  0   2  11   4   1   0 228   1   0   0   0   0]
 [  0   5   0   0   1   0   2 248   0   0   0   0]
 [  0   6   0   0   5   1   0   1 241   3   0   0]
 [  0   1   0   1  18   0   0   0   7 227   1   1]
 [  0   3   0   0   8   0   0   0   0   2 230   3]
 [  0   6   0   5   7   4   0   1   0   2   2 233]]
INFO:tensorflow:Step 16000: Validation accuracy = 92.6% (N=2835)
INFO:tensorflow:Saving to "F:\ML_Project\Data\logs&checkpoint\c_rnn\ckpt-16000"
INFO:tensorflow:Step #16010: rate 0.000100, accuracy 93.8%, cross entropy 0.181076
INFO:tensorflow:Step #16020: rate 0.000100, accuracy 91.8%, cross entropy 0.226186
INFO:tensorflow:Step #16030: rate 0.000100, accuracy 92.2%, cross entropy 0.258960
INFO:tensorflow:Step #16040: rate 0.000100, accuracy 93.0%, cross entropy 0.266706
INFO:tensorflow:Step #16050: rate 0.000100, accuracy 91.4%, cross entropy 0.223388
INFO:tensorflow:Step #16060: rate 0.000100, accuracy 90.6%, cross entropy 0.273988
INFO:tensorflow:Step #16070: rate 0.000100, accuracy 93.0%, cross entropy 0.242471
INFO:tensorflow:Step #16080: rate 0.000100, accuracy 93.0%, cross entropy 0.178144
INFO:tensorflow:Step #16090: rate 0.000100, accuracy 92.6%, cross entropy 0.192367
INFO:tensorflow:Step #16100: rate 0.000100, accuracy 91.4%, cross entropy 0.256478
INFO:tensorflow:Step #16110: rate 0.000100, accuracy 94.1%, cross entropy 0.210333
INFO:tensorflow:Step #16120: rate 0.000100, accuracy 91.4%, cross entropy 0.249506
INFO:tensorflow:Step #16130: rate 0.000100, accuracy 90.2%, cross entropy 0.262012
INFO:tensorflow:Step #16140: rate 0.000100, accuracy 94.5%, cross entropy 0.148043
INFO:tensorflow:Step #16150: rate 0.000100, accuracy 89.1%, cross entropy 0.310797
INFO:tensorflow:Step #16160: rate 0.000100, accuracy 92.6%, cross entropy 0.207691
INFO:tensorflow:Step #16170: rate 0.000100, accuracy 93.4%, cross entropy 0.154082
INFO:tensorflow:Step #16180: rate 0.000100, accuracy 87.5%, cross entropy 0.349291
INFO:tensorflow:Step #16190: rate 0.000100, accuracy 92.6%, cross entropy 0.186453
INFO:tensorflow:Step #16200: rate 0.000100, accuracy 88.7%, cross entropy 0.286523
INFO:tensorflow:Step #16210: rate 0.000100, accuracy 88.7%, cross entropy 0.276574
INFO:tensorflow:Step #16220: rate 0.000100, accuracy 91.4%, cross entropy 0.236639
INFO:tensorflow:Step #16230: rate 0.000100, accuracy 90.6%, cross entropy 0.294962
INFO:tensorflow:Step #16240: rate 0.000100, accuracy 93.8%, cross entropy 0.181118
INFO:tensorflow:Step #16250: rate 0.000100, accuracy 91.8%, cross entropy 0.227219
INFO:tensorflow:Step #16260: rate 0.000100, accuracy 94.1%, cross entropy 0.189057
INFO:tensorflow:Step #16270: rate 0.000100, accuracy 94.5%, cross entropy 0.203037
INFO:tensorflow:Step #16280: rate 0.000100, accuracy 91.0%, cross entropy 0.271446
INFO:tensorflow:Step #16290: rate 0.000100, accuracy 92.2%, cross entropy 0.275473
INFO:tensorflow:Step #16300: rate 0.000100, accuracy 91.4%, cross entropy 0.279744
INFO:tensorflow:Step #16310: rate 0.000100, accuracy 92.6%, cross entropy 0.220300
INFO:tensorflow:Step #16320: rate 0.000100, accuracy 94.5%, cross entropy 0.212878
INFO:tensorflow:Step #16330: rate 0.000100, accuracy 92.2%, cross entropy 0.229971
INFO:tensorflow:Step #16340: rate 0.000100, accuracy 91.8%, cross entropy 0.267725
INFO:tensorflow:Step #16350: rate 0.000100, accuracy 92.6%, cross entropy 0.205406
INFO:tensorflow:Step #16360: rate 0.000100, accuracy 90.2%, cross entropy 0.325401
INFO:tensorflow:Step #16370: rate 0.000100, accuracy 93.4%, cross entropy 0.212201
INFO:tensorflow:Step #16380: rate 0.000100, accuracy 92.6%, cross entropy 0.236893
INFO:tensorflow:Step #16390: rate 0.000100, accuracy 91.8%, cross entropy 0.249751
INFO:tensorflow:Step #16400: rate 0.000100, accuracy 91.0%, cross entropy 0.256999
INFO:tensorflow:Step #16410: rate 0.000100, accuracy 89.8%, cross entropy 0.279457
INFO:tensorflow:Step #16420: rate 0.000100, accuracy 91.4%, cross entropy 0.247577
INFO:tensorflow:Step #16430: rate 0.000100, accuracy 91.8%, cross entropy 0.291512
INFO:tensorflow:Step #16440: rate 0.000100, accuracy 92.2%, cross entropy 0.225072
INFO:tensorflow:Step #16450: rate 0.000100, accuracy 94.1%, cross entropy 0.244552
INFO:tensorflow:Step #16460: rate 0.000100, accuracy 93.0%, cross entropy 0.224426
INFO:tensorflow:Step #16470: rate 0.000100, accuracy 89.8%, cross entropy 0.282357
INFO:tensorflow:Step #16480: rate 0.000100, accuracy 92.6%, cross entropy 0.221232
INFO:tensorflow:Step #16490: rate 0.000100, accuracy 92.2%, cross entropy 0.222330
INFO:tensorflow:Step #16500: rate 0.000100, accuracy 91.8%, cross entropy 0.259473
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 215   6   6   2   2   1   7   6   4   4   5]
 [  0   0 250   6   2   0   2   0   0   1   0   0]
 [  0   2   1 259   1   1   0   0   0   0   0   6]
 [  0   4   0   0 242   0   0   0   0  13   1   0]
 [  0   0   1   7   0 251   1   0   1   0   1   2]
 [  0   1  11   4   1   0 229   1   0   0   0   0]
 [  0   4   0   1   1   0   2 248   0   0   0   0]
 [  0   5   0   0   4   0   0   1 242   5   0   0]
 [  0   1   0   1  15   0   0   0   4 234   0   1]
 [  0   3   0   0   7   0   0   0   0   4 229   3]
 [  0   6   0   6   6   4   0   1   0   4   2 231]]
INFO:tensorflow:Step 16500: Validation accuracy = 92.8% (N=2835)
INFO:tensorflow:Step #16510: rate 0.000100, accuracy 90.6%, cross entropy 0.256883
INFO:tensorflow:Step #16520: rate 0.000100, accuracy 89.5%, cross entropy 0.298141
INFO:tensorflow:Step #16530: rate 0.000100, accuracy 90.6%, cross entropy 0.289385
INFO:tensorflow:Step #16540: rate 0.000100, accuracy 93.8%, cross entropy 0.176848
INFO:tensorflow:Step #16550: rate 0.000100, accuracy 91.8%, cross entropy 0.240018
INFO:tensorflow:Step #16560: rate 0.000100, accuracy 92.6%, cross entropy 0.213626
INFO:tensorflow:Step #16570: rate 0.000100, accuracy 93.0%, cross entropy 0.226064
INFO:tensorflow:Step #16580: rate 0.000100, accuracy 91.0%, cross entropy 0.250075
INFO:tensorflow:Step #16590: rate 0.000100, accuracy 96.1%, cross entropy 0.156937
INFO:tensorflow:Step #16600: rate 0.000100, accuracy 92.6%, cross entropy 0.210011
INFO:tensorflow:Step #16610: rate 0.000100, accuracy 92.6%, cross entropy 0.270394
INFO:tensorflow:Step #16620: rate 0.000100, accuracy 92.2%, cross entropy 0.285834
INFO:tensorflow:Step #16630: rate 0.000100, accuracy 94.5%, cross entropy 0.185466
INFO:tensorflow:Step #16640: rate 0.000100, accuracy 90.6%, cross entropy 0.245775
INFO:tensorflow:Step #16650: rate 0.000100, accuracy 94.5%, cross entropy 0.162907
INFO:tensorflow:Step #16660: rate 0.000100, accuracy 93.8%, cross entropy 0.179997
INFO:tensorflow:Step #16670: rate 0.000100, accuracy 91.0%, cross entropy 0.261533
INFO:tensorflow:Step #16680: rate 0.000100, accuracy 90.2%, cross entropy 0.281502
INFO:tensorflow:Step #16690: rate 0.000100, accuracy 90.6%, cross entropy 0.278844
INFO:tensorflow:Step #16700: rate 0.000100, accuracy 93.8%, cross entropy 0.185162
INFO:tensorflow:Step #16710: rate 0.000100, accuracy 92.6%, cross entropy 0.221618
INFO:tensorflow:Step #16720: rate 0.000100, accuracy 93.8%, cross entropy 0.219774
INFO:tensorflow:Step #16730: rate 0.000100, accuracy 91.4%, cross entropy 0.240424
INFO:tensorflow:Step #16740: rate 0.000100, accuracy 92.2%, cross entropy 0.267636
INFO:tensorflow:Step #16750: rate 0.000100, accuracy 92.6%, cross entropy 0.231756
INFO:tensorflow:Step #16760: rate 0.000100, accuracy 91.0%, cross entropy 0.244119
INFO:tensorflow:Step #16770: rate 0.000100, accuracy 92.2%, cross entropy 0.190415
INFO:tensorflow:Step #16780: rate 0.000100, accuracy 93.4%, cross entropy 0.228397
INFO:tensorflow:Step #16790: rate 0.000100, accuracy 91.4%, cross entropy 0.233340
INFO:tensorflow:Step #16800: rate 0.000100, accuracy 91.4%, cross entropy 0.223574
INFO:tensorflow:Step #16810: rate 0.000100, accuracy 94.1%, cross entropy 0.218914
INFO:tensorflow:Step #16820: rate 0.000100, accuracy 91.0%, cross entropy 0.244403
INFO:tensorflow:Step #16830: rate 0.000100, accuracy 91.0%, cross entropy 0.235015
INFO:tensorflow:Step #16840: rate 0.000100, accuracy 91.0%, cross entropy 0.280339
INFO:tensorflow:Step #16850: rate 0.000100, accuracy 93.4%, cross entropy 0.222116
INFO:tensorflow:Step #16860: rate 0.000100, accuracy 91.0%, cross entropy 0.273280
INFO:tensorflow:Step #16870: rate 0.000100, accuracy 92.2%, cross entropy 0.245285
INFO:tensorflow:Step #16880: rate 0.000100, accuracy 92.6%, cross entropy 0.328480
INFO:tensorflow:Step #16890: rate 0.000100, accuracy 93.4%, cross entropy 0.220316
INFO:tensorflow:Step #16900: rate 0.000100, accuracy 90.6%, cross entropy 0.269663
INFO:tensorflow:Step #16910: rate 0.000100, accuracy 92.6%, cross entropy 0.270028
INFO:tensorflow:Step #16920: rate 0.000100, accuracy 95.3%, cross entropy 0.135403
INFO:tensorflow:Step #16930: rate 0.000100, accuracy 93.0%, cross entropy 0.274575
INFO:tensorflow:Step #16940: rate 0.000100, accuracy 93.4%, cross entropy 0.227375
INFO:tensorflow:Step #16950: rate 0.000100, accuracy 93.4%, cross entropy 0.234530
INFO:tensorflow:Step #16960: rate 0.000100, accuracy 91.8%, cross entropy 0.222388
INFO:tensorflow:Step #16970: rate 0.000100, accuracy 91.8%, cross entropy 0.210310
INFO:tensorflow:Step #16980: rate 0.000100, accuracy 90.6%, cross entropy 0.247698
INFO:tensorflow:Step #16990: rate 0.000100, accuracy 95.7%, cross entropy 0.165088
INFO:tensorflow:Step #17000: rate 0.000100, accuracy 90.6%, cross entropy 0.282622
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 213   7   8   3   2   2   7   5   3   3   5]
 [  0   0 250   6   2   0   2   0   0   1   0   0]
 [  0   2   1 258   1   1   1   0   0   0   0   6]
 [  0   5   0   0 247   0   0   0   0   8   0   0]
 [  0   0   1   8   0 251   0   1   0   0   0   3]
 [  0   1  12   4   1   0 228   1   0   0   0   0]
 [  0   4   0   1   1   0   2 248   0   0   0   0]
 [  0   6   0   0   5   1   0   1 240   4   0   0]
 [  0   1   0   1  18   0   0   0   4 230   1   1]
 [  0   3   0   1   8   0   0   0   0   1 230   3]
 [  0   6   1   5   7   4   0   1   0   2   2 232]]
INFO:tensorflow:Step 17000: Validation accuracy = 92.7% (N=2835)
INFO:tensorflow:Step #17010: rate 0.000100, accuracy 91.0%, cross entropy 0.269057
INFO:tensorflow:Step #17020: rate 0.000100, accuracy 91.4%, cross entropy 0.279205
INFO:tensorflow:Step #17030: rate 0.000100, accuracy 93.0%, cross entropy 0.187156
INFO:tensorflow:Step #17040: rate 0.000100, accuracy 92.2%, cross entropy 0.219278
INFO:tensorflow:Step #17050: rate 0.000100, accuracy 93.0%, cross entropy 0.201227
INFO:tensorflow:Step #17060: rate 0.000100, accuracy 93.4%, cross entropy 0.190784
INFO:tensorflow:Step #17070: rate 0.000100, accuracy 91.4%, cross entropy 0.225089
INFO:tensorflow:Step #17080: rate 0.000100, accuracy 91.4%, cross entropy 0.203098
INFO:tensorflow:Step #17090: rate 0.000100, accuracy 92.6%, cross entropy 0.225185
INFO:tensorflow:Step #17100: rate 0.000100, accuracy 96.1%, cross entropy 0.137492
INFO:tensorflow:Step #17110: rate 0.000100, accuracy 90.6%, cross entropy 0.297238
INFO:tensorflow:Step #17120: rate 0.000100, accuracy 91.4%, cross entropy 0.294608
INFO:tensorflow:Step #17130: rate 0.000100, accuracy 92.6%, cross entropy 0.235129
INFO:tensorflow:Step #17140: rate 0.000100, accuracy 90.2%, cross entropy 0.306972
INFO:tensorflow:Step #17150: rate 0.000100, accuracy 93.0%, cross entropy 0.196060
INFO:tensorflow:Step #17160: rate 0.000100, accuracy 93.0%, cross entropy 0.213928
INFO:tensorflow:Step #17170: rate 0.000100, accuracy 94.5%, cross entropy 0.198399
INFO:tensorflow:Step #17180: rate 0.000100, accuracy 94.9%, cross entropy 0.173100
INFO:tensorflow:Step #17190: rate 0.000100, accuracy 91.8%, cross entropy 0.254139
INFO:tensorflow:Step #17200: rate 0.000100, accuracy 93.0%, cross entropy 0.250233
INFO:tensorflow:Step #17210: rate 0.000100, accuracy 90.6%, cross entropy 0.270636
INFO:tensorflow:Step #17220: rate 0.000100, accuracy 91.8%, cross entropy 0.239161
INFO:tensorflow:Step #17230: rate 0.000100, accuracy 91.8%, cross entropy 0.246436
INFO:tensorflow:Step #17240: rate 0.000100, accuracy 94.5%, cross entropy 0.151440
INFO:tensorflow:Step #17250: rate 0.000100, accuracy 92.6%, cross entropy 0.200961
INFO:tensorflow:Step #17260: rate 0.000100, accuracy 91.0%, cross entropy 0.240918
INFO:tensorflow:Step #17270: rate 0.000100, accuracy 93.4%, cross entropy 0.204915
INFO:tensorflow:Step #17280: rate 0.000100, accuracy 91.0%, cross entropy 0.295742
INFO:tensorflow:Step #17290: rate 0.000100, accuracy 91.0%, cross entropy 0.268962
INFO:tensorflow:Step #17300: rate 0.000100, accuracy 94.5%, cross entropy 0.187054
INFO:tensorflow:Step #17310: rate 0.000100, accuracy 92.2%, cross entropy 0.225159
INFO:tensorflow:Step #17320: rate 0.000100, accuracy 92.6%, cross entropy 0.244748
INFO:tensorflow:Step #17330: rate 0.000100, accuracy 89.5%, cross entropy 0.282180
INFO:tensorflow:Step #17340: rate 0.000100, accuracy 93.0%, cross entropy 0.184872
INFO:tensorflow:Step #17350: rate 0.000100, accuracy 91.4%, cross entropy 0.240598
INFO:tensorflow:Step #17360: rate 0.000100, accuracy 93.0%, cross entropy 0.191587
INFO:tensorflow:Step #17370: rate 0.000100, accuracy 91.4%, cross entropy 0.295604
INFO:tensorflow:Step #17380: rate 0.000100, accuracy 94.9%, cross entropy 0.179350
INFO:tensorflow:Step #17390: rate 0.000100, accuracy 89.8%, cross entropy 0.302691
INFO:tensorflow:Step #17400: rate 0.000100, accuracy 90.2%, cross entropy 0.256015
INFO:tensorflow:Step #17410: rate 0.000100, accuracy 93.4%, cross entropy 0.166659
INFO:tensorflow:Step #17420: rate 0.000100, accuracy 94.1%, cross entropy 0.186683
INFO:tensorflow:Step #17430: rate 0.000100, accuracy 92.2%, cross entropy 0.260529
INFO:tensorflow:Step #17440: rate 0.000100, accuracy 93.8%, cross entropy 0.178565
INFO:tensorflow:Step #17450: rate 0.000100, accuracy 93.8%, cross entropy 0.254407
INFO:tensorflow:Step #17460: rate 0.000100, accuracy 88.3%, cross entropy 0.293355
INFO:tensorflow:Step #17470: rate 0.000100, accuracy 93.8%, cross entropy 0.178436
INFO:tensorflow:Step #17480: rate 0.000100, accuracy 91.4%, cross entropy 0.251368
INFO:tensorflow:Step #17490: rate 0.000100, accuracy 91.0%, cross entropy 0.256045
INFO:tensorflow:Step #17500: rate 0.000100, accuracy 94.5%, cross entropy 0.187292
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 219   6   6   2   2   1   7   4   3   4   4]
 [  0   0 250   6   2   0   2   1   0   0   0   0]
 [  0   2   1 257   1   2   1   0   0   0   0   6]
 [  0   5   0   0 243   0   0   1   0  11   0   0]
 [  0   0   1   8   0 251   0   0   1   0   1   2]
 [  0   2   8   4   1   0 231   1   0   0   0   0]
 [  0   6   0   1   1   0   2 246   0   0   0   0]
 [  0   6   0   0   5   1   0   1 240   4   0   0]
 [  0   1   0   1  15   0   0   0   4 233   1   1]
 [  0   3   0   0   7   0   1   0   0   3 231   1]
 [  0   6   0   6   7   4   0   1   0   2   2 232]]
INFO:tensorflow:Step 17500: Validation accuracy = 92.9% (N=2835)
INFO:tensorflow:Step #17510: rate 0.000100, accuracy 96.1%, cross entropy 0.119543
INFO:tensorflow:Step #17520: rate 0.000100, accuracy 90.6%, cross entropy 0.249053
INFO:tensorflow:Step #17530: rate 0.000100, accuracy 94.5%, cross entropy 0.165344
INFO:tensorflow:Step #17540: rate 0.000100, accuracy 90.6%, cross entropy 0.244279
INFO:tensorflow:Step #17550: rate 0.000100, accuracy 88.7%, cross entropy 0.298513
INFO:tensorflow:Step #17560: rate 0.000100, accuracy 94.5%, cross entropy 0.191878
INFO:tensorflow:Step #17570: rate 0.000100, accuracy 89.1%, cross entropy 0.353409
INFO:tensorflow:Step #17580: rate 0.000100, accuracy 94.1%, cross entropy 0.179001
INFO:tensorflow:Step #17590: rate 0.000100, accuracy 93.0%, cross entropy 0.193460
INFO:tensorflow:Step #17600: rate 0.000100, accuracy 91.4%, cross entropy 0.272825
INFO:tensorflow:Step #17610: rate 0.000100, accuracy 93.0%, cross entropy 0.239850
INFO:tensorflow:Step #17620: rate 0.000100, accuracy 89.8%, cross entropy 0.256658
INFO:tensorflow:Step #17630: rate 0.000100, accuracy 93.4%, cross entropy 0.177825
INFO:tensorflow:Step #17640: rate 0.000100, accuracy 94.5%, cross entropy 0.173309
INFO:tensorflow:Step #17650: rate 0.000100, accuracy 91.0%, cross entropy 0.260434
INFO:tensorflow:Step #17660: rate 0.000100, accuracy 90.2%, cross entropy 0.240556
INFO:tensorflow:Step #17670: rate 0.000100, accuracy 90.2%, cross entropy 0.260729
INFO:tensorflow:Step #17680: rate 0.000100, accuracy 92.2%, cross entropy 0.262160
INFO:tensorflow:Step #17690: rate 0.000100, accuracy 91.8%, cross entropy 0.234324
INFO:tensorflow:Step #17700: rate 0.000100, accuracy 92.6%, cross entropy 0.233821
INFO:tensorflow:Step #17710: rate 0.000100, accuracy 92.2%, cross entropy 0.224503
INFO:tensorflow:Step #17720: rate 0.000100, accuracy 93.0%, cross entropy 0.203462
INFO:tensorflow:Step #17730: rate 0.000100, accuracy 89.8%, cross entropy 0.296301
INFO:tensorflow:Step #17740: rate 0.000100, accuracy 93.0%, cross entropy 0.229391
INFO:tensorflow:Step #17750: rate 0.000100, accuracy 95.7%, cross entropy 0.144261
INFO:tensorflow:Step #17760: rate 0.000100, accuracy 90.6%, cross entropy 0.253474
INFO:tensorflow:Step #17770: rate 0.000100, accuracy 93.0%, cross entropy 0.159744
INFO:tensorflow:Step #17780: rate 0.000100, accuracy 90.6%, cross entropy 0.261918
INFO:tensorflow:Step #17790: rate 0.000100, accuracy 91.8%, cross entropy 0.287696
INFO:tensorflow:Step #17800: rate 0.000100, accuracy 93.8%, cross entropy 0.226476
INFO:tensorflow:Step #17810: rate 0.000100, accuracy 93.4%, cross entropy 0.238125
INFO:tensorflow:Step #17820: rate 0.000100, accuracy 93.4%, cross entropy 0.192536
INFO:tensorflow:Step #17830: rate 0.000100, accuracy 92.2%, cross entropy 0.206053
INFO:tensorflow:Step #17840: rate 0.000100, accuracy 91.8%, cross entropy 0.220773
INFO:tensorflow:Step #17850: rate 0.000100, accuracy 93.0%, cross entropy 0.203480
INFO:tensorflow:Step #17860: rate 0.000100, accuracy 94.1%, cross entropy 0.169694
INFO:tensorflow:Step #17870: rate 0.000100, accuracy 90.2%, cross entropy 0.289261
INFO:tensorflow:Step #17880: rate 0.000100, accuracy 93.8%, cross entropy 0.199807
INFO:tensorflow:Step #17890: rate 0.000100, accuracy 93.8%, cross entropy 0.230227
INFO:tensorflow:Step #17900: rate 0.000100, accuracy 91.8%, cross entropy 0.257234
INFO:tensorflow:Step #17910: rate 0.000100, accuracy 93.0%, cross entropy 0.222460
INFO:tensorflow:Step #17920: rate 0.000100, accuracy 94.1%, cross entropy 0.180073
INFO:tensorflow:Step #17930: rate 0.000100, accuracy 87.5%, cross entropy 0.349511
INFO:tensorflow:Step #17940: rate 0.000100, accuracy 91.4%, cross entropy 0.258494
INFO:tensorflow:Step #17950: rate 0.000100, accuracy 92.2%, cross entropy 0.256271
INFO:tensorflow:Step #17960: rate 0.000100, accuracy 91.8%, cross entropy 0.226147
INFO:tensorflow:Step #17970: rate 0.000100, accuracy 91.4%, cross entropy 0.213671
INFO:tensorflow:Step #17980: rate 0.000100, accuracy 91.8%, cross entropy 0.273385
INFO:tensorflow:Step #17990: rate 0.000100, accuracy 93.0%, cross entropy 0.264122
INFO:tensorflow:Step #18000: rate 0.000100, accuracy 93.4%, cross entropy 0.195701
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 214   5   7   2   2   1   8   5   3   5   6]
 [  0   0 250   6   2   0   2   0   1   0   0   0]
 [  0   2   1 259   1   1   1   0   0   0   0   5]
 [  0   5   0   0 241   0   0   0   0  13   1   0]
 [  0   0   1   7   0 252   0   0   1   0   1   2]
 [  0   1   8   4   1   0 232   1   0   0   0   0]
 [  0   5   0   1   1   0   2 247   0   0   0   0]
 [  0   5   0   0   3   0   0   2 243   4   0   0]
 [  0   1   0   1  12   0   0   0   5 235   1   1]
 [  0   2   0   1   7   0   1   0   0   3 229   3]
 [  0   7   0   8   7   4   0   1   0   2   2 229]]
INFO:tensorflow:Step 18000: Validation accuracy = 92.8% (N=2835)
INFO:tensorflow:Saving to "F:\ML_Project\Data\logs&checkpoint\c_rnn\ckpt-18000"
INFO:tensorflow:Step #18010: rate 0.000100, accuracy 92.6%, cross entropy 0.211017
INFO:tensorflow:Step #18020: rate 0.000100, accuracy 89.5%, cross entropy 0.280403
INFO:tensorflow:Step #18030: rate 0.000100, accuracy 91.8%, cross entropy 0.226205
INFO:tensorflow:Step #18040: rate 0.000100, accuracy 90.6%, cross entropy 0.261173
INFO:tensorflow:Step #18050: rate 0.000100, accuracy 91.0%, cross entropy 0.266978
INFO:tensorflow:Step #18060: rate 0.000100, accuracy 94.5%, cross entropy 0.167025
INFO:tensorflow:Step #18070: rate 0.000100, accuracy 90.6%, cross entropy 0.270716
INFO:tensorflow:Step #18080: rate 0.000100, accuracy 92.2%, cross entropy 0.214581
INFO:tensorflow:Step #18090: rate 0.000100, accuracy 89.8%, cross entropy 0.339442
INFO:tensorflow:Step #18100: rate 0.000100, accuracy 91.0%, cross entropy 0.261796
INFO:tensorflow:Step #18110: rate 0.000100, accuracy 90.6%, cross entropy 0.253479
INFO:tensorflow:Step #18120: rate 0.000100, accuracy 92.6%, cross entropy 0.256492
INFO:tensorflow:Step #18130: rate 0.000100, accuracy 92.2%, cross entropy 0.213114
INFO:tensorflow:Step #18140: rate 0.000100, accuracy 93.0%, cross entropy 0.224753
INFO:tensorflow:Step #18150: rate 0.000100, accuracy 93.8%, cross entropy 0.191691
INFO:tensorflow:Step #18160: rate 0.000100, accuracy 92.2%, cross entropy 0.226742
INFO:tensorflow:Step #18170: rate 0.000100, accuracy 93.0%, cross entropy 0.205302
INFO:tensorflow:Step #18180: rate 0.000100, accuracy 93.0%, cross entropy 0.199060
INFO:tensorflow:Step #18190: rate 0.000100, accuracy 91.8%, cross entropy 0.207176
INFO:tensorflow:Step #18200: rate 0.000100, accuracy 91.4%, cross entropy 0.257514
INFO:tensorflow:Step #18210: rate 0.000100, accuracy 93.8%, cross entropy 0.199702
INFO:tensorflow:Step #18220: rate 0.000100, accuracy 93.4%, cross entropy 0.246298
INFO:tensorflow:Step #18230: rate 0.000100, accuracy 92.2%, cross entropy 0.237486
INFO:tensorflow:Step #18240: rate 0.000100, accuracy 92.6%, cross entropy 0.204502
INFO:tensorflow:Step #18250: rate 0.000100, accuracy 89.1%, cross entropy 0.294413
INFO:tensorflow:Step #18260: rate 0.000100, accuracy 91.0%, cross entropy 0.273077
INFO:tensorflow:Step #18270: rate 0.000100, accuracy 90.2%, cross entropy 0.274281
INFO:tensorflow:Step #18280: rate 0.000100, accuracy 93.0%, cross entropy 0.216994
INFO:tensorflow:Step #18290: rate 0.000100, accuracy 94.1%, cross entropy 0.156811
INFO:tensorflow:Step #18300: rate 0.000100, accuracy 92.2%, cross entropy 0.235193
INFO:tensorflow:Step #18310: rate 0.000100, accuracy 92.6%, cross entropy 0.228132
INFO:tensorflow:Step #18320: rate 0.000100, accuracy 91.4%, cross entropy 0.238711
INFO:tensorflow:Step #18330: rate 0.000100, accuracy 94.9%, cross entropy 0.148597
INFO:tensorflow:Step #18340: rate 0.000100, accuracy 88.7%, cross entropy 0.340194
INFO:tensorflow:Step #18350: rate 0.000100, accuracy 93.4%, cross entropy 0.181186
INFO:tensorflow:Step #18360: rate 0.000100, accuracy 93.8%, cross entropy 0.176973
INFO:tensorflow:Step #18370: rate 0.000100, accuracy 92.6%, cross entropy 0.197169
INFO:tensorflow:Step #18380: rate 0.000100, accuracy 93.8%, cross entropy 0.244813
INFO:tensorflow:Step #18390: rate 0.000100, accuracy 94.9%, cross entropy 0.172426
INFO:tensorflow:Step #18400: rate 0.000100, accuracy 91.4%, cross entropy 0.249682
INFO:tensorflow:Step #18410: rate 0.000100, accuracy 94.1%, cross entropy 0.187022
INFO:tensorflow:Step #18420: rate 0.000100, accuracy 91.8%, cross entropy 0.249675
INFO:tensorflow:Step #18430: rate 0.000100, accuracy 92.6%, cross entropy 0.245816
INFO:tensorflow:Step #18440: rate 0.000100, accuracy 92.6%, cross entropy 0.287044
INFO:tensorflow:Step #18450: rate 0.000100, accuracy 93.4%, cross entropy 0.206284
INFO:tensorflow:Step #18460: rate 0.000100, accuracy 95.3%, cross entropy 0.133314
INFO:tensorflow:Step #18470: rate 0.000100, accuracy 93.8%, cross entropy 0.194169
INFO:tensorflow:Step #18480: rate 0.000100, accuracy 91.0%, cross entropy 0.235962
INFO:tensorflow:Step #18490: rate 0.000100, accuracy 91.4%, cross entropy 0.228207
INFO:tensorflow:Step #18500: rate 0.000100, accuracy 92.6%, cross entropy 0.181793
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 215   6   5   2   2   2   7   6   3   4   6]
 [  0   0 250   6   2   0   2   0   0   1   0   0]
 [  0   2   1 259   1   1   1   0   0   0   0   5]
 [  0   5   0   0 242   0   0   0   0  12   1   0]
 [  0   0   1   6   0 252   0   0   1   0   1   3]
 [  0   1  11   4   1   0 229   1   0   0   0   0]
 [  0   5   0   0   1   0   2 248   0   0   0   0]
 [  0   5   0   0   2   0   0   2 241   7   0   0]
 [  0   1   0   1  18   0   0   0   4 231   0   1]
 [  0   1   0   0   5   1   1   0   0   5 230   3]
 [  0   4   0   8   6   4   0   1   0   4   2 231]]
INFO:tensorflow:Step 18500: Validation accuracy = 92.7% (N=2835)
INFO:tensorflow:Step #18510: rate 0.000100, accuracy 91.4%, cross entropy 0.277130
INFO:tensorflow:Step #18520: rate 0.000100, accuracy 89.8%, cross entropy 0.283526
INFO:tensorflow:Step #18530: rate 0.000100, accuracy 93.8%, cross entropy 0.191722
INFO:tensorflow:Step #18540: rate 0.000100, accuracy 92.2%, cross entropy 0.213389
INFO:tensorflow:Step #18550: rate 0.000100, accuracy 92.6%, cross entropy 0.258180
INFO:tensorflow:Step #18560: rate 0.000100, accuracy 91.8%, cross entropy 0.227471
INFO:tensorflow:Step #18570: rate 0.000100, accuracy 90.6%, cross entropy 0.253265
INFO:tensorflow:Step #18580: rate 0.000100, accuracy 92.6%, cross entropy 0.190946
INFO:tensorflow:Step #18590: rate 0.000100, accuracy 91.0%, cross entropy 0.234167
INFO:tensorflow:Step #18600: rate 0.000100, accuracy 93.0%, cross entropy 0.178747
INFO:tensorflow:Step #18610: rate 0.000100, accuracy 93.0%, cross entropy 0.226063
INFO:tensorflow:Step #18620: rate 0.000100, accuracy 93.4%, cross entropy 0.225451
INFO:tensorflow:Step #18630: rate 0.000100, accuracy 88.7%, cross entropy 0.348956
INFO:tensorflow:Step #18640: rate 0.000100, accuracy 89.1%, cross entropy 0.290816
INFO:tensorflow:Step #18650: rate 0.000100, accuracy 94.1%, cross entropy 0.210609
INFO:tensorflow:Step #18660: rate 0.000100, accuracy 93.4%, cross entropy 0.198391
INFO:tensorflow:Step #18670: rate 0.000100, accuracy 93.4%, cross entropy 0.177944
INFO:tensorflow:Step #18680: rate 0.000100, accuracy 90.2%, cross entropy 0.284197
INFO:tensorflow:Step #18690: rate 0.000100, accuracy 95.3%, cross entropy 0.163676
INFO:tensorflow:Step #18700: rate 0.000100, accuracy 90.2%, cross entropy 0.310510
INFO:tensorflow:Step #18710: rate 0.000100, accuracy 93.0%, cross entropy 0.226667
INFO:tensorflow:Step #18720: rate 0.000100, accuracy 89.8%, cross entropy 0.321372
INFO:tensorflow:Step #18730: rate 0.000100, accuracy 94.1%, cross entropy 0.193825
INFO:tensorflow:Step #18740: rate 0.000100, accuracy 90.2%, cross entropy 0.253761
INFO:tensorflow:Step #18750: rate 0.000100, accuracy 90.6%, cross entropy 0.289268
INFO:tensorflow:Step #18760: rate 0.000100, accuracy 91.0%, cross entropy 0.304210
INFO:tensorflow:Step #18770: rate 0.000100, accuracy 89.5%, cross entropy 0.262058
INFO:tensorflow:Step #18780: rate 0.000100, accuracy 92.2%, cross entropy 0.214409
INFO:tensorflow:Step #18790: rate 0.000100, accuracy 93.8%, cross entropy 0.196731
INFO:tensorflow:Step #18800: rate 0.000100, accuracy 89.5%, cross entropy 0.286206
INFO:tensorflow:Step #18810: rate 0.000100, accuracy 91.0%, cross entropy 0.267830
INFO:tensorflow:Step #18820: rate 0.000100, accuracy 93.0%, cross entropy 0.202916
INFO:tensorflow:Step #18830: rate 0.000100, accuracy 91.8%, cross entropy 0.266315
INFO:tensorflow:Step #18840: rate 0.000100, accuracy 89.5%, cross entropy 0.272303
INFO:tensorflow:Step #18850: rate 0.000100, accuracy 91.0%, cross entropy 0.274367
INFO:tensorflow:Step #18860: rate 0.000100, accuracy 91.8%, cross entropy 0.222884
INFO:tensorflow:Step #18870: rate 0.000100, accuracy 91.4%, cross entropy 0.267045
INFO:tensorflow:Step #18880: rate 0.000100, accuracy 89.8%, cross entropy 0.257914
INFO:tensorflow:Step #18890: rate 0.000100, accuracy 92.2%, cross entropy 0.261543
INFO:tensorflow:Step #18900: rate 0.000100, accuracy 88.7%, cross entropy 0.303210
INFO:tensorflow:Step #18910: rate 0.000100, accuracy 91.8%, cross entropy 0.210532
INFO:tensorflow:Step #18920: rate 0.000100, accuracy 92.6%, cross entropy 0.224282
INFO:tensorflow:Step #18930: rate 0.000100, accuracy 94.1%, cross entropy 0.196923
INFO:tensorflow:Step #18940: rate 0.000100, accuracy 92.2%, cross entropy 0.241464
INFO:tensorflow:Step #18950: rate 0.000100, accuracy 93.4%, cross entropy 0.192088
INFO:tensorflow:Step #18960: rate 0.000100, accuracy 91.4%, cross entropy 0.264990
INFO:tensorflow:Step #18970: rate 0.000100, accuracy 91.0%, cross entropy 0.249456
INFO:tensorflow:Step #18980: rate 0.000100, accuracy 92.6%, cross entropy 0.246229
INFO:tensorflow:Step #18990: rate 0.000100, accuracy 93.4%, cross entropy 0.221514
INFO:tensorflow:Step #19000: rate 0.000100, accuracy 95.3%, cross entropy 0.187794
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 213   5   5   3   2   2   8   5   3   6   6]
 [  0   0 250   6   2   0   2   1   0   0   0   0]
 [  0   2   1 257   1   2   1   0   0   0   0   6]
 [  0   5   0   0 242   0   0   0   0  13   0   0]
 [  0   0   1   5   0 253   0   0   1   0   1   3]
 [  0   1   8   4   1   0 232   1   0   0   0   0]
 [  0   4   0   0   1   0   2 249   0   0   0   0]
 [  0   5   0   0   5   0   0   1 241   5   0   0]
 [  0   1   0   0  15   0   0   1   6 232   0   1]
 [  0   2   0   0   7   1   1   0   0   2 232   1]
 [  0   5   0   7   7   5   0   1   0   2   2 231]]
INFO:tensorflow:Step 19000: Validation accuracy = 92.8% (N=2835)
INFO:tensorflow:Step #19010: rate 0.000100, accuracy 90.6%, cross entropy 0.264835
INFO:tensorflow:Step #19020: rate 0.000100, accuracy 89.8%, cross entropy 0.305543
INFO:tensorflow:Step #19030: rate 0.000100, accuracy 93.4%, cross entropy 0.208571
INFO:tensorflow:Step #19040: rate 0.000100, accuracy 93.0%, cross entropy 0.261666
INFO:tensorflow:Step #19050: rate 0.000100, accuracy 93.0%, cross entropy 0.221757
INFO:tensorflow:Step #19060: rate 0.000100, accuracy 92.2%, cross entropy 0.298299
INFO:tensorflow:Step #19070: rate 0.000100, accuracy 93.8%, cross entropy 0.196868
INFO:tensorflow:Step #19080: rate 0.000100, accuracy 91.4%, cross entropy 0.242895
INFO:tensorflow:Step #19090: rate 0.000100, accuracy 94.1%, cross entropy 0.190832
INFO:tensorflow:Step #19100: rate 0.000100, accuracy 94.1%, cross entropy 0.187947
INFO:tensorflow:Step #19110: rate 0.000100, accuracy 93.0%, cross entropy 0.238053
INFO:tensorflow:Step #19120: rate 0.000100, accuracy 93.8%, cross entropy 0.164793
INFO:tensorflow:Step #19130: rate 0.000100, accuracy 95.3%, cross entropy 0.185780
INFO:tensorflow:Step #19140: rate 0.000100, accuracy 92.2%, cross entropy 0.264969
INFO:tensorflow:Step #19150: rate 0.000100, accuracy 91.0%, cross entropy 0.294564
INFO:tensorflow:Step #19160: rate 0.000100, accuracy 90.2%, cross entropy 0.282521
INFO:tensorflow:Step #19170: rate 0.000100, accuracy 93.4%, cross entropy 0.225034
INFO:tensorflow:Step #19180: rate 0.000100, accuracy 93.8%, cross entropy 0.211512
INFO:tensorflow:Step #19190: rate 0.000100, accuracy 93.4%, cross entropy 0.192642
INFO:tensorflow:Step #19200: rate 0.000100, accuracy 91.8%, cross entropy 0.249811
INFO:tensorflow:Step #19210: rate 0.000100, accuracy 90.2%, cross entropy 0.240153
INFO:tensorflow:Step #19220: rate 0.000100, accuracy 91.4%, cross entropy 0.218791
INFO:tensorflow:Step #19230: rate 0.000100, accuracy 92.2%, cross entropy 0.226610
INFO:tensorflow:Step #19240: rate 0.000100, accuracy 91.8%, cross entropy 0.254447
INFO:tensorflow:Step #19250: rate 0.000100, accuracy 94.5%, cross entropy 0.180483
INFO:tensorflow:Step #19260: rate 0.000100, accuracy 92.6%, cross entropy 0.295495
INFO:tensorflow:Step #19270: rate 0.000100, accuracy 93.0%, cross entropy 0.191990
INFO:tensorflow:Step #19280: rate 0.000100, accuracy 93.4%, cross entropy 0.192013
INFO:tensorflow:Step #19290: rate 0.000100, accuracy 90.2%, cross entropy 0.276832
INFO:tensorflow:Step #19300: rate 0.000100, accuracy 92.2%, cross entropy 0.227789
INFO:tensorflow:Step #19310: rate 0.000100, accuracy 93.8%, cross entropy 0.179820
INFO:tensorflow:Step #19320: rate 0.000100, accuracy 94.1%, cross entropy 0.209203
INFO:tensorflow:Step #19330: rate 0.000100, accuracy 91.8%, cross entropy 0.238423
INFO:tensorflow:Step #19340: rate 0.000100, accuracy 91.4%, cross entropy 0.258825
INFO:tensorflow:Step #19350: rate 0.000100, accuracy 92.6%, cross entropy 0.213057
INFO:tensorflow:Step #19360: rate 0.000100, accuracy 93.8%, cross entropy 0.189943
INFO:tensorflow:Step #19370: rate 0.000100, accuracy 94.5%, cross entropy 0.143517
INFO:tensorflow:Step #19380: rate 0.000100, accuracy 94.5%, cross entropy 0.159045
INFO:tensorflow:Step #19390: rate 0.000100, accuracy 93.4%, cross entropy 0.218437
INFO:tensorflow:Step #19400: rate 0.000100, accuracy 90.6%, cross entropy 0.271961
INFO:tensorflow:Step #19410: rate 0.000100, accuracy 90.6%, cross entropy 0.276391
INFO:tensorflow:Step #19420: rate 0.000100, accuracy 91.4%, cross entropy 0.249405
INFO:tensorflow:Step #19430: rate 0.000100, accuracy 92.6%, cross entropy 0.273868
INFO:tensorflow:Step #19440: rate 0.000100, accuracy 92.2%, cross entropy 0.232920
INFO:tensorflow:Step #19450: rate 0.000100, accuracy 94.5%, cross entropy 0.174000
INFO:tensorflow:Step #19460: rate 0.000100, accuracy 92.2%, cross entropy 0.224050
INFO:tensorflow:Step #19470: rate 0.000100, accuracy 95.3%, cross entropy 0.146753
INFO:tensorflow:Step #19480: rate 0.000100, accuracy 88.3%, cross entropy 0.341786
INFO:tensorflow:Step #19490: rate 0.000100, accuracy 93.8%, cross entropy 0.206269
INFO:tensorflow:Step #19500: rate 0.000100, accuracy 90.6%, cross entropy 0.270566
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 213   5   8   2   2   1   7   6   3   5   6]
 [  0   0 250   6   1   0   2   0   1   1   0   0]
 [  0   2   1 259   1   1   1   0   0   0   0   5]
 [  0   5   0   0 244   0   0   0   0  11   0   0]
 [  0   1   1   5   0 253   0   0   1   0   1   2]
 [  0   1   7   4   1   0 233   1   0   0   0   0]
 [  0   4   0   0   1   1   2 248   0   0   0   0]
 [  0   5   0   0   2   0   0   1 245   4   0   0]
 [  0   1   0   1  18   0   0   0   4 231   0   1]
 [  0   2   0   0   5   1   0   0   1   4 231   2]
 [  0   4   0   8   6   4   0   1   0   3   2 232]]
INFO:tensorflow:Step 19500: Validation accuracy = 93.1% (N=2835)
INFO:tensorflow:Step #19510: rate 0.000100, accuracy 93.0%, cross entropy 0.216592
INFO:tensorflow:Step #19520: rate 0.000100, accuracy 93.8%, cross entropy 0.209606
INFO:tensorflow:Step #19530: rate 0.000100, accuracy 95.3%, cross entropy 0.126580
INFO:tensorflow:Step #19540: rate 0.000100, accuracy 93.4%, cross entropy 0.212000
INFO:tensorflow:Step #19550: rate 0.000100, accuracy 93.0%, cross entropy 0.195344
INFO:tensorflow:Step #19560: rate 0.000100, accuracy 94.1%, cross entropy 0.176460
INFO:tensorflow:Step #19570: rate 0.000100, accuracy 94.9%, cross entropy 0.168133
INFO:tensorflow:Step #19580: rate 0.000100, accuracy 91.8%, cross entropy 0.288438
INFO:tensorflow:Step #19590: rate 0.000100, accuracy 93.4%, cross entropy 0.199701
INFO:tensorflow:Step #19600: rate 0.000100, accuracy 94.5%, cross entropy 0.186289
INFO:tensorflow:Step #19610: rate 0.000100, accuracy 86.7%, cross entropy 0.363726
INFO:tensorflow:Step #19620: rate 0.000100, accuracy 91.8%, cross entropy 0.247285
INFO:tensorflow:Step #19630: rate 0.000100, accuracy 93.0%, cross entropy 0.230985
INFO:tensorflow:Step #19640: rate 0.000100, accuracy 92.2%, cross entropy 0.240712
INFO:tensorflow:Step #19650: rate 0.000100, accuracy 93.4%, cross entropy 0.310240
INFO:tensorflow:Step #19660: rate 0.000100, accuracy 91.0%, cross entropy 0.241309
INFO:tensorflow:Step #19670: rate 0.000100, accuracy 90.6%, cross entropy 0.314461
INFO:tensorflow:Step #19680: rate 0.000100, accuracy 93.4%, cross entropy 0.261613
INFO:tensorflow:Step #19690: rate 0.000100, accuracy 92.2%, cross entropy 0.265044
INFO:tensorflow:Step #19700: rate 0.000100, accuracy 94.1%, cross entropy 0.154023
INFO:tensorflow:Step #19710: rate 0.000100, accuracy 92.6%, cross entropy 0.211510
INFO:tensorflow:Step #19720: rate 0.000100, accuracy 91.4%, cross entropy 0.245322
INFO:tensorflow:Step #19730: rate 0.000100, accuracy 91.0%, cross entropy 0.279068
INFO:tensorflow:Step #19740: rate 0.000100, accuracy 92.2%, cross entropy 0.233427
INFO:tensorflow:Step #19750: rate 0.000100, accuracy 91.0%, cross entropy 0.254821
INFO:tensorflow:Step #19760: rate 0.000100, accuracy 93.0%, cross entropy 0.195095
INFO:tensorflow:Step #19770: rate 0.000100, accuracy 92.6%, cross entropy 0.195544
INFO:tensorflow:Step #19780: rate 0.000100, accuracy 93.4%, cross entropy 0.177315
INFO:tensorflow:Step #19790: rate 0.000100, accuracy 91.4%, cross entropy 0.270017
INFO:tensorflow:Step #19800: rate 0.000100, accuracy 94.5%, cross entropy 0.151360
INFO:tensorflow:Step #19810: rate 0.000100, accuracy 89.1%, cross entropy 0.337191
INFO:tensorflow:Step #19820: rate 0.000100, accuracy 94.9%, cross entropy 0.209034
INFO:tensorflow:Step #19830: rate 0.000100, accuracy 90.2%, cross entropy 0.283246
INFO:tensorflow:Step #19840: rate 0.000100, accuracy 92.6%, cross entropy 0.212964
INFO:tensorflow:Step #19850: rate 0.000100, accuracy 89.8%, cross entropy 0.293609
INFO:tensorflow:Step #19860: rate 0.000100, accuracy 90.6%, cross entropy 0.259123
INFO:tensorflow:Step #19870: rate 0.000100, accuracy 93.4%, cross entropy 0.215870
INFO:tensorflow:Step #19880: rate 0.000100, accuracy 95.3%, cross entropy 0.159533
INFO:tensorflow:Step #19890: rate 0.000100, accuracy 89.1%, cross entropy 0.276180
INFO:tensorflow:Step #19900: rate 0.000100, accuracy 91.4%, cross entropy 0.205786
INFO:tensorflow:Step #19910: rate 0.000100, accuracy 90.6%, cross entropy 0.264059
INFO:tensorflow:Step #19920: rate 0.000100, accuracy 93.8%, cross entropy 0.190213
INFO:tensorflow:Step #19930: rate 0.000100, accuracy 89.1%, cross entropy 0.301389
INFO:tensorflow:Step #19940: rate 0.000100, accuracy 89.1%, cross entropy 0.318690
INFO:tensorflow:Step #19950: rate 0.000100, accuracy 94.9%, cross entropy 0.168648
INFO:tensorflow:Step #19960: rate 0.000100, accuracy 92.6%, cross entropy 0.242380
INFO:tensorflow:Step #19970: rate 0.000100, accuracy 95.3%, cross entropy 0.197101
INFO:tensorflow:Step #19980: rate 0.000100, accuracy 91.8%, cross entropy 0.244811
INFO:tensorflow:Step #19990: rate 0.000100, accuracy 93.0%, cross entropy 0.259888
INFO:tensorflow:Step #20000: rate 0.000100, accuracy 92.6%, cross entropy 0.222704
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 215   7   6   2   1   2   8   5   3   5   4]
 [  0   0 250   6   2   0   2   1   0   0   0   0]
 [  0   2   1 258   1   1   1   0   0   0   0   6]
 [  0   5   0   0 246   0   0   0   0   8   1   0]
 [  0   0   2   7   0 249   1   0   1   0   1   3]
 [  0   0  10   4   1   0 231   1   0   0   0   0]
 [  0   4   0   0   1   0   2 249   0   0   0   0]
 [  0   5   0   0   3   1   0   3 242   3   0   0]
 [  0   1   0   1  19   0   0   0   4 230   0   1]
 [  0   2   0   0   7   1   1   0   0   2 232   1]
 [  0   5   0   9   6   4   0   2   0   2   2 230]]
INFO:tensorflow:Step 20000: Validation accuracy = 92.8% (N=2835)
INFO:tensorflow:Saving to "F:\ML_Project\Data\logs&checkpoint\c_rnn\ckpt-20000"
INFO:tensorflow:Step #20010: rate 0.000020, accuracy 89.1%, cross entropy 0.321400
INFO:tensorflow:Step #20020: rate 0.000020, accuracy 90.6%, cross entropy 0.279088
INFO:tensorflow:Step #20030: rate 0.000020, accuracy 92.2%, cross entropy 0.215548
INFO:tensorflow:Step #20040: rate 0.000020, accuracy 93.0%, cross entropy 0.257838
INFO:tensorflow:Step #20050: rate 0.000020, accuracy 91.4%, cross entropy 0.260339
INFO:tensorflow:Step #20060: rate 0.000020, accuracy 93.0%, cross entropy 0.224594
INFO:tensorflow:Step #20070: rate 0.000020, accuracy 91.4%, cross entropy 0.219292
INFO:tensorflow:Step #20080: rate 0.000020, accuracy 95.3%, cross entropy 0.141037
INFO:tensorflow:Step #20090: rate 0.000020, accuracy 91.0%, cross entropy 0.282105
INFO:tensorflow:Step #20100: rate 0.000020, accuracy 93.4%, cross entropy 0.199807
INFO:tensorflow:Step #20110: rate 0.000020, accuracy 92.6%, cross entropy 0.241908
INFO:tensorflow:Step #20120: rate 0.000020, accuracy 91.8%, cross entropy 0.243910
INFO:tensorflow:Step #20130: rate 0.000020, accuracy 91.8%, cross entropy 0.217434
INFO:tensorflow:Step #20140: rate 0.000020, accuracy 93.0%, cross entropy 0.227389
INFO:tensorflow:Step #20150: rate 0.000020, accuracy 93.4%, cross entropy 0.170074
INFO:tensorflow:Step #20160: rate 0.000020, accuracy 91.4%, cross entropy 0.243432
INFO:tensorflow:Step #20170: rate 0.000020, accuracy 92.2%, cross entropy 0.219573
INFO:tensorflow:Step #20180: rate 0.000020, accuracy 94.1%, cross entropy 0.183171
INFO:tensorflow:Step #20190: rate 0.000020, accuracy 90.2%, cross entropy 0.264229
INFO:tensorflow:Step #20200: rate 0.000020, accuracy 90.2%, cross entropy 0.285005
INFO:tensorflow:Step #20210: rate 0.000020, accuracy 93.0%, cross entropy 0.198407
INFO:tensorflow:Step #20220: rate 0.000020, accuracy 91.8%, cross entropy 0.282600
INFO:tensorflow:Step #20230: rate 0.000020, accuracy 91.4%, cross entropy 0.239081
INFO:tensorflow:Step #20240: rate 0.000020, accuracy 92.2%, cross entropy 0.198489
INFO:tensorflow:Step #20250: rate 0.000020, accuracy 93.8%, cross entropy 0.245405
INFO:tensorflow:Step #20260: rate 0.000020, accuracy 89.5%, cross entropy 0.257475
INFO:tensorflow:Step #20270: rate 0.000020, accuracy 92.6%, cross entropy 0.208147
INFO:tensorflow:Step #20280: rate 0.000020, accuracy 91.0%, cross entropy 0.283862
INFO:tensorflow:Step #20290: rate 0.000020, accuracy 92.6%, cross entropy 0.208989
INFO:tensorflow:Step #20300: rate 0.000020, accuracy 91.4%, cross entropy 0.217977
INFO:tensorflow:Step #20310: rate 0.000020, accuracy 92.6%, cross entropy 0.248016
INFO:tensorflow:Step #20320: rate 0.000020, accuracy 94.5%, cross entropy 0.150815
INFO:tensorflow:Step #20330: rate 0.000020, accuracy 94.1%, cross entropy 0.232284
INFO:tensorflow:Step #20340: rate 0.000020, accuracy 93.4%, cross entropy 0.220617
INFO:tensorflow:Step #20350: rate 0.000020, accuracy 91.0%, cross entropy 0.249905
INFO:tensorflow:Step #20360: rate 0.000020, accuracy 93.0%, cross entropy 0.197340
INFO:tensorflow:Step #20370: rate 0.000020, accuracy 93.4%, cross entropy 0.236533
INFO:tensorflow:Step #20380: rate 0.000020, accuracy 94.1%, cross entropy 0.200166
INFO:tensorflow:Step #20390: rate 0.000020, accuracy 95.7%, cross entropy 0.133948
INFO:tensorflow:Step #20400: rate 0.000020, accuracy 88.3%, cross entropy 0.332416
INFO:tensorflow:Step #20410: rate 0.000020, accuracy 95.3%, cross entropy 0.172274
INFO:tensorflow:Step #20420: rate 0.000020, accuracy 93.4%, cross entropy 0.195460
INFO:tensorflow:Step #20430: rate 0.000020, accuracy 91.4%, cross entropy 0.247660
INFO:tensorflow:Step #20440: rate 0.000020, accuracy 91.4%, cross entropy 0.271849
INFO:tensorflow:Step #20450: rate 0.000020, accuracy 92.6%, cross entropy 0.248536
INFO:tensorflow:Step #20460: rate 0.000020, accuracy 91.0%, cross entropy 0.233508
INFO:tensorflow:Step #20470: rate 0.000020, accuracy 91.0%, cross entropy 0.250287
INFO:tensorflow:Step #20480: rate 0.000020, accuracy 94.1%, cross entropy 0.182409
INFO:tensorflow:Step #20490: rate 0.000020, accuracy 91.8%, cross entropy 0.262211
INFO:tensorflow:Step #20500: rate 0.000020, accuracy 91.8%, cross entropy 0.258428
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 217   6   5   2   1   2   8   5   3   4   5]
 [  0   0 250   6   2   0   2   0   1   0   0   0]
 [  0   2   1 257   1   2   1   0   0   0   0   6]
 [  0   5   0   0 246   0   0   0   0   8   1   0]
 [  0   0   1   5   0 252   1   0   1   0   1   3]
 [  0   1  10   4   1   0 230   1   0   0   0   0]
 [  0   4   0   0   1   1   2 248   0   0   0   0]
 [  0   5   0   0   3   0   0   3 243   3   0   0]
 [  0   1   0   0  19   0   0   1   4 230   0   1]
 [  0   3   0   0   7   1   0   0   0   3 231   1]
 [  0   5   0   6   6   4   0   2   0   2   2 233]]
INFO:tensorflow:Step 20500: Validation accuracy = 93.0% (N=2835)
INFO:tensorflow:Step #20510: rate 0.000020, accuracy 90.6%, cross entropy 0.309035
INFO:tensorflow:Step #20520: rate 0.000020, accuracy 93.4%, cross entropy 0.186121
INFO:tensorflow:Step #20530: rate 0.000020, accuracy 93.4%, cross entropy 0.208119
INFO:tensorflow:Step #20540: rate 0.000020, accuracy 92.6%, cross entropy 0.211226
INFO:tensorflow:Step #20550: rate 0.000020, accuracy 93.4%, cross entropy 0.219038
INFO:tensorflow:Step #20560: rate 0.000020, accuracy 91.8%, cross entropy 0.256486
INFO:tensorflow:Step #20570: rate 0.000020, accuracy 87.9%, cross entropy 0.311575
INFO:tensorflow:Step #20580: rate 0.000020, accuracy 91.4%, cross entropy 0.247706
INFO:tensorflow:Step #20590: rate 0.000020, accuracy 93.8%, cross entropy 0.192138
INFO:tensorflow:Step #20600: rate 0.000020, accuracy 93.4%, cross entropy 0.238288
INFO:tensorflow:Step #20610: rate 0.000020, accuracy 93.8%, cross entropy 0.212478
INFO:tensorflow:Step #20620: rate 0.000020, accuracy 94.9%, cross entropy 0.194340
INFO:tensorflow:Step #20630: rate 0.000020, accuracy 93.0%, cross entropy 0.218659
INFO:tensorflow:Step #20640: rate 0.000020, accuracy 90.2%, cross entropy 0.282506
INFO:tensorflow:Step #20650: rate 0.000020, accuracy 92.2%, cross entropy 0.270124
INFO:tensorflow:Step #20660: rate 0.000020, accuracy 93.0%, cross entropy 0.190495
INFO:tensorflow:Step #20670: rate 0.000020, accuracy 91.4%, cross entropy 0.252512
INFO:tensorflow:Step #20680: rate 0.000020, accuracy 91.8%, cross entropy 0.261419
INFO:tensorflow:Step #20690: rate 0.000020, accuracy 93.0%, cross entropy 0.214662
INFO:tensorflow:Step #20700: rate 0.000020, accuracy 88.7%, cross entropy 0.293682
INFO:tensorflow:Step #20710: rate 0.000020, accuracy 93.4%, cross entropy 0.200461
INFO:tensorflow:Step #20720: rate 0.000020, accuracy 95.3%, cross entropy 0.128989
INFO:tensorflow:Step #20730: rate 0.000020, accuracy 94.9%, cross entropy 0.157926
INFO:tensorflow:Step #20740: rate 0.000020, accuracy 94.1%, cross entropy 0.223665
INFO:tensorflow:Step #20750: rate 0.000020, accuracy 93.8%, cross entropy 0.170242
INFO:tensorflow:Step #20760: rate 0.000020, accuracy 94.5%, cross entropy 0.185982
INFO:tensorflow:Step #20770: rate 0.000020, accuracy 93.0%, cross entropy 0.219070
INFO:tensorflow:Step #20780: rate 0.000020, accuracy 92.2%, cross entropy 0.243232
INFO:tensorflow:Step #20790: rate 0.000020, accuracy 94.1%, cross entropy 0.154388
INFO:tensorflow:Step #20800: rate 0.000020, accuracy 91.8%, cross entropy 0.200211
INFO:tensorflow:Step #20810: rate 0.000020, accuracy 96.1%, cross entropy 0.133296
INFO:tensorflow:Step #20820: rate 0.000020, accuracy 93.0%, cross entropy 0.178999
INFO:tensorflow:Step #20830: rate 0.000020, accuracy 92.6%, cross entropy 0.226302
INFO:tensorflow:Step #20840: rate 0.000020, accuracy 92.2%, cross entropy 0.242108
INFO:tensorflow:Step #20850: rate 0.000020, accuracy 91.0%, cross entropy 0.294156
INFO:tensorflow:Step #20860: rate 0.000020, accuracy 93.0%, cross entropy 0.253364
INFO:tensorflow:Step #20870: rate 0.000020, accuracy 91.0%, cross entropy 0.247456
INFO:tensorflow:Step #20880: rate 0.000020, accuracy 92.6%, cross entropy 0.226144
INFO:tensorflow:Step #20890: rate 0.000020, accuracy 90.2%, cross entropy 0.249860
INFO:tensorflow:Step #20900: rate 0.000020, accuracy 92.2%, cross entropy 0.299247
INFO:tensorflow:Step #20910: rate 0.000020, accuracy 94.9%, cross entropy 0.174067
INFO:tensorflow:Step #20920: rate 0.000020, accuracy 90.2%, cross entropy 0.302008
INFO:tensorflow:Step #20930: rate 0.000020, accuracy 94.1%, cross entropy 0.176385
INFO:tensorflow:Step #20940: rate 0.000020, accuracy 93.8%, cross entropy 0.197444
INFO:tensorflow:Step #20950: rate 0.000020, accuracy 89.5%, cross entropy 0.286096
INFO:tensorflow:Step #20960: rate 0.000020, accuracy 94.9%, cross entropy 0.185614
INFO:tensorflow:Step #20970: rate 0.000020, accuracy 93.8%, cross entropy 0.223212
INFO:tensorflow:Step #20980: rate 0.000020, accuracy 91.0%, cross entropy 0.249719
INFO:tensorflow:Step #20990: rate 0.000020, accuracy 89.8%, cross entropy 0.285001
INFO:tensorflow:Step #21000: rate 0.000020, accuracy 92.6%, cross entropy 0.239047
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 217   6   4   2   1   2   8   5   3   4   6]
 [  0   0 250   6   2   0   2   0   1   0   0   0]
 [  0   2   1 257   1   2   1   0   0   0   0   6]
 [  0   5   0   0 244   0   0   0   0  10   1   0]
 [  0   0   1   5   0 253   0   0   1   0   1   3]
 [  0   1   8   4   1   0 232   1   0   0   0   0]
 [  0   4   0   0   1   1   2 248   0   0   0   0]
 [  0   5   0   0   3   0   0   2 243   4   0   0]
 [  0   1   0   0  18   0   0   1   6 229   0   1]
 [  0   3   0   0   7   0   0   0   0   3 231   2]
 [  0   5   0   5   6   4   0   1   0   3   2 234]]
INFO:tensorflow:Step 21000: Validation accuracy = 93.1% (N=2835)
INFO:tensorflow:Step #21010: rate 0.000020, accuracy 92.2%, cross entropy 0.185597
INFO:tensorflow:Step #21020: rate 0.000020, accuracy 94.1%, cross entropy 0.162162
INFO:tensorflow:Step #21030: rate 0.000020, accuracy 93.4%, cross entropy 0.218677
INFO:tensorflow:Step #21040: rate 0.000020, accuracy 93.8%, cross entropy 0.188067
INFO:tensorflow:Step #21050: rate 0.000020, accuracy 91.8%, cross entropy 0.261269
INFO:tensorflow:Step #21060: rate 0.000020, accuracy 92.2%, cross entropy 0.196379
INFO:tensorflow:Step #21070: rate 0.000020, accuracy 91.4%, cross entropy 0.248199
INFO:tensorflow:Step #21080: rate 0.000020, accuracy 90.6%, cross entropy 0.228094
INFO:tensorflow:Step #21090: rate 0.000020, accuracy 94.5%, cross entropy 0.168412
INFO:tensorflow:Step #21100: rate 0.000020, accuracy 92.2%, cross entropy 0.223768
INFO:tensorflow:Step #21110: rate 0.000020, accuracy 92.6%, cross entropy 0.239335
INFO:tensorflow:Step #21120: rate 0.000020, accuracy 94.1%, cross entropy 0.211048
INFO:tensorflow:Step #21130: rate 0.000020, accuracy 93.4%, cross entropy 0.193706
INFO:tensorflow:Step #21140: rate 0.000020, accuracy 89.8%, cross entropy 0.278039
INFO:tensorflow:Step #21150: rate 0.000020, accuracy 92.2%, cross entropy 0.195484
INFO:tensorflow:Step #21160: rate 0.000020, accuracy 93.0%, cross entropy 0.226671
INFO:tensorflow:Step #21170: rate 0.000020, accuracy 91.8%, cross entropy 0.247138
INFO:tensorflow:Step #21180: rate 0.000020, accuracy 94.1%, cross entropy 0.174442
INFO:tensorflow:Step #21190: rate 0.000020, accuracy 93.4%, cross entropy 0.231385
INFO:tensorflow:Step #21200: rate 0.000020, accuracy 94.5%, cross entropy 0.150320
INFO:tensorflow:Step #21210: rate 0.000020, accuracy 93.8%, cross entropy 0.246918
INFO:tensorflow:Step #21220: rate 0.000020, accuracy 94.5%, cross entropy 0.197703
INFO:tensorflow:Step #21230: rate 0.000020, accuracy 94.1%, cross entropy 0.190029
INFO:tensorflow:Step #21240: rate 0.000020, accuracy 92.6%, cross entropy 0.185824
INFO:tensorflow:Step #21250: rate 0.000020, accuracy 91.4%, cross entropy 0.257220
INFO:tensorflow:Step #21260: rate 0.000020, accuracy 93.0%, cross entropy 0.225640
INFO:tensorflow:Step #21270: rate 0.000020, accuracy 93.0%, cross entropy 0.210945
INFO:tensorflow:Step #21280: rate 0.000020, accuracy 91.4%, cross entropy 0.227611
INFO:tensorflow:Step #21290: rate 0.000020, accuracy 92.6%, cross entropy 0.211188
INFO:tensorflow:Step #21300: rate 0.000020, accuracy 92.2%, cross entropy 0.202504
INFO:tensorflow:Step #21310: rate 0.000020, accuracy 91.4%, cross entropy 0.222650
INFO:tensorflow:Step #21320: rate 0.000020, accuracy 92.6%, cross entropy 0.204930
INFO:tensorflow:Step #21330: rate 0.000020, accuracy 93.4%, cross entropy 0.223942
INFO:tensorflow:Step #21340: rate 0.000020, accuracy 93.0%, cross entropy 0.198875
INFO:tensorflow:Step #21350: rate 0.000020, accuracy 93.4%, cross entropy 0.230302
INFO:tensorflow:Step #21360: rate 0.000020, accuracy 93.4%, cross entropy 0.185480
INFO:tensorflow:Step #21370: rate 0.000020, accuracy 92.2%, cross entropy 0.219032
INFO:tensorflow:Step #21380: rate 0.000020, accuracy 89.8%, cross entropy 0.290666
INFO:tensorflow:Step #21390: rate 0.000020, accuracy 89.5%, cross entropy 0.334859
INFO:tensorflow:Step #21400: rate 0.000020, accuracy 94.9%, cross entropy 0.193588
INFO:tensorflow:Step #21410: rate 0.000020, accuracy 91.4%, cross entropy 0.230907
INFO:tensorflow:Step #21420: rate 0.000020, accuracy 89.5%, cross entropy 0.281436
INFO:tensorflow:Step #21430: rate 0.000020, accuracy 93.4%, cross entropy 0.207906
INFO:tensorflow:Step #21440: rate 0.000020, accuracy 92.6%, cross entropy 0.192457
INFO:tensorflow:Step #21450: rate 0.000020, accuracy 91.8%, cross entropy 0.244471
INFO:tensorflow:Step #21460: rate 0.000020, accuracy 91.8%, cross entropy 0.241228
INFO:tensorflow:Step #21470: rate 0.000020, accuracy 93.4%, cross entropy 0.237101
INFO:tensorflow:Step #21480: rate 0.000020, accuracy 90.2%, cross entropy 0.353517
INFO:tensorflow:Step #21490: rate 0.000020, accuracy 90.2%, cross entropy 0.284932
INFO:tensorflow:Step #21500: rate 0.000020, accuracy 94.5%, cross entropy 0.180376
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 217   6   6   2   1   1   7   5   3   4   6]
 [  0   0 249   6   2   0   3   0   1   0   0   0]
 [  0   2   1 257   1   2   1   0   0   0   0   6]
 [  0   5   0   0 243   0   0   0   0  11   1   0]
 [  0   0   1   5   0 252   0   0   1   0   1   4]
 [  0   1  10   4   1   0 230   1   0   0   0   0]
 [  0   4   0   0   1   1   2 248   0   0   0   0]
 [  0   5   0   0   3   0   0   2 243   4   0   0]
 [  0   1   0   0  18   0   0   1   7 228   0   1]
 [  0   2   0   0   7   1   0   0   0   3 230   3]
 [  0   5   0   6   6   4   0   1   0   3   2 233]]
INFO:tensorflow:Step 21500: Validation accuracy = 92.8% (N=2835)
INFO:tensorflow:Step #21510: rate 0.000020, accuracy 93.0%, cross entropy 0.237760
INFO:tensorflow:Step #21520: rate 0.000020, accuracy 94.5%, cross entropy 0.140684
INFO:tensorflow:Step #21530: rate 0.000020, accuracy 96.1%, cross entropy 0.128536
INFO:tensorflow:Step #21540: rate 0.000020, accuracy 92.6%, cross entropy 0.229804
INFO:tensorflow:Step #21550: rate 0.000020, accuracy 94.1%, cross entropy 0.190996
INFO:tensorflow:Step #21560: rate 0.000020, accuracy 92.6%, cross entropy 0.173712
INFO:tensorflow:Step #21570: rate 0.000020, accuracy 94.5%, cross entropy 0.162488
INFO:tensorflow:Step #21580: rate 0.000020, accuracy 91.4%, cross entropy 0.215005
INFO:tensorflow:Step #21590: rate 0.000020, accuracy 94.9%, cross entropy 0.169675
INFO:tensorflow:Step #21600: rate 0.000020, accuracy 95.3%, cross entropy 0.140426
INFO:tensorflow:Step #21610: rate 0.000020, accuracy 96.5%, cross entropy 0.144895
INFO:tensorflow:Step #21620: rate 0.000020, accuracy 93.4%, cross entropy 0.205610
INFO:tensorflow:Step #21630: rate 0.000020, accuracy 91.0%, cross entropy 0.320067
INFO:tensorflow:Step #21640: rate 0.000020, accuracy 93.8%, cross entropy 0.204251
INFO:tensorflow:Step #21650: rate 0.000020, accuracy 94.9%, cross entropy 0.180619
INFO:tensorflow:Step #21660: rate 0.000020, accuracy 91.8%, cross entropy 0.221863
INFO:tensorflow:Step #21670: rate 0.000020, accuracy 95.3%, cross entropy 0.136789
INFO:tensorflow:Step #21680: rate 0.000020, accuracy 91.8%, cross entropy 0.283892
INFO:tensorflow:Step #21690: rate 0.000020, accuracy 91.4%, cross entropy 0.260418
INFO:tensorflow:Step #21700: rate 0.000020, accuracy 92.2%, cross entropy 0.238916
INFO:tensorflow:Step #21710: rate 0.000020, accuracy 91.4%, cross entropy 0.231658
INFO:tensorflow:Step #21720: rate 0.000020, accuracy 92.2%, cross entropy 0.193134
INFO:tensorflow:Step #21730: rate 0.000020, accuracy 89.5%, cross entropy 0.330336
INFO:tensorflow:Step #21740: rate 0.000020, accuracy 92.6%, cross entropy 0.219532
INFO:tensorflow:Step #21750: rate 0.000020, accuracy 91.8%, cross entropy 0.231684
INFO:tensorflow:Step #21760: rate 0.000020, accuracy 93.4%, cross entropy 0.214511
INFO:tensorflow:Step #21770: rate 0.000020, accuracy 89.1%, cross entropy 0.298334
INFO:tensorflow:Step #21780: rate 0.000020, accuracy 92.2%, cross entropy 0.314380
INFO:tensorflow:Step #21790: rate 0.000020, accuracy 95.7%, cross entropy 0.149205
INFO:tensorflow:Step #21800: rate 0.000020, accuracy 93.0%, cross entropy 0.224424
INFO:tensorflow:Step #21810: rate 0.000020, accuracy 90.6%, cross entropy 0.230277
INFO:tensorflow:Step #21820: rate 0.000020, accuracy 93.0%, cross entropy 0.174736
INFO:tensorflow:Step #21830: rate 0.000020, accuracy 92.2%, cross entropy 0.248088
INFO:tensorflow:Step #21840: rate 0.000020, accuracy 93.8%, cross entropy 0.205470
INFO:tensorflow:Step #21850: rate 0.000020, accuracy 92.6%, cross entropy 0.231387
INFO:tensorflow:Step #21860: rate 0.000020, accuracy 93.0%, cross entropy 0.194420
INFO:tensorflow:Step #21870: rate 0.000020, accuracy 93.8%, cross entropy 0.213349
INFO:tensorflow:Step #21880: rate 0.000020, accuracy 94.9%, cross entropy 0.137260
INFO:tensorflow:Step #21890: rate 0.000020, accuracy 93.4%, cross entropy 0.202612
INFO:tensorflow:Step #21900: rate 0.000020, accuracy 92.2%, cross entropy 0.243218
INFO:tensorflow:Step #21910: rate 0.000020, accuracy 90.2%, cross entropy 0.313135
INFO:tensorflow:Step #21920: rate 0.000020, accuracy 90.2%, cross entropy 0.243413
INFO:tensorflow:Step #21930: rate 0.000020, accuracy 93.0%, cross entropy 0.241999
INFO:tensorflow:Step #21940: rate 0.000020, accuracy 91.4%, cross entropy 0.242010
INFO:tensorflow:Step #21950: rate 0.000020, accuracy 92.6%, cross entropy 0.206782
INFO:tensorflow:Step #21960: rate 0.000020, accuracy 93.0%, cross entropy 0.195528
INFO:tensorflow:Step #21970: rate 0.000020, accuracy 92.2%, cross entropy 0.252792
INFO:tensorflow:Step #21980: rate 0.000020, accuracy 94.5%, cross entropy 0.154026
INFO:tensorflow:Step #21990: rate 0.000020, accuracy 91.0%, cross entropy 0.324529
INFO:tensorflow:Step #22000: rate 0.000020, accuracy 92.6%, cross entropy 0.242634
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 214   6   6   2   1   1   8   5   3   4   8]
 [  0   0 250   6   2   0   2   0   1   0   0   0]
 [  0   2   1 258   1   2   0   0   0   0   0   6]
 [  0   5   0   0 243   0   0   0   0  11   1   0]
 [  0   0   1   5   0 252   0   0   1   0   1   4]
 [  0   1  10   4   1   0 230   1   0   0   0   0]
 [  0   4   0   0   1   1   2 248   0   0   0   0]
 [  0   5   0   0   4   0   0   1 242   5   0   0]
 [  0   1   0   1  18   0   0   0   5 230   0   1]
 [  0   2   0   0   7   0   0   0   0   3 231   3]
 [  0   5   0   7   6   4   0   1   0   3   2 232]]
INFO:tensorflow:Step 22000: Validation accuracy = 92.8% (N=2835)
INFO:tensorflow:Saving to "F:\ML_Project\Data\logs&checkpoint\c_rnn\ckpt-22000"
INFO:tensorflow:Step #22010: rate 0.000020, accuracy 92.2%, cross entropy 0.224722
INFO:tensorflow:Step #22020: rate 0.000020, accuracy 93.8%, cross entropy 0.193826
INFO:tensorflow:Step #22030: rate 0.000020, accuracy 94.1%, cross entropy 0.170554
INFO:tensorflow:Step #22040: rate 0.000020, accuracy 91.8%, cross entropy 0.234566
INFO:tensorflow:Step #22050: rate 0.000020, accuracy 91.8%, cross entropy 0.217976
INFO:tensorflow:Step #22060: rate 0.000020, accuracy 93.4%, cross entropy 0.201750
INFO:tensorflow:Step #22070: rate 0.000020, accuracy 91.8%, cross entropy 0.265537
INFO:tensorflow:Step #22080: rate 0.000020, accuracy 91.8%, cross entropy 0.238948
INFO:tensorflow:Step #22090: rate 0.000020, accuracy 91.8%, cross entropy 0.224141
INFO:tensorflow:Step #22100: rate 0.000020, accuracy 94.1%, cross entropy 0.175382
INFO:tensorflow:Step #22110: rate 0.000020, accuracy 90.6%, cross entropy 0.262633
INFO:tensorflow:Step #22120: rate 0.000020, accuracy 93.0%, cross entropy 0.219418
INFO:tensorflow:Step #22130: rate 0.000020, accuracy 93.0%, cross entropy 0.194160
INFO:tensorflow:Step #22140: rate 0.000020, accuracy 94.5%, cross entropy 0.179234
INFO:tensorflow:Step #22150: rate 0.000020, accuracy 92.2%, cross entropy 0.230691
INFO:tensorflow:Step #22160: rate 0.000020, accuracy 90.2%, cross entropy 0.347471
INFO:tensorflow:Step #22170: rate 0.000020, accuracy 96.1%, cross entropy 0.139465
INFO:tensorflow:Step #22180: rate 0.000020, accuracy 92.6%, cross entropy 0.198601
INFO:tensorflow:Step #22190: rate 0.000020, accuracy 91.0%, cross entropy 0.299430
INFO:tensorflow:Step #22200: rate 0.000020, accuracy 90.2%, cross entropy 0.263714
INFO:tensorflow:Step #22210: rate 0.000020, accuracy 89.1%, cross entropy 0.351336
INFO:tensorflow:Step #22220: rate 0.000020, accuracy 93.0%, cross entropy 0.251422
INFO:tensorflow:Step #22230: rate 0.000020, accuracy 91.4%, cross entropy 0.284529
INFO:tensorflow:Step #22240: rate 0.000020, accuracy 95.7%, cross entropy 0.155203
INFO:tensorflow:Step #22250: rate 0.000020, accuracy 91.8%, cross entropy 0.238677
INFO:tensorflow:Step #22260: rate 0.000020, accuracy 90.6%, cross entropy 0.252349
INFO:tensorflow:Step #22270: rate 0.000020, accuracy 95.3%, cross entropy 0.160996
INFO:tensorflow:Step #22280: rate 0.000020, accuracy 94.1%, cross entropy 0.167052
INFO:tensorflow:Step #22290: rate 0.000020, accuracy 92.2%, cross entropy 0.241635
INFO:tensorflow:Step #22300: rate 0.000020, accuracy 92.2%, cross entropy 0.215445
INFO:tensorflow:Step #22310: rate 0.000020, accuracy 94.1%, cross entropy 0.175472
INFO:tensorflow:Step #22320: rate 0.000020, accuracy 89.8%, cross entropy 0.265530
INFO:tensorflow:Step #22330: rate 0.000020, accuracy 91.4%, cross entropy 0.259858
INFO:tensorflow:Step #22340: rate 0.000020, accuracy 96.5%, cross entropy 0.146836
INFO:tensorflow:Step #22350: rate 0.000020, accuracy 92.6%, cross entropy 0.184084
INFO:tensorflow:Step #22360: rate 0.000020, accuracy 90.2%, cross entropy 0.306657
INFO:tensorflow:Step #22370: rate 0.000020, accuracy 94.9%, cross entropy 0.149550
INFO:tensorflow:Step #22380: rate 0.000020, accuracy 92.6%, cross entropy 0.200587
INFO:tensorflow:Step #22390: rate 0.000020, accuracy 93.8%, cross entropy 0.168516
INFO:tensorflow:Step #22400: rate 0.000020, accuracy 90.2%, cross entropy 0.295270
INFO:tensorflow:Step #22410: rate 0.000020, accuracy 92.6%, cross entropy 0.224843
INFO:tensorflow:Step #22420: rate 0.000020, accuracy 92.2%, cross entropy 0.253433
INFO:tensorflow:Step #22430: rate 0.000020, accuracy 92.6%, cross entropy 0.235034
INFO:tensorflow:Step #22440: rate 0.000020, accuracy 91.8%, cross entropy 0.227875
INFO:tensorflow:Step #22450: rate 0.000020, accuracy 91.8%, cross entropy 0.196090
INFO:tensorflow:Step #22460: rate 0.000020, accuracy 93.4%, cross entropy 0.218797
INFO:tensorflow:Step #22470: rate 0.000020, accuracy 93.4%, cross entropy 0.156634
INFO:tensorflow:Step #22480: rate 0.000020, accuracy 93.0%, cross entropy 0.229931
INFO:tensorflow:Step #22490: rate 0.000020, accuracy 93.4%, cross entropy 0.204679
INFO:tensorflow:Step #22500: rate 0.000020, accuracy 92.2%, cross entropy 0.187908
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 217   6   5   3   1   2   7   5   3   4   5]
 [  0   0 250   6   2   0   2   0   1   0   0   0]
 [  0   2   1 257   1   2   1   0   0   0   0   6]
 [  0   5   0   0 241   0   0   0   0  13   1   0]
 [  0   0   1   5   0 253   0   0   1   0   1   3]
 [  0   1   8   4   1   0 232   1   0   0   0   0]
 [  0   4   0   0   1   0   2 249   0   0   0   0]
 [  0   5   0   0   5   0   0   1 242   4   0   0]
 [  0   1   0   0  15   0   0   1   4 234   0   1]
 [  0   3   0   0   7   1   0   0   0   3 230   2]
 [  0   6   0   4   7   4   0   1   0   2   2 234]]
INFO:tensorflow:Step 22500: Validation accuracy = 93.1% (N=2835)
INFO:tensorflow:Step #22510: rate 0.000020, accuracy 90.2%, cross entropy 0.261407
INFO:tensorflow:Step #22520: rate 0.000020, accuracy 87.5%, cross entropy 0.341859
INFO:tensorflow:Step #22530: rate 0.000020, accuracy 91.8%, cross entropy 0.283543
INFO:tensorflow:Step #22540: rate 0.000020, accuracy 89.8%, cross entropy 0.281598
INFO:tensorflow:Step #22550: rate 0.000020, accuracy 90.6%, cross entropy 0.258991
INFO:tensorflow:Step #22560: rate 0.000020, accuracy 91.8%, cross entropy 0.284768
INFO:tensorflow:Step #22570: rate 0.000020, accuracy 90.6%, cross entropy 0.242952
INFO:tensorflow:Step #22580: rate 0.000020, accuracy 92.6%, cross entropy 0.211188
INFO:tensorflow:Step #22590: rate 0.000020, accuracy 92.6%, cross entropy 0.234075
INFO:tensorflow:Step #22600: rate 0.000020, accuracy 95.3%, cross entropy 0.139055
INFO:tensorflow:Step #22610: rate 0.000020, accuracy 91.8%, cross entropy 0.246340
INFO:tensorflow:Step #22620: rate 0.000020, accuracy 94.1%, cross entropy 0.180103
INFO:tensorflow:Step #22630: rate 0.000020, accuracy 92.6%, cross entropy 0.249345
INFO:tensorflow:Step #22640: rate 0.000020, accuracy 94.9%, cross entropy 0.173287
INFO:tensorflow:Step #22650: rate 0.000020, accuracy 89.8%, cross entropy 0.255149
INFO:tensorflow:Step #22660: rate 0.000020, accuracy 92.6%, cross entropy 0.174444
INFO:tensorflow:Step #22670: rate 0.000020, accuracy 91.0%, cross entropy 0.252190
INFO:tensorflow:Step #22680: rate 0.000020, accuracy 91.4%, cross entropy 0.216773
INFO:tensorflow:Step #22690: rate 0.000020, accuracy 95.3%, cross entropy 0.133757
INFO:tensorflow:Step #22700: rate 0.000020, accuracy 90.6%, cross entropy 0.277387
INFO:tensorflow:Step #22710: rate 0.000020, accuracy 92.6%, cross entropy 0.276747
INFO:tensorflow:Step #22720: rate 0.000020, accuracy 92.2%, cross entropy 0.204838
INFO:tensorflow:Step #22730: rate 0.000020, accuracy 90.2%, cross entropy 0.245862
INFO:tensorflow:Step #22740: rate 0.000020, accuracy 92.2%, cross entropy 0.210702
INFO:tensorflow:Step #22750: rate 0.000020, accuracy 90.2%, cross entropy 0.276105
INFO:tensorflow:Step #22760: rate 0.000020, accuracy 92.6%, cross entropy 0.236139
INFO:tensorflow:Step #22770: rate 0.000020, accuracy 95.7%, cross entropy 0.148991
INFO:tensorflow:Step #22780: rate 0.000020, accuracy 92.6%, cross entropy 0.204371
INFO:tensorflow:Step #22790: rate 0.000020, accuracy 93.8%, cross entropy 0.209958
INFO:tensorflow:Step #22800: rate 0.000020, accuracy 90.6%, cross entropy 0.252373
INFO:tensorflow:Step #22810: rate 0.000020, accuracy 90.2%, cross entropy 0.262015
INFO:tensorflow:Step #22820: rate 0.000020, accuracy 89.5%, cross entropy 0.299603
INFO:tensorflow:Step #22830: rate 0.000020, accuracy 94.1%, cross entropy 0.199258
INFO:tensorflow:Step #22840: rate 0.000020, accuracy 90.6%, cross entropy 0.251054
INFO:tensorflow:Step #22850: rate 0.000020, accuracy 93.8%, cross entropy 0.216380
INFO:tensorflow:Step #22860: rate 0.000020, accuracy 90.6%, cross entropy 0.266192
INFO:tensorflow:Step #22870: rate 0.000020, accuracy 95.3%, cross entropy 0.145171
INFO:tensorflow:Step #22880: rate 0.000020, accuracy 93.0%, cross entropy 0.222520
INFO:tensorflow:Step #22890: rate 0.000020, accuracy 94.5%, cross entropy 0.162713
INFO:tensorflow:Step #22900: rate 0.000020, accuracy 93.4%, cross entropy 0.211775
INFO:tensorflow:Step #22910: rate 0.000020, accuracy 93.8%, cross entropy 0.181391
INFO:tensorflow:Step #22920: rate 0.000020, accuracy 91.0%, cross entropy 0.239140
INFO:tensorflow:Step #22930: rate 0.000020, accuracy 87.9%, cross entropy 0.330755
INFO:tensorflow:Step #22940: rate 0.000020, accuracy 93.4%, cross entropy 0.198473
INFO:tensorflow:Step #22950: rate 0.000020, accuracy 91.8%, cross entropy 0.211760
INFO:tensorflow:Step #22960: rate 0.000020, accuracy 89.8%, cross entropy 0.309699
INFO:tensorflow:Step #22970: rate 0.000020, accuracy 90.6%, cross entropy 0.298036
INFO:tensorflow:Step #22980: rate 0.000020, accuracy 93.0%, cross entropy 0.226954
INFO:tensorflow:Step #22990: rate 0.000020, accuracy 91.0%, cross entropy 0.209928
INFO:tensorflow:Step #23000: rate 0.000020, accuracy 91.4%, cross entropy 0.240398
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 217   6   5   2   2   1   8   5   3   4   5]
 [  0   0 250   6   2   0   2   0   1   0   0   0]
 [  0   2   1 257   1   2   1   0   0   0   0   6]
 [  0   5   0   0 241   0   0   0   0  13   1   0]
 [  0   0   1   5   0 252   0   0   1   0   1   4]
 [  0   2  10   4   1   0 229   1   0   0   0   0]
 [  0   4   0   0   1   1   2 248   0   0   0   0]
 [  0   5   0   0   5   0   0   1 242   4   0   0]
 [  0   1   0   1  16   0   0   0   4 233   0   1]
 [  0   2   0   0   7   1   0   0   0   3 230   3]
 [  0   5   0   5   7   4   0   1   0   2   2 234]]
INFO:tensorflow:Step 23000: Validation accuracy = 92.9% (N=2835)
INFO:tensorflow:Step #23010: rate 0.000020, accuracy 96.9%, cross entropy 0.101303
INFO:tensorflow:Step #23020: rate 0.000020, accuracy 90.2%, cross entropy 0.269126
INFO:tensorflow:Step #23030: rate 0.000020, accuracy 94.9%, cross entropy 0.170425
INFO:tensorflow:Step #23040: rate 0.000020, accuracy 92.6%, cross entropy 0.190470
INFO:tensorflow:Step #23050: rate 0.000020, accuracy 93.4%, cross entropy 0.212850
INFO:tensorflow:Step #23060: rate 0.000020, accuracy 93.8%, cross entropy 0.180508
INFO:tensorflow:Step #23070: rate 0.000020, accuracy 92.6%, cross entropy 0.215963
INFO:tensorflow:Step #23080: rate 0.000020, accuracy 96.1%, cross entropy 0.143021
INFO:tensorflow:Step #23090: rate 0.000020, accuracy 91.8%, cross entropy 0.195519
INFO:tensorflow:Step #23100: rate 0.000020, accuracy 93.8%, cross entropy 0.223483
INFO:tensorflow:Step #23110: rate 0.000020, accuracy 91.0%, cross entropy 0.306031
INFO:tensorflow:Step #23120: rate 0.000020, accuracy 94.9%, cross entropy 0.198455
INFO:tensorflow:Step #23130: rate 0.000020, accuracy 93.8%, cross entropy 0.203903
INFO:tensorflow:Step #23140: rate 0.000020, accuracy 93.0%, cross entropy 0.212831
INFO:tensorflow:Step #23150: rate 0.000020, accuracy 89.5%, cross entropy 0.283890
INFO:tensorflow:Step #23160: rate 0.000020, accuracy 94.5%, cross entropy 0.204634
INFO:tensorflow:Step #23170: rate 0.000020, accuracy 92.2%, cross entropy 0.226628
INFO:tensorflow:Step #23180: rate 0.000020, accuracy 93.0%, cross entropy 0.200123
INFO:tensorflow:Step #23190: rate 0.000020, accuracy 93.0%, cross entropy 0.242122
INFO:tensorflow:Step #23200: rate 0.000020, accuracy 92.6%, cross entropy 0.214860
INFO:tensorflow:Step #23210: rate 0.000020, accuracy 93.4%, cross entropy 0.228636
INFO:tensorflow:Step #23220: rate 0.000020, accuracy 91.4%, cross entropy 0.240707
INFO:tensorflow:Step #23230: rate 0.000020, accuracy 94.1%, cross entropy 0.198240
INFO:tensorflow:Step #23240: rate 0.000020, accuracy 96.5%, cross entropy 0.130841
INFO:tensorflow:Step #23250: rate 0.000020, accuracy 92.2%, cross entropy 0.226074
INFO:tensorflow:Step #23260: rate 0.000020, accuracy 93.0%, cross entropy 0.236263
INFO:tensorflow:Step #23270: rate 0.000020, accuracy 90.2%, cross entropy 0.242293
INFO:tensorflow:Step #23280: rate 0.000020, accuracy 94.1%, cross entropy 0.212827
INFO:tensorflow:Step #23290: rate 0.000020, accuracy 91.4%, cross entropy 0.218481
INFO:tensorflow:Step #23300: rate 0.000020, accuracy 92.2%, cross entropy 0.261096
INFO:tensorflow:Step #23310: rate 0.000020, accuracy 91.4%, cross entropy 0.203861
INFO:tensorflow:Step #23320: rate 0.000020, accuracy 94.1%, cross entropy 0.159945
INFO:tensorflow:Step #23330: rate 0.000020, accuracy 93.4%, cross entropy 0.207205
INFO:tensorflow:Step #23340: rate 0.000020, accuracy 92.2%, cross entropy 0.264300
INFO:tensorflow:Step #23350: rate 0.000020, accuracy 92.6%, cross entropy 0.229183
INFO:tensorflow:Step #23360: rate 0.000020, accuracy 93.4%, cross entropy 0.195916
INFO:tensorflow:Step #23370: rate 0.000020, accuracy 92.2%, cross entropy 0.211268
INFO:tensorflow:Step #23380: rate 0.000020, accuracy 91.8%, cross entropy 0.264797
INFO:tensorflow:Step #23390: rate 0.000020, accuracy 91.4%, cross entropy 0.237979
INFO:tensorflow:Step #23400: rate 0.000020, accuracy 95.3%, cross entropy 0.150233
INFO:tensorflow:Step #23410: rate 0.000020, accuracy 92.6%, cross entropy 0.205790
INFO:tensorflow:Step #23420: rate 0.000020, accuracy 92.2%, cross entropy 0.223962
INFO:tensorflow:Step #23430: rate 0.000020, accuracy 94.1%, cross entropy 0.201008
INFO:tensorflow:Step #23440: rate 0.000020, accuracy 89.8%, cross entropy 0.290644
INFO:tensorflow:Step #23450: rate 0.000020, accuracy 89.5%, cross entropy 0.316550
INFO:tensorflow:Step #23460: rate 0.000020, accuracy 90.6%, cross entropy 0.240327
INFO:tensorflow:Step #23470: rate 0.000020, accuracy 92.6%, cross entropy 0.245213
INFO:tensorflow:Step #23480: rate 0.000020, accuracy 94.5%, cross entropy 0.173226
INFO:tensorflow:Step #23490: rate 0.000020, accuracy 95.3%, cross entropy 0.108140
INFO:tensorflow:Step #23500: rate 0.000020, accuracy 93.0%, cross entropy 0.233681
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 216   7   5   2   2   2   8   5   3   4   4]
 [  0   0 250   6   2   0   2   0   1   0   0   0]
 [  0   2   1 257   1   2   1   0   0   0   0   6]
 [  0   5   0   0 241   0   0   0   0  13   1   0]
 [  0   0   1   5   0 252   0   0   1   0   1   4]
 [  0   2   8   4   1   0 231   1   0   0   0   0]
 [  0   4   0   0   1   0   2 249   0   0   0   0]
 [  0   5   0   0   3   0   0   2 243   4   0   0]
 [  0   1   0   1  17   0   0   0   5 231   0   1]
 [  0   2   0   0   7   0   0   0   0   3 231   3]
 [  0   5   0   6   6   4   0   2   0   2   2 233]]
INFO:tensorflow:Step 23500: Validation accuracy = 92.9% (N=2835)
INFO:tensorflow:Step #23510: rate 0.000020, accuracy 90.2%, cross entropy 0.271275
INFO:tensorflow:Step #23520: rate 0.000020, accuracy 89.5%, cross entropy 0.348144
INFO:tensorflow:Step #23530: rate 0.000020, accuracy 90.6%, cross entropy 0.291009
INFO:tensorflow:Step #23540: rate 0.000020, accuracy 94.5%, cross entropy 0.185754
INFO:tensorflow:Step #23550: rate 0.000020, accuracy 91.8%, cross entropy 0.238212
INFO:tensorflow:Step #23560: rate 0.000020, accuracy 91.8%, cross entropy 0.292476
INFO:tensorflow:Step #23570: rate 0.000020, accuracy 92.2%, cross entropy 0.214973
INFO:tensorflow:Step #23580: rate 0.000020, accuracy 93.4%, cross entropy 0.201535
INFO:tensorflow:Step #23590: rate 0.000020, accuracy 93.4%, cross entropy 0.212320
INFO:tensorflow:Step #23600: rate 0.000020, accuracy 90.6%, cross entropy 0.309433
INFO:tensorflow:Step #23610: rate 0.000020, accuracy 91.0%, cross entropy 0.268469
INFO:tensorflow:Step #23620: rate 0.000020, accuracy 91.8%, cross entropy 0.235631
INFO:tensorflow:Step #23630: rate 0.000020, accuracy 92.6%, cross entropy 0.189316
INFO:tensorflow:Step #23640: rate 0.000020, accuracy 90.2%, cross entropy 0.303607
INFO:tensorflow:Step #23650: rate 0.000020, accuracy 91.8%, cross entropy 0.233804
INFO:tensorflow:Step #23660: rate 0.000020, accuracy 90.2%, cross entropy 0.299668
INFO:tensorflow:Step #23670: rate 0.000020, accuracy 94.1%, cross entropy 0.149857
INFO:tensorflow:Step #23680: rate 0.000020, accuracy 91.4%, cross entropy 0.267516
INFO:tensorflow:Step #23690: rate 0.000020, accuracy 93.4%, cross entropy 0.198987
INFO:tensorflow:Step #23700: rate 0.000020, accuracy 92.6%, cross entropy 0.268210
INFO:tensorflow:Step #23710: rate 0.000020, accuracy 93.8%, cross entropy 0.176835
INFO:tensorflow:Step #23720: rate 0.000020, accuracy 95.7%, cross entropy 0.161799
INFO:tensorflow:Step #23730: rate 0.000020, accuracy 91.8%, cross entropy 0.218942
INFO:tensorflow:Step #23740: rate 0.000020, accuracy 91.4%, cross entropy 0.235729
INFO:tensorflow:Step #23750: rate 0.000020, accuracy 92.2%, cross entropy 0.220336
INFO:tensorflow:Step #23760: rate 0.000020, accuracy 93.4%, cross entropy 0.197919
INFO:tensorflow:Step #23770: rate 0.000020, accuracy 93.4%, cross entropy 0.234914
INFO:tensorflow:Step #23780: rate 0.000020, accuracy 90.6%, cross entropy 0.240907
INFO:tensorflow:Step #23790: rate 0.000020, accuracy 93.4%, cross entropy 0.198347
INFO:tensorflow:Step #23800: rate 0.000020, accuracy 93.8%, cross entropy 0.167220
INFO:tensorflow:Step #23810: rate 0.000020, accuracy 92.2%, cross entropy 0.217962
INFO:tensorflow:Step #23820: rate 0.000020, accuracy 94.1%, cross entropy 0.172111
INFO:tensorflow:Step #23830: rate 0.000020, accuracy 92.6%, cross entropy 0.198358
INFO:tensorflow:Step #23840: rate 0.000020, accuracy 91.0%, cross entropy 0.299078
INFO:tensorflow:Step #23850: rate 0.000020, accuracy 90.6%, cross entropy 0.286411
INFO:tensorflow:Step #23860: rate 0.000020, accuracy 91.0%, cross entropy 0.260809
INFO:tensorflow:Step #23870: rate 0.000020, accuracy 94.9%, cross entropy 0.177322
INFO:tensorflow:Step #23880: rate 0.000020, accuracy 90.2%, cross entropy 0.268620
INFO:tensorflow:Step #23890: rate 0.000020, accuracy 93.0%, cross entropy 0.198158
INFO:tensorflow:Step #23900: rate 0.000020, accuracy 94.9%, cross entropy 0.161135
INFO:tensorflow:Step #23910: rate 0.000020, accuracy 93.8%, cross entropy 0.223829
INFO:tensorflow:Step #23920: rate 0.000020, accuracy 92.6%, cross entropy 0.229528
INFO:tensorflow:Step #23930: rate 0.000020, accuracy 92.6%, cross entropy 0.249376
INFO:tensorflow:Step #23940: rate 0.000020, accuracy 91.8%, cross entropy 0.231191
INFO:tensorflow:Step #23950: rate 0.000020, accuracy 92.2%, cross entropy 0.244552
INFO:tensorflow:Step #23960: rate 0.000020, accuracy 94.5%, cross entropy 0.155097
INFO:tensorflow:Step #23970: rate 0.000020, accuracy 90.2%, cross entropy 0.285022
INFO:tensorflow:Step #23980: rate 0.000020, accuracy 92.6%, cross entropy 0.199786
INFO:tensorflow:Step #23990: rate 0.000020, accuracy 94.5%, cross entropy 0.195310
INFO:tensorflow:Step #24000: rate 0.000020, accuracy 94.9%, cross entropy 0.205938
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 215   7   5   2   2   2   8   5   3   4   5]
 [  0   0 250   6   2   0   2   0   1   0   0   0]
 [  0   2   1 257   1   2   1   0   0   0   0   6]
 [  0   5   0   0 242   0   0   0   0  12   1   0]
 [  0   0   1   5   0 253   0   0   1   0   1   3]
 [  0   1   8   4   1   0 232   1   0   0   0   0]
 [  0   4   0   0   1   1   2 248   0   0   0   0]
 [  0   5   0   0   5   0   0   1 241   5   0   0]
 [  0   1   0   1  17   0   0   0   5 231   0   1]
 [  0   2   0   0   7   0   0   0   0   3 231   3]
 [  0   5   0   7   6   4   0   1   0   3   2 232]]
INFO:tensorflow:Step 24000: Validation accuracy = 92.8% (N=2835)
INFO:tensorflow:Saving to "F:\ML_Project\Data\logs&checkpoint\c_rnn\ckpt-24000"
INFO:tensorflow:Step #24010: rate 0.000020, accuracy 91.4%, cross entropy 0.235842
INFO:tensorflow:Step #24020: rate 0.000020, accuracy 93.0%, cross entropy 0.256397
INFO:tensorflow:Step #24030: rate 0.000020, accuracy 93.4%, cross entropy 0.176012
INFO:tensorflow:Step #24040: rate 0.000020, accuracy 92.6%, cross entropy 0.220536
INFO:tensorflow:Step #24050: rate 0.000020, accuracy 91.4%, cross entropy 0.256542
INFO:tensorflow:Step #24060: rate 0.000020, accuracy 93.4%, cross entropy 0.225411
INFO:tensorflow:Step #24070: rate 0.000020, accuracy 91.0%, cross entropy 0.217913
INFO:tensorflow:Step #24080: rate 0.000020, accuracy 92.6%, cross entropy 0.252284
INFO:tensorflow:Step #24090: rate 0.000020, accuracy 92.2%, cross entropy 0.289721
INFO:tensorflow:Step #24100: rate 0.000020, accuracy 94.1%, cross entropy 0.202949
INFO:tensorflow:Step #24110: rate 0.000020, accuracy 91.8%, cross entropy 0.237964
INFO:tensorflow:Step #24120: rate 0.000020, accuracy 92.2%, cross entropy 0.239492
INFO:tensorflow:Step #24130: rate 0.000020, accuracy 93.0%, cross entropy 0.178342
INFO:tensorflow:Step #24140: rate 0.000020, accuracy 90.2%, cross entropy 0.279321
INFO:tensorflow:Step #24150: rate 0.000020, accuracy 94.1%, cross entropy 0.164627
INFO:tensorflow:Step #24160: rate 0.000020, accuracy 91.4%, cross entropy 0.220247
INFO:tensorflow:Step #24170: rate 0.000020, accuracy 91.8%, cross entropy 0.275613
INFO:tensorflow:Step #24180: rate 0.000020, accuracy 90.6%, cross entropy 0.275955
INFO:tensorflow:Step #24190: rate 0.000020, accuracy 93.0%, cross entropy 0.281593
INFO:tensorflow:Step #24200: rate 0.000020, accuracy 93.8%, cross entropy 0.182021
INFO:tensorflow:Step #24210: rate 0.000020, accuracy 91.8%, cross entropy 0.257157
INFO:tensorflow:Step #24220: rate 0.000020, accuracy 90.2%, cross entropy 0.267270
INFO:tensorflow:Step #24230: rate 0.000020, accuracy 92.2%, cross entropy 0.200127
INFO:tensorflow:Step #24240: rate 0.000020, accuracy 92.2%, cross entropy 0.241889
INFO:tensorflow:Step #24250: rate 0.000020, accuracy 89.5%, cross entropy 0.290148
INFO:tensorflow:Step #24260: rate 0.000020, accuracy 89.8%, cross entropy 0.269348
INFO:tensorflow:Step #24270: rate 0.000020, accuracy 94.1%, cross entropy 0.208909
INFO:tensorflow:Step #24280: rate 0.000020, accuracy 92.6%, cross entropy 0.208505
INFO:tensorflow:Step #24290: rate 0.000020, accuracy 91.8%, cross entropy 0.246753
INFO:tensorflow:Step #24300: rate 0.000020, accuracy 93.8%, cross entropy 0.205648
INFO:tensorflow:Step #24310: rate 0.000020, accuracy 93.0%, cross entropy 0.188803
INFO:tensorflow:Step #24320: rate 0.000020, accuracy 94.9%, cross entropy 0.155265
INFO:tensorflow:Step #24330: rate 0.000020, accuracy 91.4%, cross entropy 0.234518
INFO:tensorflow:Step #24340: rate 0.000020, accuracy 93.0%, cross entropy 0.240100
INFO:tensorflow:Step #24350: rate 0.000020, accuracy 92.6%, cross entropy 0.229942
INFO:tensorflow:Step #24360: rate 0.000020, accuracy 92.2%, cross entropy 0.230796
INFO:tensorflow:Step #24370: rate 0.000020, accuracy 94.9%, cross entropy 0.140538
INFO:tensorflow:Step #24380: rate 0.000020, accuracy 92.2%, cross entropy 0.201685
INFO:tensorflow:Step #24390: rate 0.000020, accuracy 89.8%, cross entropy 0.248077
INFO:tensorflow:Step #24400: rate 0.000020, accuracy 93.0%, cross entropy 0.205993
INFO:tensorflow:Step #24410: rate 0.000020, accuracy 93.0%, cross entropy 0.222079
INFO:tensorflow:Step #24420: rate 0.000020, accuracy 94.9%, cross entropy 0.164624
INFO:tensorflow:Step #24430: rate 0.000020, accuracy 87.9%, cross entropy 0.364804
INFO:tensorflow:Step #24440: rate 0.000020, accuracy 94.5%, cross entropy 0.190868
INFO:tensorflow:Step #24450: rate 0.000020, accuracy 92.2%, cross entropy 0.229163
INFO:tensorflow:Step #24460: rate 0.000020, accuracy 94.1%, cross entropy 0.262672
INFO:tensorflow:Step #24470: rate 0.000020, accuracy 93.0%, cross entropy 0.203265
INFO:tensorflow:Step #24480: rate 0.000020, accuracy 91.4%, cross entropy 0.261158
INFO:tensorflow:Step #24490: rate 0.000020, accuracy 93.8%, cross entropy 0.213344
INFO:tensorflow:Step #24500: rate 0.000020, accuracy 93.4%, cross entropy 0.188966
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 217   5   4   2   1   2   8   5   3   4   7]
 [  0   0 250   6   2   0   2   0   1   0   0   0]
 [  0   2   1 257   1   2   1   0   0   0   0   6]
 [  0   5   0   0 241   0   0   0   0  13   1   0]
 [  0   0   1   5   0 253   0   0   1   0   1   3]
 [  0   2   8   4   1   0 231   1   0   0   0   0]
 [  0   4   0   0   1   0   2 249   0   0   0   0]
 [  0   5   0   0   3   0   0   2 242   5   0   0]
 [  0   1   0   1  18   0   0   0   4 231   0   1]
 [  0   2   0   0   7   0   0   0   0   3 231   3]
 [  0   6   0   5   6   4   0   1   0   3   2 233]]
INFO:tensorflow:Step 24500: Validation accuracy = 92.9% (N=2835)
INFO:tensorflow:Step #24510: rate 0.000020, accuracy 93.8%, cross entropy 0.231462
INFO:tensorflow:Step #24520: rate 0.000020, accuracy 93.4%, cross entropy 0.231743
INFO:tensorflow:Step #24530: rate 0.000020, accuracy 90.2%, cross entropy 0.260827
INFO:tensorflow:Step #24540: rate 0.000020, accuracy 93.0%, cross entropy 0.201092
INFO:tensorflow:Step #24550: rate 0.000020, accuracy 96.1%, cross entropy 0.148132
INFO:tensorflow:Step #24560: rate 0.000020, accuracy 95.3%, cross entropy 0.169378
INFO:tensorflow:Step #24570: rate 0.000020, accuracy 91.4%, cross entropy 0.234262
INFO:tensorflow:Step #24580: rate 0.000020, accuracy 90.6%, cross entropy 0.252393
INFO:tensorflow:Step #24590: rate 0.000020, accuracy 92.6%, cross entropy 0.187204
INFO:tensorflow:Step #24600: rate 0.000020, accuracy 90.6%, cross entropy 0.276962
INFO:tensorflow:Step #24610: rate 0.000020, accuracy 92.6%, cross entropy 0.183811
INFO:tensorflow:Step #24620: rate 0.000020, accuracy 93.0%, cross entropy 0.221376
INFO:tensorflow:Step #24630: rate 0.000020, accuracy 90.6%, cross entropy 0.311814
INFO:tensorflow:Step #24640: rate 0.000020, accuracy 93.8%, cross entropy 0.214084
INFO:tensorflow:Step #24650: rate 0.000020, accuracy 93.0%, cross entropy 0.169434
INFO:tensorflow:Step #24660: rate 0.000020, accuracy 93.8%, cross entropy 0.178515
INFO:tensorflow:Step #24670: rate 0.000020, accuracy 91.8%, cross entropy 0.203335
INFO:tensorflow:Step #24680: rate 0.000020, accuracy 91.4%, cross entropy 0.277760
INFO:tensorflow:Step #24690: rate 0.000020, accuracy 90.6%, cross entropy 0.285752
INFO:tensorflow:Step #24700: rate 0.000020, accuracy 95.7%, cross entropy 0.146947
INFO:tensorflow:Step #24710: rate 0.000020, accuracy 92.6%, cross entropy 0.235564
INFO:tensorflow:Step #24720: rate 0.000020, accuracy 93.8%, cross entropy 0.172436
INFO:tensorflow:Step #24730: rate 0.000020, accuracy 94.1%, cross entropy 0.179889
INFO:tensorflow:Step #24740: rate 0.000020, accuracy 91.4%, cross entropy 0.248150
INFO:tensorflow:Step #24750: rate 0.000020, accuracy 89.5%, cross entropy 0.272013
INFO:tensorflow:Step #24760: rate 0.000020, accuracy 93.8%, cross entropy 0.201132
INFO:tensorflow:Step #24770: rate 0.000020, accuracy 92.2%, cross entropy 0.213136
INFO:tensorflow:Step #24780: rate 0.000020, accuracy 91.0%, cross entropy 0.250874
INFO:tensorflow:Step #24790: rate 0.000020, accuracy 89.5%, cross entropy 0.282766
INFO:tensorflow:Step #24800: rate 0.000020, accuracy 94.1%, cross entropy 0.202257
INFO:tensorflow:Step #24810: rate 0.000020, accuracy 91.4%, cross entropy 0.210020
INFO:tensorflow:Step #24820: rate 0.000020, accuracy 87.5%, cross entropy 0.372040
INFO:tensorflow:Step #24830: rate 0.000020, accuracy 94.1%, cross entropy 0.198312
INFO:tensorflow:Step #24840: rate 0.000020, accuracy 93.0%, cross entropy 0.211668
INFO:tensorflow:Step #24850: rate 0.000020, accuracy 91.0%, cross entropy 0.218574
INFO:tensorflow:Step #24860: rate 0.000020, accuracy 93.0%, cross entropy 0.219841
INFO:tensorflow:Step #24870: rate 0.000020, accuracy 93.8%, cross entropy 0.204559
INFO:tensorflow:Step #24880: rate 0.000020, accuracy 94.9%, cross entropy 0.200825
INFO:tensorflow:Step #24890: rate 0.000020, accuracy 89.8%, cross entropy 0.287325
INFO:tensorflow:Step #24900: rate 0.000020, accuracy 93.0%, cross entropy 0.207222
INFO:tensorflow:Step #24910: rate 0.000020, accuracy 91.8%, cross entropy 0.211626
INFO:tensorflow:Step #24920: rate 0.000020, accuracy 93.4%, cross entropy 0.187285
INFO:tensorflow:Step #24930: rate 0.000020, accuracy 93.8%, cross entropy 0.187549
INFO:tensorflow:Step #24940: rate 0.000020, accuracy 93.0%, cross entropy 0.285353
INFO:tensorflow:Step #24950: rate 0.000020, accuracy 91.0%, cross entropy 0.239994
INFO:tensorflow:Step #24960: rate 0.000020, accuracy 92.2%, cross entropy 0.241091
INFO:tensorflow:Step #24970: rate 0.000020, accuracy 93.4%, cross entropy 0.187228
INFO:tensorflow:Step #24980: rate 0.000020, accuracy 93.4%, cross entropy 0.183938
INFO:tensorflow:Step #24990: rate 0.000020, accuracy 91.0%, cross entropy 0.311596
INFO:tensorflow:Step #25000: rate 0.000020, accuracy 94.9%, cross entropy 0.170364
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 214   6   5   3   2   1   7   5   3   5   7]
 [  0   0 249   6   2   0   3   0   1   0   0   0]
 [  0   2   1 257   1   2   1   0   0   0   0   6]
 [  0   5   0   0 242   0   0   0   0  12   1   0]
 [  0   0   1   5   0 252   0   0   1   0   1   4]
 [  0   2   8   4   1   0 231   1   0   0   0   0]
 [  0   4   0   0   1   1   2 248   0   0   0   0]
 [  0   5   0   0   5   0   0   1 241   5   0   0]
 [  0   1   0   1  16   0   0   0   5 232   0   1]
 [  0   2   0   0   7   0   0   0   0   2 232   3]
 [  0   5   0   6   7   4   0   1   0   2   2 233]]
INFO:tensorflow:Step 25000: Validation accuracy = 92.8% (N=2835)
INFO:tensorflow:Step #25010: rate 0.000020, accuracy 93.0%, cross entropy 0.246305
INFO:tensorflow:Step #25020: rate 0.000020, accuracy 91.4%, cross entropy 0.265104
INFO:tensorflow:Step #25030: rate 0.000020, accuracy 94.5%, cross entropy 0.164892
INFO:tensorflow:Step #25040: rate 0.000020, accuracy 92.2%, cross entropy 0.246288
INFO:tensorflow:Step #25050: rate 0.000020, accuracy 94.1%, cross entropy 0.164741
INFO:tensorflow:Step #25060: rate 0.000020, accuracy 89.5%, cross entropy 0.296583
INFO:tensorflow:Step #25070: rate 0.000020, accuracy 93.0%, cross entropy 0.199220
INFO:tensorflow:Step #25080: rate 0.000020, accuracy 92.2%, cross entropy 0.243543
INFO:tensorflow:Step #25090: rate 0.000020, accuracy 93.8%, cross entropy 0.231417
INFO:tensorflow:Step #25100: rate 0.000020, accuracy 96.1%, cross entropy 0.123631
INFO:tensorflow:Step #25110: rate 0.000020, accuracy 92.2%, cross entropy 0.235084
INFO:tensorflow:Step #25120: rate 0.000020, accuracy 93.8%, cross entropy 0.215507
INFO:tensorflow:Step #25130: rate 0.000020, accuracy 92.6%, cross entropy 0.242306
INFO:tensorflow:Step #25140: rate 0.000020, accuracy 93.4%, cross entropy 0.213064
INFO:tensorflow:Step #25150: rate 0.000020, accuracy 92.2%, cross entropy 0.185160
INFO:tensorflow:Step #25160: rate 0.000020, accuracy 92.2%, cross entropy 0.203929
INFO:tensorflow:Step #25170: rate 0.000020, accuracy 90.6%, cross entropy 0.251635
INFO:tensorflow:Step #25180: rate 0.000020, accuracy 93.0%, cross entropy 0.194575
INFO:tensorflow:Step #25190: rate 0.000020, accuracy 90.6%, cross entropy 0.241002
INFO:tensorflow:Step #25200: rate 0.000020, accuracy 93.8%, cross entropy 0.222072
INFO:tensorflow:Step #25210: rate 0.000020, accuracy 90.2%, cross entropy 0.243053
INFO:tensorflow:Step #25220: rate 0.000020, accuracy 91.0%, cross entropy 0.276431
INFO:tensorflow:Step #25230: rate 0.000020, accuracy 94.1%, cross entropy 0.134901
INFO:tensorflow:Step #25240: rate 0.000020, accuracy 91.8%, cross entropy 0.242152
INFO:tensorflow:Step #25250: rate 0.000020, accuracy 93.0%, cross entropy 0.227618
INFO:tensorflow:Step #25260: rate 0.000020, accuracy 91.0%, cross entropy 0.265348
INFO:tensorflow:Step #25270: rate 0.000020, accuracy 91.8%, cross entropy 0.220131
INFO:tensorflow:Step #25280: rate 0.000020, accuracy 92.2%, cross entropy 0.224849
INFO:tensorflow:Step #25290: rate 0.000020, accuracy 93.4%, cross entropy 0.206480
INFO:tensorflow:Step #25300: rate 0.000020, accuracy 91.8%, cross entropy 0.241773
INFO:tensorflow:Step #25310: rate 0.000020, accuracy 91.4%, cross entropy 0.246966
INFO:tensorflow:Step #25320: rate 0.000020, accuracy 91.8%, cross entropy 0.243331
INFO:tensorflow:Step #25330: rate 0.000020, accuracy 93.0%, cross entropy 0.186994
INFO:tensorflow:Step #25340: rate 0.000020, accuracy 91.0%, cross entropy 0.217872
INFO:tensorflow:Step #25350: rate 0.000020, accuracy 94.1%, cross entropy 0.167602
INFO:tensorflow:Step #25360: rate 0.000020, accuracy 92.2%, cross entropy 0.265311
INFO:tensorflow:Step #25370: rate 0.000020, accuracy 93.8%, cross entropy 0.173320
INFO:tensorflow:Step #25380: rate 0.000020, accuracy 93.8%, cross entropy 0.160420
INFO:tensorflow:Step #25390: rate 0.000020, accuracy 91.4%, cross entropy 0.222162
INFO:tensorflow:Step #25400: rate 0.000020, accuracy 93.0%, cross entropy 0.210149
INFO:tensorflow:Step #25410: rate 0.000020, accuracy 93.4%, cross entropy 0.231733
INFO:tensorflow:Step #25420: rate 0.000020, accuracy 94.5%, cross entropy 0.187559
INFO:tensorflow:Step #25430: rate 0.000020, accuracy 93.4%, cross entropy 0.207033
INFO:tensorflow:Step #25440: rate 0.000020, accuracy 91.8%, cross entropy 0.248922
INFO:tensorflow:Step #25450: rate 0.000020, accuracy 91.8%, cross entropy 0.211091
INFO:tensorflow:Step #25460: rate 0.000020, accuracy 94.5%, cross entropy 0.191267
INFO:tensorflow:Step #25470: rate 0.000020, accuracy 95.3%, cross entropy 0.151913
INFO:tensorflow:Step #25480: rate 0.000020, accuracy 91.4%, cross entropy 0.254715
INFO:tensorflow:Step #25490: rate 0.000020, accuracy 92.6%, cross entropy 0.233019
INFO:tensorflow:Step #25500: rate 0.000020, accuracy 93.0%, cross entropy 0.196489
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 214   6   6   2   2   1   8   5   3   4   7]
 [  0   0 248   6   2   0   4   0   1   0   0   0]
 [  0   2   1 258   1   1   1   0   0   0   0   6]
 [  0   5   0   0 240   0   1   0   0  13   1   0]
 [  0   0   1   5   0 253   0   0   1   0   1   3]
 [  0   1   8   4   1   0 232   1   0   0   0   0]
 [  0   4   0   0   1   1   2 248   0   0   0   0]
 [  0   5   0   0   3   1   0   2 242   4   0   0]
 [  0   1   0   1  16   0   0   0   6 231   0   1]
 [  0   2   0   0   7   1   0   0   0   3 230   3]
 [  0   5   0   8   6   4   0   2   0   2   2 231]]
INFO:tensorflow:Step 25500: Validation accuracy = 92.7% (N=2835)
INFO:tensorflow:Step #25510: rate 0.000020, accuracy 92.6%, cross entropy 0.220591
INFO:tensorflow:Step #25520: rate 0.000020, accuracy 94.5%, cross entropy 0.243171
INFO:tensorflow:Step #25530: rate 0.000020, accuracy 88.3%, cross entropy 0.312858
INFO:tensorflow:Step #25540: rate 0.000020, accuracy 94.5%, cross entropy 0.170183
INFO:tensorflow:Step #25550: rate 0.000020, accuracy 91.4%, cross entropy 0.240890
INFO:tensorflow:Step #25560: rate 0.000020, accuracy 89.1%, cross entropy 0.317149
INFO:tensorflow:Step #25570: rate 0.000020, accuracy 91.0%, cross entropy 0.244612
INFO:tensorflow:Step #25580: rate 0.000020, accuracy 92.2%, cross entropy 0.225652
INFO:tensorflow:Step #25590: rate 0.000020, accuracy 92.6%, cross entropy 0.203041
INFO:tensorflow:Step #25600: rate 0.000020, accuracy 94.1%, cross entropy 0.183186
INFO:tensorflow:Step #25610: rate 0.000020, accuracy 93.0%, cross entropy 0.241692
INFO:tensorflow:Step #25620: rate 0.000020, accuracy 91.4%, cross entropy 0.202807
INFO:tensorflow:Step #25630: rate 0.000020, accuracy 93.0%, cross entropy 0.199234
INFO:tensorflow:Step #25640: rate 0.000020, accuracy 93.8%, cross entropy 0.171682
INFO:tensorflow:Step #25650: rate 0.000020, accuracy 91.8%, cross entropy 0.226179
INFO:tensorflow:Step #25660: rate 0.000020, accuracy 94.9%, cross entropy 0.204622
INFO:tensorflow:Step #25670: rate 0.000020, accuracy 91.8%, cross entropy 0.237505
INFO:tensorflow:Step #25680: rate 0.000020, accuracy 92.6%, cross entropy 0.204062
INFO:tensorflow:Step #25690: rate 0.000020, accuracy 90.6%, cross entropy 0.243295
INFO:tensorflow:Step #25700: rate 0.000020, accuracy 94.5%, cross entropy 0.192277
INFO:tensorflow:Step #25710: rate 0.000020, accuracy 93.8%, cross entropy 0.202192
INFO:tensorflow:Step #25720: rate 0.000020, accuracy 91.0%, cross entropy 0.261115
INFO:tensorflow:Step #25730: rate 0.000020, accuracy 88.3%, cross entropy 0.314284
INFO:tensorflow:Step #25740: rate 0.000020, accuracy 93.8%, cross entropy 0.234831
INFO:tensorflow:Step #25750: rate 0.000020, accuracy 90.2%, cross entropy 0.294953
INFO:tensorflow:Step #25760: rate 0.000020, accuracy 92.2%, cross entropy 0.211505
INFO:tensorflow:Step #25770: rate 0.000020, accuracy 93.4%, cross entropy 0.181406
INFO:tensorflow:Step #25780: rate 0.000020, accuracy 93.4%, cross entropy 0.214752
INFO:tensorflow:Step #25790: rate 0.000020, accuracy 91.0%, cross entropy 0.260731
INFO:tensorflow:Step #25800: rate 0.000020, accuracy 93.8%, cross entropy 0.197998
INFO:tensorflow:Step #25810: rate 0.000020, accuracy 90.2%, cross entropy 0.311204
INFO:tensorflow:Step #25820: rate 0.000020, accuracy 90.6%, cross entropy 0.314652
INFO:tensorflow:Step #25830: rate 0.000020, accuracy 93.4%, cross entropy 0.213047
INFO:tensorflow:Step #25840: rate 0.000020, accuracy 93.8%, cross entropy 0.226877
INFO:tensorflow:Step #25850: rate 0.000020, accuracy 93.8%, cross entropy 0.165317
INFO:tensorflow:Step #25860: rate 0.000020, accuracy 94.5%, cross entropy 0.199505
INFO:tensorflow:Step #25870: rate 0.000020, accuracy 93.0%, cross entropy 0.244925
INFO:tensorflow:Step #25880: rate 0.000020, accuracy 93.4%, cross entropy 0.222796
INFO:tensorflow:Step #25890: rate 0.000020, accuracy 92.6%, cross entropy 0.174984
INFO:tensorflow:Step #25900: rate 0.000020, accuracy 94.5%, cross entropy 0.167832
INFO:tensorflow:Step #25910: rate 0.000020, accuracy 91.0%, cross entropy 0.264830
INFO:tensorflow:Step #25920: rate 0.000020, accuracy 94.9%, cross entropy 0.178557
INFO:tensorflow:Step #25930: rate 0.000020, accuracy 91.8%, cross entropy 0.240925
INFO:tensorflow:Step #25940: rate 0.000020, accuracy 95.3%, cross entropy 0.164688
INFO:tensorflow:Step #25950: rate 0.000020, accuracy 93.8%, cross entropy 0.199845
INFO:tensorflow:Step #25960: rate 0.000020, accuracy 92.6%, cross entropy 0.221156
INFO:tensorflow:Step #25970: rate 0.000020, accuracy 94.1%, cross entropy 0.179619
INFO:tensorflow:Step #25980: rate 0.000020, accuracy 92.2%, cross entropy 0.231874
INFO:tensorflow:Step #25990: rate 0.000020, accuracy 93.8%, cross entropy 0.198051
INFO:tensorflow:Step #26000: rate 0.000020, accuracy 90.6%, cross entropy 0.285153
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 218   5   6   2   1   1   7   5   3   5   5]
 [  0   0 249   6   2   0   3   0   1   0   0   0]
 [  0   2   1 259   1   1   0   0   0   0   0   6]
 [  0   5   0   0 240   0   1   0   0  13   1   0]
 [  0   1   1   5   0 252   0   0   1   0   1   3]
 [  0   2   8   4   1   0 231   1   0   0   0   0]
 [  0   4   0   0   1   0   2 249   0   0   0   0]
 [  0   5   0   0   3   0   0   3 242   4   0   0]
 [  0   1   0   1  18   0   0   0   5 230   0   1]
 [  0   2   0   0   7   1   0   0   0   3 230   3]
 [  0   5   0   7   6   4   0   2   0   2   2 232]]
INFO:tensorflow:Step 26000: Validation accuracy = 92.8% (N=2835)
INFO:tensorflow:Saving to "F:\ML_Project\Data\logs&checkpoint\c_rnn\ckpt-26000"
INFO:tensorflow:Step #26010: rate 0.000020, accuracy 93.4%, cross entropy 0.218370
INFO:tensorflow:Step #26020: rate 0.000020, accuracy 93.8%, cross entropy 0.189010
INFO:tensorflow:Step #26030: rate 0.000020, accuracy 90.2%, cross entropy 0.310205
INFO:tensorflow:Step #26040: rate 0.000020, accuracy 94.9%, cross entropy 0.157249
INFO:tensorflow:Step #26050: rate 0.000020, accuracy 93.4%, cross entropy 0.201296
INFO:tensorflow:Step #26060: rate 0.000020, accuracy 93.0%, cross entropy 0.219248
INFO:tensorflow:Step #26070: rate 0.000020, accuracy 93.0%, cross entropy 0.228074
INFO:tensorflow:Step #26080: rate 0.000020, accuracy 89.5%, cross entropy 0.271954
INFO:tensorflow:Step #26090: rate 0.000020, accuracy 93.4%, cross entropy 0.186615
INFO:tensorflow:Step #26100: rate 0.000020, accuracy 95.7%, cross entropy 0.176850
INFO:tensorflow:Step #26110: rate 0.000020, accuracy 89.5%, cross entropy 0.290568
INFO:tensorflow:Step #26120: rate 0.000020, accuracy 94.1%, cross entropy 0.173773
INFO:tensorflow:Step #26130: rate 0.000020, accuracy 91.8%, cross entropy 0.252175
INFO:tensorflow:Step #26140: rate 0.000020, accuracy 92.2%, cross entropy 0.212264
INFO:tensorflow:Step #26150: rate 0.000020, accuracy 94.5%, cross entropy 0.201202
INFO:tensorflow:Step #26160: rate 0.000020, accuracy 92.2%, cross entropy 0.215491
INFO:tensorflow:Step #26170: rate 0.000020, accuracy 92.6%, cross entropy 0.219075
INFO:tensorflow:Step #26180: rate 0.000020, accuracy 94.1%, cross entropy 0.199061
INFO:tensorflow:Step #26190: rate 0.000020, accuracy 94.5%, cross entropy 0.178288
INFO:tensorflow:Step #26200: rate 0.000020, accuracy 96.1%, cross entropy 0.138666
INFO:tensorflow:Step #26210: rate 0.000020, accuracy 90.2%, cross entropy 0.260012
INFO:tensorflow:Step #26220: rate 0.000020, accuracy 95.3%, cross entropy 0.152661
INFO:tensorflow:Step #26230: rate 0.000020, accuracy 94.1%, cross entropy 0.197458
INFO:tensorflow:Step #26240: rate 0.000020, accuracy 93.4%, cross entropy 0.172365
INFO:tensorflow:Step #26250: rate 0.000020, accuracy 93.8%, cross entropy 0.231944
INFO:tensorflow:Step #26260: rate 0.000020, accuracy 94.1%, cross entropy 0.158078
INFO:tensorflow:Step #26270: rate 0.000020, accuracy 92.6%, cross entropy 0.235483
INFO:tensorflow:Step #26280: rate 0.000020, accuracy 91.0%, cross entropy 0.317775
INFO:tensorflow:Step #26290: rate 0.000020, accuracy 93.0%, cross entropy 0.256373
INFO:tensorflow:Step #26300: rate 0.000020, accuracy 90.6%, cross entropy 0.269528
INFO:tensorflow:Step #26310: rate 0.000020, accuracy 92.2%, cross entropy 0.228489
INFO:tensorflow:Step #26320: rate 0.000020, accuracy 91.8%, cross entropy 0.245770
INFO:tensorflow:Step #26330: rate 0.000020, accuracy 93.4%, cross entropy 0.205982
INFO:tensorflow:Step #26340: rate 0.000020, accuracy 90.6%, cross entropy 0.269190
INFO:tensorflow:Step #26350: rate 0.000020, accuracy 92.6%, cross entropy 0.251194
INFO:tensorflow:Step #26360: rate 0.000020, accuracy 90.2%, cross entropy 0.263041
INFO:tensorflow:Step #26370: rate 0.000020, accuracy 90.2%, cross entropy 0.274748
INFO:tensorflow:Step #26380: rate 0.000020, accuracy 91.0%, cross entropy 0.269259
INFO:tensorflow:Step #26390: rate 0.000020, accuracy 93.0%, cross entropy 0.197158
INFO:tensorflow:Step #26400: rate 0.000020, accuracy 93.4%, cross entropy 0.169564
INFO:tensorflow:Step #26410: rate 0.000020, accuracy 93.8%, cross entropy 0.215585
INFO:tensorflow:Step #26420: rate 0.000020, accuracy 92.2%, cross entropy 0.217689
INFO:tensorflow:Step #26430: rate 0.000020, accuracy 94.5%, cross entropy 0.164141
INFO:tensorflow:Step #26440: rate 0.000020, accuracy 91.8%, cross entropy 0.219968
INFO:tensorflow:Step #26450: rate 0.000020, accuracy 91.4%, cross entropy 0.240482
INFO:tensorflow:Step #26460: rate 0.000020, accuracy 93.0%, cross entropy 0.230451
INFO:tensorflow:Step #26470: rate 0.000020, accuracy 91.0%, cross entropy 0.294646
INFO:tensorflow:Step #26480: rate 0.000020, accuracy 91.0%, cross entropy 0.216119
INFO:tensorflow:Step #26490: rate 0.000020, accuracy 93.0%, cross entropy 0.196808
INFO:tensorflow:Step #26500: rate 0.000020, accuracy 92.2%, cross entropy 0.218662
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 217   5   6   2   2   1   6   5   3   5   6]
 [  0   0 250   6   2   0   2   0   1   0   0   0]
 [  0   2   1 258   1   2   0   0   0   0   0   6]
 [  0   5   0   0 241   0   0   0   0  13   1   0]
 [  0   0   1   5   0 253   0   0   1   0   1   3]
 [  0   2   8   4   1   0 231   1   0   0   0   0]
 [  0   6   0   0   1   0   2 247   0   0   0   0]
 [  0   5   0   0   4   0   0   2 242   4   0   0]
 [  0   1   0   1  17   0   0   0   5 231   0   1]
 [  0   2   0   0   7   1   0   0   0   2 231   3]
 [  0   5   0   6   6   4   0   1   0   3   2 233]]
INFO:tensorflow:Step 26500: Validation accuracy = 92.9% (N=2835)
INFO:tensorflow:Step #26510: rate 0.000020, accuracy 93.0%, cross entropy 0.229390
INFO:tensorflow:Step #26520: rate 0.000020, accuracy 91.0%, cross entropy 0.255381
INFO:tensorflow:Step #26530: rate 0.000020, accuracy 92.6%, cross entropy 0.213749
INFO:tensorflow:Step #26540: rate 0.000020, accuracy 91.0%, cross entropy 0.229941
INFO:tensorflow:Step #26550: rate 0.000020, accuracy 92.6%, cross entropy 0.233771
INFO:tensorflow:Step #26560: rate 0.000020, accuracy 95.3%, cross entropy 0.142333
INFO:tensorflow:Step #26570: rate 0.000020, accuracy 91.8%, cross entropy 0.237867
INFO:tensorflow:Step #26580: rate 0.000020, accuracy 93.4%, cross entropy 0.164058
INFO:tensorflow:Step #26590: rate 0.000020, accuracy 94.9%, cross entropy 0.165250
INFO:tensorflow:Step #26600: rate 0.000020, accuracy 94.1%, cross entropy 0.160120
INFO:tensorflow:Step #26610: rate 0.000020, accuracy 90.2%, cross entropy 0.268755
INFO:tensorflow:Step #26620: rate 0.000020, accuracy 91.4%, cross entropy 0.253449
INFO:tensorflow:Step #26630: rate 0.000020, accuracy 93.0%, cross entropy 0.205320
INFO:tensorflow:Step #26640: rate 0.000020, accuracy 93.0%, cross entropy 0.204467
INFO:tensorflow:Step #26650: rate 0.000020, accuracy 94.9%, cross entropy 0.178093
INFO:tensorflow:Step #26660: rate 0.000020, accuracy 95.7%, cross entropy 0.127405
INFO:tensorflow:Step #26670: rate 0.000020, accuracy 91.0%, cross entropy 0.247210
INFO:tensorflow:Step #26680: rate 0.000020, accuracy 93.4%, cross entropy 0.211521
INFO:tensorflow:Step #26690: rate 0.000020, accuracy 92.6%, cross entropy 0.220137
INFO:tensorflow:Step #26700: rate 0.000020, accuracy 91.8%, cross entropy 0.228659
INFO:tensorflow:Step #26710: rate 0.000020, accuracy 95.3%, cross entropy 0.147013
INFO:tensorflow:Step #26720: rate 0.000020, accuracy 89.5%, cross entropy 0.299059
INFO:tensorflow:Step #26730: rate 0.000020, accuracy 93.4%, cross entropy 0.205481
INFO:tensorflow:Step #26740: rate 0.000020, accuracy 93.0%, cross entropy 0.218056
INFO:tensorflow:Step #26750: rate 0.000020, accuracy 91.4%, cross entropy 0.250271
INFO:tensorflow:Step #26760: rate 0.000020, accuracy 91.4%, cross entropy 0.289131
INFO:tensorflow:Step #26770: rate 0.000020, accuracy 96.1%, cross entropy 0.143540
INFO:tensorflow:Step #26780: rate 0.000020, accuracy 90.6%, cross entropy 0.248252
INFO:tensorflow:Step #26790: rate 0.000020, accuracy 92.2%, cross entropy 0.219761
INFO:tensorflow:Step #26800: rate 0.000020, accuracy 89.5%, cross entropy 0.293078
INFO:tensorflow:Step #26810: rate 0.000020, accuracy 92.6%, cross entropy 0.189019
INFO:tensorflow:Step #26820: rate 0.000020, accuracy 92.2%, cross entropy 0.233676
INFO:tensorflow:Step #26830: rate 0.000020, accuracy 91.4%, cross entropy 0.273803
INFO:tensorflow:Step #26840: rate 0.000020, accuracy 93.8%, cross entropy 0.236729
INFO:tensorflow:Step #26850: rate 0.000020, accuracy 93.4%, cross entropy 0.205543
INFO:tensorflow:Step #26860: rate 0.000020, accuracy 89.8%, cross entropy 0.286769
INFO:tensorflow:Step #26870: rate 0.000020, accuracy 92.6%, cross entropy 0.282285
INFO:tensorflow:Step #26880: rate 0.000020, accuracy 92.2%, cross entropy 0.265430
INFO:tensorflow:Step #26890: rate 0.000020, accuracy 95.3%, cross entropy 0.139590
INFO:tensorflow:Step #26900: rate 0.000020, accuracy 91.8%, cross entropy 0.205136
INFO:tensorflow:Step #26910: rate 0.000020, accuracy 93.8%, cross entropy 0.193490
INFO:tensorflow:Step #26920: rate 0.000020, accuracy 94.1%, cross entropy 0.184421
INFO:tensorflow:Step #26930: rate 0.000020, accuracy 91.4%, cross entropy 0.283413
INFO:tensorflow:Step #26940: rate 0.000020, accuracy 93.0%, cross entropy 0.169133
INFO:tensorflow:Step #26950: rate 0.000020, accuracy 91.8%, cross entropy 0.203873
INFO:tensorflow:Step #26960: rate 0.000020, accuracy 94.9%, cross entropy 0.177163
INFO:tensorflow:Step #26970: rate 0.000020, accuracy 93.8%, cross entropy 0.202645
INFO:tensorflow:Step #26980: rate 0.000020, accuracy 93.0%, cross entropy 0.217237
INFO:tensorflow:Step #26990: rate 0.000020, accuracy 91.0%, cross entropy 0.244268
INFO:tensorflow:Step #27000: rate 0.000020, accuracy 93.4%, cross entropy 0.193393
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 214   6   6   3   1   2   7   5   3   5   6]
 [  0   0 250   6   2   0   2   0   1   0   0   0]
 [  0   2   1 259   1   1   0   0   0   0   0   6]
 [  0   5   0   0 243   0   0   0   0  11   1   0]
 [  0   1   1   6   0 251   0   0   1   0   1   3]
 [  0   2  10   4   1   0 229   1   0   0   0   0]
 [  0   4   0   0   1   0   2 249   0   0   0   0]
 [  0   5   0   0   5   0   0   1 241   5   0   0]
 [  0   1   0   1  18   0   0   0   5 230   0   1]
 [  0   2   0   0   7   1   0   0   0   3 230   3]
 [  0   4   0   6   7   4   0   1   0   3   2 233]]
INFO:tensorflow:Step 27000: Validation accuracy = 92.7% (N=2835)
INFO:tensorflow:Step #27010: rate 0.000020, accuracy 92.2%, cross entropy 0.278606
INFO:tensorflow:Step #27020: rate 0.000020, accuracy 93.4%, cross entropy 0.196641
INFO:tensorflow:Step #27030: rate 0.000020, accuracy 91.0%, cross entropy 0.239557
INFO:tensorflow:Step #27040: rate 0.000020, accuracy 91.8%, cross entropy 0.233537
INFO:tensorflow:Step #27050: rate 0.000020, accuracy 96.1%, cross entropy 0.142817
INFO:tensorflow:Step #27060: rate 0.000020, accuracy 93.4%, cross entropy 0.201421
INFO:tensorflow:Step #27070: rate 0.000020, accuracy 91.8%, cross entropy 0.231962
INFO:tensorflow:Step #27080: rate 0.000020, accuracy 93.0%, cross entropy 0.212812
INFO:tensorflow:Step #27090: rate 0.000020, accuracy 92.6%, cross entropy 0.242072
INFO:tensorflow:Step #27100: rate 0.000020, accuracy 93.8%, cross entropy 0.187971
INFO:tensorflow:Step #27110: rate 0.000020, accuracy 92.6%, cross entropy 0.220678
INFO:tensorflow:Step #27120: rate 0.000020, accuracy 91.8%, cross entropy 0.243974
INFO:tensorflow:Step #27130: rate 0.000020, accuracy 91.0%, cross entropy 0.256081
INFO:tensorflow:Step #27140: rate 0.000020, accuracy 94.1%, cross entropy 0.208828
INFO:tensorflow:Step #27150: rate 0.000020, accuracy 94.5%, cross entropy 0.192116
INFO:tensorflow:Step #27160: rate 0.000020, accuracy 93.4%, cross entropy 0.207712
INFO:tensorflow:Step #27170: rate 0.000020, accuracy 90.2%, cross entropy 0.280231
INFO:tensorflow:Step #27180: rate 0.000020, accuracy 93.4%, cross entropy 0.213903
INFO:tensorflow:Step #27190: rate 0.000020, accuracy 91.4%, cross entropy 0.240636
INFO:tensorflow:Step #27200: rate 0.000020, accuracy 93.8%, cross entropy 0.201660
INFO:tensorflow:Step #27210: rate 0.000020, accuracy 94.1%, cross entropy 0.239415
INFO:tensorflow:Step #27220: rate 0.000020, accuracy 93.8%, cross entropy 0.179631
INFO:tensorflow:Step #27230: rate 0.000020, accuracy 94.5%, cross entropy 0.155642
INFO:tensorflow:Step #27240: rate 0.000020, accuracy 94.1%, cross entropy 0.163711
INFO:tensorflow:Step #27250: rate 0.000020, accuracy 92.2%, cross entropy 0.207396
INFO:tensorflow:Step #27260: rate 0.000020, accuracy 92.2%, cross entropy 0.228954
INFO:tensorflow:Step #27270: rate 0.000020, accuracy 94.5%, cross entropy 0.153750
INFO:tensorflow:Step #27280: rate 0.000020, accuracy 91.0%, cross entropy 0.253615
INFO:tensorflow:Step #27290: rate 0.000020, accuracy 90.2%, cross entropy 0.311537
INFO:tensorflow:Step #27300: rate 0.000020, accuracy 93.0%, cross entropy 0.253075
INFO:tensorflow:Step #27310: rate 0.000020, accuracy 93.4%, cross entropy 0.195235
INFO:tensorflow:Step #27320: rate 0.000020, accuracy 96.5%, cross entropy 0.145344
INFO:tensorflow:Step #27330: rate 0.000020, accuracy 93.8%, cross entropy 0.216201
INFO:tensorflow:Step #27340: rate 0.000020, accuracy 94.1%, cross entropy 0.173697
INFO:tensorflow:Step #27350: rate 0.000020, accuracy 95.3%, cross entropy 0.136806
INFO:tensorflow:Step #27360: rate 0.000020, accuracy 94.1%, cross entropy 0.197333
INFO:tensorflow:Step #27370: rate 0.000020, accuracy 91.0%, cross entropy 0.279870
INFO:tensorflow:Step #27380: rate 0.000020, accuracy 91.8%, cross entropy 0.214502
INFO:tensorflow:Step #27390: rate 0.000020, accuracy 93.4%, cross entropy 0.226798
INFO:tensorflow:Step #27400: rate 0.000020, accuracy 91.8%, cross entropy 0.210992
INFO:tensorflow:Step #27410: rate 0.000020, accuracy 96.5%, cross entropy 0.166964
INFO:tensorflow:Step #27420: rate 0.000020, accuracy 90.6%, cross entropy 0.297011
INFO:tensorflow:Step #27430: rate 0.000020, accuracy 94.5%, cross entropy 0.192354
INFO:tensorflow:Step #27440: rate 0.000020, accuracy 95.3%, cross entropy 0.146218
INFO:tensorflow:Step #27450: rate 0.000020, accuracy 91.4%, cross entropy 0.273077
INFO:tensorflow:Step #27460: rate 0.000020, accuracy 94.1%, cross entropy 0.153883
INFO:tensorflow:Step #27470: rate 0.000020, accuracy 93.4%, cross entropy 0.182789
INFO:tensorflow:Step #27480: rate 0.000020, accuracy 94.9%, cross entropy 0.172636
INFO:tensorflow:Step #27490: rate 0.000020, accuracy 91.0%, cross entropy 0.295853
INFO:tensorflow:Step #27500: rate 0.000020, accuracy 96.9%, cross entropy 0.141217
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 217   6   4   2   1   2   8   5   3   5   5]
 [  0   0 248   6   2   0   4   0   1   0   0   0]
 [  0   2   1 257   1   2   1   0   0   0   0   6]
 [  0   5   0   0 241   0   0   0   0  13   1   0]
 [  0   0   1   5   0 253   0   0   1   0   1   3]
 [  0   2   8   4   1   0 231   1   0   0   0   0]
 [  0   4   0   0   1   0   2 249   0   0   0   0]
 [  0   5   0   0   3   0   0   3 242   4   0   0]
 [  0   1   0   1  16   0   0   0   6 231   0   1]
 [  0   2   0   0   7   1   0   0   0   3 230   3]
 [  0   5   0   4   6   4   0   2   0   2   2 235]]
INFO:tensorflow:Step 27500: Validation accuracy = 92.9% (N=2835)
INFO:tensorflow:Step #27510: rate 0.000020, accuracy 90.6%, cross entropy 0.300031
INFO:tensorflow:Step #27520: rate 0.000020, accuracy 91.0%, cross entropy 0.275294
INFO:tensorflow:Step #27530: rate 0.000020, accuracy 92.6%, cross entropy 0.220230
INFO:tensorflow:Step #27540: rate 0.000020, accuracy 91.4%, cross entropy 0.243992
INFO:tensorflow:Step #27550: rate 0.000020, accuracy 91.0%, cross entropy 0.226026
INFO:tensorflow:Step #27560: rate 0.000020, accuracy 93.4%, cross entropy 0.200574
INFO:tensorflow:Step #27570: rate 0.000020, accuracy 92.6%, cross entropy 0.217324
INFO:tensorflow:Step #27580: rate 0.000020, accuracy 94.9%, cross entropy 0.184643
INFO:tensorflow:Step #27590: rate 0.000020, accuracy 94.1%, cross entropy 0.184354
INFO:tensorflow:Step #27600: rate 0.000020, accuracy 92.6%, cross entropy 0.226326
INFO:tensorflow:Step #27610: rate 0.000020, accuracy 92.6%, cross entropy 0.196245
INFO:tensorflow:Step #27620: rate 0.000020, accuracy 92.2%, cross entropy 0.219555
INFO:tensorflow:Step #27630: rate 0.000020, accuracy 91.4%, cross entropy 0.252455
INFO:tensorflow:Step #27640: rate 0.000020, accuracy 89.5%, cross entropy 0.262185
INFO:tensorflow:Step #27650: rate 0.000020, accuracy 92.2%, cross entropy 0.237582
INFO:tensorflow:Step #27660: rate 0.000020, accuracy 93.4%, cross entropy 0.199271
INFO:tensorflow:Step #27670: rate 0.000020, accuracy 96.1%, cross entropy 0.178286
INFO:tensorflow:Step #27680: rate 0.000020, accuracy 92.2%, cross entropy 0.258206
INFO:tensorflow:Step #27690: rate 0.000020, accuracy 93.4%, cross entropy 0.182359
INFO:tensorflow:Step #27700: rate 0.000020, accuracy 92.2%, cross entropy 0.214224
INFO:tensorflow:Step #27710: rate 0.000020, accuracy 89.8%, cross entropy 0.252263
INFO:tensorflow:Step #27720: rate 0.000020, accuracy 90.6%, cross entropy 0.251033
INFO:tensorflow:Step #27730: rate 0.000020, accuracy 91.0%, cross entropy 0.252887
INFO:tensorflow:Step #27740: rate 0.000020, accuracy 92.6%, cross entropy 0.232253
INFO:tensorflow:Step #27750: rate 0.000020, accuracy 92.2%, cross entropy 0.252285
INFO:tensorflow:Step #27760: rate 0.000020, accuracy 90.6%, cross entropy 0.291988
INFO:tensorflow:Step #27770: rate 0.000020, accuracy 93.4%, cross entropy 0.258114
INFO:tensorflow:Step #27780: rate 0.000020, accuracy 93.4%, cross entropy 0.224788
INFO:tensorflow:Step #27790: rate 0.000020, accuracy 93.8%, cross entropy 0.180015
INFO:tensorflow:Step #27800: rate 0.000020, accuracy 96.5%, cross entropy 0.092208
INFO:tensorflow:Step #27810: rate 0.000020, accuracy 91.0%, cross entropy 0.226354
INFO:tensorflow:Step #27820: rate 0.000020, accuracy 91.8%, cross entropy 0.198300
INFO:tensorflow:Step #27830: rate 0.000020, accuracy 91.0%, cross entropy 0.290635
INFO:tensorflow:Step #27840: rate 0.000020, accuracy 94.9%, cross entropy 0.214145
INFO:tensorflow:Step #27850: rate 0.000020, accuracy 91.0%, cross entropy 0.266162
INFO:tensorflow:Step #27860: rate 0.000020, accuracy 93.4%, cross entropy 0.203820
INFO:tensorflow:Step #27870: rate 0.000020, accuracy 92.2%, cross entropy 0.201751
INFO:tensorflow:Step #27880: rate 0.000020, accuracy 91.4%, cross entropy 0.255942
INFO:tensorflow:Step #27890: rate 0.000020, accuracy 94.9%, cross entropy 0.174182
INFO:tensorflow:Step #27900: rate 0.000020, accuracy 90.2%, cross entropy 0.274967
INFO:tensorflow:Step #27910: rate 0.000020, accuracy 93.0%, cross entropy 0.187138
INFO:tensorflow:Step #27920: rate 0.000020, accuracy 92.2%, cross entropy 0.248330
INFO:tensorflow:Step #27930: rate 0.000020, accuracy 93.0%, cross entropy 0.197906
INFO:tensorflow:Step #27940: rate 0.000020, accuracy 93.0%, cross entropy 0.209880
INFO:tensorflow:Step #27950: rate 0.000020, accuracy 90.2%, cross entropy 0.325218
INFO:tensorflow:Step #27960: rate 0.000020, accuracy 94.9%, cross entropy 0.167369
INFO:tensorflow:Step #27970: rate 0.000020, accuracy 94.1%, cross entropy 0.168714
INFO:tensorflow:Step #27980: rate 0.000020, accuracy 91.8%, cross entropy 0.211385
INFO:tensorflow:Step #27990: rate 0.000020, accuracy 91.8%, cross entropy 0.222307
INFO:tensorflow:Step #28000: rate 0.000020, accuracy 89.1%, cross entropy 0.287137
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 216   5   6   2   1   2   8   5   3   5   5]
 [  0   0 248   6   2   0   4   0   1   0   0   0]
 [  0   2   1 257   1   2   1   0   0   0   0   6]
 [  0   5   0   0 241   0   0   0   0  13   1   0]
 [  0   0   1   5   0 253   0   0   1   0   1   3]
 [  0   2   8   4   1   0 231   1   0   0   0   0]
 [  0   4   0   0   1   0   2 249   0   0   0   0]
 [  0   5   0   0   3   0   0   3 242   4   0   0]
 [  0   1   0   1  15   0   0   0   6 232   0   1]
 [  0   2   0   0   7   1   0   0   0   3 230   3]
 [  0   5   0   7   6   4   0   2   0   2   2 232]]
INFO:tensorflow:Step 28000: Validation accuracy = 92.8% (N=2835)
INFO:tensorflow:Saving to "F:\ML_Project\Data\logs&checkpoint\c_rnn\ckpt-28000"
INFO:tensorflow:Step #28010: rate 0.000020, accuracy 93.0%, cross entropy 0.188549
INFO:tensorflow:Step #28020: rate 0.000020, accuracy 94.5%, cross entropy 0.181103
INFO:tensorflow:Step #28030: rate 0.000020, accuracy 92.2%, cross entropy 0.221079
INFO:tensorflow:Step #28040: rate 0.000020, accuracy 91.8%, cross entropy 0.235845
INFO:tensorflow:Step #28050: rate 0.000020, accuracy 91.8%, cross entropy 0.227945
INFO:tensorflow:Step #28060: rate 0.000020, accuracy 92.6%, cross entropy 0.228574
INFO:tensorflow:Step #28070: rate 0.000020, accuracy 92.6%, cross entropy 0.195344
INFO:tensorflow:Step #28080: rate 0.000020, accuracy 89.8%, cross entropy 0.308310
INFO:tensorflow:Step #28090: rate 0.000020, accuracy 93.8%, cross entropy 0.171429
INFO:tensorflow:Step #28100: rate 0.000020, accuracy 91.8%, cross entropy 0.207085
INFO:tensorflow:Step #28110: rate 0.000020, accuracy 94.9%, cross entropy 0.166285
INFO:tensorflow:Step #28120: rate 0.000020, accuracy 91.8%, cross entropy 0.244985
INFO:tensorflow:Step #28130: rate 0.000020, accuracy 88.7%, cross entropy 0.379396
INFO:tensorflow:Step #28140: rate 0.000020, accuracy 94.9%, cross entropy 0.145871
INFO:tensorflow:Step #28150: rate 0.000020, accuracy 90.6%, cross entropy 0.251500
INFO:tensorflow:Step #28160: rate 0.000020, accuracy 90.2%, cross entropy 0.268116
INFO:tensorflow:Step #28170: rate 0.000020, accuracy 91.0%, cross entropy 0.243289
INFO:tensorflow:Step #28180: rate 0.000020, accuracy 95.3%, cross entropy 0.162175
INFO:tensorflow:Step #28190: rate 0.000020, accuracy 92.6%, cross entropy 0.243892
INFO:tensorflow:Step #28200: rate 0.000020, accuracy 92.2%, cross entropy 0.223031
INFO:tensorflow:Step #28210: rate 0.000020, accuracy 89.1%, cross entropy 0.328179
INFO:tensorflow:Step #28220: rate 0.000020, accuracy 93.4%, cross entropy 0.193256
INFO:tensorflow:Step #28230: rate 0.000020, accuracy 91.4%, cross entropy 0.255141
INFO:tensorflow:Step #28240: rate 0.000020, accuracy 95.3%, cross entropy 0.176023
INFO:tensorflow:Step #28250: rate 0.000020, accuracy 92.6%, cross entropy 0.213837
INFO:tensorflow:Step #28260: rate 0.000020, accuracy 90.6%, cross entropy 0.278742
INFO:tensorflow:Step #28270: rate 0.000020, accuracy 87.9%, cross entropy 0.312757
INFO:tensorflow:Step #28280: rate 0.000020, accuracy 92.2%, cross entropy 0.258254
INFO:tensorflow:Step #28290: rate 0.000020, accuracy 93.4%, cross entropy 0.206529
INFO:tensorflow:Step #28300: rate 0.000020, accuracy 94.1%, cross entropy 0.152513
INFO:tensorflow:Step #28310: rate 0.000020, accuracy 91.8%, cross entropy 0.203397
INFO:tensorflow:Step #28320: rate 0.000020, accuracy 91.4%, cross entropy 0.244782
INFO:tensorflow:Step #28330: rate 0.000020, accuracy 92.6%, cross entropy 0.252022
INFO:tensorflow:Step #28340: rate 0.000020, accuracy 94.1%, cross entropy 0.144642
INFO:tensorflow:Step #28350: rate 0.000020, accuracy 92.2%, cross entropy 0.188796
INFO:tensorflow:Step #28360: rate 0.000020, accuracy 91.8%, cross entropy 0.259645
INFO:tensorflow:Step #28370: rate 0.000020, accuracy 94.1%, cross entropy 0.199639
INFO:tensorflow:Step #28380: rate 0.000020, accuracy 92.2%, cross entropy 0.210767
INFO:tensorflow:Step #28390: rate 0.000020, accuracy 93.0%, cross entropy 0.191111
INFO:tensorflow:Step #28400: rate 0.000020, accuracy 90.6%, cross entropy 0.252732
INFO:tensorflow:Step #28410: rate 0.000020, accuracy 93.8%, cross entropy 0.169252
INFO:tensorflow:Step #28420: rate 0.000020, accuracy 94.1%, cross entropy 0.182630
INFO:tensorflow:Step #28430: rate 0.000020, accuracy 91.0%, cross entropy 0.288905
INFO:tensorflow:Step #28440: rate 0.000020, accuracy 94.9%, cross entropy 0.132947
INFO:tensorflow:Step #28450: rate 0.000020, accuracy 93.0%, cross entropy 0.251582
INFO:tensorflow:Step #28460: rate 0.000020, accuracy 93.8%, cross entropy 0.167668
INFO:tensorflow:Step #28470: rate 0.000020, accuracy 93.0%, cross entropy 0.216717
INFO:tensorflow:Step #28480: rate 0.000020, accuracy 93.4%, cross entropy 0.173426
INFO:tensorflow:Step #28490: rate 0.000020, accuracy 91.4%, cross entropy 0.230337
INFO:tensorflow:Step #28500: rate 0.000020, accuracy 92.6%, cross entropy 0.217047
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 216   7   5   2   1   1   8   5   3   4   6]
 [  0   0 250   6   2   0   2   1   0   0   0   0]
 [  0   2   1 257   1   2   1   0   0   0   0   6]
 [  0   5   0   0 241   0   0   0   0  13   1   0]
 [  0   0   1   5   0 254   0   0   1   0   0   3]
 [  0   2  10   4   1   0 229   1   0   0   0   0]
 [  0   4   0   0   1   0   2 249   0   0   0   0]
 [  0   5   0   0   3   0   0   2 242   5   0   0]
 [  0   1   0   1  15   0   0   0   6 232   0   1]
 [  0   2   0   0   7   1   0   0   0   3 229   4]
 [  0   5   0   6   6   4   0   2   0   2   2 233]]
INFO:tensorflow:Step 28500: Validation accuracy = 92.8% (N=2835)
INFO:tensorflow:Step #28510: rate 0.000020, accuracy 94.5%, cross entropy 0.149095
INFO:tensorflow:Step #28520: rate 0.000020, accuracy 94.5%, cross entropy 0.187144
INFO:tensorflow:Step #28530: rate 0.000020, accuracy 91.8%, cross entropy 0.254301
INFO:tensorflow:Step #28540: rate 0.000020, accuracy 93.0%, cross entropy 0.216575
INFO:tensorflow:Step #28550: rate 0.000020, accuracy 94.1%, cross entropy 0.249417
INFO:tensorflow:Step #28560: rate 0.000020, accuracy 93.4%, cross entropy 0.166449
INFO:tensorflow:Step #28570: rate 0.000020, accuracy 94.9%, cross entropy 0.181768
INFO:tensorflow:Step #28580: rate 0.000020, accuracy 88.7%, cross entropy 0.326001
INFO:tensorflow:Step #28590: rate 0.000020, accuracy 93.0%, cross entropy 0.194756
INFO:tensorflow:Step #28600: rate 0.000020, accuracy 93.8%, cross entropy 0.239971
INFO:tensorflow:Step #28610: rate 0.000020, accuracy 92.6%, cross entropy 0.206049
INFO:tensorflow:Step #28620: rate 0.000020, accuracy 92.6%, cross entropy 0.217195
INFO:tensorflow:Step #28630: rate 0.000020, accuracy 91.4%, cross entropy 0.273976
INFO:tensorflow:Step #28640: rate 0.000020, accuracy 93.8%, cross entropy 0.164232
INFO:tensorflow:Step #28650: rate 0.000020, accuracy 92.2%, cross entropy 0.244282
INFO:tensorflow:Step #28660: rate 0.000020, accuracy 91.8%, cross entropy 0.243610
INFO:tensorflow:Step #28670: rate 0.000020, accuracy 93.0%, cross entropy 0.214591
INFO:tensorflow:Step #28680: rate 0.000020, accuracy 91.0%, cross entropy 0.310111
INFO:tensorflow:Step #28690: rate 0.000020, accuracy 93.4%, cross entropy 0.188448
INFO:tensorflow:Step #28700: rate 0.000020, accuracy 94.5%, cross entropy 0.188741
INFO:tensorflow:Step #28710: rate 0.000020, accuracy 91.4%, cross entropy 0.284032
INFO:tensorflow:Step #28720: rate 0.000020, accuracy 94.5%, cross entropy 0.192906
INFO:tensorflow:Step #28730: rate 0.000020, accuracy 88.7%, cross entropy 0.335864
INFO:tensorflow:Step #28740: rate 0.000020, accuracy 92.2%, cross entropy 0.234061
INFO:tensorflow:Step #28750: rate 0.000020, accuracy 90.2%, cross entropy 0.236770
INFO:tensorflow:Step #28760: rate 0.000020, accuracy 92.2%, cross entropy 0.227185
INFO:tensorflow:Step #28770: rate 0.000020, accuracy 92.2%, cross entropy 0.220788
INFO:tensorflow:Step #28780: rate 0.000020, accuracy 93.4%, cross entropy 0.218981
INFO:tensorflow:Step #28790: rate 0.000020, accuracy 92.2%, cross entropy 0.290838
INFO:tensorflow:Step #28800: rate 0.000020, accuracy 90.2%, cross entropy 0.352259
INFO:tensorflow:Step #28810: rate 0.000020, accuracy 89.8%, cross entropy 0.282469
INFO:tensorflow:Step #28820: rate 0.000020, accuracy 91.8%, cross entropy 0.190873
INFO:tensorflow:Step #28830: rate 0.000020, accuracy 89.8%, cross entropy 0.320249
INFO:tensorflow:Step #28840: rate 0.000020, accuracy 91.8%, cross entropy 0.221385
INFO:tensorflow:Step #28850: rate 0.000020, accuracy 95.3%, cross entropy 0.213127
INFO:tensorflow:Step #28860: rate 0.000020, accuracy 93.0%, cross entropy 0.193433
INFO:tensorflow:Step #28870: rate 0.000020, accuracy 93.8%, cross entropy 0.214725
INFO:tensorflow:Step #28880: rate 0.000020, accuracy 90.6%, cross entropy 0.241883
INFO:tensorflow:Step #28890: rate 0.000020, accuracy 89.8%, cross entropy 0.308669
INFO:tensorflow:Step #28900: rate 0.000020, accuracy 91.4%, cross entropy 0.272221
INFO:tensorflow:Step #28910: rate 0.000020, accuracy 94.5%, cross entropy 0.209264
INFO:tensorflow:Step #28920: rate 0.000020, accuracy 92.2%, cross entropy 0.247893
INFO:tensorflow:Step #28930: rate 0.000020, accuracy 89.8%, cross entropy 0.287709
INFO:tensorflow:Step #28940: rate 0.000020, accuracy 90.2%, cross entropy 0.256264
INFO:tensorflow:Step #28950: rate 0.000020, accuracy 92.2%, cross entropy 0.200806
INFO:tensorflow:Step #28960: rate 0.000020, accuracy 91.4%, cross entropy 0.257439
INFO:tensorflow:Step #28970: rate 0.000020, accuracy 92.6%, cross entropy 0.226597
INFO:tensorflow:Step #28980: rate 0.000020, accuracy 94.9%, cross entropy 0.179843
INFO:tensorflow:Step #28990: rate 0.000020, accuracy 94.5%, cross entropy 0.190183
INFO:tensorflow:Step #29000: rate 0.000020, accuracy 94.9%, cross entropy 0.170380
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 216   6   7   2   1   1   8   5   3   5   4]
 [  0   0 251   6   2   0   1   0   1   0   0   0]
 [  0   2   1 258   1   2   0   0   0   0   0   6]
 [  0   5   0   0 240   0   0   1   0  13   1   0]
 [  0   0   1   5   0 254   0   0   1   0   1   2]
 [  0   2   8   4   1   0 231   1   0   0   0   0]
 [  0   4   0   0   1   0   2 249   0   0   0   0]
 [  0   5   0   0   4   0   0   2 243   3   0   0]
 [  0   1   0   1  15   0   0   0   7 231   0   1]
 [  0   2   0   0   7   1   0   0   0   2 231   3]
 [  0   6   0   8   6   4   0   2   0   2   2 230]]
INFO:tensorflow:Step 29000: Validation accuracy = 92.9% (N=2835)
INFO:tensorflow:Step #29010: rate 0.000020, accuracy 90.2%, cross entropy 0.245251
INFO:tensorflow:Step #29020: rate 0.000020, accuracy 94.9%, cross entropy 0.154780
INFO:tensorflow:Step #29030: rate 0.000020, accuracy 92.6%, cross entropy 0.190537
INFO:tensorflow:Step #29040: rate 0.000020, accuracy 94.9%, cross entropy 0.206683
INFO:tensorflow:Step #29050: rate 0.000020, accuracy 92.2%, cross entropy 0.241782
INFO:tensorflow:Step #29060: rate 0.000020, accuracy 91.4%, cross entropy 0.263543
INFO:tensorflow:Step #29070: rate 0.000020, accuracy 94.5%, cross entropy 0.167187
INFO:tensorflow:Step #29080: rate 0.000020, accuracy 93.8%, cross entropy 0.198692
INFO:tensorflow:Step #29090: rate 0.000020, accuracy 93.8%, cross entropy 0.221409
INFO:tensorflow:Step #29100: rate 0.000020, accuracy 91.0%, cross entropy 0.233301
INFO:tensorflow:Step #29110: rate 0.000020, accuracy 92.2%, cross entropy 0.221457
INFO:tensorflow:Step #29120: rate 0.000020, accuracy 92.6%, cross entropy 0.228565
INFO:tensorflow:Step #29130: rate 0.000020, accuracy 93.4%, cross entropy 0.192451
INFO:tensorflow:Step #29140: rate 0.000020, accuracy 89.8%, cross entropy 0.249141
INFO:tensorflow:Step #29150: rate 0.000020, accuracy 94.5%, cross entropy 0.157407
INFO:tensorflow:Step #29160: rate 0.000020, accuracy 94.1%, cross entropy 0.178689
INFO:tensorflow:Step #29170: rate 0.000020, accuracy 94.1%, cross entropy 0.202458
INFO:tensorflow:Step #29180: rate 0.000020, accuracy 94.1%, cross entropy 0.162691
INFO:tensorflow:Step #29190: rate 0.000020, accuracy 89.5%, cross entropy 0.300710
INFO:tensorflow:Step #29200: rate 0.000020, accuracy 91.0%, cross entropy 0.211402
INFO:tensorflow:Step #29210: rate 0.000020, accuracy 93.0%, cross entropy 0.255355
INFO:tensorflow:Step #29220: rate 0.000020, accuracy 92.2%, cross entropy 0.219566
INFO:tensorflow:Step #29230: rate 0.000020, accuracy 94.9%, cross entropy 0.178165
INFO:tensorflow:Step #29240: rate 0.000020, accuracy 96.1%, cross entropy 0.114334
INFO:tensorflow:Step #29250: rate 0.000020, accuracy 90.2%, cross entropy 0.249135
INFO:tensorflow:Step #29260: rate 0.000020, accuracy 94.1%, cross entropy 0.207150
INFO:tensorflow:Step #29270: rate 0.000020, accuracy 94.9%, cross entropy 0.168890
INFO:tensorflow:Step #29280: rate 0.000020, accuracy 94.1%, cross entropy 0.163803
INFO:tensorflow:Step #29290: rate 0.000020, accuracy 93.0%, cross entropy 0.204690
INFO:tensorflow:Step #29300: rate 0.000020, accuracy 89.8%, cross entropy 0.301904
INFO:tensorflow:Step #29310: rate 0.000020, accuracy 92.6%, cross entropy 0.249220
INFO:tensorflow:Step #29320: rate 0.000020, accuracy 93.0%, cross entropy 0.180209
INFO:tensorflow:Step #29330: rate 0.000020, accuracy 92.6%, cross entropy 0.215859
INFO:tensorflow:Step #29340: rate 0.000020, accuracy 93.4%, cross entropy 0.244102
INFO:tensorflow:Step #29350: rate 0.000020, accuracy 88.3%, cross entropy 0.316129
INFO:tensorflow:Step #29360: rate 0.000020, accuracy 91.0%, cross entropy 0.256591
INFO:tensorflow:Step #29370: rate 0.000020, accuracy 91.0%, cross entropy 0.228213
INFO:tensorflow:Step #29380: rate 0.000020, accuracy 93.8%, cross entropy 0.210800
INFO:tensorflow:Step #29390: rate 0.000020, accuracy 91.8%, cross entropy 0.227736
INFO:tensorflow:Step #29400: rate 0.000020, accuracy 90.6%, cross entropy 0.242741
INFO:tensorflow:Step #29410: rate 0.000020, accuracy 90.6%, cross entropy 0.234746
INFO:tensorflow:Step #29420: rate 0.000020, accuracy 93.8%, cross entropy 0.216033
INFO:tensorflow:Step #29430: rate 0.000020, accuracy 91.4%, cross entropy 0.211058
INFO:tensorflow:Step #29440: rate 0.000020, accuracy 92.6%, cross entropy 0.262401
INFO:tensorflow:Step #29450: rate 0.000020, accuracy 92.2%, cross entropy 0.227865
INFO:tensorflow:Step #29460: rate 0.000020, accuracy 94.1%, cross entropy 0.174615
INFO:tensorflow:Step #29470: rate 0.000020, accuracy 88.3%, cross entropy 0.351385
INFO:tensorflow:Step #29480: rate 0.000020, accuracy 92.2%, cross entropy 0.205826
INFO:tensorflow:Step #29490: rate 0.000020, accuracy 94.9%, cross entropy 0.202067
INFO:tensorflow:Step #29500: rate 0.000020, accuracy 93.8%, cross entropy 0.186602
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 217   7   6   4   1   2   7   5   2   4   3]
 [  0   0 248   6   2   0   4   0   0   1   0   0]
 [  0   2   1 257   1   2   1   0   0   0   0   6]
 [  0   5   0   0 246   0   0   0   0   9   0   0]
 [  0   1   1   6   0 252   0   0   0   0   1   3]
 [  0   2   8   4   1   0 231   1   0   0   0   0]
 [  0   3   0   0   1   0   2 249   0   0   0   1]
 [  0   5   0   0   5   0   0   1 242   4   0   0]
 [  0   1   0   1  18   0   0   0   5 230   0   1]
 [  0   2   0   0   7   1   0   0   0   2 231   3]
 [  0   5   0   6   7   4   0   1   0   3   2 232]]
INFO:tensorflow:Step 29500: Validation accuracy = 92.9% (N=2835)
INFO:tensorflow:Step #29510: rate 0.000020, accuracy 92.6%, cross entropy 0.177311
INFO:tensorflow:Step #29520: rate 0.000020, accuracy 92.6%, cross entropy 0.230221
INFO:tensorflow:Step #29530: rate 0.000020, accuracy 93.8%, cross entropy 0.223158
INFO:tensorflow:Step #29540: rate 0.000020, accuracy 92.2%, cross entropy 0.244890
INFO:tensorflow:Step #29550: rate 0.000020, accuracy 93.0%, cross entropy 0.238204
INFO:tensorflow:Step #29560: rate 0.000020, accuracy 92.2%, cross entropy 0.255197
INFO:tensorflow:Step #29570: rate 0.000020, accuracy 93.0%, cross entropy 0.181363
INFO:tensorflow:Step #29580: rate 0.000020, accuracy 91.8%, cross entropy 0.240243
INFO:tensorflow:Step #29590: rate 0.000020, accuracy 89.1%, cross entropy 0.283933
INFO:tensorflow:Step #29600: rate 0.000020, accuracy 93.4%, cross entropy 0.195594
INFO:tensorflow:Step #29610: rate 0.000020, accuracy 94.1%, cross entropy 0.188251
INFO:tensorflow:Step #29620: rate 0.000020, accuracy 94.1%, cross entropy 0.173482
INFO:tensorflow:Step #29630: rate 0.000020, accuracy 86.7%, cross entropy 0.360153
INFO:tensorflow:Step #29640: rate 0.000020, accuracy 94.1%, cross entropy 0.179688
INFO:tensorflow:Step #29650: rate 0.000020, accuracy 92.6%, cross entropy 0.206788
INFO:tensorflow:Step #29660: rate 0.000020, accuracy 92.2%, cross entropy 0.195170
INFO:tensorflow:Step #29670: rate 0.000020, accuracy 96.1%, cross entropy 0.136263
INFO:tensorflow:Step #29680: rate 0.000020, accuracy 91.4%, cross entropy 0.241725
INFO:tensorflow:Step #29690: rate 0.000020, accuracy 90.2%, cross entropy 0.228436
INFO:tensorflow:Step #29700: rate 0.000020, accuracy 93.4%, cross entropy 0.214612
INFO:tensorflow:Step #29710: rate 0.000020, accuracy 94.1%, cross entropy 0.189804
INFO:tensorflow:Step #29720: rate 0.000020, accuracy 93.4%, cross entropy 0.165716
INFO:tensorflow:Step #29730: rate 0.000020, accuracy 92.2%, cross entropy 0.273514
INFO:tensorflow:Step #29740: rate 0.000020, accuracy 94.5%, cross entropy 0.171226
INFO:tensorflow:Step #29750: rate 0.000020, accuracy 93.0%, cross entropy 0.186878
INFO:tensorflow:Step #29760: rate 0.000020, accuracy 92.2%, cross entropy 0.227226
INFO:tensorflow:Step #29770: rate 0.000020, accuracy 94.5%, cross entropy 0.163125
INFO:tensorflow:Step #29780: rate 0.000020, accuracy 93.8%, cross entropy 0.201178
INFO:tensorflow:Step #29790: rate 0.000020, accuracy 91.4%, cross entropy 0.251664
INFO:tensorflow:Step #29800: rate 0.000020, accuracy 94.5%, cross entropy 0.182626
INFO:tensorflow:Step #29810: rate 0.000020, accuracy 93.0%, cross entropy 0.240293
INFO:tensorflow:Step #29820: rate 0.000020, accuracy 91.4%, cross entropy 0.229350
INFO:tensorflow:Step #29830: rate 0.000020, accuracy 94.5%, cross entropy 0.173695
INFO:tensorflow:Step #29840: rate 0.000020, accuracy 93.4%, cross entropy 0.212065
INFO:tensorflow:Step #29850: rate 0.000020, accuracy 90.6%, cross entropy 0.282047
INFO:tensorflow:Step #29860: rate 0.000020, accuracy 91.4%, cross entropy 0.244891
INFO:tensorflow:Step #29870: rate 0.000020, accuracy 89.8%, cross entropy 0.245292
INFO:tensorflow:Step #29880: rate 0.000020, accuracy 93.0%, cross entropy 0.228149
INFO:tensorflow:Step #29890: rate 0.000020, accuracy 91.8%, cross entropy 0.289536
INFO:tensorflow:Step #29900: rate 0.000020, accuracy 92.2%, cross entropy 0.206924
INFO:tensorflow:Step #29910: rate 0.000020, accuracy 92.2%, cross entropy 0.220470
INFO:tensorflow:Step #29920: rate 0.000020, accuracy 91.0%, cross entropy 0.230725
INFO:tensorflow:Step #29930: rate 0.000020, accuracy 89.8%, cross entropy 0.278700
INFO:tensorflow:Step #29940: rate 0.000020, accuracy 91.8%, cross entropy 0.248990
INFO:tensorflow:Step #29950: rate 0.000020, accuracy 91.0%, cross entropy 0.288127
INFO:tensorflow:Step #29960: rate 0.000020, accuracy 93.4%, cross entropy 0.162497
INFO:tensorflow:Step #29970: rate 0.000020, accuracy 92.6%, cross entropy 0.201288
INFO:tensorflow:Step #29980: rate 0.000020, accuracy 91.8%, cross entropy 0.211419
INFO:tensorflow:Step #29990: rate 0.000020, accuracy 92.2%, cross entropy 0.203361
INFO:tensorflow:Step #30000: rate 0.000020, accuracy 89.8%, cross entropy 0.291596
INFO:tensorflow:Confusion Matrix:
 [[  0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 217   6   5   2   1   2   8   5   3   5   4]
 [  0   0 248   6   2   0   4   0   1   0   0   0]
 [  0   2   1 258   1   1   1   0   0   0   0   6]
 [  0   5   0   0 241   0   0   0   0  13   1   0]
 [  0   0   1   5   0 253   0   0   1   0   1   3]
 [  0   2   8   4   1   0 231   1   0   0   0   0]
 [  0   4   0   0   1   0   2 249   0   0   0   0]
 [  0   5   0   0   4   0   0   2 243   3   0   0]
 [  0   1   0   1  16   0   0   0   7 230   0   1]
 [  0   2   0   0   7   1   0   0   0   2 231   3]
 [  0   5   0   7   6   4   0   2   0   2   2 232]]
INFO:tensorflow:Step 30000: Validation accuracy = 92.9% (N=2835)
INFO:tensorflow:Saving to "F:\ML_Project\Data\logs&checkpoint\c_rnn\ckpt-30000"
INFO:tensorflow:Training Completed.
>>> 
