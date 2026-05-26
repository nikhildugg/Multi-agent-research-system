# DuggResearchMind 🔬

<p align="center">
  <a href="https://github.com/nikhildugg/Multi-agent-research-system">
    <img src="https://img.shields.io/badge/Developer-Nikhil-blue?style=for-the-badge&logo=github" alt="Developer"/>
  </a>
  <a href="https://ai.google.dev/">
    <img src="https://img.shields.io/badge/Model-Gemini%203.5%20Flash-orange?style=for-the-badge&logo=google" alt="Model"/>
  </a>
  <a href="https://www.langchain.com/">
    <img src="https://img.shields.io/badge/Framework-LangChain-green?style=for-the-badge" alt="Framework"/>
  </a>
  <a href="https://www.wikipedia.org/">
    <img src="https://img.shields.io/badge/API-Wikipedia-red?style=for-the-badge" alt="API"/>
  </a>
</p>

<p align="center">
  <strong>A professional, collaborative multi-agent AI research system that automates the process of web searching, document scraping, cohesive reporting, and critical scoring.</strong>
</p>

<p align="center">
  Developed by <a href="https://github.com/nikhildugg"><strong>Nikhil (@nikhildugg)</strong></a>.
</p>

---

## 🌟 Key Features

* **Multi-Agent Collaboration**: Orchestrated using LangChain to connect specialized, focused agents.
* **Dynamic Gemini Reasoning**: Powered natively by Google's cutting-edge **Gemini 3.5 Flash** model with a zero-setup local key loader.
* **Zero-Setup Search**: Programmatically queries the **Wikipedia Search API** completely free with no API keys required.
* **Resource Extraction & Scraping**: Cleanly scrapes and extracts text content from target resources for deep analysis.
* **Professional Drafting**: Formulates beautifully-structured Markdown reports including Introduction, Key Findings, Conclusions, and verified Sources.
* **Strict Critics & Evaluation**: An independent critic agent scores, highlights strengths, outlines areas of improvement, and provides a final review of the drafted report.

---

## 🏗️ System Architecture

<p align="center">
  <img src="https://mermaid.ink/svg/pako:eNqFkMEKwjAMhl8l5Ox9gR49iB5EZ7xD2pUtNLWlbh2MvbuptzG8SQ758-X7k6yQc1aoz-r6rZJChdK50C0z52L72m37E7Nis1qH7QEzEkvmTPvYbnswCzanTdi_wXhWSc16NToqFUpT4VwF0sU2vX-xYxacmK52f3HjWaU459XoqFSQpvx5ClT-jXqWc5ZnXWep5N_orCjH7V_oWc5Zvnn9wUxF-r9-AZXkcu0" alt="System Architecture Flow"/>
</p>

---

## 🚀 Getting Started

### 📋 Prerequisites
Ensure you have Python 3.10+ installed.

### ⚙️ Setup & Installation

1. **Navigate to the Repository Directory**:
   ```bash
   cd Multi-agent-research-system
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   The system automatically attempts to read your existing **`GEMINI_API_KEY`** or **`GOOGLE_API_KEY`** from your system environment or local config files. If not found, create a `.env` file in the root directory and specify:
   ```env
   GOOGLE_API_KEY=your_gemini_api_key_here
   ```

---

## 🏃 Running the Application

### 🖥️ Run via CLI (Terminal)
To run the complete research and review pipeline directly inside the terminal:
```bash
python main.py
```

---

## 📄 License
This project is open-source and available under the MIT License.
