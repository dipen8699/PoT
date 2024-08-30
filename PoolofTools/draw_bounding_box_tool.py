import sys

from langchain.tools import tool
import cv2
import numpy as np

@tool('draw_bounding_box_tool', return_direct=False)
def draw_bounding_box(image_path: str, boxes: list) -> str:
    """This tool takes an image path and a list of bounding boxes to draw on the image."""
    try:
        # Read the image
        image = cv2.imread(image_path)
        
        # Draw bounding boxes
        for box in boxes:
            x, y, w, h = box
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        # Save the modified image
        output_path = 'output_image.jpg'
        cv2.imwrite(output_path, image)
        
        return f'Bounding boxes drawn and saved to {output_path}'
    except:
        return 'Error: ' + str(sys.exc_info())