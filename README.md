# Human vs AI: A Comparison of Human and LLM Wikispeedia Strategy
   
*Klech:* 

- Ernesto Bocini (359541)
- Lorenzo Drudi (367980)
- Kaede Johnson (357472)
- Hanwen Zhang (370374)
- Xingyue Zhang (351693)

[Datastory](https://drudilorenzo.github.io/ada-klech-data-story/) \ 
[Datastory repository](https://github.com/drudilorenzo/ada-klech-data-story)

## Abstract
   
LLMs are trained on extremely large corpuses of texts, most of the time written by humans over decades. This enables them to generate human-like sentences and reply to questions in a sound way. But how closely do they adopt human ways of thought? Would an LLM play a game involving semantic relationships the same way humans do? Would they play it better?

To answer these questions, we enlist an LLM as a participant in Wikispeedia, a game wherein players navigate from one Wikipedia page to another using as few clicks on Wikipedia page links as possible. We then compare the LLM’s results to human results, considering in particular speed, completion rates, strategic use of Wikipedia pages with many links, progression towards goal over time, and location of clicks on the page. Our findings contribute to a societal question more pressing in the past year than perhaps any time in human history: (when) will AI overtake humans’ ability to think creatively?

## Research Questions
   
- Who is better at Wikispeedia: Humanity or an LLM?
- If there is a clear winner, what strategy or phenomenon is producing their advantage?


## Additional Datasets
   
The chief external dataset is composed of the paths Mistral selects when participating in the Wikispeedia game (or as close as we can get to Wikispeedia given our computational and financial limitations). 
This data was developed using a stable, curated prompt deployed iteratively and manually to Mistral via LMQL to ensure bounded responses.
We selected the 75 most popular origin-goal Wikipedia page pairs played by humans (e.g. Africa-England) to deploy, and had Mistral 'play' these game pairs with the following prompt:

"""

We now play the following game:
I will give you a target word and a list from which you can choose an option. If the list contains the target word, you choose it. Otherwise you choose the option that is most similar to it. Before starting, I give you one examples, then it's your turn:
EXAMPLE:
Target word: George_Washington
Available options: [[Able_Archer_83, Afghanistan, , Estonia, Europe, Finland, France, French_language, George_W._Bush, Hungary, September_11,_2001_attacks, United_States]]
Reasoning: I need to find something inside the list related to the target: 'George_Washington'. George Washington was the first president of United States and he lived in United States.
Answer: Hence the answer is: 'United_States'.
YOUR TURN:
Target word: {TARGET}
Available options: [[{LIST OF LINKS}]]
Reasoning: [REASONING]
Answer: Hence the choice is: '[ANSWER]'

"""

Above, TARGET refers to the end goal of a given Wikispeedia game while LIST OF LINKS refers to the alphabetized list of outgoing links on a given Wikipedia page. We used this prompt to have Mistral play 75 different Wikispeedia game pairs 30 times each, amounting to 2250 game paths. 

We arrived at Mistral, the prompt above, and LMQL following an arduous development phase evaluating other possibilities. This is to say that any 'rule' differences from true Wikispeedia induced by our prompt were in our view necessary to enable the pursuit of this project.

## Methods and Results

Let 'identity' refer to a player's status as human or LLM and 'pair' refer to a Wikispeedia game's origin-goal Wikipedia page pair.

- Who is better at Wikispeedia: Humanity or an LLM?

To determine who is better at Wikispeedia, we first calculate Student t-tests on differences in game path lengths at the pair level between humans and Mistral. We also calculate a global t-test on differences between human and Mistral data matched by game pair. The results show that humans are generally faster at Wikispeedia than Mistral, though this is not universal to all game pairs.

We also demonstrate with cumulative completion plots that Mistral is more likely than humans to complete a game pair even if it does not have a speed advantage.

- If there is a clear winner, what strategy or phenomenon is producing their advantage?

We first analyze the pattern of page degrees over time for human game paths and Mistral game paths, averaging page degrees across all games of similar length by identity. We observe Mistral's general inability to implement the human strategy of 'zooming-out' to a hub and zooming back in to a goal, as evidenced by the shape of its degree path curve.

We then apply spaCy embeddings to Wikipedia page names to calculate average cosine similarity to goal over time by identity. We find humans consistently take an initial semantic step away from their goal, whereas Mistral does not. Ostensibly a response to our prompt, this difference strategy is core to Mistral's inability to zoom out, and may well be the chief factor leading to humans' speed win.

Finally, we use geometric information about link location to visualize click locations for humans and hypothetical click locations for Mistral, observing a difference in click location on Wikipedia page. We compare CCDFs of degrees for pages more likely to be high on a page when appearing as a link versus those less likely to be high on a page when appearing as a link, finding that links that appear lower tend to point to pages of lower degree. We conclude that Mistral's blindness to location in combination with a singular focus on semantic similarity may lead it to pursue greedy but ultimately inefficient page paths. 

## Timeline

Friday, November 17
- Milestone 2 deadline
- Baseline analysis pipeline implemented for human data

--

Thursday, November 23
- Further inspection of LLMs and prompt architecture
- Complete analysis pipeline implemented for human data

--

Friday, December 1
- Homework 2 deadline
- Subset of game pairs (top 75), LLM (Mistral), prompt structure selected
- Mistral data collection launched

--

Thursday, December 7
- Half of Mistral data collected, review results for issues
- Mistral Wikispeedia data patched into analysis pipeline
- Quantitative comparisons between human and Mistral speed, completion rates

--

Tuesday, December 12
- All Mistral data collected
- Visualizations for headline performance comparisons
- Begin investigating why the victor is the victor

Thursday, December 14
- Data story webpage launched
- Quantiative investigation into zoom-out, zoom-in strategy as well as semantic similarity to goal

--

Tuesday, December 19
- Visualizations complete
- Data Story rough draft
- Webpage rought draft

Thursday, December 21
- Finalize Data Story

Friday, December 22
- Finalize Webpage, analysis notebook, and README
- Milestone 3 deadline


## Organization within the team

General Tasks:
- Develop and Launch Mistral Querying: Ernesto, Lorenzo
- Exploratory Analysis, Game Pair Subset: Hanwen, Xingyue
- Click Location Heatmap: Hanwen, Xingyue
- Non-Heatmap Human vs. Mistral Analysis: Lorenzo, Kaede
- Data Story Webpage: Lorenzo
- Data Story and README Text: Kaede
- Overview of notebook code: Ernesto

  ## Bibliography
  - Robert West and Jure Leskovec: Human Wayfinding in Information Networks. 21st International World Wide Web Conference (WWW), 2012.
  - Robert West, Joelle Pineau, and Doina Precup: Wikispeedia: An Online Game for Inferring Semantic Distances between Concepts. 21st International Joint Conference on Artificial Intelligence (IJCAI), 2009.
