from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import datetime
import time

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

file_list = drive.ListFile({'q': "mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList() 

for file1 in file_list:
    if file1['title'] == 'DriveSyncFiles':
        drive_sync_list = drive.ListFile({'q': "'1KVO1LSuUQpU45FlWDMuq6f-PHPBELAYV' in parents and trashed=false"}).GetList()
        #print(drive_sync_list)
        #print(type(drive_sync_list))
        #print(len(drive_sync_list))
        #time.sleep(1000)
        
        for sync_file in drive_sync_list:
            print('title: %s, id: %s' % (sync_file['title'], sync_file['id']))
            if sync_file['title'] == str(datetime.datetime.now().date()):

                print(sync_file['title'])
                print(sync_file['id'])

                test_list = drive.ListFile({'q': "'{0}' in parents and trashed = false".format(sync_file['id'])}).GetList()
                print(test_list)
                
                for i in range(len(test_list)):
                    print(test_list[i])
                    
                print(len(test_list))
                
                
                break
            else:
                print('This does not match.')
                
time.sleep(1000)
            
print(datetime.datetime.now().date())

#V1.5
test_list = drive.ListFile({'q': " '1KVO1LSuUQpU45FlWDMuq6f-PHPBELAYV' in parents and trashed = false"}).GetList()
#test_list = drive.ListFile({'q': "'{0}' in '1KVO1LSuUQpU45FlWDMuq6f-PHPBELAYV' in parents and trashed = false".format(sync_file['id'])}).GetList()
print(test_list)
#test = "'1KVO1LSuUQpU45FlWDMuq6f-PHPBELAYV' in parents and trashed=false"
#print(test)
#print(type(test))

# ^ Should be in the right forma?

#V1.4
#dict_test = {'q': "'{0}' in parents and trashed = false".format(sync_file['id'])}
#print(dict_test)
#print(type(dict_test))
#print(dict_test['q'])
#print(type(dict_test['q']))

#V1.3
#dict_test = {'q': 'test{0}'.format(sync_file['id'])}
#print(dict_test)

#dict_test = {'q': "'{0}'"}.format(sync_file['id'])
#print(dict_test)

#V1.2
#print('Hi there,{0}'.format(sync_file['id']))

#test_list = drive.ListFile({'q': "'{0}' in parents and trashed=false"}).format(.GetList()


#V1.1
#test_list = drive.ListFile({'q': "'{0}' in parents and trashed=false"}).GetList()
#print(test_list)

#print('One more time.')
#test_list = drive.ListFile({'q': " '1KVO1LSuUQpU45FlWDMuq6f-PHPBELAYV' in parents and trashed = false"}).GetList()            
#print(test_list)
            
            
            #sync_file.GetContentFile(sync_file['title'], mimetype='text/csv')
            
            #if sync_file['mimeType'] in mimetypes:
            #    print(sync_file['mimeType'])
            #else:
            #    print('NoMime')
            #r'C:\Users\XXXXX\Desktop\googedrive\\' + item['title']
            #sync_file.GetContentFile(filename = sync_file['title'])
#print('title: %s, id: %s' % (file1['title'], file1['id']))