# Jamworks2 Python Library # 

## Usage ##

Put the jw2client.py in your working directory.
In your application, import the Library 

```
from jw2client import *
```

### Create a Jawworks2 Object ###

To access the Jamworks2 Client methods, one must firs create an Instance containg the urls for the Applications Api. By now you can point Core (for account,users and authentication methods ) and Contents ( for file manipulation)

```
jw2 = Jamworks(JW2_CORE_URL,JW2_CONTENT_URL)
```

### Authorization ###

To call the following methods, the user must obtain the access token, for that just call the auth() methond passing user and password.

```
jw2.auth(USER,PASSWORD)
```

Once the authorization is sucessfull, you can check the internal token atribute 

```
print(jw2.token)
```

### Get a Contents File Info ###
To get the file information about a Contents node_id just call the getContentsFileInfo method passing the id of the file node.

```
node = getContentsFileInfo(node_id)
```

The method returns an object containing the following structure
* node_id => Id of the file node confirmed when the method is sucessfull
* tenant_id => Id of the tenant owner of the file node
* folder_parent_id => Id of the file node parent (generally a folder)
* name => Name of the file node 
* type => Type of the file node ('file'  and 'folder' by now)
* mime => The mimetype of the file_node
* extension => Extension if appliable
* filesize => File size in bytes
* content_hash => Checksum of the file content
* users_id => User id of file node's owner 
* created_at => Created date
* updated_at => Last Update date
* google_document_id => In case of a Google Drive document, it's documentid


### Download a Contents File ###

Just pass the node_id you want to download and point where it must be written in the filesystem

```
contentsDownloadFile(node_id,filename)
```

### Upload a Contents File ###

To upload a file from the filesystem, point the account tenant_id, the parent_node_id where the file must be parented to (usually it's folder id) and the name of the file to upload. Jamworks will register the file with the same filename. 

```
contentsUploadFile(tenant_id,parent_nodeid,filename)
```


### Example: Generating a rendition of an image file (Using ImageMagick) ###


* Importing the Library
```
from jw2client import *
import sys
from wand.image import Image
``` 

* Setting Application URLs and creating a Jamworks2 Instance
```
JW2_CORE_URL = 'https://jamworks-core.vati.rocks'
JW2_CONTENT_URL = 'https://jamworks-content.vati.rocks'
jw2 = Jamworks(JW2_CORE_URL,JW2_CONTENT_URL)
```

* Setting username and password and getting the credentials
```
USER = 'testeuser@emal.com'
PASS = '1234' 
jw2.auth(USER,PASS)
print(jw2.token)
```

* Getting the node_id from command line arguments and getting a node object
```
node_id = sys.argv[1]
node = jw2.getContentsFileInfo(node_id)
```

* Checking if the node is an image type, obtaining it's thumbnail and sending it to Jamworks2
```
if "image" in node.mime:
    jw2.contentsDownloadFile(node_id,node.name)
    image = Image(filename = node.name)
    w, h = image.width, image.height
    thumb_width = 100
    factor = thumb_width/float(w)
    thumb_height = int(h * factor)
    image.resize(thumb_width,thumb_height)
    image = image.convert('png')
    thumb_name = 'thumb_'+node.name+'.png'
    image.save(filename = thumb_name)
    uploaded_file = jw2.contentsUploadFile(node.tenant_id,node.folder_parent_id,thumb_name)
```



