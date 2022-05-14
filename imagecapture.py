import cv2
from time import strftime

key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0)
while True:
    try:
        check, frame = webcam.read()
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        if key == ord('s'):
            string = str(strftime('%H:%M:%S:%p'))+'.jpg'
            cv2.imwrite(filename=string, img=frame)
            img_new = cv2.imread(string, cv2.IMREAD_GRAYSCALE)
            cv2.waitKey(1000)
            print("Image saved!")
            continue

        elif key == ord('q'):
            print("Camera OFF!")
            webcam.release()
            cv2.destroyAllWindows()
            break

    except(KeyboardInterrupt):
        print("Camera OFF!")
        cv2.destroyAllWindows()
        break
