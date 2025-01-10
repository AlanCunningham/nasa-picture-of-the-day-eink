import requests
import settings
import shutil
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from inky.auto import auto


def main():
    display = auto()

    # Get the nasa image of the day api response
    nasa_endpoint = f"https://api.nasa.gov/planetary/apod?api_key={settings.nasa_api_key}"
    response = requests.get(nasa_endpoint).json()
    image_url = response["url"]
    title = response["title"]

    print(title, image_url)

    image_download = requests.get(image_url, stream=True)
    with open("image.png", "wb") as image_file:
        image_download.raw.decode_content = True
        shutil.copyfileobj(image_download.raw, image_file)

    # Resize the image for the eink display (losing the aspect ratio in the process)
    image = Image.open("image.png")
    resized_image = image.resize((800, 480))
    resized_image.save("resized.png")

    # Draw the title onto the image
    draw = ImageDraw.Draw(resized_image)
    title_font = ImageFont.truetype("Font.ttc", 35)
    text_coords = (75, 410)
    draw.text(text_coords, title, font=title_font, fill="white", stroke_width=2, stroke_fill="black")

    # Brighten the image slightly
    enhancer = ImageEnhance.Brightness(resized_image)
    resized_image = enhancer.enhance(1.5)

    display.set_image(resized_image)
    display.show()


if __name__ == "__main__":
    main()
