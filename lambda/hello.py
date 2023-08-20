import json

def handler(event, context):
    print("request: {}".format(json.dumps(event)))
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/plain"
        },
        "body": "You've successfully invoked the lambda {}\n".format(event["path"])
    }