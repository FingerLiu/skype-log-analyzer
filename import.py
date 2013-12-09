import random

import predictionio

random.seed()

client = predictionio.Client(appkey="KaJwG2eUkmt4iTjiAHcw56hPQyW8FbeWKD5YfQAK7OldYSuvv2Sk0Wqxqa7XPkTz")

# generate 10 users, with user ids 1,2,....,10
user_ids = [str(i) for i in range(1, 51)]
for user_id in user_ids:
    print "Add user", user_id
    client.create_user(user_id)

# generate 50 items, with item ids 1,2,....,50
# assign type id 1 to all of them
item_ids = [str(i) for i in range(1, 51)]
for item_id in item_ids:
    print "Add item", item_id
    client.create_item(item_id, ('1',))

# each user randomly views 10 items
for user_id in user_ids:
    for viewed_item in random.sample(item_ids, 10):
        print "User", user_id ,"views item", viewed_item
        client.identify(user_id)
        client.record_action_on_item("view", viewed_item)

client.close()
