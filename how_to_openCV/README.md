# OpenCV Cheat Sheet

###Read, write and formats
Images ARE simply np.arrays!

im = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # _COLOR
cv2.imwrite(filename, im)

Convert between formats
ime= cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)  # Converting colors

Transformations

im2 = cv2.resize(im, (width, height), interpolation=cv2.INTER_LINEAR) 

Draw simple stuff

im = cv2.line(im, (0,0), (511,511), (255,0,0), 5)  # Thickness 5

im = cv2.fillPoly(im, pts=contours_list, color=(255,255,255))  # *
* contours.dtype=np.int32, im.dtype=uint8(?), contours_list =[2d-arrays]

im = cv2.circle(im, (cx, cy), radius, col_tuple, thickness) 
im = cv2.rectangle(im, (x1, y1), (x2, y2), col_tuple, thickness) 



Text
https://www.geeksforgeeks.org/python-opencv-cv2-puttext-method/

cv2.putText(im, "text", (10, 50), font, 0.5, 255, 1)  # Coors LL corn of text  

Contours (list of array.shape(x, 2), dtype int32, ikke uint8)
_, bin_im = cv2.threshold(im, 127, 255, 0)  # Grey im, threshold, up, low
conts, _ = cv2.findContours(bin_im, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
area = cv2.contourArea(contour)  # may use to filter on size
https://docs.opencv.org/3.4/dd/d49/tutorial_py_contour_features.html
https://docs.opencv.org/master/d1/d32/tutorial_py_contour_properties.html
im = cv2.drawContours(im, contours_list, -1, (0,255,0), -1) # -1 = all; fill
M = cv2.moments(cont) # M["01"] er 1.moment sum(dist1) for akse 1 
M["m01"] / M["m10"]) == ratio  # Høyde/Bredde for rene rektangler


Maskering
im = np.where(mask==255, mask, im)  #mask color == 255. RGB is ok.
Se analyze queue actual
cv2.mean(im, mask)  # 1st verdi ret. mask.dtype = np.uint8, bruk 0 og 255.



Filtere
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_filtering/py_filtering.html
kernel = np.ones((5,5),np.float32)/25; cv2.filter2D(img,-1,kernel)
cv2.blur(im, (5,5))  # Mean. May expand to count filter by mono pxls. 
cv2.GaussianBlur(im, ksize_2dtuple, 0) # 0 calculates sigma in the kernel
cv2.Laplacian(im, ddepth=cv2.CV_16S, ksize=3)
cv2.medianBlur(im, 5)
cv2.bilateralFilter(im, 9, 75, 75)  # Les om dette…
Display images (put this in a  while True loop)
cv2.imshow("MyWindow", im)
k = cv2.waitKey(ms)  #
if k % 256 == num: # 27=Esc, 32=Space, 49-57=1-9
cv2.destroyAllWindows()  # When having left the loop
