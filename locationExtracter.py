import base64
import requests

# df = pd.DataFrame("CollectedData.csv")
client_key = '4cHuVVUX1PCBd5NSRLPrQIdt1'
client_secret = '"Zb7d1f5PDQKk7p3LqXzP1hcabrbPm2aVR17glNZceYe5D2kfg2'


key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
b64_encoded_key = base64.b64encode(key_secret)
b64_encoded_key = b64_encoded_key.decode('ascii')

base_url = 'https://api.twitter.com/'
auth_url = '{}oauth2/token'.format(base_url)

auth_headers = {
    'Authorization': 'Basic {}'.format(b64_encoded_key),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

auth_data = {
    'grant_type': 'client_credentials'
}

auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

print(auth_resp.status_code)
access_token = auth_resp.json()['access_token']
search_headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}

search_url = '{}1.1/statuses/show.json?id={}'.format(
    base_url, 1287363592396759041)

search_resp = requests.get(
    search_url, headers=search_headers, params=search_params)

tweet_data = search_resp.json()["coordinates"]

print(tweet_data)
