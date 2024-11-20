import json
with open("colors.json", "r") as f:
    data = json.load(f)
    
    print(json.dumps(data, indent=4))
    
    for type in data['batters']['batter']:
        print(data['name'])
        print(data['type'])
        print(type['type'])
    
