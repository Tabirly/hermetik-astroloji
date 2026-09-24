import os
import base64
from PIL import Image
from io import BytesIO

def process_images():
    images = [
        "sabian-sembolu-koc-1-derece-nigredo.jpeg",
        "sabian-sembolu-koc-2-derece-nigredo.jpeg",
        "sabian-sembolu-koc-3-derece-albedo.jpeg",
        "sabian-sembolu-boga-1-derece-albedo.jpeg",
        "sabian-sembolu-boga-2-derece-rubedo.jpeg",
        "sabian-sembolu-boga-3-derece-rubedo.jpeg",
        "sabian-sembolu-ikizler-1-derece-albedo.jpeg"
    ]
    
    mapping = {}
    
    for img_file in images:
        if os.path.exists(img_file):
            print(f"Processing {img_file}...")
            img = Image.open(img_file)
            # Resize image to a reasonable web size for cards, e.g. 400x600 max
            img.thumbnail((400, 600), Image.Resampling.LANCZOS)
            
            # Save to BytesIO with compression
            buffer = BytesIO()
            img.save(buffer, format="JPEG", quality=70, optimize=True)
            
            # Convert to base64
            b64_str = base64.b64encode(buffer.getvalue()).decode('utf-8')
            
            # Key for mapping, e.g., "koc-1"
            parts = img_file.split('-')
            key = f"{parts[2]}-{parts[3]}"
            mapping[key] = f"data:image/jpeg;base64,{b64_str}"
            
    # Write to a JS file so build_html.py can include it
    with open("image_data.js", "w", encoding="utf-8") as f:
        f.write("const TEST_IMAGES = {\n")
        for k, v in mapping.items():
            f.write(f'  "{k}": "{v}",\n')
        f.write("};\n")
    print("Done!")

if __name__ == "__main__":
    process_images()
