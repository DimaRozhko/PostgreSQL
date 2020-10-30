import psycopg2
from psycopg2.extras import DictCursor
from datetime import datetime
from entity.Departament import Departament
from entity.Order import Order
from entity.Person import Person
from entity.Thing import Thing
from entity.Type import Type
from processing.basic import ExceptionsMVC as ex_mvc
now = datetime.now()


class ProcessDB(object):

    # Constructor
    def __init__(self):
        self.__connection = psycopg2.connect(dbname='store', user='postgres',
                                             password='2000', host='localhost')
        self.__cur = self.__connection.cursor(cursor_factory=DictCursor)
        self.__listNameTables = []
        self.__listTable = []
        # print('Constructor called.')

    def set_list_table(self, table):
        self.__listTable = table

    def get_list_table(self):
        return self.__listTable

    # Deleting (Calling destructor)
    def __del__(self):
        self.__connection.close()
        self.__cur.close()
        # print('Destructor called.')

    def execute_query(self, query):
        self.__cur.execute(query)
        self.__connection.commit()

    # Setter __listNameTables
    def set_list_name_tables(self, list_name):
        self.__listNameTables = list_name

    # Getter __listNameTables
    def get_list_name_tables(self):
        return self.__listNameTables

    # Check exist tables (name)
    def scan_and_save_table_names(self):
        self.__cur.execute("""SELECT table_name FROM information_schema.tables
                            WHERE table_schema = 'public'""")
        lst = []
        for table in self.__cur.fetchall():
            self.__listNameTables += table

    # Print all name tables in list
    def print_table_names(self):
        self.__cur.execute("SELECT current_database();")
        str_db_name = ""
        for db_name in self.__cur.fetchone():
            str_db_name += " " + db_name
        print("Name of all table in databases" + str_db_name + ":")
        for name in self.__listNameTables:
            print("\t" + name)

    def set_listTable_by_db(self, name_table_db):
        print(f"\nTABLE \"{name_table_db}\":")
        self.__cur.execute("SELECT * "
                           "FROM \"" + name_table_db + "\";")
        row = self.__cur.fetchone()
        if name_table_db.upper() == 'DEPARTAMENT':
            entity = Departament()
        elif name_table_db.upper() == 'ORDER':
            entity = Order()
        elif name_table_db.upper() == 'PERSON':
            entity = Person()
        elif name_table_db.upper() == 'THING':
            entity = Thing()
        elif name_table_db.upper() == 'TYPE':
            entity = Type()
        self.__listTable.append(entity.generator(row))
        while row is not None:
            row = self.__cur.fetchone()
            self.__listTable.append(entity.generator(row))


    def __sql_info_column(self, target_table, column_info_table):
        return self.__cur.execute(f"SELECT {column_info_table} "
                                  "FROM information_schema.COLUMNS "
                                  f"WHERE TABLE_NAME = '{target_table}';")

    def print_atr_type_and_return(self, table):
        print(f"\nDATATYPE OF ATTRIBUTE IN TABLE \"{table}\"")
        self.__sql_info_column(table, "DATA_TYPE")
        atr_type = self.__cur.fetchall()
        cur_name = []
        while atr_type is not None:
            cur_name += atr_type
            atr_type = self.__cur.fetchone()
        atr_type = cur_name
        self.__sql_info_column(table, "COLUMN_NAME")
        cur_name = self.__cur.fetchone()
        i = 0
        while cur_name is not None:
            atr_type[i] += cur_name
            i += 1
            cur_name = self.__cur.fetchone()
        self.__connection.commit()
        return atr_type

    def check_exist_table(self, table_name):
        if table_name in self.__listNameTables:
            return True
        else:
            return False

    def del_row_in_table(self, table_name, cond):
        # self.print_table_db(table_name)
        # print(self.print_atr_type_and_return(table_name))
        try:
            self.__cur.execute(f"DELETE FROM {table_name} "
                           f"WHERE {cond}")
            self.__connection.commit()
        except psycopg2.errors.lookup("23503"):
            raise ex_mvc.ItemHaveForeign()

    def update_table(self, table_name, set_condition, where_condition):
        # self.print_table_db(table_name)
        # print(self.print_atr_type_and_return(table_name))
        self.__cur.execute("UPDATE " + table_name + " SET " + set_condition +
                           " WHERE " + where_condition + ";")
        self.__connection.commit()

    def random_generate_and_print(self, num_row):
        self.__cur.execute("SELECT trunc(73 + random()*15), "
                           "    chr(trunc(73 + random()*15)::int) || chr(trunc(73 + random()*15)::int)"
                           f" FROM generate_series(1,{num_row})")
        num_row = 1
        for row in self.__cur.fetchall():
            print(str(num_row) + " | " + str({'num': row[0],
                                              'random string:': row[1]}))
            num_row += 1
        self.__connection.commit()

    def find_in_table(self, table_name):
        print("Current Time =", now.time())
        query = "SELECT a.name, b.type_name, a.quantity " \
                "\nFROM thing a INNER JOIN type b ON(a.type_id=b.type_id) " \
                "\nWHERE type_name LIKE 'plants';"
        # "WHERE type_name='plants'" -- old syntax
        print('QUERY : \n\t' + query)
        print("-----------------------")
        self.__cur.execute(query)
        for row in self.__cur.fetchall():
            print(row)
        self.__connection.commit()
        print("Current Time =", now.time())
        print("-----------------------")
        query = "SELECT a.name, b.type_name, a.quantity, o.date " \
                "\nFROM thing a INNER JOIN public.type b ON(a.type_id=b.type_id) " \
                "\n\tINNER JOIN public.order o ON(o.order_id=a.order_id)" \
                "\nWHERE o.date BETWEEN TO_DATE('01.01.2001', 'DD.MM.YYYY') " \
                "\n\tAND TO_DATE('31.12.2001', 'DD.MM.YYYY');"
        print('QUERY : \n\t' + query)
        print("-----------------------")
        self.__cur.execute(query)
        for row in self.__cur.fetchall():
            print(row)
        self.__connection.commit()
        print("Current Time =", now.time())
        print("-----------------------")
        query = "SELECT a.name, b.type_name, a.quantity, o.quantity, p.name, b.spoil_quick " \
                "\nFROM thing a INNER JOIN public.type b ON(a.type_id=b.type_id) " \
                "\n\t             INNER JOIN public.order o ON(o.order_id=a.order_id)" \
                "\n\t             INNER JOIN person p ON(o.person_id=p.person_id) " \
                "\nWHERE b.spoil_quick IS true; "
        print('QUERY : \n\t' + query)
        print("-----------------------")
        self.__cur.execute(query)
        for row in self.__cur.fetchall():
            print(row)
        self.__connection.commit()
        print("Current Time =", now.time())
        print("-----------------------")
        print("-----------------------")
        print("CHANGE DATE IN QUERY:"
              "\nSELECT a.name, b.type_name, a.quantity, o.date " \
              "\nFROM thing a INNER JOIN public.type b ON(a.type_id=b.type_id) " \
              "\n\tINNER JOIN public.order o ON(o.order_id=a.order_id)" \
              "\nWHERE o.date BETWEEN TO_DATE('01.01.2001', 'DD.MM.YYYY') " \
              "\n\tAND TO_DATE('31.12.2001', 'DD.MM.YYYY');")
        print("-----------------------")
        print("INPUT FIRST DATE IN FORMAT 'DD.MM.YYYY':")
        query = "SELECT a.name, b.type_name, a.quantity, o.date " \
                "\nFROM thing a INNER JOIN public.type b ON(a.type_id=b.type_id) " \
                "\n\tINNER JOIN public.order o ON(o.order_id=a.order_id)" \
                "\nWHERE o.date BETWEEN TO_DATE(\'"
        query += input() + '\', \'DD.MM.YYYY\') \n\t  AND TO_DATE(\''
        print("INPUT SECOND DATE IN FORMAT 'DD.MM.YYYY':")
        query += input() + '\', \'DD.MM.YYYY\');'
        self.__cur.execute(query)
        for row in self.__cur.fetchall():
            print(row)
        self.__connection.commit()
