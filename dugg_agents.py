"""
DuggResearchMind - Agent Orchestration
Author: Nikhil (github.com/nikhildugg)

Orchestrates Gemini 3.5 Flash agents and LangChain reasoning chains.
"""

from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dugg_tools import web_search, scrape_url 
from dotenv import load_dotenv
import os

load_dotenv()

# Dynamically load Gemini API Key from local config files if not in env
if not os.getenv("GOOGLE_API_KEY") and not os.getenv("GEMINI_API_KEY"):
    openclaw_path = r"C:\Users\nikhi\.openclaw\.env"
    if os.path.exists(openclaw_path):
        with open(openclaw_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("GEMINI_API_KEY=") or line.startswith("GOOGLE_API_KEY="):
                    val = line.split("=")[1].strip()
                    os.environ["GOOGLE_API_KEY"] = val
                    break

# Primary Gemini LLM
llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash", temperature=0)

def build_search_agent():
    """Builds a search agent equipped with web searching capabilities."""
    return create_agent(
        model=llm,
        tools=[web_search]
    )

def build_reader_agent():
    """Builds a reader agent equipped with web scraping capabilities."""
    return create_agent(
        model=llm,
        tools=[scrape_url]
    )

# Prompt template and chain for the Research Writer agent
writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write clear, structured and insightful reports."),
    ("human", """Write a detailed research report on the topic below.

Topic: {topic}

Research Gathered:
{research}

Structure the report as:
- Introduction
- Key Findings (minimum 3 well-explained points)
- Conclusion
- Sources (list all URLs found in the research)

Be detailed, factual and professional."""),
])

writer_chain = writer_prompt | llm | StrOutputParser()

# Prompt template and chain for the Research Critic agent
critic_prompt = ChatPromptTemplate.from_messages([
     ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
..."""),
])

critic_chain = critic_prompt | llm | StrOutputParser()
