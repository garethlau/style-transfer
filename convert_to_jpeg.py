import imghdr
# import cv2
import os
import glob

for folder in ['mountains', 'abstract']:
    image_path = os.path.join(os.getcwd(), ('images/' + folder))
    print(image_path)
    for file in glob.glob(image_path + '/*.jpg'):
        # image = cv2.imread(file)
        file_type = imghdr.what(file)
        if file_type != 'jpeg':
            print(file + " - invalid - " + str(file_type))
