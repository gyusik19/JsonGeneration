import csv
import json
from collections import OrderedDict

base_path = "data/"
json_path = "json/"


def strToSec(str_time):
    tmp = str_time.split(":")
    result = 3600 * int(tmp[0]) + 60 * int(tmp[1]) + int(tmp[2])
    return result


def getContents(csv_path, threshold):
    ret = []
    with open(base_path+csv_path, 'r') as csv_file:
        rdr = csv.reader(csv_file)
        next(rdr)
        for csv_line in rdr:
            if float(csv_line[3]) > threshold:
                item = {}
                item['time_start'] = strToSec(csv_line[0])
                item['time_end'] = strToSec(csv_line[1])
                item['content'] = csv_line[2]
                ret.append(item)
    return ret


def generateJson(line_str):
    file_name = line_str[1][:-4] + '.json'
    file_data = {}
    with open(file_name, 'w', encoding="utf-8") as json_file:
        file_data["title"] = line_str[0]
        file_data["link"] = line_str[2]
        file_data["contents"] = getContents(line_str[1], 0.99)
        # print(getContents(line_str[1], 0.99))
        json.dump(file_data, json_file, ensure_ascii=False, indent="\t")


if __name__=="__main__":
    with open(base_path+'index.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for line in reader:
            generateJson(line)