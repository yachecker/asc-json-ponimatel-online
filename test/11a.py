import unittest
import sys
sys.path.append('..')  # Add parent directory to the system path
from main import parse_timetable


class TestTimetableParser(unittest.TestCase):
  def test_valid_timetable(self):
    # Call the parse_timetable function (without providing direct input)
    parsed_timetable = parse_timetable(weekday=1, className='7a', subGroup=1)

    # Expected output after parsing the timetable internally
    expected_output = {
      'Monday':[
        {
          'name': 'Кураторский час',
          'room': '222',
          'teacher':'Каримова Арайлым',
          'periods':1
        },
        {
          'name': 'Музыка',
          'room': '303',
          'teacher':'Амангельды Айсулу',
          'periods':1
        },
        {
          'name': 'Информатика',
          'room': '254',
          'teacher':'Ахметова Балгын',
          'periods':2
        },
                {
          'name': 'Физика',
          'room': '242',
          'teacher':'Тутебаева Айсулу',
          'periods':1
        },
        {
          'name': 'Домбыра',
          'room': '',
          'teacher':'Токтаган Айтжан',
          'periods':1
        },
        {
          'name': 'Математика',
          'room': '223',
          'teacher':'Джубатканов Кушаныш',
          'periods':1
        },
      ],

    }

    self.assertEqual(parsed_timetable, expected_output)

  # Add more tests for other scenarios and edge cases

if __name__ == '__main__':
  unittest.main()
