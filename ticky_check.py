#!/usr/bin/env python3

from re import findall
from csv import DictWriter
from operator import itemgetter
from sys import argv

def get_error():
    errors = {}
    with open(argv[1], "r") as file:
        for i in file.readlines():
            key = findall(r"[R] ([\w ']+)", i)
            if not key:
                continue
            key = key[0].strip()
            if key not in errors:
                errors[key] = 1
            else:
                errors[key] += 1
    sorted_data = sorted(errors.items(), key=itemgetter(1), reverse=True)
    result = []
    for i in range(len(sorted_data)):
        result.append({"Error": sorted_data[i][0], "Count": sorted_data[i][1]})
    return result

def get_username():
    users = {}
    with open(argv[1], "r") as file:
        for i in file.readlines():
            user = findall(r"\(([\w.]+)\)", i)[0].strip()
            is_info = True if findall(r"(\w[A-Z]+)", i)[0].strip() == "INFO" else False
            if user not in users:
                if is_info:
                    users[user] = {"info": 1, "error": 0}
                else:
                    users[user] = {"info": 0, "error": 1}
            else:
                if is_info:
                    users[user]["info"] += 1
                else:
                    users[user]["error"] += 1
    sorted_data =  sorted(users.items())
    result = []
    for i in range(len(sorted_data)):
        result.append({"Username": sorted_data[i][0], "INFO": sorted_data[i][1]["info"], "ERROR": sorted_data[i][1]["error"]})
    return result[:8]

def export_to_csv(path ,data, fieldname):
    with open(path, "w") as file:
        writer = DictWriter(file, fieldname)
        writer.writeheader()
        writer.writerows(data)
    print("Export {} has been successfully".format(path))

error = get_error()
username = get_username()
fieldnames = ["Error", "Count"]
export_to_csv("error_message.csv", error, fieldnames)
fieldnames = ["Username", "INFO", "ERROR"]
export_to_csv("user_statistics.csv", username, fieldnames)

