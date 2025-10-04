import requests
import random
def api():
    
    if textdata["success"] and "data" in textdata:
        text = textdata['data']
        kind = text['kind']
        id = text['id']
        link = text['selfLink']
        title = text['volumeInfo']['title']
        author = text['volumeInfo']['authors'][0]
        publisher = text['volumeInfo']['publisher']
        publisheddate = text['volumeInfo']['publishedDate']
        description = text['volumeInfo']['description']
        return id,kind,link,title,author,publisher,publisheddate,description
    else:
        raise Exception("data not found")
def main():
    try:
            
        id, kind, link, title, author, publisher, publisheddate, description =api()
        print(f"Id: {id}\nLINK: {link}\nTitle: {title}\nAuthor: {author}\nPublisher: {publisher}\nPublished Date: {publisheddate}\nDescription: {description}")
    except Exception as e:
        print(f"Error is {e}")
ab = 0
while ab<5:
    n = random.randint(1, 40)
    m = "https://api.freeapi.app/api/v1/public/books/"
    url = m + str(n)
    responce = requests.get(url)
    textdata = responce.json()
    if __name__ == "__main__":
        main()
    ab=ab+1
