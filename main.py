import gpt4free
import re
from gpt4free import Provider

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
    abstract = "2005 represents the tenth planting season since genetically modified (GM) crops were first grown in 1996. This milestone provides the opportunity to critically assess the impact this technology is having on global agriculture. This study examines specific global economic impacts on farm income and environmental impacts of the technology with respect to pesticide usage and greenhouse gas emissions for each of the countries where GM crops have been grown since 1996. The analysis shows that there have been substantial net economic benefits at the farm level amounting to a cumulative total of $27 billion. The technology has reduced pesticide spraying by 172 million kg and has reduced the environmental footprint associated with pesticide use by 14%. The technology has also significantly reduced the release of greenhouse gas emissions from agriculture, which is equivalent to removing five million cars from the roads."
    print(analyze_abstract(abstract))