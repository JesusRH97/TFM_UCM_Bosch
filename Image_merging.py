import cv2
import numpy
import os

input_images_path = "/home/jesus/Escritorio/Imagenes_tres_algoritmos"
files_names = os.listdir(input_images_path)
print(files_names)


output_images_path = "/home/jesus/Escritorio/Imagenes_merged"
if not os.path.exists(output_images_path):
    os.makedirs(output_images_path)
    print("Directorio creado: ", output_images_path)


for file_name in files_names:
	image = cv2.imread(input_images_path + "/" + file_name)

	if image is None:
		continue

	image_yolo = image[0:381, 762:1143]
	image_sem = image[381:762, 381:762]
	image_auto = image[762:1143, 0:381]
	image_final = cv2.hconcat([image_yolo, image_sem, image_auto])
	cv2.imwrite(output_images_path + "/" + file_name, image_final)
    
