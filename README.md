# Sign Language Recognition Project

This project is a full-stack application for recognizing sign language from video using deep learning.  
It consists of a **Flask backend** (Python) that uses a YOLOv8 model for sign detection, and an **Angular frontend** for user interaction.

---

## Features

- Upload sign language videos via the web interface
- Backend processes videos using a YOLOv8 model and returns the recognized sign
- Modern Angular frontend with Bootstrap styling

---

## Project Structure

```
Sign-language/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── uploads/
│
└── frontend/
    ├── package.json
    └── src/
        ├── styles.css
        └── ... (Angular app files)
```

---

## Setup Instructions

### 1. Backend (Flask + YOLOv8)

1. **Navigate to the backend folder:**
    ```
    cd backend
    ```

2. **Create a virtual environment (optional but recommended):**
    ```
    python -m venv venv
    venv\Scripts\activate   # On Windows
    ```

3. **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```

4. **Ensure your YOLO model file (`best.pt`) is present at `../src/best.pt` at the root or update the path in `app.py`.** 

    Link to model file - https://drive.google.com/file/d/1oHEa9N6cpwVdYXZoa_XCDtaUNFH_MdCW/view?usp=sharing

5. **Run the backend server:**
    ```
    python app.py
    ```

---

### 2. Frontend (Angular)

1. **Navigate to the frontend folder:**
    ```
    cd frontend
    ```

2. **Install dependencies:**
    ```
    npm install
    ```

3. **Run the Angular development server:**
    ```
    ng serve
    ```

4. **Open your browser and go to** [http://localhost:4200](http://localhost:4200)

---

## Usage

- Use the web interface to upload a sign language video.
- The backend will process the video and return the recognized sign.

---

## Notes

- Make sure Python and Node.js are installed on your system.
- The backend uses a YOLOv8 model; ensure the model weights are available at the specified path.
- If you encounter issues with dependencies, check the versions in `requirements.txt` and `package.json`.

---

## License

This project is for educational purposes.