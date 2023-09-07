# Reinhard-color-transformation

## How it Works
This script first converts the template and target images from BGR color space to LAB color space. Then, it calculates the mean and standard deviation of the LAB channels for both images. Next, it iterates through each pixel in the target image, adjusts the LAB channel values based on the mean and standard deviation, and clamps the values to the valid range. Finally, it converts the image back to the BGR color space and displays the result.
## Examples
Here are example images before and after color transfer:


template image

![download (1)](https://github.com/nalden141/Reinhard-color-transformation/assets/68941924/7ee754a7-0dd4-441a-9cdf-4baf734ecacc)


target image

![images](https://github.com/nalden141/Reinhard-color-transformation/assets/68941924/8bda2297-c7c8-4e76-917a-7ed94ed7c66d)


color transferred image

![transformationIMAGE](https://github.com/nalden141/Reinhard-color-transformation/assets/68941924/fc2e0aa9-a728-4280-9291-d2c101ad2a61)

