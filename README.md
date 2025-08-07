# 🤖 Simple Gemini CLI Agent

This is a AI assistant built using the **Google Gemini 2.5 Flash model** and the **OpenAI Agents SDK**. It takes input from the user in the terminal and returns smart, helpful responses instantly.

---

## 🛠️ Technologies Used

- Python (3.10+)
- [OpenAI Agents SDK](https://github.com/openai/openai-python)
- Google Gemini API
- `uv` – ultra-fast Python package and environment manager
- `python-dotenv` – to manage environment variables using a `.env` file

---

## 🚀 Full Setup Guide

Follow these steps to set up and run this project from scratch:

### ✅ 1. Install Python

Make sure Python 3.10+ is installed.

- Download from: https://www.python.org/downloads/
- Confirm installation:

```bash
python --version
```

### ✅ 2. Install `uv` (if not installed)

[`uv`](https://github.com/astral-sh/uv) is a fast Python package manager and virtual environment tool.

```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```

Check if installed:

```bash
uv --version
```

### ✅ 3. Initialize the Project with `uv`

```bash
uv init
```

### ✅ 4. Add Required Packages

```bash
uv add openai-agents python-dotenv
```

### ✅ 5. Create a Virtual Environment

```bash
uv venv
```

Activate it:

- macOS/Linux:
  ```bash
  source .venv/bin/activate
  ```

- Windows:
  ```bash
  .venv\Scripts\activate
  ```

### ✅ 6. Get Your Gemini API Key

Visit 👉 [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey) to generate your API key.

### ✅ 7. Create a `.env` File

In your project root, create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key
```

### ✅ 8. Create the Agent Script

Create  `simple_agent.py` with the logic.

### ✅ 9. Run the Agent

```bash
uv run simple_agent.py
```

---

## 💡 Example Interaction

```text
Enter your prompt (or type 'exit' to quit): What is AI?
AI stands for Artificial Intelligence...
```

---

## 📁 Project Structure

```
My_First_Agent/
├── simple_agent.py
├── .env
├── .venv/
├── pyproject.toml
└── README.md
```

---

### END ###

