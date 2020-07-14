import requests

lines = []
stations = []
count = 0

# resp = requests.get('https://api.tfl.gov.uk/Line/Mode/dlr%2Coverground%2Ctflrail%2Ctram%2Ctube')
resp = requests.get('https://api.tfl.gov.uk/Line/Mode/tube')
if resp.status_code != 200:
    raise Exception('GET err {}'.format(resp.status_code))
for item in resp.json():
    lines.append(item['id'])
for line in lines:
    print('# {} #'.format(line))
    resp = requests.get('https://api.tfl.gov.uk/Line/{}/Route/Sequence/all'.format(line))
    if resp.status_code != 200:
        raise Exception('GET err {}'.format(resp.status_code))
    for station in resp.json()['stations']:
        name = station['name']
        if(name[-19:] == "Underground Station"):
            name = name[:-20]
        if(name[-9:] == "Tram Stop"):
            name = name[:-10]
        if(name[-12:] == "Rail Station"):
            name = name[:-13]
        if(name not in stations):
            count+=1
        stations.append(name)
        print(name)

print(count)

# get stations (central)

# resp = requests.get('https://api.tfl.gov.uk/Line/central/Route/Sequence/all')
# if resp.status_code != 200:
#     raise Exception('GET err {}'.format(resp.status_code))
# for station in resp.json()['stations']:
#     name = station['name']
#     if(name[-19:] == "Underground Station"):
#         print(name[:-20])
#     else:
#         print(name)

# get lines

# resp = requests.get('https://api.tfl.gov.uk/Line/Mode/dlr%2Coverground%2Ctflrail%2Ctram%2Ctube')
# if resp.status_code != 200:
#     raise Exception('GET err {}'.format(resp.status_code))
# for item in resp.json():
#     lines.append(item['name'])
# for line in lines:
#     print(line)

# get modes

# resp = requests.get('https://api.tfl.gov.uk/Line/Meta/Modes')
# if resp.status_code != 200:
#     raise Exception('GET err {}'.format(resp.status_code))
# for item in resp.json():
#     print(item['modeName'])