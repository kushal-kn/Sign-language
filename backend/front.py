# from flask import Flask, jsonify
# import os
# import subprocess
# import time
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler

# app = Flask(__name__)

# # Folder to watch for new videos
# WATCH_FOLDER = "C:/Users/abhay/project/src"

# class OnMyWatch:
#     def __init__(self):
#         self.observer = Observer()

#     def run(self):
#         event_handler = Handler()
#         self.observer.schedule(event_handler, WATCH_FOLDER, recursive=True)
#         self.observer.start()
#         try:
#             while True:
#                 time.sleep(5)
#         except:
#             self.observer.stop()
#             print("Observer Stopped")
#         self.observer.join()

# class Handler(FileSystemEventHandler):
#     @staticmethod
#     def on_created(event):
#         if event.is_directory:
#             return None
#         if event.event_type == 'created':
#             # Delay processing to avoid incomplete file issues (especially for larger files)
#             time.sleep(1)  # Wait a bit for the file to fully write (can adjust based on typical file write times)
#             normalized_path = event.src_path.replace('\\', '/')
#             if normalized_path.endswith('.webm'):
#                 print("Received created event - %s." % normalized_path)
#                 Handler.execute_yolo(normalized_path)
#             else:
#                 print(f"Ignored file (not a .webm or still writing): {normalized_path}")

#     @staticmethod
#     def execute_yolo(video_path):
#         cmd = f"yolo task=detect mode=predict model=C:/Users/abhay/project/src/best.pt conf=0.25 source={video_path}"
#         try:
#             subprocess.run(cmd, shell=True, check=True)
#             print(f"Command executed successfully: {cmd}")
#         except subprocess.CalledProcessError as e:
#             print(f"An error occurred while executing YOLO command: {e}")

# @app.route('/')
# def index():
#     return jsonify({"status": "Application is running and monitoring..."})

# if __name__ == '__main__':
#     watch = OnMyWatch()
#     watch.run()
#     app.run(host='0.0.0.0', port=5000, use_reloader=False)

import subprocess
import argparse

def execute_yolo(video_path):
    """
    Executes the YOLO command on the specified video file.
    """
    # Define the command to run YOLO; you might need to adjust paths and parameters depending on your setup
    cmd = f"yolo task=detect mode=predict model=C:/virus/Final year project/sign-master/src/best.pt conf=0.25 source={video_path}"
    try:
        # Execute the command
        subprocess.run(cmd, shell=True, check=True)
        print(f"Command executed successfully: {cmd}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing YOLO command: {e}")

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Process a video file with YOLO.")
    parser.add_argument("video_path", type=str, help="Path to the video file.")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Check the file extension
    if not args.video_path.endswith('.webm'):
        print("This script only processes .webm files.")
        return
    
    # Execute YOLO on the provided video file
    execute_yolo(args.video_path)

if __name__ == "__main__":
    main()
