# import os
# import shutil

# # get current working directory
# cwd = os.getcwd()
# print("-->"+cwd)
# directory = "\mama.mdb"
# path = cwd+directory
# print(path)

# try:
#     os.makedirs(path, exist_ok = True)
#     print("Directory '%s' created successfully" % directory)
# except OSError as error:
#     print("Directory '%s' can not be created" % directory)

# # shutil.copyfile(original_1, target)


# from comtypes.client import CreateObject

# access = CreateObject('Access.Application')

# from comtypes.gen import Access

# DBEngine = access.DBEngine
# db = DBEngine.CreateDatabase('test.mdb', Access.DB_LANG_GENERAL)
# For me, test.mdb was created in my My Documents folder when I ran the script

# db.BeginTrans()

# db.Execute("CREATE TABLE test (ID Text, numapples Integer)")
# db.Execute("INSERT INTO test VALUES ('ABC', 3)")

# db.CommitTrans()
# db.Close()


# import pyodbc

# conn_str = (
#     r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
#     r'DBQ=D:\\python\\New_folder\\mama_2\\mama.mdb;'
#     )
# cnxn = pyodbc.connect(conn_str)
# crsr = cnxn.cursor()
# for table_info in crsr.tables(tableType='TABLE'):
#     print(table_info.table_name)


# loop --> for loop
#      --> while loop
