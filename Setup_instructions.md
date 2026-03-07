# Multimodal News → Tweet Generator

Setup Instructions

## 1. Clone the Repository

First, clone the project from GitHub.

```bash
git clone https://github.com/Luffyii/multimodal-news-tweet-generator.git
cd multimodal-news-tweet-generator
```

---

## 2. Backend Setup

### Create Virtual Environment

Navigate to the backend folder and create a virtual environment.

```bash
cd backend
python -m venv venv
```

Activate the environment.

Windows:

```bash
venv\Scripts\activate
```

Mac / Linux:

```bash
source venv/bin/activate
```

---

### Install Dependencies

Install all required Python libraries.

```bash
pip install -r requirements.txt
```

If the requirements file is missing, install manually:

```bash
pip install fastapi uvicorn pillow pytesseract transformers torch tweepy rouge-score nltk evaluate
```

---

### Download NLTK Resources

Start Python:

```bash
python
```

Then run:

```python
import nltk
nltk.download('punkt')
exit()
```

---

### Run the Backend Server

```bash
uvicorn main:app --reload
```

Backend will start at:

```
http://127.0.0.1:8000
```

API documentation:

```
http://127.0.0.1:8000/docs
```

---

## 3. Frontend Setup

Open a new terminal and move to the frontend folder.

```bash
cd frontend
```

Install Node.js dependencies.

```bash
npm install
```

Start the development server.

```bash
npm run dev
```

Frontend will run at:

```
http://localhost:5173
```

---

## 4. Twitter API Setup (Optional)

To enable automatic tweet posting:

1. Create a developer account on Twitter/X.
2. Create a new application.
3. Generate the following credentials:

* API Key
* API Secret
* Access Token
* Access Token Secret

Add them inside the backend `.env` file.

```
API_KEY=your_api_key
API_SECRET=your_api_secret
ACCESS_TOKEN=your_access_token
ACCESS_TOKEN_SECRET=your_access_token_secret
```

---

## 5. Running the Full Application

1. Start backend server
2. Start frontend server
3. Open browser:

```
http://localhost:5173
```

Upload a news image and the system will automatically generate a tweet.

---

## 6. Project Structure

```
multimodal-news-tweet-generator
│
├── backend
│   ├── main.py
│   ├── services
│   ├── evaluation
│   └── requirements.txt
│
├── frontend
│   ├── src
│   ├── package.json
│   └── vite.config.js
│
├── README.md
└── SETUP_INSTRUCTIONS.md
```

---

## 7. Troubleshooting

### ModuleNotFoundError

Run:

```bash
pip install -r requirements.txt
```

### Port Already in Use

Change the backend port:

```bash
uvicorn main:app --reload --port 8001
```

### Node Modules Issue

```bash
rm -rf node_modules
npm install
```

---

## 8. Test the System

1. Upload a news image
2. OCR extracts the text
3. Caption model analyzes the image
4. Tweet generator produces a summarized tweet
5. Optionally post directly to Twitter

---

## 9. Requirements

Software Required:

* Python 3.9+
* Node.js 18+
* npm
* Git
