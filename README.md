# Implementing basic concepts and algorithms

Implementation of the some interesting concepts and algorithms to help understand them better

## K- means algorithm ##

K means is an unsupervised machine learning algorithm that clusters similar points that are close in an n dimensional space

This is one of the very first algorithms that I was able to comprehend and appreciate, It is incredibly simple and also effective in nature. In My implementation I have first used a library to get the answer in a single step and then implement the algorithm from scratch to verify the correctness.
* Input: The points in the plane inside a txt file
* Output: Centroids of K clusters are saved in the txt file

## Convolutions ##

A convolution is very useful for signal processing in general. There is a lot of complex mathematical theory available for convolutions. 

http://machinelearninguru.com/computer_vision/basics/convolution/image_convolution_1.html

You can use a simple matrix as an image convolution kernel and do some interesting things!

## Deep Dream ##

A base image is used, which is fed to the pre-trained CNN. Then, forward pass is done till a particular layer. Now, to get a sense of what that layer has learned, we need to maximize the activations through that layer.

The gradients of that layer are set equal to the activations from that layer, and then gradient ascent is done on the input image. This maximizes the activations of that layer.




