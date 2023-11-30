import sys
# sys.path.append('..')
import unittest
from ..__main__ import Parser


class TestTimetableParser(unittest.TestCase):
    def test_valid_timetable(self):
        # Call the parse_timetable function (without providing direct input)
        parsed_timetable = Parser.parse_timetable(className='12c', subGroup=1)['Wednesday']

        # Expected output after parsing the timetable internally
        expected_output = [(1,
                            {'group': 1,
                             'name': 'География',
                             'periods': 2,
                             'room': '301',
                             'teacher': 'Нургалиева Гульжан'}),
                           (1,
                            {'group': 1,
                             'name': 'Экономика',
                             'periods': 2,
                             'room': '155',
                             'teacher': 'Акшалова Айнаш'}),
                           (1,
                            {'group': 1,
                             'name': 'Графика',
                             'periods': 2,
                             'room': '33P',
                             'teacher': 'Баудинов Дулат'}),
                           (3,
                            {'group': 1,
                             'name': 'Химия',
                             'periods': 2,
                             'room': '244',
                             'teacher': 'Уралбаева Карлыгаш'}),
                           (3,
                            {'group': 1,
                             'name': 'Информатика',
                             'periods': 2,
                             'room': '256',
                             'teacher': 'Есмагамбетова Динара'}),
                           (3,
                            {'group': 1,
                             'name': 'Физика',
                             'periods': 2,
                             'room': '332',
                             'teacher': 'Шаланова Жанат'}),
                           (3,
                            {'group': 3,
                             'name': 'Физика',
                             'periods': 2,
                             'room': '332',
                             'teacher': 'Сайлауханов Нуржан'}),
                           (5,
                            {'group': 3,
                             'name': 'Физкультура',
                             'periods': 2,
                             'room': 'Спортзал 3',
                             'teacher': 'Бектемиров Манарбек'}),
                           (7,
                            {'group': 1,
                             'name': 'МЭСК: Я1',
                             'periods': 2,
                             'room': '301',
                             'teacher': 'Бешимбаева Калдыкыз'}),
                           (10,
                            {'group': 3,
                             'name': 'НВ и ТП',
                             'periods': 1,
                             'room': [],
                             'teacher': 'Аубакиров Нуралы'})]

        self.assertEqual(parsed_timetable, expected_output,
                         msg='Everything is stable now... Test ran through successfully')

    # Add more tests fo r other scenarios and edge cases


if __name__ == '__main__':
    unittest.main()
