################################################################################
# run_experiment.py                                                            #
# Ian Marci  2017                                                              #
# Defines knn classifier and runs 4-fold on data in Data/NetworkInput.         #
# Prints accuracy for each fold as well as confusion matrix.                   #
################################################################################

import tensorflow as tf
import numpy as np

from classifier_input_functions import choose_test_set, get_network_input

# Path and placeholder definitions
train_path = 'Data/NetworkTrain/'
test_path = 'Data/NetworkTest/'

x_train = tf.placeholder('float', [None, 200])
x_test = tf.placeholder('float', [200])

# Distance to decide nearest neighbor
distance = tf.reduce_sum(tf.abs(tf.add(x_train, tf.negative(x_test))),
                                                            reduction_indices=1)
# Prediction chooses lowest distance
pred = tf.argmin(distance, 0)

################################
# 4-fold cross validation loop #
################################

init = tf.global_variables_initializer()
with tf.Session() as sess:
    for i in range(4):
        sess.run(init)

        choice = i + 1
        choose_test_set(str(choice))

        train_data, train_labels = get_network_input(train_path)
        test_data, test_labels = get_network_input(test_path)

        accuracy = 0
        predictions = np.zeros((len(test_data)))
        labels = np.zeros((len(test_data)))

        for i in range(len(test_data)):
            nn_index = sess.run(pred, feed_dict={x_train: train_data,
                                                 x_test: test_data[i, :]})
            predictions[i] = np.argmax(train_labels[nn_index])
            labels[i] = np.argmax(test_labels[i])
            if predictions[i] == labels[i]:
                accuracy += 1./len(test_data)
        confusion = tf.confusion_matrix(labels=labels, predictions=predictions)
        print(confusion.eval())
        print('Test Accuracy:', accuracy)
