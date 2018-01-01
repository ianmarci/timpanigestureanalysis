import numpy as np

from classifier_function import classifier
from choose_test_set import choose_test_set


#accuracies = np.zeros(21, 10) 3 counts * 7 folds, 10 accuracies each

accuracies = np.zeros((4, 1))

for i in range(0, 4):
    choice = i + 1

    choose_test_set(str(choice))


    accuracies[i, 0] = classifier()
    print('Accuracy: ', accuracies[i, 0])
    iteration = i
    print('Iteration', iteration + 1,'of 4.')



#print(accuracies)
f = open('TestAccuracy.txt', 'w')
for k in range(0, len(accuracies)):
    f.write('Test ' + str(k) + '\r\n')
    average = np.mean(accuracies[k])
    f.write('    Average Accuracy: ' + str(average) + '\r\n')
    f.write('    Accuracy: ' + str(accuracies[k,:]) + '\r\n')
    #print('Accuracy:', accuracy)
f.close()
