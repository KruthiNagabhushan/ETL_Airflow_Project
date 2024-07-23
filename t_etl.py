import uuid
import pandas as pd
import json
from datetime import datetime
import s3fs


def format_data():
    r = []
    for i in range(20):
        data = {}
        import requests

        res = requests.get("https://randomuser.me/api/")
        res = res.json()
        res = res['results'][0]

        location = res['location']
        data['id'] = uuid.uuid4()
        data['first_name'] = res['name']['first']
        data['last_name'] = res['name']['last']
        data['gender'] = res['gender']
        data['address'] = f"{str(location['street']['number'])} {location['street']['name']}, " \
                          f"{location['city']}, {location['state']}, {location['country']}"
        data['post_code'] = location['postcode']
        data['email'] = res['email']
        data['username'] = res['login']['username']
        data['dob'] = res['dob']['date']
        data['registered_date'] = res['registered']['date']
        data['phone'] = res['phone']
        data['picture'] = res['picture']['medium']
        r.append(data)

    return r

def etl():
    res = format_data()
    df = pd.DataFrame(res)
    df.to_csv("random_user_data.csv")
