import subprocess
import argparse
import os
import json
import shlex

def execute_yolo(video_path):
    cmd = [
        "yolo",
        "task=detect",
        "mode=predict",
        "model=C:/virus/FYP/Sign-language/src/best.pt",
        "conf=0.25",
        f"source={video_path}"
    ]

    print(f"Running YOLO with video: {video_path}")

    try:
        subprocess.run(cmd, check=True)
        print("YOLO prediction completed")
    except subprocess.CalledProcessError as e:
        print(f'{{"status": "error", "message": "Error executing YOLO: {e}"}}')


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Process a video file with YOLO.")
    parser.add_argument("video_path", type=str, help="Path to the video file.")
    args = parser.parse_args()

    video_path = args.video_path.strip('"') 

    if not os.path.exists(video_path):
        print(f"Video file not found: {video_path}")
        return

    if not video_path.endswith('.webm'):
        print("This script only processes .webm files.")
        return

    execute_yolo(video_path)

if __name__ == "__main__":
    main()
