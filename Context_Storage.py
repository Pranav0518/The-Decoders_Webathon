import urllib.request
from bs4 import BeautifulSoup
import re
import json
url="https://www.bajajfinserv.in/personal-loan"
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')

text=soup.text
nationality=r'Nationality:\s+(.+)\s+Age'
age=r'Age:\s+(.+?)\s+.'
Employee=r'Employee with:\s+(.+?)\s+.'
cibil=r'CIBIL score:\s+(.+?)\s+.'
Monthly=r'Monthly salary:\s+(.+?)\s+.'

nationality_m=re.search(nationality, text, re.S)
age_m=re.search(age, text, re.S)
Employee_m=re.search(Employee, text, re.S)
cibil_m=re.search(cibil, text, re.S)
Monthly_m=re.search(Monthly, text, re.S)

nationality_c = nationality_m.group(1).strip() if nationality_m else None
Employee_c = Employee_m.group(1).strip() if Employee_m else None
age_c = age_m.group(1).strip() if age_m else None
cibil_c = cibil_m.group(1).strip() if cibil_m else None
Monthly_c = Monthly_m.group(1).strip() if Monthly_m else None


data={
    "Nationality":nationality_c,
    "Age":age_c,
    "Employee":Employee_c,
    "CIBIL":cibil_c,
    "Monthly":Monthly_c

}


loan=r'Rs.\s+(.+?)\s+for'
tenure=r'of\s+(.+?)\s+.'
emi=r'first\s+(.+?)\s+,'
repay=r'Rs.\s+(.+?)\s+.'

loan_m=re.search(loan, text, re.S)
tenure_m=re.search(tenure, text, re.S)
emi_m=re.search(emi, text, re.S)
repay_m=re.search(repay, text, re.S)

loan_c = loan_m.group(1).strip() if loan_m else None
tenure_c= tenure_m.group(1).strip() if tenure_m else None
emi_c= emi_m.group(1).strip() if emi_m else None
repay_c= repay_m.group(1).strip() if repay_m else None

data1={
    "Loan":loan_c,
    "Tenure":tenure_c,
    "EMI":emi_c,
    "Repay":repay_c

}

first=r'including:\s+(.+?)\s+Instant'
second=r'facility\s+(.+?)\s+Minimal.'
third=r'approval\s+(.+?)\s+Money'
fourth=r'documentation\s+(.+?)\s+Flexible'
fifth=r'hours*\s+(.+?)\s+No hidden tenures'
sixth=r'Flexible tenures\s+(.+?)\s+ '

first_m=re.search(first, text, re.S)
second_m=re.search(second, text, re.S)
third_m=re.search(third, text, re.S)
fourth_m=re.search(fourth, text, re.S)
fifth_m=re.search(fifth, text, re.S)
sixth_m=re.search(sixth,text,re.S)

first_c = first_m.group(1).strip() if first_m else None
second_c = second_m.group(1).strip() if second_m else None
third_c = third_m.group(1).strip() if third_m else None
fourth_c = fourth_m.group(1).strip() if fourth_m else None
fifth_c = fifth_m.group(1).strip() if fifth_m else None
sixth_c = sixth_m.group(1).strip() if sixth_m else None


data2={
    "1":fifth_c,
    "2":second_c,
    "3":third_c,
    "4":fourth_c,
    "5":fifth_c,
    "6":sixth_c

}


fir=r'A\s+(.+?)\s+Monthly'
sec=r'score\s+(.+?)\s+Current.'
thi=r'Current\s+(.+?)\s+Employment'
four=r'debt\s+(.+?)\s+Age'
fif=r'status\s+(.+?)\s+Property'
six=r'Age of the applicant\s+(.+?)\s+ '

fir_m=re.search(first, text, re.S)
sec_m=re.search(second, text, re.S)
thi_m=re.search(thi, text, re.S)
four_m=re.search(four, text, re.S)
fif_m=re.search(fif, text, re.S)
six_m=re.search(six,text,re.S)

