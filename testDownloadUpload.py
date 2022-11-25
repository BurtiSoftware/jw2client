from jw2client import *
from wand.image import Image
import sys


JW2_CORE_URL = 'https://jamworks20-core.vati.rocks'
JW2_CONTENT_URL = 'https://jamworks20-content.vati.rocks'

USER = sys.argv[2]
PASS = sys.argv[3]

jw2 = Jamworks(JW2_CORE_URL,JW2_CONTENT_URL)

jw2.auth(USER,PASS)

print(jw2.token)

node_id = sys.argv[1]
node = jw2.getContentsFileInfo(node_id)


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