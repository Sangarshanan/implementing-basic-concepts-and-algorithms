# Basics of Convolutions

In order to perform convolution on an image, following steps should be taken.

* Flip the mask (horizontally and vertically) only once
* Slide the mask onto the image.
* Multiply the corresponding elements and then add them
* Repeat this procedure until all values of the image has been calculated.
