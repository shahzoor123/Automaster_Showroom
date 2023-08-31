import json 

with open('test.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
    
    
for obj in data:
    image_sha256 = obj.pop("imageSHA256")
    obj["date"] = image_sha256

  

    

updated_json = json.dumps(data, indent=2) 

   
print(updated_json)    