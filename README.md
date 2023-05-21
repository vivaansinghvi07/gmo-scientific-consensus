# Scientific Consensus on the Effects of Genetically Modified Organisms

GMOs (genetically modified organisms) are a controversial topic within science, and knowing the scientific consensus of something is crucial to understanding its implications. During my own research with GMOs, both relating to public opinion and general safety, I was curious what the consensus was. 

Therefore, by acquiring abstracts (summaries) of scientific articles pertaining to GMOs, and using AI to determine how GMOs' effects were viewed in each one, I could somewhat accurately determine the scientific viewing relating to this topic.

## Requirements

The requirements to run this project are in the `requirements.txt` file, the contents of which are shown below:

```
gpt4free==1.0.2
bs4==0.0.1
matplotlib==3.7.1
ipykernel==6.23.1
pynterface==0.1.1
```

## Method

To acquire the articles, I used [PubMed](https://pubmed.ncbi.nlm.nih.gov), using the search term `"genetically modified organisms effects on the world"`. It was worded this way in order to encapsulate environmental and economic effects as well as health effects. I took all the pages that were available and then found their abstracts using web scraping. The abstracts are stored in the `abstracts.txt` file, where each line represents one abstract.

Then, I used [`gpt4free`'s](https://github.com/xtekky/gpt4free) `Provider.You` model in order to analyze my texts. The prompt used is here:

```
Analyze the text to determine the effects of genetically modified organisms on the environment, the economy, and human health. Your output should be in the following format: "environment: <response>, economy: <response>, health: <response>",where <response> can be 'G' for good, 'B' for bad, 'N' for neutral, or 'I' for not enough information.
```

Then, by using regex to acquire the AI's ratings, I could repeat this process for many abstracts to acquire my data.

# Results

Due to the limited rate I could make requests at, I could only analyze around the first 40 abstracts. If I find a more reliable AI model in the future, I will analyze every abstract. However, with this 40, the result is shown here:

![Results](result.png)

It is well regarded that the economy is positively affected by GMOs, while the environment tends to be negatively affected, with some positive. Moreover, health is largely neutral but there are some scientists which claim that GMOs affect health negatively.