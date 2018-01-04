# Timpani Gesture Analysis

Project to visualize and classify different musical articulations of a timpani player. A k-nearest neighbor classifier implemented in Tensorflow identifies timpani gestures based only on the vertical trajectory of the mallet.

My current research involves studying the differences in gesture of the dominant and non-dominant hand of percussionists. This code will be expanded to assist me in the analysis for my Master's thesis: Handedness in Percussion Performance.

## Getting Started

The project is written using Python 3.5.4 and has not yet been made backwards compatible. Install the prerequisites (below) and clone the repository. 
### Prerequisites
```
numpy matplotlib
```
Before any gesture data can be extracted, the raw data files must be segmented.
```
python segment_stroke_data.py
```
Once the data have been segmented, 

