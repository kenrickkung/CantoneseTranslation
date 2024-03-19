import requests, uuid, json, time
# Add your key and endpoint
key = ...
endpoint = "https://api.cognitive.microsofttranslator.com"

# location, also known as region.
# required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
location = "uksouth"

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'to': ['en'],
    'from': 'yue',
}

headers = {
    'Ocp-Apim-Subscription-Key': key,
    # location required if you're using a multi-service or regional (not global) resource.
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    "charset":"UTF-8",
    'X-ClientTraceId': str(uuid.uuid4()),
}

with open("processed_data/test/yue.txt", "r") as f:
    yue = f.read().splitlines()

body = []

for y in yue:
    body.append({"Text": y})

count = 1
batch_size = 50
for i in range(0, len(body), batch_size):
    response = requests.post(constructed_url, params=params, headers=headers, json=body[i:i+batch_size])

    if response.status_code != 200:
        print("Error:", response.status_code)
        print("Message:", response.text)
    else:
        data = response.json()
        with open(f'AzureTranslator/AzureTranslationData{count}.json', "w") as f:
            json.dump(data,f,sort_keys=True, ensure_ascii=False, separators=(',', ': '))
        print(f"Completed {i+batch_size} Translations and Dumped to AzureTranslator/AzureTranslationData{count}.json suncessfully")
        count += 1
    
    time.sleep(10)
