import requests
from bs4 import BeautifulSoup
import openai
openai.api_key = "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"

url = "https://en.wikipedia.org/wiki/Beautiful_demoiselle"

response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, 'html.parser')
text = soup.get_text()

chunks = [text[i:i+3500] for i in range(0, len(text), 3500)]

summaries = []
model = "text-davinci-003"
chunks_count = 0
for chunk in chunks:
    prompt = f"Please summarize the following article: {chunk}"
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=0.5,
        max_tokens=200,
        n=1,
        stop=None,
    )
    summary = response.choices[0].text
    summaries.append(summary)

full_summary = "\n".join(summaries)

print(chunks_count)
print(full_summary)
