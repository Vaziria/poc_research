import asyncio
import os
from mitmproxy import options
from mitmproxy.tools import dump
from mitmproxy.http import HTTPFlow

import functools
import traceback


class RequestLogger:
    def load(self, loader):
        loader.add_option(
            name="validate_inbound_headers",
            typespec=bool,
            default=False,
            help="Add a count header to responses",
        )
            
    
        
    async def request(self, flow: HTTPFlow):
        print(flow.request.url)
        
        
    def response(context, flow: HTTPFlow):
        headers = dict(flow.response.headers)
        
        
def get_traceback_err(func):
    @functools.wraps(func)
    async def wrapped(*args):
        try:
            return await func(*args)
        except Exception as e:
            traceback.print_exc()
            
            
    return wrapped
        
        
class ResourceTampering:
    base_resource = 'assets_feb'
        
    def load(self, loader):
        loader.add_option(
            name="validate_inbound_headers",
            typespec=bool,
            default=False,
            help="Add a count header to responses",
        )
    
    @get_traceback_err
    async def response(self, flow: HTTPFlow):
        url = flow.request.url
        url = url.split("/")
        fname = url[-1]
        
        tamperpath = self.base_resource + "/" + fname
        if os.path.exists(tamperpath):
            print("tampering", tamperpath, "to", flow.request.url)
            with open(tamperpath, 'rb') as out:
                flow.response.content = out.read()
    

async def start_fix_proxy(host, port):
    opts = options.Options(listen_host=host, listen_port=port)

    master = dump.DumpMaster(
        opts,
        with_termlog=False,
        with_dumper=False,
    )
    master.addons.add(ResourceTampering())
    # master.addons.add(CsvWriter())
    # master.addons.add(CookiesInspect())
    # master.addons.add(ResourceTampering())
    
    await master.run()

if __name__ == '__main__':
    asyncio.run(start_fix_proxy('localhost', 8881))