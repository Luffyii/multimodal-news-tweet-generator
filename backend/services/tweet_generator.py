from transformers import pipeline

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-large"
)


def generate_hashtags(headline):

    words = headline.split()

    hashtags = []

    for w in words[:3]:
        hashtags.append("#" + w.capitalize())

    return " ".join(hashtags)


def generate_tweet(headline, ocr_text, caption, entities):

    entity_text = ", ".join(entities[:3])

    prompt = f"""
Generate a concise Twitter post summarizing the news.

Headline: {headline}

Article: {ocr_text}

Image Description: {caption}

Key Entities: {entity_text}

Rules:
- Maximum 240 characters
- Mention key people or places
- Use engaging social media tone

Tweet:
"""

    result = generator(
        prompt,
        max_new_tokens=80,
        temperature=0.7
    )

    tweet = result[0]["generated_text"]

    hashtags = generate_hashtags(headline)

    tweet = tweet + " " + hashtags

    if len(tweet) > 250:
        tweet = tweet[:247] + "..."

    return tweet