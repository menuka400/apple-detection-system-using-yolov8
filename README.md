# 🍏 Apple Detection with YOLOv8 🚀

This repository contains an **Apple Detection** project using **YOLOv8 segmentation**. The model is trained on a custom dataset and utilizes the **Ultralytics YOLOv8** framework for instance segmentation.

---

## 📌 Installation
Ensure you have **Python 3.11 or later** installed. Then, install the necessary dependencies:

```sh
pip install -r requirements.txt
```

Alternatively, install dependencies manually:

```sh
pip install opencv-python==4.8.0.76 ultralytics==8.0.20 google-colab==1.0.0
```

---

## 🏋️‍♂️ Training the Model
### 1️⃣ Mount Google Drive
Store your dataset in **Google Drive** and mount it in **Colab**:
```python
from google.colab import drive
drive.mount('/content/drive')
```

### 2️⃣ Extract the Dataset
```python
import zipfile, os
zip_file_path = "/content/drive/MyDrive/Appel/Appledetect.v4i.yolov8.zip"
extracted_dir_path = "/content/extracted"
os.makedirs(extracted_dir_path, exist_ok=True)
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extracted_dir_path)
```

### 3️⃣ Train the YOLOv8 Model
```sh
yolo task=segment mode=train model=yolov8x-seg.pt data=/content/extracted/data.yaml epochs=50 imgsz=640 plots=True
```

---

## 💾 Saving Training Results
After training, save the results to **Google Drive**:
```python
import shutil
source_path = "/content/extracted/runs/segment/train"
destination_path = "/content/drive/MyDrive/Appel/train"
shutil.copytree(source_path, destination_path, dirs_exist_ok=True)
print("✅ Training results copied successfully.")
```

---

## 🔧 Usage
- Modify `data.yaml` to specify the correct dataset paths.
- Train for more epochs or use different models (`yolov8m-seg.pt`, `yolov8l-seg.pt`) for better results.

---

## 📜 License
This project is **open-source** and available under the **MIT License**.

🔹 Happy Coding & Happy Detecting! 🎯

### ⭐ *Star this repository if you like our project!* ⭐
