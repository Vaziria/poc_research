import asyncio
import csv
from mitmproxy import options
from mitmproxy.tools import dump
from mitmproxy.http import HTTPFlow

from collections import OrderedDict


from base64 import b64encode


class RequestLogger:
    def load(self, loader):
        loader.add_option(
            name="validate_inbound_headers",
            typespec=bool,
            default=False,
            help="Add a count header to responses",
        )
            
            
    def request(self, flow: HTTPFlow):
        headers = dict(flow.request.headers)
        # pprint(headers)
        
        
    def response(context, flow: HTTPFlow):
        headers = dict(flow.response.headers)
        # pprint(headers)
        

class CsvWriter:
    
    def load(self, loader):
        loader.add_option(
            name="validate_inbound_headers",
            typespec=bool,
            default=False,
            help="Add a count header to responses",
        )
            
            
    def request(self, flow: HTTPFlow):
        headers = dict(flow.request.headers)
        
        if flow.request.url.find('/v4/search/search_items') != -1:
        
            head_key = list(headers.keys())
            
            with open('search.csv', 'a+', newline='') as file:
                
                writer = csv.DictWriter(file, fieldnames=head_key)
                writer.writerow(headers)
                
                
class CookiesInspect:
    
    old_cookies = {}
    old_headers = {}
    
    def load(self, loader):
        loader.add_option(
            name="validate_inbound_headers",
            typespec=bool,
            default=False,
            help="Add a count header to responses",
        )
            
            
    def request(self, flow: HTTPFlow):
        headers = dict(flow.request.headers)
        
        if flow.request.url.find('/v4/search/search_items') != -1:
            
            query = flow.request.url.split('?')[-1]
            
            headers = OrderedDict(flow.request.headers)
            headers['cookie'] = ''
            diff_headers = set(headers.items()) - set(self.old_headers.items())
            self.old_headers = headers
            
            cookies = OrderedDict(flow.request.cookies)
            diff = set(cookies.items()) - set(self.old_cookies.items())
            self.old_cookies = cookies
            
            print('---------------------query------------------')
            print(query)
            print('---------------------headers------------------')
            for key, vald in OrderedDict(diff_headers).items():
                print(key, '-->', vald)
            print('---------------------cookies------------------')
            for key, vald in OrderedDict(diff).items():
                print(key, '-->', vald)
                
    
            


        
            

class ResourceTampering:
    
    def load(self, loader):
        loader.add_option(
            name="validate_inbound_headers",
            typespec=bool,
            default=False,
            help="Add a count header to responses",
        )
    
    
    def response(context, flow: HTTPFlow):
        if flow.request.url.find('/shopee-pcmall-live-sg//assets/bundle.15a55f751c8d28c2.js') != -1:
            with open('./assets/bundle.15a55f751c8d28c2.js', 'rb') as out:
                flow.response.content = out.read()
                
        if flow.request.url.find('7a8a0c288aad2b15e94d84ab4405153f2685734f.js') != -1:
            
            print('tampering 7a8a0c288aad2b15e94d84ab4405153f2685734f.js')
            
            with open('./assets/7a8a0c288aad2b15e94d84ab4405153f2685734f.js', 'rb') as out:
                hasil = out.read()
                
                flow.response.content = hasil
                
        
    


async def start_proxy(host, port):
    opts = options.Options(listen_host=host, listen_port=port)

    master = dump.DumpMaster(
        opts,
        with_termlog=False,
        with_dumper=False,
    )
    # master.addons.add(RequestLogger())
    master.addons.add(CsvWriter())
    master.addons.add(CookiesInspect())
    master.addons.add(ResourceTampering())
    
    await master.run()
    return master

if __name__ == '__main__':
    asyncio.run(start_proxy('localhost', 8888))