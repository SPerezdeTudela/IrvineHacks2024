# ASL Alphabet Detector - IrvineHacks2024

### Members
Azra Zahin, Ngoc Huynh, and Sofia Perez de Tudela (with special thanks to Waddles)

### How to Run
- open the flask_app project folder in a Python virtual environment via VScode, and hit **python -m flask run** in terminal

### Project Structure
- static folder: CSS and images
- templates: HTML
- app.py: main script
- camera.py: live webcam feed for predictions
- asl_cnn.h5: keras model

### Inspiration
In an age of video streaming and video conversation, it is more important than ever to make sure that the tech space can be explored and navigated effectively by the folks in the American Sign Language (ASL) community. In order to communicate with those who don't know how to sign, ASL users often have to resign themselves to typing out their thoughts. However, doing so takes away from the expression and emotion that can be transmitted through video, defeating the purpose of using video transmission in the first place. We want to provide a synchronous transcription of ASL, in order to allow ASL users the joy of conversation afforded to their peers who can use their voice.

### What it does
The ASL Alphabet Detector takes in real time video feed from the user's webcam and maps out hand gestures using computer vision. It then sends frames capturing a unique motion to the deep learning model and outputs the English letter it's most confident every 10 frame interval.

### How we built it
First, we sourced the public ['Sign Language MNIST'](https://www.kaggle.com/datasets/datamunge/sign-language-mnist) dataset from Kaggle. We then created an image pipeline and trained our own Keras deep learning model on the different variations of hand positions in Jupyter Notebook. To take in live video feed, we integrated our trained model with the OpenCV library and abstracted the project into a user-friendly website.
