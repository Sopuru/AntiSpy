# AntiSpy
# Joshua Sopuru 
Is someone Spying me? Python Script to check if your Camera or Audio is secretly videoing you

import os
import psutil
import ctypes
import winreg
import cv2
import sounddevice as sd
import numpy as np
import time

def check_missing_files(files):
    missing_files = [file for file in files if not os.path.exists(file)]
    if missing_files:
        print(f"Missing files: {missing_files}")

def check_malicious_processes(allowed_processes):
    running_processes = [process.name() for process in psutil.process_iter(['pid', 'name'])]
    malicious_processes = [process for process in running_processes if process not in allowed_processes]
    if malicious_processes:
        print(f"Malicious processes: {malicious_processes}")

def check_camera_access():
    cap = cv2.VideoCapture(0)
    _, _ = cap.read()
    cap.release()

def check_microphone_access():
    duration = 5  # seconds
    recording = sd.rec(int(duration * 44100), channels=2, dtype=np.int16)
    sd.wait()

def main():
    # Define the files to monitor
    files_to_monitor = ['C:\\path\\to\\file1.txt', 'C:\\path\\to\\file2.txt']

    # Define the processes that are allowed
    allowed_processes = ['explorer.exe', 'svchost.exe', 'YourTrustedProcess.exe']

    try:
        while True:
            # Check for missing files
            check_missing_files(files_to_monitor)

            # Check for malicious processes
            check_malicious_processes(allowed_processes)

            # Check camera and microphone access
            check_camera_access()
            check_microphone_access()

            time.sleep(60)  # Adjust the sleep time as needed
    except KeyboardInterrupt:
        print("Monitoring stopped.")

if __name__ == "__main__":
    if ctypes.windll.shell32.IsUserAnAdmin() != 1:
        print("Please run the script as an administrator.")
    else:
        main()

Monitoring for missing files, malicious processes, and unauthorized access to camera and microphone on a Windows OS involves a combination of file system monitoring, 
process monitoring, and access control

# About the script
While this script may not cover all aspects of cybersecurity, it incorporates some key elements that can enhance security on a Windows system. Here are some advantages:

# 1. File Integrity Monitoring (FIM): 
The script checks for missing files, which can indicate tampering or unauthorized changes early. File integrity monitoring is crucial for detecting and responding to security incidents.

# 2. Process Monitoring: 
By monitoring running processes and identifying those not on the approved list, the script helps to detect potentially malicious activities. Unauthorized processes can be a sign of malware or other security threats.

# 3. Access Control: 
Checking camera and microphone access adds another layer of security. Unauthorized access to these devices could be a privacy concern, and the script helps identify such access attempts.

