import numpy as np
import cv2 as cv

frame = cv.imread('right.png')

height, width, layers = frame.shape

zeros = np.zeros((height, width), dtype="uint8") 
 
(blue, green, red) = cv.split(frame)


magenta = cv.merge([blue, zeros, red])

ciano = cv.merge([blue, green, zeros])

amarelo = cv.merge([zeros, green, red])


def concat_tile(im_list_2d):
    return cv.vconcat([cv.hconcat(im_list_h) for im_list_h in im_list_2d])

im1_s = cv.resize(frame, dsize=(0, 0), fx=0.5, fy=0.5)
im_tile = concat_tile([[frame, magenta],
                       [ciano, amarelo]])


cv.imshow('Exercicio 2', im_tile)
