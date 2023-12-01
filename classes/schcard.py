import sys

sys.path.append('..')
from ..methods import get_primary_data

PRIMARY_DATA = get_primary_data()


class SchCard:
    def __init__(self, lessonid: str, day: int, period: int, classroom_id: str):
        self.lessonid = lessonid
        self.period = period
        self.day = day
        self.classroom_id = classroom_id[0] if classroom_id else ''
        self.classroom = self.get_rooms_list()[self.classroom_id]
        # if self.day == 3:
        # print(lessonid)

    def get_rooms_list(self) -> dict:
        rooms_list = PRIMARY_DATA['r']['dbiAccessorRes']['tables'][11]["data_rows"]
        rooms = {}
        for room in rooms_list:
            if len(''.join(filter(str.isdigit, room['name']))) > 2:
                rooms[room['id']] = ''.join(filter(str.isdigit, room['name']))
            elif len(''.join(filter(str.isdigit, room['name']))) == 2:
                rooms[room['id']] = ''.join(filter(str.isdigit, room['name'])) + 'P'
            else:
                rooms[room['id']] = room['name']
        rooms[''] = ''
        return rooms

    def __str__(self):
        return f"LessonID: {self.lessonid} Day: {self.day} Period: {self.period} classroom: {self.classroom}"


if __name__ == '__main__':
    print('hello bro...')

""" 

{
   "id":"*1",
   "lessonid":"*1",
   "locked":false,
   "period":"1",
   "days":"10000",
   "weeks":"1",
   "classroomids":[
      "*73"
   ]
},
"""
