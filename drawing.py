# Python3 program to draw rectangle
# shape on solid image
import numpy as np
import cv2

# Creating a black image with 3
# channels RGB and unsigned int datatype
#img = np.zeros((400, 400, 3), dtype = "uint8")
img = cv2.imread("python.jpg")

# Creating line
#cv2.line(img, (20, 160), (100, 160), (0, 0, 255), 10)
#cv2.imshow('line', img)
#cv2.line(imageObjectName, (‘start_coordinates’), (‘end_coordinates’), (‘color_in_bgr’), ‘line_thickness’)


# Creating rectangle
cv2.rectangle(img, (30, 30), (300, 200), (0, 255, 0), 5)
#cv2.rectangle(imageObjectName, (‘top_left_vertex_coordinates’), (‘lower_right_vertex_coordinates’), (‘stroke_color_in_bgr’), ‘stroke_thickness’)

cv2.imshow('rectangle', img)

# Allows us to see image
# until closed forcefully
cv2.waitKey(0)
cv2.destroyAllWindows()
