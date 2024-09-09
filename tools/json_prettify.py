import json


# found out that when data is pulled from spotify the json objects have single quotes and that seems to be giving some problems
def replace_single_quotes_with_double_quotes(dict):
    
    string = str(dict)

    for i in string:
        if "\'":
            string += "\""
        else:
            string += i

    return eval(string)


# takes in the json object(dict) and gives you a visually readalble string.
def json_prettify(json_obj):
    return json.dumps(json_obj, sort_keys=True, indent=2)

    # return json.dumps({replace_single_quotes_with_double_quotes(json_obj)}, sort_keys=True, indent=2)

# Let's test this on the Children of Bodom id

# print(replace_single_quotes_with_double_quotes(getArtist("1xUhNgw4eJDZfvumIpcz1B")))