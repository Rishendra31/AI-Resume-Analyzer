# 📄 AI Resume Analyzer

An AI-powered Resume Analyzer built with **Python, Streamlit, LangChain, and Groq LLM** that evaluates resumes, calculates an ATS score, compares them with job descriptions, identifies missing skills, and provides AI-generated improvement suggestions.

---

## 🚀 Features

- 📄 Upload Resume (PDF)
- 📝 Extract text from resume
- 📊 Calculate ATS Score
- 🛠 Extract technical skills
- 📌 Compare resume with Job Description
- 📈 Resume Match Percentage
- ❌ Identify Missing Skills
- 🤖 AI-generated resume feedback using Groq LLM
- 💻 Simple and interactive Streamlit interface

---

## 🛠 Tech Stack

- Python
- Streamlit
- PyPDF
- LangChain
- Groq API
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity
- Python Dotenv

---

## 📂 Project Structure

```
AI-Resume-Analyzer/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
│
├── utils/
│   ├── pdf_reader.py
│   ├── resume_parser.py
│   ├── ats_score.py
│   ├── similarity.py
│   └── llm.py
│
└── uploads/
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Resume-Analyzer.git
```

### Navigate to the project

```bash
cd AI-Resume-Analyzer
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure API Key

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📊 How It Works

1. Upload a PDF resume.
2. Extract resume text.
3. Detect technical skills.
4. Calculate an ATS score.
5. Compare the resume with a job description.
6. Calculate a resume match percentage.
7. Identify missing skills.
8. Generate AI-powered feedback using Groq LLM.

---

## 📸 Screenshots

Add screenshots of the application here.

Example:

```
Home Page

Resume Analysis

AI Feedback
```

---

## 🔮 Future Improvements

- Semantic similarity using Sentence Transformers
- RAG-based resume analysis
- Downloadable PDF report
- Resume keyword optimization
- Experience and education extraction
- Interactive analytics dashboard
- Multi-language resume support

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository and submit a pull request.

---

## 👨‍💻 Author

**Rishendra Sai**

GitHub: https://github.com/Rishendra31





⭐ If you found this project useful, consider giving it a star!
