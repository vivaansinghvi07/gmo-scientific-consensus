import gpt4free
import re
import requests
from bs4 import BeautifulSoup
from gpt4free import Provider

PAGE_COUNT = 49
SEARCH_TERM = "genetically modified organisms effects on the world"
GET_SOUP = lambda url: BeautifulSoup(requests.get(url).html, "html.parser")

def get_articles():

    """
    Stores the abstracts of scholarly articles into a text file with each line representing one abstract.
    These abstracts can later be read and evaluated.
    """

    """ This part obtains the article id's to parse through, given a search term """

    article_ids = []
    search_url = f"https://pubmed.ncbi.nlm.nih.gov/?term={SEARCH_TERM.replace(' ', '%20')}&page="

    # in case of errors near the end
    try:
        for page in range(1, PAGE_COUNT):
            soup = GET_SOUP(f"{search_url}{page}")
            for link in soup.find_all("a", {"class": "docsum-title"}):
                article_ids.append(link.attrs["data-article-id"])
    except: pass        
        

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