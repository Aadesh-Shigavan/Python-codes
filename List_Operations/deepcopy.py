import copy


cloud = ['AWS', 'Azure', 'GCP', 'Firebase', ['ThinkSpeak', 'IOTCloudeCore']]

print(cloud)
	
copy_cloud = copy.deepcopy(cloud)

print(copy_cloud) 	

copy_cloud[4].append('Pubnub')

print(copy_cloud) 	

print(cloud)