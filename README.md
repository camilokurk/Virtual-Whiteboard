# Virtual Whiteboard

A virtual whiteboard application that lets you draw in the air using hand gestures. The app uses your webcam to track hand movements and translates specific finger positions into drawing commands.

## Techniques

The code uses several computer vision and image processing techniques:

- **[`cv2.flip()`](https://docs.opencv.org/4.x/d2/de8/group__core__array.html#gaca7be533e3dac7feb70fc60635adf441)** - Mirrors the webcam feed horizontally to create a natural drawing experience
- **[Color space conversion](https://docs.opencv.org/4.x/d8/d01/group__imgproc__color__conversions.html)** - Converts BGR to RGB for MediaPipe processing
- **Hand landmark detection** - Tracks 21 3D hand landmarks in real-time using MediaPipe
- **Gesture recognition** - Interprets finger positions relative to knuckles to detect drawing, erasing, and idle states
- **Frame-by-frame video processing** - Captures and processes live video at the native webcam framerate

## Technologies

- **[OpenCV](https://opencv.org/)** (4.13.0.90) - Handles video capture, image manipulation, and rendering
- **[MediaPipe](https://mediapipe.dev/)** (0.10.31) - Google's ML solution for hand tracking and landmark detection. Uses a palm detection model followed by hand landmark identification
- **[MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands.html)** - Specifically configured with high confidence thresholds (0.9 detection, 0.8 tracking) for precise gesture control

## How It Works

The application tracks your index finger tip (landmark 8) as the drawing cursor. Three gesture modes are supported:

- **Draw** - Index finger up, middle finger down
- **Navigate** - Index and middle fingers up (cursor turns red, no drawing)
- **Clear** - Index, middle, and ring fingers up (erases all points)

Drawing points are stored as pixel coordinates and rendered as filled circles on each frame. The webcam resolution is set to 1280x740 for a larger working area.
