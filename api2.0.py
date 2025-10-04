import requests
def fetch_random_quote():
    url = "https://api.freeapi.app/api/v1/public/quotes/quote/random"
    responce = requests.get(url)
    data = responce.json()
    if data['success'] and 'data' in data:
        text = data['data']
        author = text['author']
        content = text['content']
        return author, content
    else:
        raise Exception("Failed to fetch data")

def main ():
    try:
        autherNamem, conntent = fetch_random_quote()
        print(f"Auther: {autherNamem}\nQuotes: {conntent}")
    except Exception as e:
        print(f"error is {e}")
if __name__ == "__main__":
    main()