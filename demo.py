import env, json
from fec import fec
import simplejson

conn = fec.Fec(env.API_KEY)

def run():
    ret = conn.get("/candidates",
                   pages=[1,2,3,4,5],
                   params="&cycle=2012&cycle=2016&office=P")
    
    print json.dumps(ret[3])

run()
