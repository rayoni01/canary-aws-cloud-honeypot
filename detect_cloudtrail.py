import json
def handle(d):
    j=json.loads(d)
    print(f"🚨 AWS CANARY TRIGGERED: {j.get('memo')}\nIP: {j.get('src_ip')}\nAction: Disable key")
handle('{"memo":"AKIAIOSFODNN7EXAMPLE","src_ip":"54.210.12.33"}')
