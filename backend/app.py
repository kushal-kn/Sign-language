from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import subprocess
import os
import time

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['POST'])
@cross_origin()
def predict():
    # Get the video data from the request
    video_data = request.files.get('video')

    # Generate a unique filename based on the current timestamp
    timestamp = int(time.time())
    video_filename = f'received_video_{timestamp}.webm'
    print(video_filename)

    # Specify the folder path to save the video
    video_folder = 'C:/virus/Final year project/sign-master/src'
    # Create the folder if it doesn't exist
    os.makedirs(video_folder, exist_ok=True)
    video_path = os.path.join(video_folder, video_filename)
    video_data.save(video_path)

    # After saving the video, execute the second Python script
    # Change directory to where the second script is located
    script_path = 'C:/virus/Final year project/sign-master/backend/front.py'
    os.chdir(os.path.dirname(script_path))

    # Execute the second script and capture its output
    result = subprocess.run(['python', script_path],
                            capture_output=True, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        response = result.stdout
    else:
        response = f"Error: {result.stderr}"

    # Send the command output as the response back to the client
    return jsonify({'response': response})


if __name__ == '_main_':
    print('hiii')
    app.run(debug=True)
    