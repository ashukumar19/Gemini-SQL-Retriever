# SQL LLM - Natural Language to SQL Query Converter

A Streamlit web application that converts natural language questions into SQL queries using Google's Gemini AI. The app allows users to ask questions in plain English and get results from a SQLite database containing student information.

## 🚀 Features

- **Natural Language Processing**: Ask questions in plain English
- **AI-Powered SQL Generation**: Uses Google Gemini AI to convert questions to SQL
- **Interactive Web Interface**: Built with Streamlit for easy interaction
- **Real-time Database Queries**: Execute SQL queries on a SQLite database
- **Student Database**: Sample database with student information (Name, Class, Section, Marks)

## 📋 Prerequisites

- Python 3.7 or higher
- Google Gemini API key
- Required Python packages (see requirements.txt)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/SQL_LLM.git
   cd SQL_LLM
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv sqlenv
   source sqlenv/bin/activate  # On Windows: sqlenv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root and add your Google Gemini API key:
   ```
   GOOGLE_API_KEY=your_gemini_api_key_here
   ```

5. **Initialize the database**
   ```bash
   python sql.py
   ```

## 🎯 Usage

1. **Start the Streamlit app**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser** and navigate to `http://localhost:8501`

3. **Ask questions** in natural language, such as:
   - "Show all students"
   - "How many students are in Ocean Engineering class?"
   - "List students with marks greater than 85"
   - "Show students in section A"
   - "What are the average marks?"

## 📊 Database Schema

The application uses a SQLite database (`student.db`) with the following structure:

**Table: STUDENT**
- `NAME` (VARCHAR): Student's full name
- `CLASS` (VARCHAR): Student's class/major
- `SECTION` (VARCHAR): Section (A, B, C)
- `MARKS` (INT): Student's marks/score

## 🔧 Project Structure

```
SQL_LLM/
├── app.py              # Main Streamlit application
├── sql.py              # Database setup and population script
├── student.db          # SQLite database file
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (create this)
├── .gitignore         # Git ignore file
└── README.md          # This file
```

## 🎨 Example Queries

| Natural Language Question | Generated SQL Query |
|---------------------------|-------------------|
| "Show all students" | `SELECT * FROM STUDENT` |
| "How many students are in Ocean Engineering?" | `SELECT COUNT(*) FROM STUDENT WHERE CLASS="Ocean Engineering"` |
| "Students with marks > 85" | `SELECT * FROM STUDENT WHERE MARKS > 85` |
| "Average marks" | `SELECT AVG(MARKS) FROM STUDENT` |

## 🔑 API Configuration

To use this application, you need a Google Gemini API key:

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Add it to your `.env` file as `GOOGLE_API_KEY`

**Note**: This is a demo project for educational purposes. Make sure to handle API keys and sensitive data securely in production environments.
