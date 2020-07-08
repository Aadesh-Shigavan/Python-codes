cloud = ['AWS','Azure','GCP','Firebase']

#print(cloud)


copy_cloud = [] 		#['AWS', 'Azure', 'GCP', 'Firebase']
							#[]
#print(copy_cloud)

'''

copy_cloud = cloud

print(copy_cloud)

print(cloud)



copy_cloud.pop()

print(copy_cloud)				#['AWS', 'Azure', 'GCP']
						
print(cloud)					#	['AWS', 'Azure', 'GCP']




copy_cloud = cloud.copy()


print(copy_cloud)			#['AWS', 'Azure', 'GCP', 'Firebase']
							#	['AWS', 'Azure', 'GCP', 'Firebase']
print(cloud)



copy_cloud.pop()

print(copy_cloud)			#['AWS', 'Azure', 'GCP']
							#['AWS', 'Azure', 'GCP', 'Firebase']
print(cloud)

'''


copy_cloud = cloud.copy()
#print(copy_cloud)

copy_cloud.append(['ThinkSpeak','IOTCloudeCore'])

print(copy_cloud)

print(cloud)

copy_cloud[4].append('Pubnub')

print(copy_cloud)

print(cloud)