from gnewsclient import gnewsclient
keyword = input("Enter keyword you want to search: ")
print("Searching.Please wait....")
client = gnewsclient.NewsClient(topic=keyword, max_results=50)
news_list = client.get_news()

for item in news_list:
    print("Title : ", item['title'])
    print("Link : ", item['link'])
    print("")