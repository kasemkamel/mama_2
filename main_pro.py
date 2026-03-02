from customtkinter import *
from tkinter import Scrollbar , PhotoImage, messagebox
from shoglmama import *
import pyodbc
# -*- coding: UTF-8 -*-


# db connection crearion
dbname = str(f'{os.getcwd()}\\mama.mdb')
connection_str=( 
                r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' 
                r'DBQ=D:\\python\\New_folder\\mama_2\\mama.mdb;'
                )
connection = pyodbc.connect(connection_str)
command_handler = connection.cursor()
print("done")




class design:
    
    def __init__(self):
        global scrollable_frame1
        container = CTkFrame(root)
        canvas = CTkCanvas(container)
        canvas.config(bg="#343434")
        y_scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
        x_scrollbar = Scrollbar(container, orient="horizontal", command=canvas.xview)

        scrollable_frame1 = CTkFrame(canvas,width=0,height=0)
        scrollable_frame1.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        self.head_bar()
        self.get_info_from_db()
        self.emportant_button()
        
        canvas.create_window((0, 0), window=scrollable_frame1, anchor="nw",width=12990)
        canvas.configure(yscrollcommand=y_scrollbar.set,xscrollcommand=x_scrollbar.set)
        container.place(x=0,relx=0, rely=1, anchor="sw", relwidth=1, relheight=1)
        canvas.place(relx=0, rely=1, anchor="sw", relwidth=1, relheight=1)
        y_scrollbar.pack(side="right", fill="y")
        x_scrollbar.pack(side="bottom", fill="x")

    
    def get_info_from_db(self):
        command_handler.execute("SELECT * FROM employee")
        emp_list = command_handler.fetchall()
        for emp_ in emp_list:
            self.show_emp_info(emp_)
            
            
    def head_bar(self):
        # head bar
        standerd_head_bar = CTkFrame(master=scrollable_frame1,height=100,corner_radius=0)
        standerd_head_bar.grid(pady=20)

        # CTkLabel(master=standerd_head_bar,text="اضافى**", font=("arial",18),width=300,
        #          corner_radius=0,height=50).grid(column=0,row=0,padx=(2,0))
        CTkLabel(master=standerd_head_bar,text="صافى", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=1,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text="مستقطع", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=2,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text="كسب", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=3,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text="دمغة", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=4,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text="اقساط اخرى", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=5,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text="رابطة الزراعيين", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=6,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text="جمعية الحج والعمرة", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=7,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text="رعاية صحية", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=8,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text="صندوق الاعاقة", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=9,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text="جمعية فشل كلوى", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=10,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text="تكافل نقابة العاملين", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=12,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text="نقابة العاملين", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=13,row=0,padx=(2,0))
        
        CTkLabel(master=standerd_head_bar,text="مهن زراعية", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=14,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text="مهن تطبيقية", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=15,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text=" تكافل اجتماعى زراعى وعمولة", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=16,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text="مصابى الحروب والشهداء", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=17,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text="1%", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=18,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text="9%", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=19,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text="1%", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=20,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text="3%", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=21,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text="1%", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=22,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text="1.25%", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=23,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text="12%", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=24,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text="الاستحقاقات", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=25,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text="جملة", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=26,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text="3%", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=27,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text="1%", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=28,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text="1.25%", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=29,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text="12%", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=30,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text="اجر شامل", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=31,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text="اجر مكمل", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=32,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text="مزايا نقدية اخرى", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=33,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text="بدل عدوى", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=34,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text="بدل تفرغ", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=35,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text="حوافز", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=36,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text="بدل اقامة", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=37,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text="تعويضية", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=38,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text="حد ادنى", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=39,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text="حافز اثابة", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=40,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text="المرتب", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=41,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text="الاسم", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=42,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text="رقم", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=43,row=0,padx=(2,0))

        CTkLabel(master=standerd_head_bar,text="خيارات", font=("arial",18),width=300,
                 corner_radius=0,height=50).grid(column=44,row=0,padx=(2,0))


    def show_emp_info(self,info):
        emp_inf_frame = CTkFrame(master=scrollable_frame1,corner_radius=0,width=12410)
        emp_inf_frame.grid(pady=(20,0))
        
        i = 41
        emp_id = info[0]
        for item in info:
            CTkLabel(master=emp_inf_frame,text=item , font=("arial",18),width=300,
                    corner_radius=0,height=50).grid(column=i,row=0,padx=(2,0))
            i-=1

        CTkButton(master=emp_inf_frame,text="حذف", font=("arial",18),width=40,height=50,
                  corner_radius=25,command=lambda : self.delete_emp(emp_id)).grid(column=42,row=0,padx=(35,25))
        
        CTkButton(master=emp_inf_frame,text="تعديل", font=("arial",18),width=50,height=50,
                  corner_radius=25,command=lambda : self.edit_emp()).grid(column=43,row=0,padx=(10,65))
        

    def emportant_button(self):
        emportant_button_frame = CTkFrame(master=scrollable_frame1,corner_radius=0,fg_color="#343434")
        emportant_button_frame.grid(sticky="e",pady=(50,0))
        
        CTkLabel(master=emportant_button_frame,text="",height=50,width=12410).grid(column=38,row=0,)
        
        CTkButton(master=emportant_button_frame,text="تعليمات الاستخدام", font=("arial",18),width=10,height=50,
              corner_radius=25,command=lambda : self.instructions()).grid(column=39,row=0,padx=(0,35))
        
        CTkButton(master=emportant_button_frame,text="حذف الكل", font=("arial",18),width=50,height=50,
                  corner_radius=25,command=lambda : self.delete_all()).grid(column=40,row=0,padx=(10,10))
        
        CTkButton(master=emportant_button_frame,text="تحديث", font=("arial",18),width=50,height=50,
                  corner_radius=25,command=lambda : self.refresh()).grid(column=41,row=0,padx=(10,10))

        CTkButton(master=emportant_button_frame,text="اضافة", font=("arial",18),width=50,height=50,
                  corner_radius=25,command=lambda : self.add_new_emp_toplevel()).grid(column=42,row=0,padx=(10,55))
        
        
    def add_new_emp_toplevel(self):
        add_emp = CTkToplevel()
        add_emp.title("اضافة موظف جديد")
        add_emp.geometry("670x800")
        
        container = CTkFrame(add_emp)
        canvas = CTkCanvas(container)
        canvas.config(bg="#343434")
        y_scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)        
        scrollable_frame = CTkFrame(canvas,width=0,height=0)
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        
        name = CTkEntry(master=scrollable_frame,  font=("arial",18), width=350)
        name.grid(column=0,row=0,padx=10,pady=10)
        CTkLabel(master=scrollable_frame, text="* الاسم",  font=("arial",18)).grid(column=1,row=0,pady=10)
        
        salary = CTkEntry(master=scrollable_frame,  font=("arial",18), width=350)
        salary.grid(column=0,row=1,padx=10,pady=10)
        CTkLabel(master=scrollable_frame, text="* المرتب",  font=("arial",18)).grid(column=1,row=1,pady=10)
        
        rewarding_incentive = CTkEntry(master=scrollable_frame,  font=("arial",18), width=350)
        rewarding_incentive.grid(column=0,row=2,padx=10,pady=10)
        CTkLabel(master=scrollable_frame, text="* حافز اثابة",  font=("arial",18)).grid(column=1,row=2,pady=10)
        
        incentive = CTkEntry(master=scrollable_frame,  font=("arial",18), width=350)
        incentive.grid(column=0,row=3,padx=10,pady=10)
        CTkLabel(master=scrollable_frame, text="* حوافز",  font=("arial",18)).grid(column=1,row=3,pady=10)
        
        minimum = CTkEntry(master=scrollable_frame,  font=("arial",18), width=350)
        minimum.grid(column=0,row=4,padx=10,pady=10)
        CTkLabel(master=scrollable_frame, text="* حد ادنى",  font=("arial",18)).grid(column=1,row=4,pady=10)

        compensatory = CTkEntry(master=scrollable_frame,  font=("arial",18), width=350)
        compensatory.grid(column=0,row=5,padx=10,pady=10)
        CTkLabel(master=scrollable_frame, text="* تعويضية",  font=("arial",18)).grid(column=1,row=5,pady=10)
                
        accommodation_allowance = CTkEntry(master=scrollable_frame,  font=("arial",18), width=350)
        accommodation_allowance.grid(column=0,row=6,padx=10,pady=10)
        CTkLabel(master=scrollable_frame, text="* بدل اقامة",  font=("arial",18)).grid(column=1,row=6,pady=10)
        
        freetime_allowance = CTkEntry(master=scrollable_frame,  font=("arial",18), width=350)
        freetime_allowance.grid(column=0,row=7,padx=10,pady=10)
        CTkLabel(master=scrollable_frame, text="* بدل تفرغ",  font=("arial",18)).grid(column=1,row=7,pady=10)
        
        instead_of_infection = CTkEntry(master=scrollable_frame,  font=("arial",18), width=350)
        instead_of_infection.grid(column=0,row=8,padx=10,pady=10)
        CTkLabel(master=scrollable_frame, text="* بدل عدوى",  font=("arial",18)).grid(column=1,row=8,pady=10)
        
        more = CTkEntry(master=scrollable_frame,  font=("arial",18), width=350)
        more.grid(column=0,row=9,padx=10,pady=10)
        CTkLabel(master=scrollable_frame, text="* مزايا نقدية اخرى",  font=("arial",18)).grid(column=1,row=9,pady=10)
        
        martyrs_association = CTkEntry(master=scrollable_frame,  font=("arial",18), width=350)
        martyrs_association.grid(column=0,row=10,padx=10,pady=10)
        CTkLabel(master=scrollable_frame, text="* مصابى الحروب والشهداء",  font=("arial",18)).grid(column=1,row=10,pady=10)
        
        agricultural_social_solidarity = CTkEntry(master=scrollable_frame,  font=("arial",18), width=350)
        agricultural_social_solidarity.grid(column=0,row=11,padx=10,pady=10)
        CTkLabel(master=scrollable_frame, text="* تكافل اجتماعى زراعى وعمولة",  font=("arial",18)).grid(column=1,row=11,pady=10)
        
        applied_prifessions = CTkEntry(master=scrollable_frame,  font=("arial",18), width=350)
        applied_prifessions.grid(column=0,row=12,padx=10,pady=10)
        CTkLabel(master=scrollable_frame, text="* مهن تطبيقية",  font=("arial",18)).grid(column=1,row=12,pady=10)
        
        agricultural_professions = CTkEntry(master=scrollable_frame,  font=("arial",18), width=350)
        agricultural_professions.grid(column=0,row=13,padx=10,pady=10)
        CTkLabel(master=scrollable_frame, text="* مهن زراعية",  font=("arial",18)).grid(column=1,row=13,pady=10)
        
        workers_union = CTkEntry(master=scrollable_frame,  font=("arial",18), width=350)
        workers_union.grid(column=0,row=14,padx=10,pady=10)
        CTkLabel(master=scrollable_frame, text="* نقابة العاملين",  font=("arial",18)).grid(column=1,row=14,pady=10)
        
        workers_union_solidarity = CTkEntry(master=scrollable_frame,  font=("arial",18), width=350)
        workers_union_solidarity.grid(column=0,row=15,padx=10,pady=10)
        CTkLabel(master=scrollable_frame, text="* تكافل نقابة العاملين",  font=("arial",18)).grid(column=1,row=15,pady=10)
        
        KFFA = CTkEntry(master=scrollable_frame,  font=("arial",18), width=350)
        KFFA.grid(column=0,row=16,padx=10,pady=10)
        CTkLabel(master=scrollable_frame, text="* جمعية فشل كلوى",  font=("arial",18)).grid(column=1,row=16,pady=10)
        
        desability_fund = CTkEntry(master=scrollable_frame,  font=("arial",18), width=350)
        desability_fund.grid(column=0,row=17,padx=10,pady=10)
        CTkLabel(master=scrollable_frame, text="* صندوق الاعاقة",  font=("arial",18)).grid(column=1,row=17,pady=10)
        
        health_care = CTkEntry(master=scrollable_frame,  font=("arial",18), width=350)
        health_care.grid(column=0,row=18,padx=10,pady=10)
        CTkLabel(master=scrollable_frame, text="* رعاية صحية",  font=("arial",18)).grid(column=1,row=18,pady=10)
        
        hajj_and_umrah_association = CTkEntry(master=scrollable_frame,  font=("arial",18), width=350)
        hajj_and_umrah_association.grid(column=0,row=19,padx=10,pady=10)
        CTkLabel(master=scrollable_frame, text="* جمعية الحج والعمرة",  font=("arial",18)).grid(column=1,row=19,pady=10)
        
        agricultural_association = CTkEntry(master=scrollable_frame,  font=("arial",18), width=350)
        agricultural_association.grid(column=0,row=20,padx=10,pady=10)
        CTkLabel(master=scrollable_frame, text="* رابطة الزراعيين",  font=("arial",18)).grid(column=1,row=20,pady=10)
        
        other_installments = CTkEntry(master=scrollable_frame,  font=("arial",18), width=350)
        other_installments.grid(column=0,row=21,padx=10,pady=10)
        CTkLabel(master=scrollable_frame, text="* اقساط اخرى",  font=("arial",18)).grid(column=1,row=21,pady=10)
        
        button = CTkButton(master=scrollable_frame,text="موافق", font=("arial",18), command=lambda _name1=name,
                  _salary1=salary, rewarding_incentive1=rewarding_incentive, _incentive1=incentive,
                  _minimum1=minimum, _compensatory1=compensatory, _accommodation_allowance1=accommodation_allowance,
                  _freetime_allowance1=freetime_allowance, _instead_of_infection1=instead_of_infection,
                  _more1=more, _martyrs_association1=martyrs_association,
                  _agricultural_social_solidarity1=agricultural_social_solidarity,
                  _applied_prifessions1=applied_prifessions, _agricultural_professions1=agricultural_professions,
                  _workers_union1=workers_union, _workers_union_solidarity1=workers_union_solidarity, _KFFA1=KFFA,
                  _desability_fund1=desability_fund, _health_care1=health_care,
                  _hajj_and_umrah_association1=hajj_and_umrah_association,
                  _agricultural_association1=agricultural_association,
                  _other_installments1=other_installments
                  
                  : self.add_new_emp(_name1,_salary1,rewarding_incentive1,
                                     _incentive1,_minimum1,_compensatory1,
                                     _accommodation_allowance1,_freetime_allowance1,_instead_of_infection1,
                                     _more1,_martyrs_association1,_agricultural_social_solidarity1,_applied_prifessions1,
                                     _agricultural_professions1,_workers_union1,_workers_union_solidarity1,_KFFA1,
                                     _desability_fund1,_health_care1,_hajj_and_umrah_association1,
                                     _agricultural_association1,_other_installments1))
        button.grid(column=1,row=22,pady=30)

                
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=y_scrollbar.set)
        container.place(x=0,relx=0, rely=1, anchor="sw", relwidth=1, relheight=1)
        canvas.place(relx=0, rely=1, anchor="sw", relwidth=1, relheight=1)
        y_scrollbar.pack(side="right", fill="y")


    def add_new_emp(self,name,salary,rewarding_incentive,incentive,minimum,compensatory,accommodation_allowance,freetime_allowance,instead_of_infection,more,martyrs_association,agricultural_social_solidarity,applied_prifessions,agricultural_professions,workers_union,workers_union_solidarity,KFFA,desability_fund,health_care,hajj_and_umrah_association,agricultural_association,other_installments):
        
        name = name.get()
        try:
            salary = float(salary.get())
            rewarding_incentive = float(rewarding_incentive.get())
            incentive = float(incentive.get())
            minimum = float(minimum.get())
            compensatory = float(compensatory.get())
            accommodation_allowance = float(accommodation_allowance.get())
            freetime_allowance = float(freetime_allowance.get())
            instead_of_infection = float(instead_of_infection.get())
            more = float(more.get())
            martyrs_association = float(martyrs_association.get())
            agricultural_social_solidarity = float(agricultural_social_solidarity.get())
            applied_prifessions = float(applied_prifessions.get())
            agricultural_professions = float(agricultural_professions.get())
            workers_union = float(workers_union.get())
            workers_union_solidarity = float(workers_union_solidarity.get())
            KFFA = float(KFFA.get())
            desability_fund = float(desability_fund.get())
            health_care = float(health_care.get())
            hajj_and_umrah_association = float(hajj_and_umrah_association.get())
            agricultural_association = float(agricultural_association.get())
            other_installments = float(other_installments.get())
        except:
            messagebox.showwarning("حاسبى حاسبى", "راجعى الى انتى مدخلاه دا يا هناء \n لو فى مساحة امسحيها \n اتأكدى ان كلهم ارقام")
        
        emp = employee(name,salary,rewarding_incentive,incentive,minimum,compensatory,accommodation_allowance,freetime_allowance,instead_of_infection,more,martyrs_association,other_installments,agricultural_social_solidarity,applied_prifessions,agricultural_professions,workers_union,workers_union_solidarity,KFFA,desability_fund,health_care,hajj_and_umrah_association,agricultural_association)
        info = emp.emp_enfo_collection()
        query = f"INSERT INTO employee(name_,salary,rewarding_incentive,incentive,minimum,compensatory,accommodation_allowance,freetime_allowance,instead_of_infection,more,supplementary_wage,comprehensive_wage,percent_1,percent_2,percent_3,percent_4,percentage_wage,entitlements,percent_5,percent_6,percent_7,percent_8,percent_9,percent_10,percent_11,martyrs_association,agricultural_social_solidarity,applied_prifessions,agricultural_professions,workers_union,workers_union_solidarity,KFFA,desability_fund,health_care,hajj_and_umrah_association,agricultural_association,other_installments,damga,illegal_laziness,elmostaqtaa,safy) VALUES ('{info[0]}',{info[1]},{info[2]},{info[3]},{info[4]},{info[5]},{info[6]},{info[7]},{info[8]},{info[9]},{info[10]},{info[11]},{info[12]},{info[13]},{info[14]},{info[15]},{info[16]},{info[17]},{info[18]},{info[19]},{info[20]},{info[21]},{info[22]},{info[23]},{info[24]},{info[25]},{info[26]},{info[27]},{info[28]},{info[29]},{info[30]},{info[31]},{info[32]},{info[33]},{info[34]},{info[35]},{info[36]},{info[37]},{info[38]},{info[39]},{info[40]});"
        command_handler.execute(query)
        command_handler.commit()
        self.refresh()


    def refresh(self):
        command_handler.execute("SELECT name_, salary, rewarding_incentive, incentive ,minimum ,compensatory ,accommodation_allowance ,freetime_allowance ,instead_of_infection ,more ,martyrs_association ,other_installments ,agricultural_social_solidarity ,applied_prifessions ,agricultural_professions ,workers_union ,workers_union_solidarity ,KFFA ,desability_fund ,health_care ,hajj_and_umrah_association ,agricultural_association FROM employee")
        emp_list = command_handler.fetchall()
        if emp_list:
            command_handler.execute("DELETE FROM employee")
            for employee_ in emp_list:
                name,salary,rewarding_incentive,incentive,minimum,compensatory,accommodation_allowance,freetime_allowance,instead_of_infection,more,martyrs_association,other_installments,agricultural_social_solidarity,applied_prifessions,agricultural_professions,workers_union,workers_union_solidarity,KFFA,desability_fund,health_care,hajj_and_umrah_association,agricultural_association = employee_
                emp = employee(name,salary,rewarding_incentive,incentive,minimum,compensatory,accommodation_allowance,freetime_allowance,instead_of_infection,more,martyrs_association,other_installments,agricultural_social_solidarity,applied_prifessions,agricultural_professions,workers_union,workers_union_solidarity,KFFA,desability_fund,health_care,hajj_and_umrah_association,agricultural_association)
                info = emp.emp_enfo_collection()
                query = f"INSERT INTO employee(name_, salary, rewarding_incentive ,incentive ,minimum ,compensatory ,accommodation_allowance ,freetime_allowance ,instead_of_infection ,more ,supplementary_wage ,comprehensive_wage ,percent_1 ,percent_2 ,percent_3 ,percent_4 ,percentage_wage ,entitlements ,percent_5 ,percent_6 ,percent_7 ,percent_8 ,percent_9 ,percent_10 ,percent_11 ,martyrs_association ,agricultural_social_solidarity ,applied_prifessions ,agricultural_professions ,workers_union ,workers_union_solidarity ,KFFA ,desability_fund ,health_care ,hajj_and_umrah_association ,agricultural_association ,other_installments ,damga ,illegal_laziness ,elmostaqtaa ,safy) VALUES ('{info[0]}',{info[1]},{info[2]},{info[3]},{info[4]},{info[5]},{info[6]},{info[7]},{info[8]},{info[9]},{info[10]},{info[11]},{info[12]},{info[13]},{info[14]},{info[15]},{info[16]},{info[17]},{info[18]},{info[19]},{info[20]},{info[21]},{info[22]},{info[23]},{info[24]},{info[25]},{info[26]},{info[27]},{info[28]},{info[29]},{info[30]},{info[31]},{info[32]},{info[33]},{info[34]},{info[35]},{info[36]},{info[37]},{info[38]},{info[39]},{info[40]});"
                command_handler.execute(query)
                command_handler.commit()
        scrollable_frame1.destroy()
        self.__init__()
    
    
    def delete_all(self):
        command_handler.execute("DELETE FROM employee")
        command_handler.commit()
        self.refresh()


    def edit_emp(self):
        messagebox.showerror("وقفى","دا مش شغال دلوقتى ...")
    

    def delete_emp(self,emp_id):
        command_handler.execute("DELETE FROM employee WHERE id = {}".format(emp_id))
        command_handler.commit()
        self.refresh()
    

    # ارشادات
    def instructions(self):
        instructions = CTkToplevel()
        instructions.geometry("500x700")
        instructions.title("ارشادات")




root = CTk()
root.title("موارد هناء المالية")
root.attributes("-fullscreen", True)
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
#img = PhotoImage(root,file="mama\icons\lamp.png")
#root.iconbitmap(img)

p = design()

root.mainloop()