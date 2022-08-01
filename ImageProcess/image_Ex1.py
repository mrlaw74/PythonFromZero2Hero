import sys
import os
from PIL import Image

# grab first and second argument -- > sys module
path = f"{os.getcwd()}/image"
# print(path)
directory = f"{os.getcwd()}/ImageConverted"
# print(directory)
# Check is new/ exists, if not create --> os module
if not os.path.exists(directory):
    os.makedirs(directory)
# Loop through Pokedex --> PIL module
for filename in os.listdir(path):
    clean_name = os.path.splitext(filename)[0]
    img = Image.open(f"{path}/{filename}")
    img.save(f"{directory}/{clean_name}.png", 'png')
    print(f"all done")
# Convert images to png
# Save to the new folder.