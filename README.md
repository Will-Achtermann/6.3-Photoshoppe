# 6.3-Photoshoppe

**Assignment: Building a Simple "Photoshoppe" Image Editor in Python with Tkinter**

In this assignment, you will create a simplified image editor using Python’s Tkinter library and PIL (Pillow) for image manipulation. This "Photoshoppe" program should allow users to apply various filters and effects to images, such as black and white, sepia, invert, contrast adjustment, and more. The goal is to build a GUI where users can load an image, apply effects, and save the edited image.

### Requirements

1. **Image Loading and Displaying:**
   - Provide an input field and button where the user can enter the file name of an image to load.
   - Resize the image to fit within a 600x400 display on the canvas.

2. **Basic Filters:**
   - **Black & White**: Convert the image to grayscale.
   - **Sepia**: Apply a sepia tone to the image by adjusting pixel colors.
   - **Invert**: Invert all colors in the image.
   - **Increase Contrast**: Increase the contrast level of the image.
   - **Line Drawing**: Create a "line drawing" effect by finding and displaying edges in the image.
   - **Pointillism**: Apply a pointillism effect by drawing small circles of varying color intensities on the image.

3. **Pixelate Mode:**
   - Allow users to pixelate selected areas of the image.
   - Activate pixelate mode with a button. When enabled, let users click and drag to define a rectangular area for pixelation.

4. **Crop Mode:**
   - Allow users to crop selected areas of the image.
   - Activate crop mode with a button. When enabled, let users select an area to crop with a click-and-drag motion.

5. **Saving Modified Image:**
   - Provide a "Save" button to save the modified image under a new file name.

6. **GUI Layout (using Tkinter):**
   - Organize buttons for each filter and effect on the left side.
   - Display the image on a 600x400 canvas on the right.
   - Show any error messages, such as "File not found," in the console if a file can't be loaded.

### Instructions
1. **Setup**: Install the Pillow library for image manipulation:
   ```bash
   pip install pillow
   ```

2. **Create Functions for Each Filter and Effect**:
   - Use functions to organize your code.
   - For example, create `apply_black_and_white()`, `apply_sepia()`, `apply_invert()`, and so on, each applying a different effect.

3. **Implement the GUI in Tkinter**:
   - Use a canvas widget to display the image.
   - Add buttons for each filter and effect.
   - Create entry fields and buttons for loading and saving images.

4. **Event Handling**:
   - Use mouse events (`<Button-1>`, `<B1-Motion>`, and `<ButtonRelease-1>`) to let users select areas of the image for cropping or pixelation.

5. **Testing**:
   - Test your program with different images and effects to ensure each filter and mode works correctly.

### Grading Rubric
1. **Functionality** (60 points)
   - Image loading and displaying (10 points)
   - Filter application (5 points each for each filter)
   - Pixelate and crop modes (15 points each)
   - Save functionality (5 points)

2. **User Interface and Usability** (20 points)
   - Intuitive button layout (10 points)
   - Error handling for missing files (10 points)

3. **Code Quality and Structure** (20 points)
   - Clear, organized, and well-commented code (10 points)
   - Efficient use of functions and event handling (10 points)
