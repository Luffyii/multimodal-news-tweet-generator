# Multimodal News → Tweet Generator

An AI-powered system that automatically generates concise tweets from news images using multimodal AI models.

The system extracts textual content from news images using OCR, analyzes the visual content using an image captioning model, and combines both to generate an informative tweet.

---

# Project Overview

This project demonstrates how multimodal AI can be used to transform news content into social media-ready posts automatically.

The system processes a news image, extracts textual information, analyzes the visual context, and generates a short tweet summarizing the news content.

The generated tweet can optionally be posted directly to Twitter using the Twitter API.

---

# Features

• Extracts text from news images using OCR
• Generates image captions using a vision-language model
• Produces concise tweets from extracted content
• Interactive web interface for uploading news images
• Optional Twitter API integration for automatic posting
• Evaluation metrics for generated tweets (BLEU, ROUGE, BERTScore)

---

# System Architecture

User Upload Image
↓
Frontend (React + Vite UI)
↓
FastAPI Backend
↓
OCR Module (Tesseract)
↓
Image Caption Module (BLIP / Vision Transformer)
↓
Tweet Generation Module (Transformer Model)
↓
Generated Tweet
↓
Optional Twitter Posting (Tweepy API)

---

# Technology Stack

Frontend
React, Vite, Axios, TailwindCSS

Backend
FastAPI, Python

Cloud / Deployment (optional)
Render / Docker / HuggingFace Spaces

Tools & Frameworks
Tesseract OCR, Tweepy

AI / ML Models
Transformers (HuggingFace), BLIP Image Captioning Model

Evaluation Metrics
BLEU Score
ROUGE Score
BERTScore

---

# Project Structure

multimodal-news-tweet-generator

backend
│
├── main.py
├── services
│   ├── ocr_service.py
│   ├── image_caption_service.py
│   ├── tweet_generator.py
│   └── twitter_service.py
│
├── evaluation
│   └── evaluate_model.py
│
└── requirements.txt

frontend
│
├── src
│   ├── App.jsx
│   ├── main.jsx
│   └── index.css
│
├── package.json
└── vite.config.js

README.md
SETUP_INSTRUCTIONS.md

---

# Setup Instructions

Clone the repository

git clone https://github.com/your-username/multimodal-news-tweet-generator.git
cd multimodal-news-tweet-generator

---

## Backend Setup

cd backend

Create virtual environment

python -m venv venv

Activate environment

Windows
venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

Run the backend server

uvicorn main:app --reload

Backend will run at

http://127.0.0.1:8000

---

## Frontend Setup

cd frontend

Install dependencies

npm install

Start the frontend

npm run dev

Frontend will run at

http://localhost:5173

---

# Evaluation Metrics

To evaluate tweet generation performance the following metrics are used:

BLEU Score
Measures n-gram similarity between generated tweet and reference tweet.

ROUGE Score
Measures overlap between generated and reference summaries.

BERTScore
Measures semantic similarity using contextual embeddings.

---

# Example Workflow

1 Upload a news image
2 OCR extracts text from the image
3 Image caption model analyzes visual content
4 Tweet generator summarizes the information
5 Generated tweet is displayed to the user
6 Optionally post tweet using Twitter API

---

# Innovation

• Combines visual and textual information for content generation
• Automates social media summarization for news articles
• Integrates OCR, vision models, and NLP models into a unified pipeline

---

# Future Enhancements

• Support for multiple languages
• Improved tweet summarization using larger language models
• Real-time news monitoring system
• Automatic hashtag and trend detection
• Deployment as a public web application

---

# Author

Akshai S
BTech – Computer Science Engineering

---

# License

This project is for academic and research purposes.
