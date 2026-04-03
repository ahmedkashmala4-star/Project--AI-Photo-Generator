import requests
import io
import base64
from PIL import Image
import streamlit as st

API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-xl-base-1.0"
API_TOKEN = "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" 
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def process_image(input_image, prompt, mode):
    
    input_image = input_image.resize((1024, 1024))
    buffered = io.BytesIO()
    input_image.save(buffered, format="JPEG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

    if mode == "🚀 Cloud API (Fast)":
        enhanced_prompt = f"Professional product shot of the uploaded object, {prompt}, masterpiece, 8k, photorealistic, cinematic lighting, studio quality, highly detailed"
        
        payload = {
            "inputs": enhanced_prompt,
            "parameters": {
                "image": img_base64,
                "strength": 0.7,
                "num_inference_steps": 30,
                "guidance_scale": 7.5,
                "negative_prompt": "white background, plain background, blurry, distorted, low quality, messy"
            }
        }

        try:
            with st.spinner("Connecting to AI Router..."):
                response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
                
                if response.status_code == 200:
                    return Image.open(io.BytesIO(response.content))
                
                elif response.status_code == 503:
                    st.warning("Model is loading. Please try again in 15-20 seconds.")
                    return input_image
                
                else:
                    st.error(f"Router Error {response.status_code}: {response.text}")
                    return input_image
                    
        except Exception as e:
            st.error(f"Connection Error: {str(e)}")
            return input_image
    
    return input_image