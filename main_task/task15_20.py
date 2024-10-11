# TASK 15: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes input of someone's basic salary and benefits, adds them to find the gross salary then uses  the gross salary to find the NHIF. 
# To find the Kenya NHIF Rate using THIS LINK:  

def find_gross_salary(a,b):
    gross=a+b
    return gross

basic_salary=float(input("enter basic salary: "))
benefits = float(input("enter benefits: "))

gross_salary=find_gross_salary(basic_salary,benefits)
print(gross_salary)
# nhif
def find_nhif(gross):
    if gross<6000 and gross>0:
        nhif_contribution=150
    elif gross >=6000 and gross<=7999:
        nhif_contribution=300
    elif gross>=8000 and gross<=11999:
        nhif_contribution=400
    elif gross>=12000 and gross<=14999:
        nhif_contribution=500
    return nhif_contribution

NHIF=find_nhif(gross_salary)
print(NHIF)

# nssf
def find_nssf(gross):
    if gross<18000:
        nssf_contribution=gross*0.06
    else:
        nssf_contribution=18000*0.06
    return nssf_contribution

NSSF=find_nssf(gross_salary)
print(NSSF)
# nhdf 
def find_nhdf(sal):
    nhdf=sal*0.015
    return nhdf
NHDF=find_nhdf(gross_salary)
print(NHDF)
# taxable income
def find_tax(gross,nssf,nhif,nhdf):
    tax=gross-(nssf+nhif+nhdf)
    return tax
taxable_income=find_tax(gross_salary,NSSF,NHIF,NHDF)
print(taxable_income)

# payee
def find_payee(invoice,relief=2400):
    if invoice<=24000:
        payee=0
    elif invoice>24000 and invoice<=32333:
        payee=(24000*0.1)+((invoice-24000)*0.25)-relief
    elif invoice>32333 and invoice<=500000:
        payee=(24000*0.1)+(8333*0.25)+((invoice-32333)*0.3)-relief
    elif invoice>500000 and invoice<=800000:
        payee=(24000*0.1)+(8333*0.25)+(467667*0.3)+((invoice-500000)*0.325)-relief
    else:
        payee=(24000*0.1)+(8333*0.25)+(467667*0.3)+(300000*0.325)+((invoice-800000)*0.35)-relief
    return payee

Payee = find_payee(taxable_income)
print(Payee)

# net pay
# 20
def calc_net(gross,nssf,nhdf,nhif,payee):
    net=gross-(nssf+nhdf+nhif+payee)
    return net

net_pay=calc_net(gross_salary,NSSF,NHDF,NHIF,Payee)

print(net_pay)