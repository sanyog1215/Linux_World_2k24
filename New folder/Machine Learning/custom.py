import numpy as np
import cv2

def create_custom_image():
    # Define the size of the image (height, width, channels) and create an empty image with three channels (RGB), initialized to zero (black)
    image = np.zeros((512, 512, 3), dtype=np.uint8)

    # Draw a green rectangle with a new position and size
    cv2.rectangle(image, (50, 50), (300, 300), (0, 255, 0), -1)

    # Draw a yellow circle with a new position and radius
    cv2.circle(image, (400, 100), 75, (0, 255, 255), -1)

    # Draw a red line with a new start and end position, and thicker line width
    cv2.line(image, (512, 0), (0, 512), (0, 0, 255), 10)

    # Draw an ellipse with a different center, axes length, angle, startAngle, and endAngle
    cv2.ellipse(image, (256, 400), (100, 50), 45, 0, 360, (255, 0, 255), -1)

    # Add some white text to the image with a new position
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, 'Custom Image', (50, 450), font, 2, (255, 255, 255), 3, cv2.LINE_AA)

    # Display the image
    cv2.imshow('Modified Custom Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Optionally, save the image to a file
    cv2.imwrite('modified_custom_image.png', image)

# Run the function
create_custom_image()
