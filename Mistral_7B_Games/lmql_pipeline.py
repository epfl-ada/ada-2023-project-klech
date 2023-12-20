import asyncio as asyncio
import lmql
import pandas as pd
import pickle
from tqdm import tqdm 
import os

from helpers import get_links_from_wikipedia_page


df = pd.read_csv('pipeline_dataset.csv') # run Mistral_Game_NB.ipynb for obtaining this 

if os.path.exists('Mistral_Games.pickle'):
    with open('Mistral_Games.pickle', 'rb') as file:
        results = pickle.load(file)
else:
    results = {}


for row in tqdm(range(len(df)), desc='GAMES'):

    GAME = df.game_pair[row]
    TARGET = df.target[row]
    
    if GAME not in results:
        results[GAME] = {}

    for i in tqdm(range(30), desc=f'30 repetitions for the game {GAME}'): # repeat every game 10 times

        START = df.origin[row]
        blacklist = set()
        steps = []

        while START != TARGET:
            
            ls = get_links_from_wikipedia_page(START)
            filtered_ls = [item for item in ls if item not in blacklist]

            @lmql.query(
                model=lmql.model(
                    "mistralai/Mistral-7B-Instruct-v0.1", endpoint="localhost:2830", trust_env = True, trust_remote_code=True, #10.91.44.122
                ),
                decoder="sample",
                temperature=0.5,
                top_k=10,
                max_len=4096
            )

            async def prompt():
                '''lmql
                """ We now play the following game: I will give you a target word and a list from which you can choose an option. If the list contains the target word, you choose it. Otherwise you choose the option that is most similar to it. Before starting, I give you one examples, then it's your turn:
                
                EXAMPLE:
                Target word: George_Washington
                Available options: [[Able_Archer_83, Afghanistan, , Estonia, Europe, Finland, France, French_language, George_W._Bush, Hungary,   September_11,_2001_attacks, United_States]] 
                Reasoning: I need to find something inside the list related to the target: 'George_Washington'. George Washington was the first president of United States and he lived in United States.
                Answer: Hence the answer is: 'United_States'.

                YOUR TURN
                Target word: {TARGET}
                Available options: [[{filtered_ls}]]
                Reasoning: [REASONING]
                Answer: Hence the choice is: '[ANSWER]'.""" where not "\n" in REASONING and len(REASONING) < 1500 and ANSWER in filtered_ls
                '''

            async def main():
                global START, it, steps

                if TARGET in ls:
                    new_answer = TARGET

                else:
                    print("Main")
                    result = await prompt()
                    print('REASONING: ', result.variables["REASONING"])
                    print('ANSWER: ', result.variables['ANSWER'])
                    print('RESULT: ', result)
                    new_answer =  result.variables['ANSWER']

                START = new_answer
                steps.append(new_answer)
                if steps.count(new_answer) >= 2:
                    blacklist.add(new_answer)

                if len(steps) >= 20:
                    START = TARGET
                
            async def run_main():
                await main()

            asyncio.run(run_main())

        new_key = f'rep{i}'
        results[GAME][new_key] = steps

        # save everytime
        print('Saving the results before next iteration')
        with open('Mistral_Games.pickle', 'wb') as file:
            pickle.dump(results, file)
