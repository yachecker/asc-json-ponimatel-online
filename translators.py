from methods import * 

def get_subject_name(lesson_id):
    pretty_subjects = get_subjects_list(write=True)
    return pretty_subjects[lesson_id]

def get_room_name(id):
    return get_rooms_list()[id]

def get_room_names(idlist):
  res = []
  for id in idlist:
    res.append(get_room_name(id))
  return res

def get_group_name(lesson):
  return lesson['groupnames'][0] if lesson['groupnames'][0] else 'Общий'

def get_day_name(day):
  return ['Понедельник','Вторник','Среда','Четверг','Пятница', 'what no day omg'][day-1]

if __name__ == '__main__':
    print('bro, do you really have life? why are you even testing this not as a module... go touch grass bro...')
    
    