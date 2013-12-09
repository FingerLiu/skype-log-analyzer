import predictionio

client = predictionio.Client(appkey="KaJwG2eUkmt4iTjiAHcw56hPQyW8FbeWKD5YfQAK7OldYSuvv2Sk0Wqxqa7XPkTz")

# Recommend 5 items to each user
user_ids = [str(x) for x in range(8, 16)]
for user_id in user_ids:
    print "Retrieve top 5 recommendations for user", user_id
    try:
        client.identify(user_id)
        rec = client.get_itemrec_topn("ItemRecEngine1", 2)
        print rec
    except predictionio.ItemRecNotFoundError as e:
        print 'Caught exception:', e.strerror()
