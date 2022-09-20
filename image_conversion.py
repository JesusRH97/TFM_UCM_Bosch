import cv2
import os

input_images_path = "/home/jesus/Escritorio/Ground_truth_test/Imagen_3"
files_names = os.listdir(input_images_path)
print(files_names)

output_images_path = "/home/jesus/Escritorio/Converted/Imagen_3"
if not os.path.exists(output_images_path):
    os.makedirs(output_images_path)
    print("Directorio creado: ", output_images_path)

count = 0
for file_name in files_names:
    
    '''
    if file_name.split(".")[-1] not in ["jpeg", "png"]:
        continue
    '''
    image_path = input_images_path + "/" + file_name
    print(image_path)
    image = cv2.imread(image_path)
    
    if image is None:
        continue

    image[image == 1] = 255
    image[image == 2] = 0

    image = cv2.resize(image, (256, 256))

    cv2.imwrite(output_images_path + "/" + file_name, image)
    '''
    cv2.imshow("Image", image)
    cv2.waitKey(0)
cv2.destroyAllWindows()
'''