# going through a folder and reading all the files in it
import os, xmltodict, json, shutil
from pathlib import Path

path = '/Users/jonasvandenbulcke/Downloads/Fenstererkennung/dataset/dataset/tf/camera_optimal_output50/Annotations'

# print(os.listdir(path))

file_names = [xml.strip('.xml') for xml in os.listdir(path)]

dicts = [json.dumps(xmltodict.parse(open(os.path.join(path, xml), 'r').read())) for xml in os.listdir(path)]

dicts = [json.loads(d) for d in dicts]

n_dicts = {}

print(dicts[0]['annotation']['filename'])

for d in dicts:
    n_dicts[d['annotation']['filename']] = {
        'window': [[
            [loc_d['bndbox']['xmin'], loc_d['bndbox']['ymin']], 
            [loc_d['bndbox']['xmax'], loc_d['bndbox']['ymax']]
            ] for loc_d in filter(lambda x: x['name'] == 'window', d['annotation']['object'])
        ],
        'door': [[
            [loc_d['bndbox']['xmin'], loc_d['bndbox']['ymin']], 
            [loc_d['bndbox']['xmax'], loc_d['bndbox']['ymax']]
            ] for loc_d in filter(lambda x: x['name'] == 'door', d['annotation']['object'])
        ],
    }

json.dump(n_dicts, open('./images/labels.json', 'w'))

images_path = '/Users/jonasvandenbulcke/Downloads/Fenstererkennung/dataset/dataset/tf/camera_optimal_output50/JPEGImages'


for img in os.listdir(images_path):
    if Path(img).stem in n_dicts:
        shutil.copy(os.path.join(images_path, img), os.path.join('./images/', img))