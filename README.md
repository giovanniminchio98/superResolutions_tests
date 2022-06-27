# superResolutions_tests
Tests of superResolution models, focused on the use (not implementation) or EDSR model

Example of results:

This first image is the orignal image, w. a dimensions of 124x118 (32.6 KB)

![aa](https://user-images.githubusercontent.com/69788614/176034546-8ee2ae94-3ed8-4952-bdd7-bb237738ad2f.png)

The next one is an image obtained with the EDSR model w. a scale x4 (from the image shown above), w. dimensions are now 496x472 (403 KB)

![scaled_4x](https://user-images.githubusercontent.com/69788614/176034779-437c3d54-9ae8-43b5-bc55-fbf2963e4eb0.png)

The next would be the upsampled image we would have obtained by only resizing the orignal one...is clearly visible that the result is way worse than compared to the previous image, obtain with the EDSR model (provided by pytorch) for superResolution. w. dimensions 496x472 (348 KB)

![resized](https://user-images.githubusercontent.com/69788614/176036001-037b3ffb-104c-48a8-b54c-142dafe26e7f.png)



