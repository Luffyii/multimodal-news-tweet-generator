import fitz
import os


def extract_images_from_pdf(pdf_path, output_folder="uploads"):

    doc = fitz.open(pdf_path)

    image_paths = []

    for page_index in range(len(doc)):

        page = doc.load_page(page_index)

        images = page.get_images(full=True)

        for img_index, img in enumerate(images):

            xref = img[0]

            base_image = doc.extract_image(xref)

            image_bytes = base_image["image"]

            image_path = os.path.join(
                output_folder,
                f"page{page_index}_img{img_index}.png"
            )

            with open(image_path, "wb") as f:
                f.write(image_bytes)

            image_paths.append(image_path)

    return image_paths