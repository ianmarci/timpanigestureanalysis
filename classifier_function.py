import tensorflow as tf
import numpy as np
import glob
from get_network_input import get_network_input

def classifier():

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

    with tf.Session() as sess:
        sess.run(init)

        for i in range(len(test_data)):
            nn_index = sess.run(pred, feed_dict={xtr: train_data, xte: test_data[i, :]})
            prediction = np.argmax(train_labels[nn_index])
            correct_answer = np.argmax(test_labels[i])
            print('Test', i, 'Prediction: ', prediction,
                'True Class: ', correct_answer)
            if prediction == correct_answer:
                accuracy += 1./len(test_data)

    print('Test Accuracy:', accuracy)
    return accuracy
