from flask import Flask, request, jsonify
from flask_cors import CORS
from ultralytics import YOLO
from collections import Counter
import os

app = Flask(__name__)
CORS(app)

# Load YOLOv8 sign language model
model = YOLO("../src/best.pt")  # Adjust the path to your model file

# Create uploads folder if it doesn't exist
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/predict', methods=['POST'])
def predict():
    if 'video' not in request.files:
        return jsonify({'status': 'error', 'message': 'No video part in the request'}), 400

    video = request.files['video']

    if video.filename == '':
        return jsonify({'status': 'error', 'message': 'No selected video'}), 400

    # Save the uploaded video
    save_path = os.path.join(UPLOAD_FOLDER, video.filename)
    video.save(save_path)

    try:
        # Run prediction using YOLO model
        results = model(save_path)

        # List to store recognized signs
        recognized_signs = []

        # Loop through detections and extract class labels
        for result in results:
            boxes = result.boxes
            if boxes is not None and boxes.cls is not None:
                for cls_id in boxes.cls:
                    label = model.names[int(cls_id)]
                    recognized_signs.append(label)

        # Count and get the most frequent label
        sign_counts = Counter(recognized_signs)
        most_common_sign = sign_counts.most_common(1)[0][0] if sign_counts else None

        return jsonify({
            'status': 'success',
            'recognizedSign': most_common_sign,
            'message': 'YOLO prediction completed'
        })

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)