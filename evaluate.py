import cv2
import os
import numpy as np


def evaluate():

    cont = 0

    images_path = "/home/jesus/Escritorio/mvtec/USS63/mvtecCAE/ssim/28-07-2021_12-53-07/test/ssim_float64/segmentation/defect"

    gt_path = "/home/jesus/Escritorio/Converted/Imagen_3"

    images_file_names = os.listdir(images_path)
    gt_file_names = os.listdir(gt_path)

    tp = np.zeros(3)
    fp = np.zeros(3)
    fn = np.zeros(3)
    n_pixels = np.zeros(3)

    for i in gt_file_names:
        for j in images_file_names:
            if i == j:
                pr = cv2.imread(images_path + "/" + i)
                gt = cv2.imread(gt_path + "/" + j)

                for cl_i in range(3):
                    tp[cl_i] += np.sum((pr == cl_i) * (gt == cl_i))
                    fp[cl_i] += np.sum((pr == cl_i) * ((gt != cl_i)))
                    fn[cl_i] += np.sum((pr != cl_i) * ((gt == cl_i)))
                    n_pixels[cl_i] += np.sum(gt == cl_i)

    cl_wise_score = tp / (tp + fp + fn + 0.000000000001)
    n_pixels_norm = n_pixels / np.sum(n_pixels)
    frequency_weighted_IU = np.sum(cl_wise_score*n_pixels_norm)
    mean_IU = np.mean(cl_wise_score)

    print(cl_wise_score)
    print(frequency_weighted_IU)
    print(mean_IU)


evaluate()