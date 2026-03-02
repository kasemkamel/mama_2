from tkinter import messagebox

class employee:
    # البراميتر : الاسم و المرتب و حافز الاثابة و الحوافز و الحد الادنى و تعويضية و بدل اقامة و بدل تفرغ و بدل عدوى و مذايا نقدية اخرى 
    # و لحساب مصابى الحروب والشهداء و اقساط اخرى و تكافل اجتماعى زراعى وعمولة و مهن تطبيقيه و مهن زراعية 
    # و نقابة العاملين و تكافل نقابة العاملين و جمعية اصدقاء فشل كلوى و صندوق الاعاقة و رعاية صحية و جمعية الحج والعمرة و رابطة الزراعيين
    def __init__(self, name, salary, rewarding_incentive, incentive, minimum, compensatory, accommodation_allowance, freetime_allowance, 
                 instead_of_infection, more, martyrs_association=0, other_installments=0, agricultural_social_solidarity=0, 
                 applied_prifessions=0, agricultural_professions=0, workers_union=0, workers_union_solidarity=0, KFFA = 0, 
                 desability_fund = 0, health_care = 0, hajj_and_umrah_association = 0, agricultural_association = 0):
        
        # variables
        self.name = name                                                                            # الاسم
        self.salary = salary                                                                        # المرتب
        self.rewarding_incentive = rewarding_incentive                                              # حافز اثابة
        self.incentive = incentive                                                                  # حوافز
        self.minimum = minimum                                                                      # حد ادنى
        self.compensatory = compensatory                                                            # تعويضية
        self.accommodation_allowance = accommodation_allowance                                      # بدل اقامة
        self.freetime_allowance = freetime_allowance                                                # بدل تفرغ
        self.instead_of_infection = instead_of_infection                                            # بدل عدوى
        self.more = more                                                                            # مزايا نقدية اخرى
        
        # المستقطع كل ما هو اتى :
        self.martyrs_association = martyrs_association                                              # لحساب مصابى الحروب والشهداء
        self.other_installments = other_installments                                                # اقساط اخرى
        self.agricultural_social_solidarity = agricultural_social_solidarity                        # تكافل اجتماعى زراعى وعمولة
        self.applied_prifessions = applied_prifessions                                              # مهن تطبيقيه
        self.agricultural_professions = agricultural_professions                                    # مهن زراعية
        self.workers_union = workers_union                                                          # نقابة العاملين
        self.workers_union_solidarity = workers_union_solidarity                                    # تكافل نقابة العاملين
        self.KFFA = KFFA                                                                            # جمعية اصدقاء فشل كلوى
        self.desability_fund = desability_fund                                                      # صندوق الاعاقة
        self.health_care = health_care                                                              # رعاية صحية
        self.hajj_and_umrah_association = hajj_and_umrah_association                                # جمعية الحج والعمرة
        self.agricultural_association = agricultural_association                                    # رابطة الزراعيين
        


    # حساب الاجر المكمل...
    def supplementary_wage(self):
        supplementary_wage = (self.rewarding_incentive + self.incentive + self.minimum + self.compensatory + 
                              self.accommodation_allowance + self.freetime_allowance + self.instead_of_infection + 
                              self.more)
        return round(supplementary_wage,2)
    
    
    # حساب الاجر الشامل
    def comprehensive_wage(self):
        comprehensive_wage = self.supplementary_wage() + self.salary
        return round(comprehensive_wage,2)
    
    
    # حساب النسب الاولى
    def first_percentage(self):
        _12 = (self.comprehensive_wage() * 12) / 100
        _1_25 = (self.comprehensive_wage() * 1.25) / 100
        _1 = (self.comprehensive_wage() * 1) / 100
        _3 = (self.comprehensive_wage() * 3) / 100
        
        f_percentage = [round(_12,2),round(_1_25,2),round(_1,2),round(_3,2)] 
        return f_percentage
    
    
    # حساب جملة النسب الاولى
    def percentage_wage(self):
        percentage_wage = sum(self.first_percentage())
        return round(percentage_wage,2)

    
    # حساب الاستحقاقات
    def entitlements(self):
        entitlement = self.comprehensive_wage() + self.percentage_wage()
        return round(entitlement,2)

    
    #  حساب النسب التانية
    def secound_percentage(self):
        _1 = round(((self.comprehensive_wage() * 1) / 100),2)
        _9 = round(((self.comprehensive_wage() * 9) / 100),2)
        _1 = round(((self.comprehensive_wage() * 1) / 100),2)
        s_percentage = [*self.first_percentage(),_1, _9, _1]
        return s_percentage
    
    
    # حساب جملة النسب الثانية
    def secound_percentage_wage(self):
        secound_percentage_wage = sum(self.secound_percentage())
        return round(secound_percentage_wage,2)
    
    
    # غلط ولازم تتصلح ابقى راجع هناء ... 
    # حساب الكسب
    def illegal_laziness(self):
        annual_salary = self.comprehensive_wage() *12
        annual_salary_13_ = (annual_salary * 0.13)
        the_proposal = annual_salary - annual_salary_13_
        proposal_subtract_annual_gulids = the_proposal - ((self.applied_prifessions + 
                                                           self.agricultural_professions + 
                                                           self.workers_union)*12)
        the_rest = proposal_subtract_annual_gulids - 24000
        if the_rest <= 15000:
            illegal_laziness = (the_rest *0.025)
        else:
            illegal_laziness = (15000 *0.025) + ((the_rest-15000) * 0.1)
        
        return round(illegal_laziness/12, 2)
    
    
    # حساب الدمغة
    def damga(self):
        annual_salary = self.comprehensive_wage() *12
        annual_salary_13_ = (annual_salary * 0.13)
        the_proposal = annual_salary - annual_salary_13_
        proposal_subtract_annual_gulids = the_proposal - ((self.applied_prifessions + 
                                                           self.agricultural_professions + 
                                                           self.workers_union)*12)
        damga = proposal_subtract_annual_gulids * 0.0075
        return round(damga/12,2)
    
    
    # حساب المستقطع
    def elmostaqtaa(self):
        elmostaqtaa = (self.martyrs_association + self.agricultural_social_solidarity + 
                       self.applied_prifessions + self.agricultural_professions + self.workers_union + 
                       self.workers_union_solidarity + self.KFFA + self.desability_fund + self.health_care + 
                       self.hajj_and_umrah_association + self.agricultural_association + self.other_installments +  
                       self.secound_percentage_wage()+self.damga()+self.illegal_laziness())
        return round(elmostaqtaa,2)
    
    
    # صافى
    def safy(self):
        safy = self.entitlements() - self.elmostaqtaa()
        return round(safy,2)

  
    # الخارج
    def emp_enfo_collection(self):
        info_list = [self.name,self.salary, self.rewarding_incentive, self.incentive, 
                                self.minimum, self.compensatory, self.accommodation_allowance, 
                                self.freetime_allowance, self.instead_of_infection, self.more,
                                self.supplementary_wage(), self.comprehensive_wage(), *self.first_percentage(), 
                                self.percentage_wage(), self.entitlements(), *self.secound_percentage(),
                                self.martyrs_association, self.agricultural_social_solidarity,
                                self.applied_prifessions, self.agricultural_professions, self.workers_union,
                                self.workers_union_solidarity, self.KFFA, self.desability_fund, self.health_care, 
                                self.hajj_and_umrah_association ,self.agricultural_association,
                                self.other_installments, self.illegal_laziness(),
                                self.damga(), self.elmostaqtaa(), self.safy()]
        return info_list
        
# emp = employee("hana", 2590.21 ,950, 327.71, 338.88, 
#                        19.82, 28.80, 0,0,0, 1.91, 0,0,
#                        0,0,0,0,0, 5, 0,0,0)
# print(emp.emp_enfo_collection())

# البراميتر : الاسم و المرتب و حافز الاثابة و الحوافز و الحد الادنى و تعويضية و بدل اقامة و بدل تفرغ و بدل عدوى و مذايا نقدية اخرى 
# و لحساب مصابى الحروب والشهداء و اقساط اخرى و تكافل اجتماعى زراعى وعمولة و مهن تطبيقيه و مهن زراعية 
# و نقابة العاملين و تكافل نقابة العاملين و جمعية اصدقاء فشل كلوى و صندوق الاعاقة و رعاية صحية و جمعية الحج والعمرة و رابطة الزراعيين
