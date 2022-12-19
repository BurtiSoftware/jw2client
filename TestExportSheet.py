from jw2client import *
import sys


JW2_CORE_URL = "http://jamworks20-core.vati.rocks:86" 
JW2_CONTENT_URL = "https://jamworks20-content.vati.rocks"

USER = sys.argv[3]
PASS = sys.argv[4]

jw2 = Jamworks(JW2_CORE_URL,JW2_CONTENT_URL)


jw2.auth(USER,PASS)

print(jw2.token)

node_id = sys.argv[1]
sheet_name = sys.argv[2]

json = jw2.contentsExportSheet(node_id,sheet_name,"json")

print(json)