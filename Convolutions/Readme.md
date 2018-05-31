# Basics of Convolutions

Convolution is one of the most important operations in signal and image processing. It could operate in 1D speech processing, 2D image processing or 3D video processing. 

In order to perform convolution on an image, following steps should be taken.

* Flip the mask (horizontally and vertically) only once
* Slide the mask onto the image.
* Multiply the corresponding elements and then add them
* Repeat this procedure until all values of the image has been calculated.

![alt text](http://machinelearninguru.com/_images/topics/computer_vision/basics/convolution/1.JPG)

