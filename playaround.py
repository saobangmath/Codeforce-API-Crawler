import requests
class Crawler:
    def __init__(self):
        self.endpoint = "https://codeforces.com/api/"
    # blog entry view
    def blogEntryView(self, id):
        response = requests.get(self.endpoint + "blogEntry.view?blogEntryId={}".format(id))
        assert (response.status_code == 200)
        return response.json()["result"]
    # blog entry comments
    def blogEntryComments(self, id):
        response = requests.get(self.endpoint + "blogEntry.comments?blogEntryId={}".format(id))
        assert (response.status_code == 200)
        return response.json()["result"]
    # contest hacks
    def contestHacks(self, id):
        response = requests.get(self.endpoint + "blogEntry.comments?blogEntryId={}".format(id))
        assert (response.status_code == 200)
        return response.json()["result"]
     # contest user rating
    def userRating(self, name):
        response = requests.get(self.endpoint + "user.rating?handle=" + name)
        assert (response.status_code == 200)
        return response.json()["result"][-1]["newRating"]
    # all active user rateList
    def userRateList(self):
        response = requests.get(self.endpoint + "user.ratedList?activeOnly=true")
        assert (response.status_code == 200)
        return response.json()["result"]

def main():
    crawler = Crawler()
    allUsers = crawler.userRateList()
    for i in range(25): # top 25 in the world
        print(allUsers[i]["handle"] + ": " + str(allUsers[i]["rating"]), end = "\n")


if __name__ == "__main__":
    main()