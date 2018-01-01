import tensorflow as tf
import numpy as np
import glob
from get_network_input import get_network_input

trainpath = 'Data/NetworkTrain/'
train_data, train_labels = get_network_input(trainpath)

testpath = 'Data/NetworkTest/'
test_data, test_labels = get_network_input(testpath)

xtr = tf.placeholder('float', [None, 245])
xte = tf.placeholder('float', [245])

distance = tf.reduce_sum(tf.abs(tf.add(xtr, tf.negative(xte))), reduction_indices=1)
pred = tf.argmin(distance, 0)

accuracy = 0

init = tf.global_variables_initializer()

predictions = np.zeros((len(test_data)))
labels = np.zeros((len(test_data)))

with tf.Session() as sess:
    sess.run(init)

    for i in range(len(test_data)):
        nn_index = sess.run(pred, feed_dict={xtr: train_data, xte: test_data[i, :]})
        predictions[i] = np.argmax(train_labels[nn_index])
        labels[i] = np.argmax(test_labels[i])
        print('Test', i, 'Prediction: ', predictions[i],
            'True Class: ', labels[i])
        if predictions[i] == labels[i]:
            accuracy += 1./len(test_data)
    confusion = tf.confusion_matrix(labels=labels, predictions=predictions)
    print(confusion.eval())
print('Test Accuracy:', accuracy)
