# Anti-Sleep-Camera-Based-Alarm-System
A camera-based driver drowsiness detection system using Arduino UNO and OpenCV.

# Abstract
Motorist fatigue is a significant cause of road accidents.
It’s frequently touched o􀆯 by microsleep or dragged eye
check. This design presents a low-cost, vision-grounded
anti-sleep alarm system that uses Arduino UNO R3,
Python with OpenCV, and a webcam. It monitors the
motorist’s eyes continuously. When doziness is detected,
it activates a buzzer and a red LED. A green LED shows
alertness. The system skips using IR detectors to keep it
simple and a􀆯ordable.

# Components Required
1) Arduino UNO R3
2) USB Cable
3) Red LED
4) Green LED
5) Buzzer
6) 220Ω resistors (3 Quantity)
7) Breadboard
8) Few Jumper Wires

# Component                            #   Arduino Pin
Green LED (Long leg → resistor → pin)       Pin 6
Red LED (Long leg → resistor → pin)         Pin 7
Buzzer                                      Pin 8
All negative legs (short)                    GND

# Customizable Parameters in Python Code

# 1) Serial Port Configuration
In the line
“arduino = serial.Serial('COM5', 9600)”
the 'COM5' value represents the serial port to which the
Arduino is connected. This should be updated based on
the actual COM port assigned by the system. Users must
ensure that the correct port (e.g., 'COM3', 'COM6', etc.) is
specified according to their setup.

# 2) Eye Closure Duration Threshold
In the line
“elif current_time - closed_eyes_start >= 2:”
the value 2 represents the duration (in seconds) for which
the eyes must remain closed before drowsiness is
detected and an alert is triggered. For more immediate
detection, this value can be reduced to 1.0 seconds or any
other appropriate threshold based on the desired
sensitivity of the system.

# How to run the Python Script
Press Windows + R
Type cmd then press ENTER key
Step 2: Navigate to the Downloads (desired path address)
Folder
cd C:\Users\KIIT\Downloads
Press ENTER key
Step 3: Run the Python File
If the script is named as drowsiness_detector.py, then type
python drowsiness_detector.py
The webcam window will open, and detection will begin.

# If the below error arises
‘python’ is not recognized as an internal or external
command…
It means Python is not added to path.
Try: py drowsiness_detector.py
