import requests, os
path = os.path.join(os.path.expanduser('~'),'AppData','Roaming','.minecraft')
print(f'Default Path: {path}')
path = input('What path is your minecraft')
if path == '':
  path = path
urls = input('url: ')
if urls = '':
  urls = requests.get('https://raw.githubusercontent.com/DarkestCodeYT/MODS/main/server.txt').text.split(',')
elif ',' in urls.split(''):
  urls = urls.split(',')
else:
  urls = requests.get(urls).text.split(',')
for filename in os.listdir(os.path.join(path,'mods')):
  if os.path.isfile(os.path.join(os.path.join(path,'mods'), filename)):
    os.remove(os.path.join(os.path.join(path,'mods'), filename))
for url in urls:
  response = requests.get(url)
  with open(os.path.join(path,url.split(r'/')[-1]),'wb') as file:
    file.write(response.content)
