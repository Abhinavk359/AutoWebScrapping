import requests
import os
from urllib.parse import urlparse, parse_qs

# Google Custom Search Engine (CSE) API key
API_KEY = 'key';

# Google Custom Search Engine (CSE) search engine ID
SEARCH_ENGINE_ID = 'id';

# Function to perform a search using Google CSE
def google_cse_search(query):
    url = f"https://www.googleapis.com/customsearch/v1?key={key}&cx={id}&q={query}"
    response = requests.get(url)
    data = response.json()
    return data

# Function to extract search results
def extract_search_results(data):
    if 'items' in data:
        return [item['link'] for item in data['items']]
    else:
        return []
    
links=[]
# Example usage
if __name__ == "__main__":
    query = input("your search query here: ")
    search_results = google_cse_search(query)
    links = extract_search_results(search_results)
    # for link in links:
    #     print(link)

# Count the number of text files in the current directory
def count_text_files(directory):
    # Initialize count variable
    count = 0
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        # Check if the file has a .txt extension
        if filename.endswith(".txt"):
            count += 1

    return count

# Example usage
directory_path = "D:\Python_mediaBias_automation"
i = count_text_files(directory_path)


from distutils.command.build_scripts import first_line_re
from genericpath import exists
from pydoc import pager
from prompt_toolkit import HTML
import requests
from bs4 import BeautifulSoup, Tag 

def generate_filename_from_url(url):
    # Parse the URL
    url=url.replace('www.','')
    url=url.replace('https://','')
    url=url.replace('.com','')
    url=url.replace('.indiatimes','')
    parsed_url = urlparse(url)
    
    # Extract the path component of the URL
    path = parsed_url.path
    
    # Split the path to get segments
    path_segments = path.split('/')
    
    # Example: Let's say you want to use the first part of the path as the filename
    if len(path_segments) >= 1:
        filename = path_segments[0]  # Using the first part of the path
    else:
        filename = "default_filename"  # Fallback filename
    filename+=str(i)   
    filename += '.txt'
    
    return filename



for url in links:
    # step 1:get the HTML
    r = requests.get(url);
    htmlContent=r.content
    # print(htmlContent);

    # step 2:Parse the HTML
    soup=BeautifulSoup(htmlContent,'html.parser');

    # step 3:HTML tree traversal 
    title=soup.title
    print(type(title))

    paras=soup.find_all('p')
    print(paras)
    headLine=soup.find('h1')
    print(headLine)

    paragraphs =soup.find_all('p')
    headLine=soup.find('h1')
    if headLine is not None:
       print("Headline of the page:",headLine.get_text())
    for para in paragraphs:
        print(para.get_text());
    
    # generating filename
    filename=generate_filename_from_url(url)

    #writing the .txt file as paragraphs
    file = open(filename, "a", encoding="utf-8")
    #Appending headline:
    if headLine is not None:
       file.write(headLine.get_text()+'\n')
    #Now writing all the paragraphs
    for para in paragraphs:
        file.write(para.get_text()+'\n')
    file.write(url)    
    file.close()
    i=i+1    


# Note: to search the news article of a specific media house , you can add the media house along with the topic in the search query.