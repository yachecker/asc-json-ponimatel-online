import requests
import os
import json
import time


def save_data_to_json(data, file_path):
    try:
        with open(file_path, "w+", encoding="UTF-8") as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(e)
        pass


directory_path = os.path.dirname(
    os.path.abspath(os.path.join(os.pardir, __file__, "../"))
)


def get_primary_data() -> dict:
    cookies = {
        "PHPSESSID": "f2ef8e802dd71a0bbae2d654825973da",
    }

    headers = {
        "authority": "nisphm.edupage.org",
        "accept": "*/*",
        "accept-language": "ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
        "content-type": "application/json; charset=UTF-8",
        # 'cookie': 'PHPSESSID=f2ef8e802dd71a0bbae2d654825973da',
        "origin": "https://nisphm.edupage.org",
        "referer": "https://nisphm.edupage.org/",
        "sec-ch-ua": '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0",
    }

    params = {
        "__func": "regularttGetData",
    }

    json_data = {
        "__args": [
            None,
            "42",
        ],
        "__gsh": "00000000",
    }

    response = requests.post(
        "https://nisphm.edupage.org/timetable/server/regulartt.js",
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    res_dict = eval(
        response.text.replace("true", "True")
        .replace("false", "False")
        .replace("null", "None")
    )
    int_time = int(time.time())
    save_data_to_json(
        res_dict,
        os.path.join(
            directory_path,
            f"primary_data_{int_time}.json",
        ),
    )
    return res_dict


need_to_create = False


def get_last_primary_json():
    global need_to_create
    latest_file = ""
    max_timestamp = 0
    for filename in os.listdir(directory_path):
        if filename.startswith("primary_data") and filename.endswith(".json"):
            timestamp = int(
                filename[filename.find("_data") + 6 : filename.find(".json")]
            )
            if timestamp > max_timestamp:
                max_timestamp = timestamp
                latest_file = filename
    if latest_file == "":
        print("need to create")
        need_to_create = True
        # print(need_to_create)
        return (True, ["", 0])
        check_availability()
    return (False, [latest_file, max_timestamp])


def check_availability():
    global need_to_create
    get_last_primary_json_info = get_last_primary_json()
    need_to_create = get_last_primary_json_info[0]
    latest_file = get_last_primary_json_info[1][0]
    max_timestamp = get_last_primary_json_info[1][1]
    # print(get_last_primary_json_info)

    if latest_file:
        if int(time.time()) - max_timestamp >= 3600:
            need_to_create = True
    if need_to_create:
        get_primary_data()
        try:
            os.remove(os.path.abspath(latest_file))
        except PermissionError:
            pass
        except FileNotFoundError:
            pass
        need_to_create = False


check_availability()
