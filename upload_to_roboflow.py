from roboflow import Roboflow
import os

# authenticate with your API key
rf = Roboflow(api_key="ywD2CEbCqqXnBx4JUSIR")

# list available workspaces
print("Available workspaces:")
print(rf.workspace())

workspace = rf.workspace("cs-thesis")
project = workspace.project("5-datasets-skin-diseases-gm8xb")

# Base folder with dataset subfolders
base_folder = "Merged"

# Walk through subfolders and upload images
for root, _, files in os.walk(base_folder):
    for file in files:
        if file.lower().endswith((".jpg", ".jpeg", ".png")):  # only image files
            image_path = os.path.join(root, file)
            try:
                project.upload(image_path)
                print(f"✅ Uploaded: {image_path}")
            except Exception as e:
                print(f"❌ Failed: {image_path} -> {e}")