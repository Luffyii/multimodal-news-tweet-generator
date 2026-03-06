from transformers import pipeline

captioner = pipeline(
    "image-to-text",
    model="Salesforce/blip-image-captioning-large"
)


def generate_caption(image_path):

    result = captioner(image_path)

    caption = result[0]["generated_text"]

    return caption