fir_c = fir_m.group(1).strip() if fir_m else None
sec_c = sec_m.group(1).strip() if fir_m else None
thr_c = thi_m.group(1).strip() if thi_m else None
four_c = four_m.group(1).strip() if four_m else None
fif_c = fif_m.group(1).strip() if fif_m else None
six_c = six_m.group(1).strip() if six_m else None


data3={
    "1":fir_c,
    "2":sec_c,
    "3":thr_c,
    "4":four_c,
    "5":fif_c,
    "6":six_c

}

hl1=r'Home loan for:\s+(.+?)\s+Government Employees'
hl2=r'Women\s+(.+?)\s+Advocates.'
hl3=r'Government Employees\s+(.+?)\s+Bank Employees'
hl4=r'Advocates\s+(.+?)\s+Private Employees'
hl5=r'Bank Employees\s+(.+?)\s+ '

hl1_m=re.search(hl1, text, re.S)
hl2_m=re.search(hl2, text, re.S)
hl3_m=re.search(hl3, text, re.S)
hl4_m=re.search(hl4, text, re.S)
hl5_m=re.search(hl5, text, re.S)


hl1_c = hl1_m.group(1).strip() if hl1_m else None
hl2_c = hl2_m.group(1).strip() if hl2_m else None
hl3_c = hl3_m.group(1).strip() if hl3_m else None
hl4_c = hl4_m.group(1).strip() if hl4_m else None
hl5_c = hl5_m.group(1).strip() if hl5_m else None


data4={
    "1":hl1_c,
    "2":hl2_c,
    "3":hl3_c,
    "4":hl4_c,
    "5":hl5_c

}
rate=r'Rate of interest\s+(.+?)\s+Processing fees'
process=r'Processing fees\s+(.+?)\s+Flexi Fee'
flexi=r'applicable below\)\s+(.+?)\s+Bounce charges'
Bounce=r'Bounce charges\s+(.+?)\s+Pre-payment charges'
Penal_interest=r'Penal interest\s+(.+?)\s+.\n'
Manadate=r'Mandate rejection charges\s+(.+?)\s+Annual maintenance charges'

rate_m=re.search(rate, text, re.S)
process_m=re.search(process, text, re.S)
Flexi_m=re.search(flexi, text, re.S)
Bounce_m=re.search(Bounce, text, re.S)
Penal_interest_m=re.search(Penal_interest, text, re.S)
Mandate_m=re.search(Manadate, text, re.S)


rate_c = rate_m.group(1).strip() if rate_m else None
process_c = process_m.group(1).strip() if process_m else None
flexi_c = Flexi_m.group(1).strip() if Flexi_m else None
Bounce_c = Bounce_m.group(1).strip() if Bounce_m else None
Penal_interest_c = Penal_interest_m.group(1).strip() if Penal_interest_m else None
Mandate_c = Mandate_m.group(1).strip() if Mandate_m else None



data5={
    "Rate of interesr":rate_c,
    "Processing fee":process_c,
    "Flexi Fee":flexi_c,
    "Bounce Charges":Bounce_c,
    "Penal interest":Penal_interest_c,
    "Mandate rection charge":Mandate_c

}


with open("sample.json","w") as outfile:
   outfile.write("\nEligibility_criteria")
   outfile.write(json.dumps(data, indent=4))
   outfile.write("\nFlexi Term loan")
   outfile.write(json.dumps(data1, indent=4))
   outfile.write("\n6 Reasons")
   outfile.write(json.dumps(data2, indent=4))
   outfile.write("\nEligible")
   outfile.write(json.dumps(data3, indent=4))
   outfile.write("\nHome Loan For")
   outfile.write(json.dumps(data4, indent=4))
   outfile.write("\nPersonal loan interest rates")
   outfile.write(json.dumps(data5, indent=4))

print("Eligibility Criteria")
print(json.dumps(data, indent=4))
print("Flexi Term loan")
print(json.dumps(data1, indent=4))
print("6 Reasons")
print(json.dumps(data2, indent=4))
print("Eligible")
print(json.dumps(data3, indent=4))
print("Home alone for")
print(json.dumps(data4, indent=4))
print("Personal loan interest rates")
print(json.dumps(data5, indent=4))






