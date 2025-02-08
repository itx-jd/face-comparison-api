# Face Comparison API

**Face Comparison API** is a simple, powerful Flask-based solution for comparing two images to determine if they feature the same person. Powered by **DeepFace**, this API allows you to easily compare faces with just a URL or base64-encoded image data.

## 🚀 Key Features

- **Flexible Input**: Supports image URLs or base64 strings.
- **Accurate Comparison**: Uses DeepFace for precise facial recognition.
- **Easy Integration**: Simple API with minimal setup.
- **Automatic Cleanup**: Handles image processing and temporary files.
- **Error Handling**: Well-defined error responses for smooth use.

## 🎯 Use Cases

- **Identity Verification**: Secure face-based authentication.
- **Security & Access Control**: Enhance security systems with face recognition.
- **Facial Recognition Projects**: Easily integrate face comparison in any app.

## 💻 API Endpoint & Usage
`POST /verify`
### Request Body Example
```json
{
  "base_image": "https://example.com/base_image.jpg",
  "comparison_image": "https://example.com/comparison_image.jpg"
}
```
Alternatively, you can use base64-encoded images:
```json
{
  "base_image_base64": "your_base64_encoded_image_here",
  "comparison_image_base64": "your_base64_encoded_image_here"
}
```
Note: You can provide either URLs or base64 strings for the images, but not both.

### Response Example
```json
{
  "verified": true,
  "distance": 0.23
}
```
### Error Response Example
```json
{
  "error": "Both base_image and comparison_image URLs are required."
}
```

## 🛠️ Installation & Setup
1. Clone the repository.
2. Install required dependencies with pip install -r requirements.txt.
3. Run the app with python app.py.
4. The server will be running on `http://localhost:3000` by default.


## ⚡ Why Use This API?

- **Fast & Reliable**: Get quick and accurate results.
- **Portable**: Simple setup, deploy, and use.
- **Cost-Effective**: Open-source and lightweight solution.

Start comparing faces today with **Face Comparison API** — fast, easy, and accurate facial recognition.
