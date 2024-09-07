from flask import Flask, request, jsonify
import requests
from deepface import DeepFace
from PIL import Image
from io import BytesIO
import os
import base64

app = Flask(__name__)


# Function to download an image from a URL
def download_image(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Extract the file name without query parameters
    img_name_with_ext = url.split("/")[-1].split("?")[0]
    
    img = Image.open(BytesIO(response.content))
    img.save(img_name_with_ext)
    return img_name_with_ext


# Function to save a base64-encoded image string to a file
def save_base64_image(base64_str):
    image_data = base64.b64decode(base64_str)
    img = Image.open(BytesIO(image_data))
    img_path = "base64_image.jpg"  # Save it with a default name
    img.save(img_path)
    return img_path


@app.route('/verify', methods=['POST'])
def compare_faces():
    # Get image data from JSON body
    data = request.get_json()
    image1_url = data.get('base_image')
    image2_url = data.get('comparison_image')
    image1_base64 = data.get('base_image_base64')
    image2_base64 = data.get('comparison_image_base64')

    # Ensure user provides either a URL or base64 for each image, but not both
    if (image1_url and image1_base64) or (image2_url and image2_base64):
        return jsonify({
            "error": "You can only provide either URL or base64 string for each image, not both."
        }), 400

    try:
        # Process base_image
        if image1_url:
            image1_path = download_image(image1_url)
        elif image1_base64:
            image1_path = save_base64_image(image1_base64)
        else:
            return jsonify({"error": "base_image URL or base_image_base64 is required."}), 400

        # Process comparison_image
        if image2_url:
            image2_path = download_image(image2_url)
        elif image2_base64:
            image2_path = save_base64_image(image2_base64)
        else:
            return jsonify({
                "error": "comparison_image URL or comparison_image_base64 is required."
            }), 400

        # Perform face verification using DeepFace
        result = DeepFace.verify(img1_path=image1_path, img2_path=image2_path)
        verification_result = {
            "verified": result["verified"],
            "distance": result["distance"]
        }

        # Clean up downloaded images after processing
        os.remove(image1_path)
        os.remove(image2_path)

        return jsonify(verification_result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)
