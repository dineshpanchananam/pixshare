import pymongo
user, pswd = "dpanchan", "Dinu@1234"
url = "mongodb://{0}:{1}@ds217131.mlab.com:17131/myapp".format(user, pswd)
# create a pymongo client
client = pymongo.MongoClient(url)
# get db handle
db = client.myapp