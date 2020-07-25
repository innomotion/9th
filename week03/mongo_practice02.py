from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

## 코딩 할 준비 ##
movie = db.movies.find_one({'title': '월-E'})
star = movie['star']

movies = list(db.movies.find({'star': star}))
for movie in movies:
    title = movie['title']
    db.movies.update({'title': title}, {'$set': {'star': 0}})
print(star)