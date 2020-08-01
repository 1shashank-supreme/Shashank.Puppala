p=int(input())
leads_list=[ ]
for x in range(p):
  leads_list.append(input())
def sorting_employees(employees_list):
    company_leads={ }
    number_of_employees={ }
    for y in employees_list:
        company=y[y.index('@')+1:y.index('.')]
        name=y[0:y.index('@')]
        if(company not in company_leads):
            company_leads[company]=[ ]
            company_leads[company].append(name)
            number_of_employees[company]=1
        else:
            company_leads[company].append(name)
            number_of_employees[company]+=1
    return company_leads, number_of_employees            
print(sorting_employees(leads_list))
