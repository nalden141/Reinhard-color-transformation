import cv2 as cv
import numpy as np

def get_mean_std(x):
    mean , std =cv.meanStdDev(x)
    mean = np.hstack(np.around(mean,2))
    std = np.hstack(np.around(std,2))

    return mean , std

template_img = cv.imread(r'C:\Users\nada\Downloads\download (1).jpg')
template_img = cv.cvtColor(template_img,cv.COLOR_BGR2LAB)
template_mean , template_std = get_mean_std(template_img)

target_img = cv.imread(r'C:\Users\nada\Downloads\images.jpg')
target_img = cv.cvtColor(target_img,cv.COLOR_BGR2LAB)
target_mean , target_std = get_mean_std(target_img)

h,w,c = target_img.shape
for i in range(h):
    for j in range(w):
        for k in range(c):
            x = target_img[i,j,k]
            x = ((x-target_mean[k])*(template_std[k]/target_std[k]))+template_mean[k]
            x = round(x)
            x = 0 if x<0 else x
            x = 255 if x>255 else x
            target_img[i,j,k]=x

target_img=cv.cvtColor(target_img,cv.COLOR_LAB2BGR)
cv.imshow('image',target_img)
cv.imwrite('transformationIMAGE.jpg',target_img)
cv.waitKey(0)
cv.destroyAllWindows()
