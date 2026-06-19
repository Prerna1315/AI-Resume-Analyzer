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

I am continuously learning and improving my skills in Python and AI.

---
Made with ❤️ by Prerna
