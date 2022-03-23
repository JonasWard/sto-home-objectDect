import os, json, pandas
from PIL import Image

from PIL import Image
# constructing the panda model

def make_df():
    names = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    return pandas.DataFrame(read_list(), columns=names)


def read_list():
    images_path = "./images"
    labels = "./images/labels.json"

    data_list = []

    with open(labels, 'r') as f:
        data = json.load(f)

        for name, objects in data.items():
            file_path = os.path.join(images_path, name+'.jpg')

            with (Image.open(file_path)) as img:
                width, height = img.size

            git_file_path = os.path.join("sto-home-objectDect/images", name+'.jpg')

            for obj_type, obj_positions in objects.items():
                for obj_loc in obj_positions:
                    data_list.append([git_file_path, width, height, obj_type, obj_loc[0][0], obj_loc[0][1], obj_loc[1][0], obj_loc[1][1]])

    return data_list

def training_class(i):
    indexed = i % 10

    if (indexed < 7):
        return 'TRAINING'
    elif (indexed < 9):
        return 'VALIDATION'
    else:
        return 'TEST'

def make_obj_det_csv():
    csv_list = []

    for i, row in enumerate(read_list()):
        filename, width, height, class_type, xmin, ymin, xmax, ymax = row
        csv_list.append("{},{},{},{},{},,,{},{},,".format(
            training_class(i), filename, class_type, str(int(xmin)/width), str(int(ymin)/height), str(int(xmax)/width), str(int(ymax)/height)
        ))

    return '\n'.join(csv_list)

if __name__ == '__main__':
    # df = make_df()
    # df.to_csv('./images/labels.csv', index=False)

    with open('./images/obj_dect.csv', 'w') as f:
        f.write(make_obj_det_csv())
