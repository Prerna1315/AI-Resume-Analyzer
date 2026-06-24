## 📷 Project Screenshots
<img width="1262" height="698" alt="Screenshot 2026-06-19 144907" src="https://github.com/user-attachments/assets/71ca2d2b-2ca2-4b5d-b2a0-c12e89f52127" />
<img width="1151" height="957" alt="image" src="https://github.com/user-attachments/assets/79155f9d-4d89-4c8f-9881-7a178dfa5b84" />
<img width="1035" height="983" alt="image" src="https://github.com/user-attachments/assets/a03d707b-be6a-494d-b616-d1595102298e" />

# AI Resume Analyzer

This is my AI Resume Analyzer project built using Python, Streamlit and Google Gemini API.

I created this project to understand how AI can be used to analyze resumes and provide useful feedback automatically. The application allows users to upload a PDF resume and get an AI-generated analysis.

## Features

- Upload resume in PDF format
- Extract text from PDF
- AI based resume analysis
- Resume summary
- Strengths and weaknesses
- ATS score
- Suggestions for improvement

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- PyPDF2
- python-dotenv

## Files

- `main.py` → Main Streamlit application
- `pdf_parser.py` → Extracts text from PDF resumes
- `gemini_analyzer.py` → Sends resume text to Gemini API and gets analysis
- `.env` → Stores Gemini API key (not uploaded to GitHub)

## How to Run

1. Clone the repository

```bash
git clone https://github.com/Prerna1315/AI-Resume-Analyzer.git
```

2. Install required libraries

```bash
pip install streamlit google-generativeai PyPDF2 python-dotenv
```

3. Create a `.env` file and add your Gemini API key

```env
GEMINI_API_KEY=YOUR_API_KEY
```

4. Run the project

```bash
streamlit run main.py
```

## About this project

I built this project while learning AI and Python projects. Through this project, I learned:

- Working with Streamlit
- PDF text extraction using PyPDF2
- Using Google Gemini API
- Environment variables with `.env`
- Building an end-to-end AI application
  
I built this project while learning AI and Python projects.
I am continuously learning and improving my skills in Python and AI.

---
Made with ❤️ by Prerna
