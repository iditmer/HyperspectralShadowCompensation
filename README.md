# Shadow Compensation in Remotely Sensed Imagery
Proof of concept for mitigating impact of shadows in hyperspectral imagery using 3D information. Much of this code was originally developed as part of a graduate project at RIT using MATLAB, though some details have been altered in the conversion to Python. The data used in the examples shown here were collected as part of one of the [DIRS](https://www.rit.edu/dirs/) imaging campaigns.

The big picture idea in this project was to develop a machine approach to appropriately scale spectra for pixels in shadows. Initial experiments demonstrated that manually providing shaded vs. non-shaded spectra as training data generally did not capture enough of the variety present in a given scene.

To compile a larger, more representative training data set, pixel pairs (shaded vs. non) were identifed automatically using lidar surface and intensity information. This process is detailed in the first two notebooks.

The resultant training data can be used to develop inputs to a non-parametric regression model. Many variations of that process have been experimented with - a couple of the simpler ones are presently outlined in the last two notebooks.
