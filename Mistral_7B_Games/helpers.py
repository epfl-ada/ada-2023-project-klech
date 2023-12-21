
import urllib.parse
import pandas as pd


data_dir = '../dependencies/wikispeedia_paths-and-graph/'

# extrapolating the link lists for a given wikipedia page:

# Dict of lists containing links
links = {}

df = pd.read_csv(data_dir + 'links.tsv', sep='\t', skiprows=12, header=None)

# Iterate over the dataframe rows
for index, row in df.iterrows():
    start_page = urllib.parse.unquote(row[0])
    link_page = urllib.parse.unquote(row[1])
    if start_page in links:
        links[start_page].append(link_page)
    else:
        links[start_page] = [link_page]

# Function for pulling links
def get_links_from_wikipedia_page(page_title: str) -> list:
    """Get links from wikipedia page

    Args:
        page_title (str): page title

    Returns:
        list: list of links from page
    """
    print('getting the links from wikipedia \n')
    return links.get(page_title, [])
