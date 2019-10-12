import matplotlib.pyplot as plt
import numpy as np
import json

filename="data.json"

with open(filename,"r") as f:

	data=json.load(f)

print(data["fields"])
names=[]
states_sp=[]
ssas_sp=[]
tots_sp=[]
states_work=[]
ssas_work=[]
tots_work=[]
states_vac=[]
ssas_vac=[]
tots_vac=[]
#South_indian_states=["Andhra Pradesh","Telangana","Tamil Nadu","Karnataka","Kerala","Goa"]
for state in data["data"]:
    #if(state[0]) in South_indian_states:
    name,state_sp,ssa_sp,tot_sp,state_work,ssa_work,tot_work,state_vac,ssa_vac,tot_vac=state
    names.append(name)
    states_sp.append(int(state_sp))
    ssas_sp.append(int(ssa_sp))
    tots_sp.append(int(tot_sp))
    states_work.append(int(state_work))
    ssas_work.append(int(ssa_work))
    tots_work.append(int(tot_work))
    states_vac.append(int(state_vac))
    ssas_vac.append(int(ssa_vac))
    tots_vac.append(int(tot_vac))


ind=[x-.3 for x in np.arange(len(names))]
ind2=[x+.3 for x in ind]
plt.figure(figsize=(20,6))
p1 = plt.bar(ind, states_work, 0.3)
p2 = plt.bar(ind,states_vac , 0.3,bottom=states_work)

p3 = plt.bar(ind2, ssas_work, 0.3)
p4 = plt.bar(ind2,ssas_vac , 0.3,bottom=ssas_work)

plt.ylabel('number of positions')
plt.xlabel("State")
plt.title('Statistics of woking and vacant primary teacher positions in india statewise')
plt.xticks(ind, names,rotation='vertical')
# plt.yticks(np.arange(0, 81, 10))

plt.legend((p1[0], p2[0],p3[0], p4[0]), ('Working - By State', ' Vacancies - By State','Working - Under SSA', 'Vacancies - Under SSA'))
plt.show()


plt.figure(figsize=(20,6))
plt.scatter(range(len(names)),tots_sp)
plt.xticks(ind, names,rotation='vertical')
plt.xlabel("State")
plt.ylabel("number of positions")
plt.title("Total no of sanctioned primary teacher positions by both state and SSA")

#plt.legend((s),(""))
plt.show()


labels=[x["label"] for x in data["fields"][1:]]
wrap_labels=["\n".join(x.split("-")) for x in labels]
plt.figure(figsize=(20,6))
s=plt.boxplot([states_sp,ssas_sp,tots_sp,states_work,ssas_work,tots_work,states_vac,ssas_vac,tots_vac])
plt.xticks(range(1,len(labels)+1),wrap_labels)
plt.xlabel("Statistic")
plt.ylabel("number of positions")
plt.title("Distribution of Statistic of sanctioned primary teacher positions in India")

plt.show()