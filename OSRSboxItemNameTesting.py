from osrsbox import items_api

database = items_api.load()

for item in database:
    print(item)
    if 'Myre snelm' in item.name and item.tradeable_on_ge:
        print (item.name)
    else:
        continue