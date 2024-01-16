import os
import cv2
import easyocr
# os.environ['OMP_NUM_THREADS'] = '1'

# os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

# Create an EasyOCR Reader for English language
reader = easyocr.Reader(['en'])

# Initialize the video capture object with the default camera (or you can pass video file)
cap = cv2.VideoCapture(0)

while True:
    # Read frames from the video capture
    ret, frame = cap.read()
    if not ret:
        break

    # Use EasyOCR to detect text
    results = reader.readtext(frame)

    # Loop through the results and draw rectangle for detection on the frame
    for (bbox, text, prob) in results:
        # Define polygon and draw it on the frame
        (top_left, top_right, bottom_right, bottom_left) = bbox
        top_left = (int(top_left[0]), int(top_left[1]))
        top_right = (int(top_right[0]), int(top_right[1]))
        bottom_right = (int(bottom_right[0]), int(bottom_right[1]))
        bottom_left = (int(bottom_left[0]), int(bottom_left[1]))

        cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)

        # # Put the OCR'ed text on the frame
        # cv2.putText(frame, text, bottom_left,
        #             cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
        if text == 'P688CC':
            cv2.putText(frame, text + '_known', bottom_left,
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
        else : 
            cv2.putText(frame, text + '_unknown', bottom_left,
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # Show the frame
    cv2.imshow('Real-time Number Plate Detection', frame)

    # Wait for the 'q' key to stop the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and destroy any OpenCV windows
cap.release()
cv2.destroyAllWindows()
