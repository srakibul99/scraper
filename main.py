import json

count = 0
followers_list = []
count_following = 0
following_list = []

followers = ['followers1.json', 'followers2.json', 'followers3.json', 'followers4.json', 'followers5.json', 'followers6.json', 'followers7.json', 'followers8.json', 'followers9.json', 'followers10.json', 'followers11.json']

following = ['following1.json', 'following2.json', 'following3.json', 'following4.json', 'following5.json', 'following6.json', 'following7.json', 'following8.json', 'following9.json', 'following10.json', 'following11.json']

for i in followers:
  f = open(i, "r")
  data = json.loads(f.read())
  
  for j in data['data']['user']['edge_followed_by']['edges']:
    name = j['node']['username']
    followers_list.append(name)
    count+=1
    
  f.close()

print(followers_list)
print(count)

for i in following:
  f = open(i, "r")
  data = json.loads(f.read())
  
  for j in data['data']['user']['edge_follow']['edges']:
    name = j['node']['username']
    following_list.append(name)
    count_following+=1
    
  f.close()

print(following_list)
print(count_following)

for i in following_list:
  if i not in followers_list:
    print(i)
