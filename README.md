# Human vs AI: A Comparison of Human and LLM Wikispeedia Strategy
   
*Klech:* 

- Ernesto Bocini (359541)
- Lorenzo Drudi (367980)
- Kaede Johnson (357472)
- Hanwen Zhang (370374)
- Xingyue Zhang (351693)

[Datastory](https://github.com/drudilorenzo/ada-klech-data-story) \
[Datastory repository](https://github.com/drudilorenzo/ada-klech-data-story)
## Abstract
   
LLMs are trained on extremely large corpuses of texts, most of the time written by humans over decades. This enables them to generate human-like sentences and reply to questions in a sound way. But how closely do they adopt human ways of thought? More specifically, can an LLM emulate through behavior the same thinking underpinning human semantic maps? 
To answer this question, we will enlist ChatGPT as a participant in Wikispeedia and evaluate its performance across a subset of popular but meaningfully diverse origin-goal page pairs previously played by humans. 
Our analysis will first parse ChatGPT's decisions for human 'readability' - that is, we will employ embeddings, TF-IDF vectorization on page content, and Wikispeedia-derived human semantic distances to determine if we, as humans, can justify ChatGPT's chosen paths. 
We will then will compare ChatGPT's paths to human paths, measuring levels of similarity in rounds-to-goal, 'zoom-in' / 'zoom-out', and rates of 'course correction', thereby quantifying ChatGPT's proximity to human strategization and ex-ante semantic mapping. 

## Research Questions
   
In the context of Wikispeedia:
- Does ChatGPT pursue page-paths that are sensical to human researchers?
- Is the previous question's answer robust to different semantic categories?
- How does ChatGPT's rounds-to-goal compare to human players'?
- Does ChatGPT employ the same 'zoom-out' to hub, 'zoom-in' to spoke Wikispeedia strategy as humans?
- How often does ChatGPT 'backtrack' compared to humans?

## Proposed Additional Datasets
   
The chief external dataset will be composed of the paths ChatGPT selects when participating in the Wikispeedia game. 
This data will be developed using a stable, curated prompt deployed iteratively and manually to chat.openai.com.
We have sampled a subset of popular origin-goal Wikipedia page pairs played by humans (e.g. Africa-England) while ensuring variation in average (human) rounds-to-goal, game backtrack rates, and semantic category. 
To have ChatGPT 'play' these game pairs, we first deploy the following instructions:

"We now play the following game: I will give you a target word and a list from which you can choose an option. If the list contains the target word, you choose it. Otherwise you choose the semantically most similar word. Before starting I will give you an example of how I would solve something similar. Ready?"

We then engage a chain of thought with 2-shot learning by providing two Wikispeedia round examples. Here is one in condensed form:

"Target word: George_Washington

Available options: < Afghanistan, ... , United_States, ..., Yugoslavia >

My answer is: 'United_States' , because United States is in the list and George Washington was the first president of United States."

Finally, we launch ChatGPT's game by providing a target and set of available options, and proceed according to its responses.

You can find a complete ChatGPT Wikispeedia game developed from our prompts [here](https://chat.openai.com/share/f14b657e-0d77-47a3-8ea5-9df58c41e39d).

We arrive at ChatGPT online and this prompt following a development phase evaluating other possibilities. Analysis of these possibilities (and justification of our selection) can be found in analysis.ipynb.

Finally, we expect to have 300 games played by ChatGPT across 10 origin-goal pairs in our final analysis (30 per pair). All 10 pairs are in the 'Organization within the team' section below.

## Methods

Let 'identity' refer to a player's status as human or LLM and 'pair' refer to a Wikispeedia game's origin-goal Wikipedia page pair.

To determine whether ChatGPT's page paths are sensical to humans *at scale*, we can retain ChatGPT Wikispeedia data, plot the average embedding-based distance to goal at the game-length level, and compare the similarity paths for humans and ChatGPT. We can supplement these results with similar analysis
using cosine distance between Wikipedia page TF-IDF vectorizations and human-game Wikispeedia derived semantic distances. Generally, semantic similarities that increase as the game approaches the goal would, under any of the distance metrics mentioned above, amount to 'readably rational' decisionmaking.

To compare average rounds-to-goal between ChatGPT and humans, we can average rounds-to-goal at the identity-pair level (e.g. ChatGPT games for the pair Africa-England receives one average), match pairs inter-identity, 
take the difference between the human and LLM averages, and perform a t-test for difference from 0 on the averages of these differences. Separately, we can create a cumulative view of the proportion of games completed by round n at the identity-pair level and compare the cumulative distributions inter-identity. 

To determine whether ChatGPT employs the same 'zoom-out' to hub, 'zoom-in' to spoke strategy as humans, we can retain ChatGPT Wikispeedia data, calculate average 
concept degree (# of outgoing Wikipedia page links) over time at the pair level, fit pair-level data to a quadratic model, and confirm the resultant model is concave (a concave quadratic curve would correspond to a 'zoom-in zoom-out' strategy under this framework). A stronger version of this test might require a given pair's average degrees to exhibit (1) exactly one local maximum that appears in round 2 or later and (2) strictly positive changes in average degree followed by strictly negative changes in average degree. A more direct comparison to human strategy would retain only games of length n for both humans and ChatGPT, chart the evolution of average degree over time for both identities, take the geographic difference between the curves, and perform a t-test for difference from 0 on the average of these differences.  

Given ChatGPT's propensity to engage in cycles - meaning it navigates to pages previously seen in its page path - we can remove intermediary pages and treat such cycles as the equivalent of a 'backtrack'. We can then compute the proportion of backtracks that occur in a given round at the identity-pair level, plot the two identites' curves, and compare proportions with t-tests for each round in a given pair.

Finally, our method for isolating 10 game pairs with sufficient variation involved retaining game pairs played 25 times or more by humans, standardizing selection variables (average rounds-to-goal, percentage of games with backtracking, maximum page degree along game path) and finding (via a loop that terminates upon convergence) a sample that effectively maximizes the sum of standardized selection variable standard errors **while also** yielding at least five distinct Wikipedia topic categories across pairs' goals.

## Proposed Timeline

Friday, November 17
- Milestone 2 deadline
- Subset of topics, LLM, prompt structure selected
- Baseline analysis pipeline implemented for human data

--

Tuesday, November 21
- 150 ChatGPT Wikispeedia paths collected

Thursday, November 23
- Complete analysis pipeline implemented for human data

--

Friday, December 1
- Homework 2 deadline

--

Tuesday, December 5
- 300 ChatGPT Wikispeedia paths collected

Thursday, December 7
- ChatGPT Wikispeedia data patched into analysis pipeline; quantitative comparisons calculated

--

Tuesday, December 12
- Visualizations + conceive of further analysis based on unanticipated ChatGPT behavior

Thursday, December 14
- Analysis of game paths complete

Saturday, December 16
- (Optional) Prompt ChatGPT to evaluate human-derived semantic scores

--

Tuesday, December 19
- Data Story rough draft

Thursday, December 21
- Finalize data story, analysis notebook, and README

Friday, December 22
- Milestone 3 deadline


## Organization within the team

Game pair assignments (30 ChatGPT paths per pair):
- 14th_century->Rainbow, Bird->Adolf_Hitler: Ernesto
- Batman->Coconut_crab, Africa->England: Lorenzo
- George_W._Bush->Monkey, Antlion->Hip_hop_Music: Kaede
- Aircraft->Google, Jesus->God: Hanwen
- Computer->Fruit, Jew->Telephone: Xingyue

General Tasks:
- Pre-process GPT game paths: Ernesto, Lorenzo
- Analysis pipeline: Kaede, Hanwen, Xingyue
- Website development: Lorenzo, Xingyue
- Data Story Visualizations: Ernesto, Hanwen
- Data Story and README Text: Kaede 
- Overview of notebook code: Ernesto, Lorenzo, Hanwen, Xingyue

  ## Questions for TA
  We have one other idea for this project: asking ChatGPT to evaluate semantic concept distances based on human-derived Wikispeedia semantic scores. Basically, we would recreate the semantic distances created in Professor West's second paper below, and randomly sample sets of three concepts with semantic scores. We would then give all three to ChatGPT and ask it to select the 'odd man out'. Our question is: would this be a worthwhile endeavour as a companion analysis to this research project? It is essentially an ex-post evaluation of human semantic meaning rather than an ex-ante evaluation.

  ## Bibliography
  - Robert West and Jure Leskovec: Human Wayfinding in Information Networks. 21st International World Wide Web Conference (WWW), 2012.
  - Robert West, Joelle Pineau, and Doina Precup: Wikispeedia: An Online Game for Inferring Semantic Distances between Concepts. 21st International Joint Conference on Artificial Intelligence (IJCAI), 2009.
