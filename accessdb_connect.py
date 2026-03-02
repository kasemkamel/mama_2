from win32com.client import Dispatch
from os.path import exists
import os



class dbconnection:
    
    def __init__(self):
        self.__creation_decision__()
        
    
    def file_exests(self):
        file_exests = exists('mama.mdb')
        return file_exests
    
    
    def create_dbfile(self):
        dbfile_created = False
        try:
            dbname = f'{os.getcwd()}\\mama.mdb'
            dbLangGeneral = ';LANGID=0x0409;CP=1252;COUNTRY=0'
            accessApp = Dispatch("Access.Application")
            dbEngine = accessApp.DBEngine
            workspace = dbEngine.Workspaces(0)
            newdb = workspace.CreateDatabase(dbname, dbLangGeneral, 64)
            newdb.Execute("""CREATE TABLE employee (
                         ID autoincrement,
                         name_ varchar(255) NOT NULL,
                         salary double,
                         rewarding_incentive double,
                         incentive double,
                         minimum double,
                         compensatory double,
                         accommodation_allowance double,
                         freetime_allowance double,
                         instead_of_infection double,
                         more double,
                         supplementary_wage double,
                         comprehensive_wage double,
                         percent_1 double,
                         percent_2 double,
                         percent_3 double,
                         percent_4 double,
                         percentage_wage double,
                         entitlements double,
                         percent_5 double,
                         percent_6 double,
                         percent_7 double,
                         percent_8 double,
                         percent_9 double,
                         percent_10 double,
                         percent_11 double,
                         martyrs_association double,
                         agricultural_social_solidarity double,
                         applied_prifessions double,
                         agricultural_professions double,
                         workers_union double,
                         workers_union_solidarity double,
                         KFFA double,
                         desability_fund double,
                         health_care double,
                         hajj_and_umrah_association double,
                         agricultural_association double,
                         other_installments double,
                         damga double,
                         illegal_laziness double,
                         elmostaqtaa double,
                         safy double);""")
            
            # If created successfully, it will be converted to true
            dbfile_created = True

        except Exception as e:
            print(e)
            pass
        
        finally:
            accessApp.DoCmd.CloseDatabase
            accessApp.Quit
            newdb = None
            workspace = None
            dbEngine = None
            accessApp = None
        
        return dbfile_created

    
    def __creation_decision__(self):
        if self.file_exests():
            print("exsists")
        else:
            print("is file created : " + str(self.create_dbfile()))
            


p = dbconnection()
