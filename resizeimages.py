import os

from PIL import Image

fit_size = int(input("Enter Size: "))
output_folder = input("Enter Output Folder Name: ")

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir('.'):
    if not filename.lower().endswith((".png", ".jpg", ".jpeg")):
        continue
    
    img = Image.open(filename)
    w, h = img.size
    
    if w > fit_size and h > fit_size:
        if w > h:
            new_w = fit_size
            new_h = int((fit_size / w) * h)
        else:
            new_h = fit_size
            new_w = int((fit_size / h) * w)
        
        img = img.resize((new_w, new_h))
        img.save(os.path.join(output_folder, filename))
        print(f"Resized and saved {filename}")

print("All images resized.")
