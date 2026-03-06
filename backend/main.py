from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os

from services.ocr_service import extract_text
from services.image_caption_service import generate_caption
from services.ner_service import extract_entities
from services.tweet_generator import generate_tweet
from services.twitter_service import post_tweet

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.get("/")
def home():
    return {"message": "Multimodal News Tweet Generator Running"}


@app.post("/generate_tweet")
async def generate_tweet_api(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # OCR
    ocr_text = extract_text(file_path)

    # Caption
    caption = generate_caption(file_path)

    # Headline
    headline = ocr_text.split("\n")[0] if ocr_text else "Breaking News"

    # Named entities
    entities = extract_entities(ocr_text)

    # Tweet generation
    tweet = generate_tweet(headline, ocr_text, caption, entities)

    return {
        "headline": headline,
        "ocr_text": ocr_text,
        "caption": caption,
        "entities": entities,
        "tweet": tweet
    }


@app.post("/post_tweet")
async def post_tweet_api(tweet_text: str):

    tweet_id = post_tweet(tweet_text)

    return {
        "message": "Tweet posted successfully",
        "tweet_id": tweet_id
    }