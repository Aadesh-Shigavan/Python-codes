AppList = ['Tiktok.apk','Shareit.apk','PUBG.apk','CamScanner.apk','UcBrowser.apk']

print(AppList)				#['Tiktok.apk', 'Shareit.apk', 'PUBG.apk', 'CamScanner.apk', 'UcBrowser.apk']

AppList.sort(key=len)

print(AppList)				#['PUBG.apk', 'Tiktok.apk', 'Shareit.apk', 'UcBrowser.apk', 'CamScanner.apk']




AppList.sort(key=len,reverse= True)			#['Tiktok.apk', 'Shareit.apk', 'PUBG.apk', 'CamScanner.apk', 'UcBrowser.apk']
											#['CamScanner.apk', 'UcBrowser.apk', 'Shareit.apk', 'Tiktok.apk', 'PUBG.apk']

print(AppList)