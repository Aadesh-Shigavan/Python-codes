final2011 = ['sehwag','Gambhir','Virat','Yuraj']

print(final2011)


final2011.append('Dhoni')        #['sehwag', 'Gambhir', 'Virat', 'Yuraj', 'Dhoni']
										 #APPEND OPERATION

print(final2011)




final2011.append(['Raina','Jadeja'])		#['sehwag', 'Gambhir', 'Virat', 'Yuraj', ['Raina', 'Jadeja']]


print(final2011)



final2011.extend(['Raina','Jadeja'])		#	EXTEND OPERATION
											#['sehwag', 'Gambhir', 'Virat', 'Yuraj', 'Raina', 'Jadeja']

print(final2011)



					
final2011.pop(0)							#POP OPERATION
											#['sehwag', 'Gambhir', 'Virat', 'Yuraj']
											#	['Gambhir', 'Virat', 'Yuraj']
	

print(final2011)



final2011.insert(3,'Dhoni')					#INSERT OPERATION
											#['sehwag', 'Gambhir', 'Virat', 'Dhoni', 'Yuraj']

print(final2011)