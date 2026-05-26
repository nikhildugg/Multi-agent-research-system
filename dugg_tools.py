"""
DuggResearchMind - Web & Scraping Tools
Author: Nikhil (github.com/nikhildugg)

Implements Wikipedia API search and web content scraping tools.
"""

from langchain.tools import tool 
import requests
from bs4 import BeautifulSoup
import os 
from dotenv import load_dotenv

load_dotenv()

@tool
def web_search(query: str) -> str:
    """Search Wikipedia for reliable and detailed encyclopedic information on a topic. Returns Titles, URLs and snippets."""
    search_url = "https://en.wikipedia.org/w/api.php"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json",
        "utf8": 1
    }
    try:
        resp = requests.get(search_url, headers=headers, params=params, timeout=10)
        if resp.status_code != 200:
            return f"Search failed with status code {resp.status_code}"
            
        data = resp.json()
        search_results = data.get("query", {}).get("search", [])
        
        results = []
        for item in search_results[:5]:
            title = item.get("title")
            pageid = item.get("pageid")
            snippet = item.get("snippet", "").replace("<span class=\"searchmatch\">", "").replace("</span>", "")
            link = f"https://en.wikipedia.org/?curid={pageid}"
            results.append(f"Title: {title}\nURL: {link}\nSnippet: {snippet}\n")
            
        if not results:
            return "No matching resources found."
            
        return "\n----\n".join(results)
    except Exception as e:
        return f"Error during search: {str(e)}"

@tool
def scrape_url(url: str) -> str:
    """Scrape and return clean text content from a given URL for deeper reading."""
    try:
        resp = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.text, "html.parser")
        
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        return soup.get_text(separator=" ", strip=True)[:3000]
    except Exception as e:
        return f"Could not scrape URL: {str(e)}"
