
import unittest

from common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
from client import Clientpart

client = Clientpart()

class TestClass(unittest.TestCase):
    '''
    Класс с тестами
    '''

    def setUp(self):
        self.err_dict = {
            RESPONSE: 400,
            ERROR: 'Bad Request'
        }
        self.ok_dict = {RESPONSE: 200}

    def test_def_presense(self):
        """Тест коректного запроса"""
        test = client.create_presence()
        test[TIME] = 1.1
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_200_ans(self):
        """Тест корректтного разбора ответа 200"""
        self.assertEqual(client.process_ans(self.ok_dict), '200 : OK')

    def test_400_ans(self):
        """Тест корректного разбора 400"""
        self.assertEqual(client.process_ans(self.err_dict), '400 : Bad Request')

    def test_no_response(self):
        """Тест исключения без поля RESPONSE"""
        self.assertRaises(ValueError, client.process_ans, {ERROR: 'Bad Request'})


if __name__ == '__main__':
    unittest.main()
