import requests, os
path = os.path.join(os.path.expanduser('~'),'AppData','Roaming','.minecraft','mods')
print(f'Default Path: {path}')
folder_path = input('What path is your minecraft')
if folder_path == '':
  folder_path = path
urls = input('url: ')
if urls = '':
  urls = requests.get('https://raw.githubusercontent.com/DarkestCodeYT/MODS/main/server/mods.txt').text
elif ',' in urls:
  urls = urls.split(',')
for filename in os.listdir(folder_path):
  file_path = os.path.join(folder_path, filename)
  if os.path.isfile(file_path):
    os.remove(file_path)
for url in urls:
  response = requests.get(url)
  with open(os.path.join(folder_path,url.split(r'/')[-1]),'wb') as file:
    file.write(response.content)
  # run minecraft
