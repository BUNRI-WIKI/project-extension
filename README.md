# Project Extension

## Overview
**Project Extension** is a web-based service that provides AI-powered solutions for detecting and classifying objects and text. This project leverages state-of-the-art machine learning models such as YOLO for image recognition and KcBERT for text classification.

## Features
### 1. Recyclable Detection & Classification (YOLO)
The project uses the **YOLO (You Only Look Once)** model to detect and classify recyclable materials from images. YOLO is a highly efficient object detection algorithm that allows for real-time identification of various objects in images. Key features include:
- **Real-time image analysis**: Classifies items like plastic, metal, and paper from uploaded images.
- **Recycling assistance**: Provides classification to assist users in correctly sorting and recycling waste.

### 2. Hate Speech Detection & Classification (KcBERT)
This project also includes a **KcBERT**-based model to detect and classify hate speech in Korean text. KcBERT is a variant of BERT (Bidirectional Encoder Representations from Transformers) fine-tuned for Korean, and it helps identify harmful or offensive content. Key features include:
- **Text sentiment analysis**: Detects different categories of hate speech, including insults, racial slurs, and offensive comments related to gender, religion, or sexual orientation.
- **Comprehensive classification**: Labels the text into categories like general statements, offensive language, and specific hate speech types.

## Technologies Used
- **YOLOv8**: For image-based recyclable detection and classification.
- **KcBERT**: For text-based hate speech detection and classification.
- **FastAPI**: A modern web framework for building and serving the API.
- **Docker**: To containerize the application for easy deployment.
- **AWS S3**: For storing model data and logs.
