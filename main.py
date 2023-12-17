import cv2
import os
import time
import uuid

images_path = '/Users/nabindev/PycharmProjects/ASl'

labels = ['also']

number_images = 15

for label in labels:

    os.mkdir('/Users/nabindev/PycharmProjects/ASl/' + label)
    cap = cv2.VideoCapture(0)
    print("Collecting Images for {}".format(label))
    time.sleep(5)

    for img_no in range(number_images):
        print("collecting image number {}".format(img_no))
        flag, frame = cap.read()
        print(flag)
        if flag:
            image_name = os.path.join(images_path, label, label+'{}.jpg'.format(img_no))
            print(image_name)
            cv2.imwrite(image_name, frame)
            cv2.imshow('frame', frame)
            time.sleep(4)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        else:
            print("Error loading frame")
    cap.release()