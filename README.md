1. Title
   
Man vs LLMachine: A Comparison of Human and LLM Wikispeedia Strategy

2. Abstract
   
LLMs are trained to interact as humans do, but do they think like humans as well? More specifically, can an LLM emulate through behavior the same thinking underpinning human semantic maps? 
To answer this question, we will enlist ChatGPT as a participant in Wikispeedia and evaluate its performance across a subset of popular but meaningfully diverse origin-goal page pairs previously played by humans. 
Our analysis will first parse ChatGPT's decisions for human 'readability' - that is, we will employ BART embeddings, TF-IDF vectorization on page content, and auxiliary prompts to determine if we, as humans, can justify ChatGPT's chosen paths. 
Next, we will compare ChatGPT's paths to human paths, measuring levels of similarity in rounds-to-goal, 'zoom-in' / 'zoom-out', and rates of 'course correction', thereby quantifying ChatGPT's proximity to human strategization and ex-ante semantic mapping. 
Finally, we will employ ChatGPT to evaluate semantic concept distances based on human-derived Wikispeedia semantic scores, quantifying its level of ex-post agreement with humans semantic mapping.

3. Research Questions
   
In the context of Wikispeedia:
- Does ChatGPT pursue page-paths that are sensical to human researchers?
- Is the answer to the previous question robust across Wikispeedia games related to different semantic concepts or of varying difficulty (as measured by average human rounds-to-goal)?
- How does ChatGPT's rounds-to-goal compare to human players?
- Does ChatGPT employ the same 'zoom-out' to hub, 'zoom-in' to spoke Wikispeedia strategy as humans?
- How often does ChatGPT 'backtrack' compared to humans?

4. Proposed Additional Datasets
   
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

5. Methods

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

Finally, our method for isolating 10 game pairs with sufficient variation involved standardizing selection variables (average rounds-to-goal, percentage of games completed, maximum page degree along game path) and finding (via a loop that terminates upon convergence) a sample that maximizes or nearly maximizes the sum of selection variable sample variance while also representing at least five distinct topic categories across pair goals.  

7. Proposed Timeline

8. Organization within the team

------------------

Title

Abstract: A 150 word description of the project idea and goals. What’s the motivation behind your project? What story would you like to tell, and why?

Research Questions: A list of research questions you would like to address during the project.

Proposed additional datasets (if any): List the additional dataset(s) you want to use (if any), and some ideas on how you expect to get, manage, process, and enrich it/them. Show us that you’ve read the docs and some examples, and that you have a clear idea on what to expect. Discuss data size and format if relevant. It is your responsibility to check that what you propose is feasible.

Methods

Proposed timeline

Organization within the team: A list of internal milestones up until project Milestone P3.

Questions for TAs (optional): Add here any questions you have for us related to the proposed project.

Notebook containing initial analyses and data handling pipelines. We will grade the correctness, quality of code, and quality of textual descriptions.

------------------

Select a project. 
Perform initial analyses and verify that what you propose is feasible given the data (including any additional data you might bring in yourself)

The goal of this milestone is to intimately acquaint yourself with the data, preprocess it, and complete all the necessary descriptive statistics tasks. 
We expect you to have a pipeline in place, fully documented in a notebook, and show us that you have clear project goals.

Show:
That you can handle the data in its size
That you understand what’s in the data (formats, distributions, missing values, correlations, etc.)
That you considered ways to enrich, filter, transform the data according to your needs
That you have a reasonable plan and ideas for methods you’re going to use, giving their essential mathematical details in the notebook
That your plan for analysis and communication is reasonable and sound, potentially discussing alternatives to your choices that you considered but dropped
We will evaluate this milestone according to how well these steps have been done and documented, the quality of the code and its documentation, the feasibility and critical awareness of the project. We will also evaluate this milestone according to how clear, reasonable, and well thought-through the project idea is. Please use the second milestone to really check with us that everything is in order with your project (idea, feasibility, etc.) before you advance too much with the final Milestone P3! There will be project office hours dedicated to helping you.

By the Milestone P2 deadline, each team should have a single public GitHub repo under the epfl-ada GitHub organization, containing the project proposal and initial analysis code.

P2 deliverable (done as a team): GitHub repository with the following:

Readme.md file containing the detailed project proposal (up to 1000 words). Your README.md should contain:
Title
Abstract: A 150 word description of the project idea and goals. What’s the motivation behind your project? What story would you like to tell, and why?
Research Questions: A list of research questions you would like to address during the project.
Proposed additional datasets (if any): List the additional dataset(s) you want to use (if any), and some ideas on how you expect to get, manage, process, and enrich it/them. Show us that you’ve read the docs and some examples, and that you have a clear idea on what to expect. Discuss data size and format if relevant. It is your responsibility to check that what you propose is feasible.
Methods
Proposed timeline
Organization within the team: A list of internal milestones up until project Milestone P3.
Questions for TAs (optional): Add here any questions you have for us related to the proposed project.
Notebook containing initial analyses and data handling pipelines. We will grade the correctness, quality of code, and quality of textual descriptions.
