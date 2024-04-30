import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Create a black canvas to draw on
canvas = None
canvas_size = (640, 480)
canvas_color = (0, 0, 0)
import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Create a black canvas to draw on
canvas = None
canvas_size = (640, 480)
canvas_color = (0, 0, 0)

cap = cv2.VideoCapture(0)
hands = mp_hands.Hands()

# Initialize drawing parameters
drawing_color = (0, 400, 0)  # Dark green color for drawing
drawing_thickness = 4  # Thickness of the drawing

# Initialize variables to store previous and current finger tip coordinates
prev_x, prev_y = None, None

while True:
    success, image = cap.read()
    if not success:
        continue

    # Flip the image horizontally for a later selfie-view display
    image = cv2.flip(image, 1)

    # Create the canvas if it is not created yet
    if canvas is None:
        canvas = 255 * np.ones((image.shape[0], image.shape[1], 3), dtype=np.uint8)
        canvas[:] = canvas_color

    # Process the image to get hand landmarks
    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Check if hand landmarks are detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Get the coordinates of the index finger tip
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            # Convert the normalized finger tip coordinates to pixel coordinates
            x, y = int(index_finger_tip.x * image.shape[1]), int(index_finger_tip.y * image.shape[0])

            # Write text at the tip of the index finger on the canvas
            cv2.putText(canvas, '', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, drawing_color, 2, cv2.LINE_AA)

            # If previous finger tip coordinates exist, draw a line between them on the canvas
            if prev_x is not None and prev_y is not None:
                cv2.line(canvas, (prev_x, prev_y), (x, y), drawing_color, drawing_thickness)

            # Update previous finger tip coordinates
            prev_x, prev_y = x, y

    # Combine the original image with the canvas
    output_image = cv2.addWeighted(image, 1, canvas, 0.5, 0)

    # Display the combined image
    cv2.imshow('MediaPipe Hands', output_image)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)
hands = mp_hands.Hands()

# Initialize drawing parameters
drawing_color = (0, 400, 0)  # Dark green color for drawing
drawing_thickness = 4  # Thickness of the drawing

# Initialize variables to store previous and current finger tip coordinates
prev_x, prev_y = None, None

while True:
    success, image = cap.read()
    if not success:
        continue

    # Flip the image horizontally for a later selfie-view display
    image = cv2.flip(image, 1)

    # Create the canvas if it is not created yet
    if canvas is None:
        canvas = 255 * np.ones((image.shape[0], image.shape[1], 3), dtype=np.uint8)
        canvas[:] = canvas_color

    # Process the image to get hand landmarks
    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Check if hand landmarks are detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Get the coordinates of the index finger tip
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            # Convert the normalized finger tip coordinates to pixel coordinates
            x, y = int(index_finger_tip.x * image.shape[1]), int(index_finger_tip.y * image.shape[0])

            # Draw a dark green circle at the tip of the index finger on the canvas
            cv2.circle(canvas, (x, y), 5, drawing_color, -1)

            # If previous finger tip coordinates exist, draw a line between them on the canvas
            if prev_x is not None and prev_y is not None:
                cv2.line(canvas, (prev_x, prev_y), (x, y), drawing_color, drawing_thickness)

            # Update previous finger tip coordinates
            prev_x, prev_y = x, y

    # Combine the original image with the canvas
    output_image = cv2.addWeighted(image, 1, canvas, 0.5, 0)

    # Display the combined image
    cv2.imshow('MediaPipe Hands', output_image)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
