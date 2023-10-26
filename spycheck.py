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