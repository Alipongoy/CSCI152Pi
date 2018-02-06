keyArray = [{'trigNumber': 11, 'echoNumber':12, 'description':'front sensor'}, {'trigNumber': 15, 'echoNumber':16, 'description':'back sensor'}]
for dictionaryObject in keyArray:
    print(f"This should be the trigNumber for {dictionaryObject['description']}: {dictionaryObject['trigNumber']}");
    print(f"This should be the echoNumber for {dictionaryObject['description']}: {dictionaryObject['echoNumber']}");