# Open the camera
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()
    
    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Perform binary thresholding
    _, binary_frame = cv2.threshold(gray_frame, 128, 255, cv2.THRESH_BINARY)
    
    # Stack grayscale and binary frames horizontally
    combined_frame = cv2.hconcat([gray_frame, binary_frame])
    
    # Display the combined frame
    cv2.imshow('Grayscale and Binary Images', combined_frame)
    
    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()