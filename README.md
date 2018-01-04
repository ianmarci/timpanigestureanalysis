# Timpani Gesture Analysis

Project to visualize and classify different musical articulations of a timpani player. A k-nearest neighbor classifier implemented in Tensorflow identifies timpani gestures based only on the vertical trajectory of the mallet. Six different articulations (accent, normal, piston, staccato, tenuto, and vertical accent) are compared. The player performed each of these articulations in three different plying positions on the drum (center, normal, and rim). Different articulations are correctly classified more than 93% of the time.

My current research involves studying the differences in gesture of the dominant and non-dominant hand of percussionists. This code will be expanded to assist me in the analysis for my Master's thesis: Handedness in Percussion Performance.

## Getting Started

The project is written using Python 3.5.4 and has not yet been made backwards compatible. Install the prerequisites and clone the repository. 

Required:
```
numpy matplotlib
ex. pip install numpy
```

## Running the experiment
Before any gesture data can be extracted, the raw data files must be segmented.
```
python segment_stroke_data.py
```
Once the data have been segmented, we must remove the outliers. Strokes made at the beginning or end of the file have artifacts from the motion capture software. Remove them using:
```
python remove_outliers.py
```
Now that the outliers have been removed, you can choose to classify or visualize the data. 

To use the classifier, divide the data into sets using:
```
python divide_into_sets.py path_to_data hand_choice
ex. python divide_into_sets.py 'Data\StrokePositionData' R
```
This example will extract all the right hand strokes from the position data folder, place it into the NetworkInput folder, and divide them into 4 sets for testing.  

### Classification
Once the data has been divided, classify by using:
```
python run_experiment.py
```

The script will print the average accuracy over the 4-fold cross validation as well as the confusion matrix.

Accuracies range from 93 - 99% based on the the distribution of stroke types placed into the sets by the divide_into_sets script.
### Visualization
To plot the data, use one of the plotting scripts.
#### Plot by Type
By using the plot_by_type function, one can see all strokes made using either the left or right hand. The strokes will be plotted by stroke type.
```
python plot_by_type.py data_type hand_choice
```
data_type can be either position, velocity, or acceleration.

hand_choice can be either R or L for right and left.


For example, to plot the position data of the right hand, use:
```
python plot_by_type.py position R
```
#### Plot Average by Type
plot_average_by_type.py uses the same arguments as plot_by_type.py but will plot the averages instead of the individual trajectories.

```
python plot_average_by_type.py velocity L
```
This will plot the average velocity of the left mallet for each stroke type.

#### Plot Raw Data
If you would like to investigate a single data file, you can by using:
```
python plot_raw_data.py path_to_data_file
ex. python plot_raw_data.py 'Data\Raw Data\Normal\AccentNormal\right1.csv'
```
This will plot the right mallet trajectory during the accented stroke capture when playing in the normal playing position.

