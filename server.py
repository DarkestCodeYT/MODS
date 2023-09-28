import requests, os
path = os.path.join(os.path.expanduser('~'),'AppData','Roaming','.minecraft')
print(f'Default Path: {path}')
path = input('What path is your minecraft')
if path == '':
  path = os.path.join(os.path.expanduser('~'),'AppData','Roaming','.minecraft')
urls = requests.get('https://raw.githubusercontent.com/DarkestCodeYT/MODS/main/server.txt').text.split(',')
for filename in os.listdir(os.path.join(path,'mods')):
  if os.path.isfile(os.path.join(os.path.join(path,'mods'), filename)):
    os.remove(os.path.join(os.path.join(path,'mods'), filename))
for url in urls:
  response = requests.get(url)
  with open(os.path.join(path,url.split(r'/')[-1]),'wb') as file:
    file.write(response.content)
