from django.db import connection
from django.test import TestCase
from .models import Table_1, Table_2


class UnitTestCase(TestCase):
    def setUp(self):
        with connection.cursor() as cursor:
            cursor.execute('INSERT INTO testapp_table_2 (field_2) VALUES ("it is text from table 2")')
            cursor.execute('INSERT INTO testapp_table_1 (field_1, table_2_id) VALUES ("Table 1 header", 1)')


    def test_app(self):
        table_1_obj = Table_1.objects.get(table_1_id=1)
        table_2_obj = Table_2.objects.get(table_2_id=1)
        self.assertEqual(table_1_obj.table_2.table_2_id, table_2_obj.table_2_id)
