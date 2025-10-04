import requests
name =[]
def fetch_randaom_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers"
    responce = requests.get(url)
    data = responce.json()
    if data['success'] and 'data' in data:
        for i in range(10):

            user_data = data['data']['data']
            usertitle = user_data[i]['name']['title']
            userfist = user_data[i]['name']['first']
            userlast = user_data[i]['name']['last']
            username = usertitle + " " + userfist + " " + userlast
            name.append(username)
        return name
    else:
        raise Exception("Failed to fetch user data")
    
def main():
    try:
        UserName = fetch_randaom_user()
        for name in UserName:
            print(f"Random User Name: {name}")
    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()
