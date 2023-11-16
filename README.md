# Man vs LLMachine: A Comparison of Human and LLM Wikispeedia Strategy
   
*Klech: Ernesto Bocini (359541), Lorenzo Drudi (367980), Kaede Johnson (357472), Hanwen Zhang (370374), Xingyue Zhang (351693)*

## Abstract
   
LLMs are trained to interact as humans do, but do they think like humans as well? More specifically, can an LLM emulate through behavior the same thinking underpinning human semantic maps? 
To answer this question, we will enlist ChatGPT as a participant in Wikispeedia and evaluate its performance across a subset of popular but meaningfully diverse origin-goal page pairs previously played by humans. 
Our analysis will first parse ChatGPT's decisions for human 'readability' - that is, we will employ BART embeddings, TF-IDF vectorization on page content, and auxiliary prompts to determine if we, as humans, can justify ChatGPT's chosen paths. 
Next, we will compare ChatGPT's paths to human paths, measuring levels of similarity in rounds-to-goal, 'zoom-in' / 'zoom-out', and rates of 'course correction', thereby quantifying ChatGPT's proximity to human strategization and ex-ante semantic mapping. 
Finally, we will employ ChatGPT to evaluate semantic concept distances based on human-derived Wikispeedia semantic scores, quantifying its level of ex-post agreement with humans semantic mapping.

## Research Questions
   
In the context of Wikispeedia:
- Does ChatGPT pursue page-paths that are sensical to human researchers?
- Is the answer to the previous question robust across Wikispeedia games related to different semantic concepts or of varying difficulty (as measured by average human rounds-to-goal)?
- How does ChatGPT's rounds-to-goal compare to human players?
- Does ChatGPT employ the same 'zoom-out' to hub, 'zoom-in' to spoke Wikispeedia strategy as humans?
- How often does ChatGPT 'backtrack' compared to humans?

## Proposed Additional Datasets
   
The chief external dataset will be composed of the paths ChatGPT selects when participating in the Wikispeedia game. 
This data will be developed using a stable, curated prompt deployed iteratively and manually to chat.openai.com.
We have sampled a subset of popular origin-goal Wikipedia page pairs played by humans (e.g. Asteroids-Vikings) while ensuring variation in average (human) rounds-to-goal, game completion rates, and topic category. 
To have ChatGPT 'play' these game pairs, we will deploy the following prompt iteratively: 

"Which concept is closest to <GOAL_CONCEPT> in the following set: <LINK_1>, <LINK_2>, ..., <LINK_N> ?"

Above, <GOAL_CONCEPT> is the final page goal and <LINK_i> refers to the ith link among a given Wikispeedia page's N links. In a given game, <GOAL_CONCEPT> will be stable,
the initial <LINK_i> set will be pulled from the starting Wikipedia page for an origin-goal pair, and each subsequent turn's <LINK_i> set will be pulled from ChatGPT's 
most recent concept (Wikipedia page) selection.

We arrive at ChatGPT online and this prompt following a development phase evaluating other possibilities. Analysis of these possibilities (and justification of our selection) can be found in _analysisfile_.ipynb.

Finally, we expect to have 300 games played by ChatGPT across 10 origin-goal pairs in our final analysis (30 per pair).

## Methods

Let 'identity' refer to a player's status as human or LLM and 'pair' refer to a Wikispeedia game's origin-goal Wikipedia page pair.

To determine whether ChatGPT's page paths are sensical to humans *at scale*, we can retain ChatGPT Wikispeedia data, plot the average BART embedding-based distance to goal and to subsequent concept 
along page paths at the pair level, and calculate the proportion of games for which these average distances strictly decrease throughout game. We can supplement these results with similar analysis
using cosine distance between Wikipedia page TF-IDF vectorizations and human-game Wikispeedia derived semantic distances. Non-increasing curves intra-game would, under any of the distance metrics
mentioned above, amount to 'readably rational' decisionmaking.

To compare average rounds-to-goal between ChatGPT and humans, we can average rounds-to-goal at the identity-pair level (e.g. ChatGPT games for the pair Asteroid-Viking receives one average), match pairs inter-identity, 
take the difference between the human and LLM averages, and perform a t-test for difference from 0 on the averages of these differences. Separately, we can create a cumulative view of the proportion of games completed by round n at the identity-pair level and compare the cumulative distributions inter-identity. 

To determine whether ChatGPT employs the same 'zoom-out' to hub, 'zoom-in' to spoke strategy as humans, we can retain ChatGPT Wikispeedia data, calculate average 
concept degree (# of outgoing Wikipedia page links) over time at the pair level, fit pair-level data to a quadratic model, and confirm the resultant model is concave (a concave quadratic curve would correspond to a 'zoom-in zoom-out' strategy under this framework). A stronger version of this test might require a given pair's average degrees to exhibit (1) exactly one local maximum that appears in round 2 or later and (2) strictly positive changes in average degree followed by strictly negative changes in average degree. A more direct comparison to human strategy would retain only games of length n for both humans and ChatGPT, chart the evolution of average degree over time for both identities, take the geographic difference between the curves, and perform a t-test for difference from 0 on the average of these differences.  

Given ChatGPT's propensity to engage in cycles - meaning it navigates to pages previously seen in its page path - we can remove intermediary pages and treat such cycles as the equivalent of a 'backtrack' (meanwhile, 'blacklisting' the concepts ChatGPT visits more than once in a game can prevent infinite cycles). We can then compute the proportion of backtracks that occur nn a given round at the identity-pair level, plot the two identites' curves, and compare proportions with t-tests for each round in a given pair.

Finally, our method for isolating 10 game pairs with sufficient variation involved standardizing selection variables (average rounds-to-goal, percentage of games completed, maximum page degree along game path) and finding (via a loop that terminates upon convergence) a sample that effectively maximizes the sum of selection variable sample variance **while also** yielding at least five distinct Wikipedia topic categories across pairs' goals.

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
- Visualizations + conceive of further analysis based on unexpected ChatGPT behavior

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
- a-b, c-d: Ernesto
- e-f, g-h: Lorenzo
- i-j, k-l: Kaede
- m-n, o-p: Hanwen
- q-r, s-t: Xingyue

General Tasks:
- Pre-process GPT game paths: Ernesto, Lorenzo
- Analysis pipeline: Kaede, Hanwen, Xingyue
- Website development: Lorenzo, Xingyue
- Data Story Visualizations: Ernesto, Hanwen
- Data Story and README Text: Kaede 
- Overview of notebook code: Ernesto, Lorenzo, Hanwen, Xingyue
