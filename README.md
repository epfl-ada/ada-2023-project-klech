1. Title
   
Man vs LLMachine: A Comparison of Human and LLM Wikispeedia Strategy

2. Abstract
   
LLMs are trained to interact as humans do, but do they think like humans as well? To answer this question, we will enlist Falcon 7B as a participant in Wikispeedia
and evaluate its performance across the most popular origin-goal page pairs played by humans. Our analysis will first parse Falcon 7B's decisions for human 'readability' - that is, 
we will employ word embeddings, TF-IDF vectorization on page content, and auxiliary prompts to determine if we, as humans, can justify Falcon 7B's chosen paths. Next, we
will compare Falcon 7B's paths to human paths, measuring levels of similarity in navigation decisions, time-to-goal, learning rate, and rates of 'course correction', thereby
gauging how closely Falcon 7B emulates human strategization. Given the extension of Wikispeedia to the domain of human information organization, these results will also
measure how effectively ChatGPT can emulate human semantic relations. 

3. Research Questions
   
In the context of Wikispeedia:
- Does Falcon 7B pursue page-paths that are sensical to human researchers?
- Can Falcon 7B explain its Wikispeedia decisions in a way that is sensical to human researchers?
- Does Falcon 7B employ the same 'zoom-out' to hub, 'zoom-in' to spoke Wikispeedia strategy as humans?
- How does Falcon 7B's rounds-to-target compare to human players?
- To what extent does Falcon 7B's strategy and performance change over successive games with the same origin-goal pair?
- How often does Falcon 7B 'backtrack' compared to humans?

4. Proposed Additional Datasets
   
The primary external dataset for this project will be composed of the paths Falcon 7B selects when presented with the Wikispeedia game. 
This data will be developed using a stable, curated prompt deployed iteratively via a HuggingFace Transformers API in Python and Google Collab.
Our proposed prompt is: "Which concept is closest to <GOAL_CONCEPT> in the following set: <LINK_1>, <LINK_2>, ..., <LINK_N> ?"

5. Methods
   
TF-IDF vectorization
Word Embeddings
Wikispeedia-derived semantic scores
OpenAI API
?

6. Proposed Timeline
?

7. Organization within the team
?

9. Questions for TAs (optional)
One possibility for extending the scope of the project (or even course correct if ChatGPT fails to provide sensible Wikispeedia paths) would be to obtain the human-derived semantic scores from Wikispeedia and evaluate ChatGPT's level of agreement. 
For example, we could repeatedly present three concepts to ChatGPT and ask it to select the 'least-similar' from the group. Levels of ChatGPT agreement with Wikispeedia-derived scores would be another approach to measuring LLM's ability to think like humans.

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
