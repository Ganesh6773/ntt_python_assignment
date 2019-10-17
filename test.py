from app import app
import unittest
from prettytable import PrettyTable


class FlaskTestCase(unittest.TestCase):

    # test for /interface/all
    def test_interface_all(self):
        tester = app.test_client(self)
        response = tester.get('/interface/all', content_type='text/json')

        # print data in ascii table kind of form

        for res in list(response.json):
            table = PrettyTable()
            table.field_names = ['key', 'value']
            for k, v in res.items():
                table.add_row([k, v])
            print(table)
        self.assertEqual(response.status_code, 200)

    def test_interface(self):
        tester = app.test_client(self)
        response = tester.get(
            '/interface/GigabitEthernet0/0', content_type='text/json')

        # print data in ascii table kind of form
        table = PrettyTable()
        table.field_names = ['key', 'value']
        for k, v in dict(response.json).items():
            table.add_row([k, v])
        print(table)
        self.assertEqual(response.status_code, 200)

    def test_interface_negative(self):
        tester = app.test_client(self)
        response = tester.get('/interface/all-', content_type='text/json')

        # print data in ascii table kind of form

        for res in list(response.json):
            table = PrettyTable()
            table.field_names = ['key', 'value']
            for k, v in res.items():
                table.add_row([k, v])
            print(table)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
