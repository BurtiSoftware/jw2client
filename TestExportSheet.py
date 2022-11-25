from jw2client import *
import sys


JW2_CORE_URL = "http://qa-core-api.vati.rocks:86"
JW2_CONTENT_URL = "http://qa-content-api.vati.rocks:89"

USER = sys.argv[3]
PASS = sys.argv[4]

jw2 = Jamworks(JW2_CORE_URL,JW2_CONTENT_URL)

jw2.auth(USER,PASS)

print(jw2.token)

node_id = sys.argv[1]
sheet_name = sys.argv[2]

json = jw2.contentsExportSheet(node_id,sheet_name,"json")

print(json)