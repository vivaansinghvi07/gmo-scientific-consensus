import gpt4free
import re
import requests
from bs4 import BeautifulSoup
from gpt4free import Provider

def get_articles():

    # obtains page ids
    article_ids = []
    search_url = r"https://pubmed.ncbi.nlm.nih.gov/?term=genetically%20modified%20organisms%20effects%20on%20the%20world&page="
    for page in range(1, 49):
        html = requests.get(f"{search_url}{page}").text
        soup = BeautifulSoup(html, "html.parser")
        for link in soup.find_all("a", {"class": "docsum-title"}):
            article_ids.append(link.attrs["data-article-id"])
    

def analyze_abstract(abstract):

    prompt = """Analyze the text to determine the effects of genetically modified organisms on the environment, the economy, and health. Your output should be in the following format: "environment: <response>, economy: <response>, health: <response>", where <response> can be 'G' for good, 'B' for bad, 'N' for neutral, or 'I' for not enough information."""
    response = "Unable to fetch the response, Please try again."

    # filter bad responses
    while "Unable to fetch the response, Please try again." in response:
        response = gpt4free.Completion.create(Provider.You, prompt=abstract+"\n"+prompt)

    response = response.lower()
        
    # get information
    try: env = re.search("environment: [a-z]", response).group().split()[1]
    except: env = None
    try: econ = re.search("economy: [a-z]", response).group().split()[1]
    except: econ = None
    try: health = re.search("health: [a-z]", response).group().split()[1]
    except: health = None
    
    return {"environment": env, "economy": econ, "health": health}

if __name__ == "__main__":
    get_articles()