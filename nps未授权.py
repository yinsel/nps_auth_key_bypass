import asyncio,hashlib,time
from mitmproxy.tools.dump import DumpMaster
from mitmproxy import http
from mitmproxy import options

def md5(s: str):
    m = hashlib.md5()
    m.update(s.encode())
    return m.hexdigest()

def get_param():
    auth_key = md5(str(int(time.time())))
    timestamp = int(time.time())
    return {"auth_key": auth_key,"timestamp":timestamp}

class NPS:
    def request(self,flow: http.HTTPFlow):
        param = get_param()
        flow.request.query.add("auth_key",param['auth_key'])
        flow.request.query.add("timestamp",param['timestamp'])
        print(flow.request.url)

async def main():
    proxy_server = "0.0.0.0"
    proxy_port = 9090
    options_ = options.Options(listen_host=proxy_server,listen_port=proxy_port)
    m = DumpMaster(options_,with_dumper=False,with_termlog=True)
    m.addons.add(NPS())
    print(f"代理服务器: http://{proxy_server}:{proxy_port}/")
    await m.run()

asyncio.run(main())