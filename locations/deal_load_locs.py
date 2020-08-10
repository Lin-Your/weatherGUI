"""
only run this module once to create the locations' information json
"""

import csv
import os.path
import json
# from settings import PATH


def deal_loc_dic():
    # input filename there
    metafile_name = r'./locations/China-City-List-latest.csv'
    if not os.path.isfile(metafile_name):
        print("There is no file 'China-City-List_latest.csv'")
        exit(0)
    locations_info = {}
    with open(metafile_name, 'r', encoding='utf-8') as f:
        f_csv = csv.reader(f)
        next(f_csv)
        next(f_csv)
        for row in f_csv:
            location_id = row[0]
            location_name_cn = row[2]
            province_name_cn = row[7]
            city_name_cn = row[9]
            if province_name_cn not in locations_info:
                locations_info[province_name_cn] = {
                    city_name_cn: {
                        location_name_cn: location_id
                    }
                }
            elif city_name_cn not in locations_info[province_name_cn]:
                locations_info[province_name_cn][city_name_cn] = {
                    location_name_cn: location_id
                }
            else:
                locations_info[province_name_cn][city_name_cn][location_name_cn] = location_id

        save_filename = r'./locations/locations_info.json'
        with open(save_filename, 'w', encoding='utf-8') as save_file:
            json.dump(locations_info, save_file, ensure_ascii=False, separators=(',', ':'), sort_keys=True)


def load_locations_info() -> dict:
    f_name = r'./locations/locations_info.json'
    if not os.path.isfile(f_name):
        deal_loc_dic()
    with open(f_name, 'r', encoding='utf-8') as f:
        return json.load(f)
