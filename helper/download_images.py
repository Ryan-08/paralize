import requests

file = open(f'data/image_links.txt', 'r')
Lines = file.readlines()
number = 5
for link in Lines:
    img_data = requests.get(link).content        
    with open(f"images/photo{number}.jpg", 'wb') as handler:
        handler.write(img_data) 
    number+=1