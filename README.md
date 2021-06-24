# Volume_and_Brightness_Control_Using_Hand_Gestures
This project aims to control the system volume and screen brightness using hand gestures. Use your left hand for brightness control and right hand for volume control. For detection of hand landmarks, mediapipe library is used.

## DEMO
https://user-images.githubusercontent.com/57738183/123324025-f8e9b600-d553-11eb-96bb-63f8b6259a23.mp4

## How to run this script

* Clone this repo
```
git clone <url>
```
* Install virtual environment
```
pip install virtualenv
```
* Create a virtual environment
```
virtualenv venv
```
* Activate virtual environment
```
venv\Scripts\activate
```
* Install all the dependencies
```
pip install -r requirements.txt
```
* Run the script
```
python volBrtnessControl.py
```
# Explanation 
The code uses mediapipe library to detect hand landmark positions and handedness. If the frame detects one hand, it finds out if its a left hand or right hand and triggers the brightness contreol and volume control function respectively. If the current frame contains both hands, both volume and brightness control functions are triggered simultaneously in different threads.
