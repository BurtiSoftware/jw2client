import requests
import json

class File:
    def __init__(self):
        self.node_id  = 0
        self.tenant_id = 0
        self.folder_parent_id= 0
        self.name = ''
        self.type = ''
        self.mime = ''
        self.extension = ''
        self.filesize = 0
        self.content_hash = ''
        self.users_id = 0
        self.created_at = ''
        self.updated_at = ''
        self.google_document_id = ''

class Jamworks:
    def __init__(self,core_url,content_url):
        self.core_url =  core_url
        self.content_url = content_url
        self.token = ''
    
    def auth(self,user,password):
        auth_url = self.core_url+"/auth/login"
        params = {'username':user,'password':password}
        response = requests.post(url=auth_url,data=params)
        ret = response.json()
        print(ret)
        self.token = ret['token']
    
    def getContentsFileInfo(self,node_id):
        info_url = self.content_url+"/entry/"+str(node_id)
        headers = {"token":self.token}

        node_data_req = requests.get(url = info_url, headers = headers)
        
        print(node_data_req)

        node_data = node_data_req.json()
        file = File()
        file.node_id  = node_data['node_id']
        file.tenant_id = node_data['tenant_id']
        file.folder_parent_id = node_data['folder_parent_id']
        file.name = node_data['name']
        file.type = node_data['type']
        file.filesize = node_data['filesize']
        file.content_hash = node_data['content_hash']

        if(file.type != 'folder'):
            file.mime = node_data['mime']
            file.extension = node_data['extension']

            file.google_document_id = node_data['google_document_id']
        file.users_id = node_data['users_id']
        file.created_at = node_data['created_at']
        file.updated_at = node_data['updated_at']

        return file

    def contentsDownloadFile(self,node_id,filename):
        download_url = self.content_url+"/actions/download/"+str(node_id)
        headers = {"token":self.token}
        with requests.get(url = download_url, headers = headers , stream = True) as r:
            with open(filename,"wb") as f:
                for chunk in r.iter_content(chunk_size = 16 * 1024):
                    f.write(chunk)


    def contentsUploadFile(self,tenant_id,parent_nodeid,filename):
        upload_url = self.content_url+"/file"
        headers = {'token': self.token}
        data = {"tenant_id":tenant_id,"folder_parent_id":parent_nodeid}
        files = { "file":open(filename,"rb")}
        response = requests.post(url = upload_url, headers=headers, files=files, data=data)
        r = response.json()
        print(r)
        return self.getContentsFileInfo(r['node_id'])
    
    def contentsUploadRendition(self,relationship_type,node_type,node_id,filename,item_index):
        upload_url = self.content_url+"/rendition/upload/"+str(node_id)
        headers = {'token': self.token}
        data = {"relationship_type":relationship_type,"node_type":node_type,"item_index":item_index}
        files = { "file":open(filename,"rb")}
        response = requests.post(url = upload_url, headers=headers, files=files, data=data)
        r = response.json()
        return r


    def contentsExportSheet(self,nodeid,sheetName='',format='json',skip=0):
        #exportUrl = self.content_url+"/file/"+str(nodeid)+"/export?sheet_name="+sheetName+"&format="+format+"&skip="+skip
        exportUrl = self.content_url+"/file/"+str(nodeid)+"/export?format="+format+"&sheet_name="+sheetName+"&skip="+str(skip)
        headers = {'token': self.token}
        response = requests.get(url=exportUrl,headers=headers)
        return response.json()

