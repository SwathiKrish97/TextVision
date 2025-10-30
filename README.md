# 🧠 TextVision  

**Transforming Text into Dynamic Fitness Videos using Stable Diffusion**

TextVision is an end-to-end text-to-video generation system designed for the **fitness domain**.  
It leverages **fine-tuned diffusion models** and **BLIP-2 captioning** to automatically generate contextually accurate fitness clips from textual prompts — reducing manual video creation time and enhancing scalability for digital fitness content.

---

## 🎯 Problem Statement

Traditional video production for fitness content is **time-consuming, costly, and non-scalable**.  
TextVision solves this by automating video generation from descriptive text, fine-tuning diffusion models specifically for **fitness movements and exercises**.

---

## 🚀 Key Features

- 🧩 **Automated Text-to-Video Pipeline** – Converts text prompts into realistic videos using four fine-tuned diffusion models (`Zeroscope`, `DamoVilab`, `Potat1`, `Animov`).  
- 🔠 **Smart Captioning with BLIP-2** – Generates contextual captions for each video frame for better visual-text alignment.  
- ⚙️ **Preprocessing Engine** – Cleans and standardizes raw data (MP4 + TXT), including frame extraction and normalization.  
- 📊 **Evaluation Metrics** – Uses CLIPSIM and FID-VID for objective performance scoring.  
- 🌐 **Web Interface (Flask App)** – Enables interactive prompt input and video output generation.  

---

## 🧠 Workflow

Text Prompt
↓
BLIP-2 Captioning → Preprocessing (Frame Extraction, Normalization)
↓
Fine-tuned Diffusion Models (Zeroscope, DamoVilab, Potat1, Animov)
↓
Generated Fitness Videos
↓
Evaluation (CLIPSIM + FID-VID)
↓
Deployment via Flask Interface


---

##🧪 Model Comparison Results

| Model           | CLIPSIM ↑ | FID-VID ↓ | Comments                          |
| --------------- | --------- | --------- | --------------------------------- |
| **Zeroscope**   | 0.3375    | 320.23    | Best performance, high fidelity   |
| **DamoVilab**   | 0.3041    | 368.81    | Balanced results                  |
| **Potat1**      | 0.2914    | 405.72    | Lightweight model                 |
| **Animov-512x** | 0.2550    | 407.55    | High resolution, slower inference |


