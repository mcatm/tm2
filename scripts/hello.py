from __future__ import print_function

import tensorflow as tf

with tf.Session():
    input1 = tf.constant([1.0, 1.0, 1.0, 1.0])
    input2 = tf.constant([2.0, 2.0, 2.0, 2.0])
    output = tf.add(input1, input2)
    result = output.eval()
    print("result: ", result)


print([x + y for x, y in zip([1.0] * 4, [2.0] * 4)])

import numpy as np
x, y = np.full(4, 1.0), np.full(4, 2.0)
print("{} + {} = {}".format(x, y, x + y))