import json

translations = []

for i in range(1,61):
    with open(f"AzureTranslator/AzureTranslationData{i}.json", "r") as f:
        t = json.load(f)
        translations.extend(t)


with open("AzureTranslator/translated.txt", "w") as f:
    for translation in translations:
        f.write(f'{translation["translations"][0]["text"]}\n')
        
