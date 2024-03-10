from bs4 import BeautifulSoup
import requests
def scrape():
    # give your url here
    url = 'your url here'
    # get the url
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text,'html.parser')
        # get the text using soup
        text = soup.get_text()
        visible_text = text.strip()
        # removing extralines
        cleaned_text_line = [line for line in visible_text.splitlines() if line.strip()]
        cleaned_text = '\n'.join(cleaned_text_line)
        
        # writing the text into the file
        output_file = "text.txt"
        with open(output_file,'w',encoding='utf8') as file:
            file.write(cleaned_text)
    else:
        print("Text content not found on the page.")
        
# calling the scrape function
scrape()