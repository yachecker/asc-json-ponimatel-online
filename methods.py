import requests
import pprint
import os

if not os.path.exists('files'):
    os.makedirs('files')


def get_primary_data() -> dict:
    cookies = {
        'PHPSESSID': 'f2ef8e802dd71a0bbae2d654825973da',
    }

    headers = {
        'authority': 'nisphm.edupage.org',
        'accept': '*/*',
        'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
        'content-type': 'application/json; charset=UTF-8',
        # 'cookie': 'PHPSESSID=f2ef8e802dd71a0bbae2d654825973da',
        'origin': 'https://nisphm.edupage.org',
        'referer': 'https://nisphm.edupage.org/',
        'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
    }

    params = {
        '__func': 'regularttGetData',
    }

    json_data = {
        '__args': [
            None,
            '42',
        ],
        '__gsh': '00000000',
    }

    response = requests.post(
        'https://nisphm.edupage.org/timetable/server/regulartt.js',
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    return eval(response.text.replace('true', 'True').replace('false', 'False').replace('null', 'None'))


PRIMARY_DATA = get_primary_data()


# i think it s understandable, have a good day
def json_pythoner(str) -> dict | list:
    return eval(str.replace('true', 'True').replace('false', 'False').replace('null', 'None').strip())


"""
returns classes list with:
key:id
value:name
"""


def get_classes_list(write=False):
    classesList = PRIMARY_DATA['r']['dbiAccessorRes']['tables'][12]["data_rows"]
    classes = {}
    for className in classesList:
        id = className["id"]
        name = className["name"][:className["name"].find('_')].lower()
        classes[id] = name
    if write:
        with open('./files/classes.txt', 'w+', encoding='UTF-8') as f:
            f.write(str(classes))
    return classes


# get all cards which refer to certain lessonID
def get_cards_list(write=False):
    cardsList = PRIMARY_DATA['r']['dbiAccessorRes']['tables'][20]["data_rows"]
    cards = []
    for card in cardsList:
        period = card["period"]
        dayConvertDict = {'10000': 1, '01000': 2, '00100': 3, '00010': 4, '00001': 5, '': 6}
        day = dayConvertDict[card['days']]
        lessonID = card['lessonid']
        classRoomId = card['classroomids']
        cards.append({'lessonid': lessonID,
                      'period': period,
                      'day': day,
                      'classRoomId': classRoomId,
                      })
    if write:
        with open('./files/cards.txt', 'w+', encoding='UTF-8') as f:
            f.write(str(cards))
    return cards


def get_cards_by_lesson_id(lesson_id):
    cardslist = get_cards_list(lesson_id)
    cards = []
    for card in cardslist:
        if card['lessonid'] == lesson_id:
            cards.append(card)

    return cards


def get_class_by_id(id):
    return get_classes_list()[id]


"""
returns teachers as a dictionary with:
key: id
value: dict {
  name,
  color
}
"""


def get_subjects_list(write=False):
    subjectsList = PRIMARY_DATA['r']['dbiAccessorRes']['tables'][13]["data_rows"]
    subjects = {}
    for recordDict in subjectsList:
        subjects[recordDict['id']] = recordDict['name']
        # sabyrzhan if you want color as well, please uncomment code below
        # subjects[recordDict['id']] = {'name': recordDict['name'], 'color': recordDict['color']}
    if write:
        with open('./files/subjects.txt', 'w+', encoding='UTF-8') as f:
            f.write(str(subjects))
    return subjects


def get_teachers_list(write=False):
    teachers_list = PRIMARY_DATA['r']['dbiAccessorRes']['tables'][14]["data_rows"]
    teachers = {}
    for teacher in teachers_list:
        teachers[teacher['id']] = {
            'name': teacher['name'],
            'color': teacher['color']
        }
    if write:
        with open('./files/teachers.txt', 'w+', encoding='UTF-8') as f:
            f.write(str(teachers))
    return teachers


def get_lessons_list():
    lessonsList = PRIMARY_DATA['r']['dbiAccessorRes']['tables'][18]["data_rows"]
    return lessonsList


def get_lesson_by_id(lessonID):
    lessonsList = get_lessons_list()

    for lesson in lessonsList:
        if lesson['id'] == lessonID:
            return lesson
    raise Exception('no such lesson niga')


def get_rooms_list():
    rooms_list = PRIMARY_DATA['r']['dbiAccessorRes']['tables'][11]["data_rows"]
    rooms = {}
    for room in rooms_list:
        if len(''.join(filter(str.isdigit, room['name']))) > 2:
            rooms[room['id']] = ''.join(filter(str.isdigit, room['name']))
        elif len(''.join(filter(str.isdigit, room['name']))) == 2:
            rooms[room['id']] = ''.join(filter(str.isdigit, room['name'])) + 'P'
        else:
            rooms[room['id']] = room['name']
    return rooms


def get_class_id(className):
    class_list = get_classes_list()
    id = ""
    for k, v in class_list.items():
        if v == className:
            id = k
    if not id:
        raise Exception(f"Class '{className}' is not found")
    return id


def get_lessons_by_class(className, write=False):
    classId = get_class_id(className)
    lessons = get_lessons_list()

    classLessons = []
    for lesson in lessons:
        if classId in lesson['classids']:
            classLessons.append(lesson)
    if write:
        with open('./files/lessons.txt', 'w+', encoding='UTF-8') as f:
            f.write(str(classLessons))
    return classLessons


if __name__ == "__main__":
    print('go booba your ass')
