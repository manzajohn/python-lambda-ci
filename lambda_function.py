print('Loading function')


def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event, indent=2))
    print("value1 = " + event['key1'])
    print("value2 = " + event['key2'])
    print("value3 = " + event['key3'])
    print("context = ", context)
    print(event)
    return event['key1']
