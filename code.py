import requests
from bs4 import BeautifulSoup
from readability import Readability
import openai
import re
import json

openai.api_key = 'YOUR_OPENAI_API_KEY'  # Replace with your actual OpenAI key

def fetch_article_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    article = soup.find('article') or soup.find('div', class_='article-body')
    if article:
        return article.get_text(separator='\n').strip()
    return ''

def analyze_readability(text):
    r = Readability(text)
    fk_score = r.flesch_kincaid()
    gf_score = r.gunning_fog()
    return {
        "Flesch-Kincaid": fk_score.score,
        "Gunning Fog": gf_score.score,
        "assessment": f"Text has a Flesch-Kincaid score of {fk_score.score:.2f} and a Gunning Fog index of {gf_score.score:.2f}, indicating it is {'not ' if fk_score.score < 60 else ''}easily readable by non-technical marketers."
    }

def analyze_with_llm(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )
    return response.choices[0].message['content']

def generate_prompt(text):
    return f"""
You are an expert in UX writing and product documentation. Analyze the following article for the following:
1. Readability for a marketer.
2. Structure and flow.
3. Completeness of information and examples.
4. Adherence to simplified Microsoft Style Guide principles (voice/tone, clarity, action-orientation).

Provide a structured JSON response with:
- A brief assessment for each category.
- Specific, actionable suggestions for improvement.

Article Content:
{text[:8000]}  # Limit to 8000 characters
"""

def analyze_article(url):
    text = fetch_article_text(url)
    readability_result = analyze_readability(text)
    llm_prompt = generate_prompt(text)
    llm_analysis = analyze_with_llm(llm_prompt)

    result = {
        "url": url,
        "readability": readability_result,
        "llm_analysis": llm_analysis
    }
    return result

if __name__ == '__main__':
    test_url = "https://help.moengage.com/hc/en-us/articles/207836953-Derived-Events-Attributes"
    result = analyze_article(test_url)
    print(json.dumps(result, indent=2))
