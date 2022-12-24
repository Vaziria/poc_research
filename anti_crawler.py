from typing import List, Union
from pydantic import BaseModel, Field
import time

from base64 import b64encode

from encript import encript_af


head_dict = {
    "FILED_VERSION_SLOT": 0,
    "FILED_START_TIME_STAMP_SLOT": 1,
    "FILED_BODY_CHECKSUM_SLOT": 2,
    "FILED_BODY_LENGTH_SLOT": 3,
    "FILED_ALGORITHM_INDICATOR_SLOT": 4,
    "FILED_VERSION_WATERMARK_SLOT": 5,
    "FILED_HEAD_TOTAL_SLOTS_NUM_SLOT": 6,
    "properties": {
        "0": {
            "type": 2051,
            "length": 105
        },
        "1": {
            "type": 291,
            "length": 77
        },
        "2": {
            "type": 291,
            "length": 7
        },
        "3": {
            "type": 291,
            "length": 105
        },
        "4": {
            "type": 291,
            "length": 77
        },
        "5": {
            "type": 291,
            "length": 7
        }
    }
}


body_dict = {
    "FILED_VIDEO_VENDER_SLOT": 0,
    "FILED_VIDEO_RENDER_SLOT": 1,
    "FILED_BATTERY_STATUS_SLOT": 2,
    "FILED_BATTERY_LEVEL_SLOT": 3,
    "FILED_BATTERY_CHARGE_STATUS_SLOT": 4,
    "FILED_SCREEN_WIDTH_SLOT": 5,
    "FILED_SCREEN_HEIGHT_SLOT": 6,
    "FILED_SCREEN_COLOR_DEPTH_SLOT": 7,
    "FILED_MAX_TOUCH_POINTS_SLOT": 8,
    "FILED_CPU_CORE_NUMBER_SLOT": 9,
    "FILED_PLUGINS_SLOT": 10,
    "FILED_PLATFORM_SLOT": 11,
    "FILED_LANGUAGE_SLOT": 12,
    "FILED_LANGUAGES_SLOT": 13,
    "FILED_CONNECTION_TYPE_SLOT": 14,
    "FILED_INNER_WIDTH_WIN_POS_SLOT": 15,
    "FILED_INNER_HEIGHT_WIN_POS_SLOT": 16,
    "FILED_HOOK_ATTRIBUTE_SLOT": 17,
    "FILED_PROXY_FLAG_SLOT": 18,
    "FILED_SCREEN_LEFT_WIN_POS_SLOT": 19,
    "FILED_SCREEN_TOP_WIN_POS_SLOT": 20,
    "FILED_PERFORMANCE_SLOT": 21,
    "FILED_EMULATOR_ATTR_SLOT": 22,
    "FILED_AUDIO_LIST_SLOT": 23,
    "FILED_VIDEO_LIST_SLOT": 24,
    "FILED_BROWSER_KERNEL_TYPE_0_SLOT": 25,
    "FILED_BROWSER_KERNEL_TYPE_1_SLOT": 26,
    "FILED_CHROME_VER_SLOT": 27,
    "FILED_FIREFOX_VER_SLOT": 28,
    "FILED_CODE_HASH_SLOT": 29,
    "FILED_TIMEZONE_OFFSET_SLOT": 30,
    "FILED_DEBUGER_MODE_SLOT": 31,
    "FILED_BEAUTIFY_SOURCE_SLOT": 32,
    "FILED_INCOGNITO_MODE_SLOT": 33,
    "FILED_RUNNING_VIRTUAL_MACHINE_SLOT": 34,
    "FILED_MOBILE_DEVICES_SLOT": 35,
    "FILED_FAKE_UA_SLOT": 36,
    "FILED_DFP_SLOT": 37,
    "FILED_WEB_SCANNER_SLOT": 38,
    "FILED_BODY_TOTAL_SLOTS_NUM_SLOT": 39,
    "properties": {
        "0": {
            "type": 2051,
            "length": 105
        },
        "1": {
            "type": 2051,
            "length": 105
        },
        "2": {
            "type": 291,
            "length": 105
        },
        "3": {
            "type": 291,
            "length": 105
        },
        "4": {
            "type": 291,
            "length": 105
        },
        "5": {
            "type": 291,
            "length": 105
        },
        "6": {
            "type": 291,
            "length": 105
        },
        "7": {
            "type": 291,
            "length": 105
        },
        "8": {
            "type": 291,
            "length": 105
        },
        "9": {
            "type": 291,
            "length": 105
        },
        "10": {
            "type": 2169,
            "length": 105
        },
        "11": {
            "type": 2051,
            "length": 105
        },
        "12": {
            "type": 2051,
            "length": 105
        },
        "13": {
            "type": 2051,
            "length": 105
        },
        "14": {
            "type": 2051,
            "length": 105
        },
        "15": {
            "type": 291,
            "length": 105
        },
        "16": {
            "type": 291,
            "length": 105
        },
        "17": {
            "type": 291,
            "length": 77
        },
        "18": {
            "type": 291,
            "length": 105
        },
        "19": {
            "type": 291,
            "length": 105
        },
        "20": {
            "type": 291,
            "length": 105
        },
        "21": {
            "type": 291,
            "length": 77
        },
        "22": {
            "type": 291,
            "length": 77
        },
        "23": {
            "type": 1938,
            "length": 105
        },
        "24": {
            "type": 1938,
            "length": 105
        },
        "25": {
            "type": 291,
            "length": 105
        },
        "26": {
            "type": 291,
            "length": 105
        },
        "27": {
            "type": 2051,
            "length": 105
        },
        "28": {
            "type": 2051,
            "length": 105
        },
        "29": {
            "type": 291,
            "length": 7
        },
        "30": {
            "type": 291,
            "length": 105
        },
        "31": {
            "type": 291,
            "length": 88
        },
        "32": {
            "type": 291,
            "length": 88
        },
        "33": {
            "type": 291,
            "length": 88
        },
        "34": {
            "type": 291,
            "length": 88
        },
        "35": {
            "type": 291,
            "length": 88
        },
        "36": {
            "type": 291,
            "length": 88
        },
        "37": {
            "type": 2051,
            "length": 105
        },
        "38": {
            "type": 291,
            "length": 7
        }
    }
}


class Serialize(BaseModel):
    
    def encode_1(self, panjang, body_value): # arg1, arg2, 
        
        if panjang == 88:
            hasil = []
            hasil.append(255 & body_value)
            
        
        elif panjang == 105:
            hasil = self.parse_1(body_value)
        
        elif panjang == 7:
            
            hasil = self.parse_2(body_value)
        
        elif panjang == 77:
            
            hasil = 4294967296
            cc = int(body_value / hasil) or 0
            counter = body_value - cc * hasil
            hasil = self.parse_2(cc) + self.parse_2(counter)
        
        return hasil
    
    def encode_2(self, body_value):
        hasil = []
        
        for c in body_value:
            hasil.append(255 & ord(c))
        
        return hasil
        
    def parse_1(self, body_value):
        hasil = []
    
        hasil.extend([body_value >> 8 & 255, 255 & body_value])

        return hasil
    
    def parse_2(self, body_value):
        hasil = []
        
        if body_value == '':
            body_value = 0
        
        val1 = body_value >> 24 & 255 
        val2 = body_value >> 16 & 255
        
        hasil.extend([body_value >> 24 & 255, body_value >> 16 & 255, body_value >> 8 & 255, 255 & body_value])

        return hasil
    
    

class BodyAf(Serialize):
    FILED_VIDEO_VENDER_SLOT: str = 'r1Google Inc. (NVIDIA)'
    FILED_VIDEO_RENDER_SLOT: str = 'x1ANGLE (NVIDIA, NVIDIA GeForce GT 730 Direct3D11 vs_5_0 ps_5_0, D3D11)'
    FILED_BATTERY_STATUS_SLOT: int = 0
    FILED_BATTERY_LEVEL_SLOT: int = 100
    FILED_BATTERY_CHARGE_STATUS_SLOT: bool = True
    FILED_SCREEN_WIDTH_SLOT: int = 1920
    FILED_SCREEN_HEIGHT_SLOT: int = 1080
    FILED_SCREEN_COLOR_DEPTH_SLOT: int = 24
    FILED_MAX_TOUCH_POINTS_SLOT: int = -1
    FILED_CPU_CORE_NUMBER_SLOT: int = 16
    FILED_PLUGINS_SLOT: List[Union[int, str]] = [5, "PDF Viewer_internal-pdf-viewer_pdf_", "Chrome PDF Viewer_internal-pdf-viewer_pdf_", "Chromium PDF Viewer_internal-pdf-viewer_pdf_", "Microsoft Edge PDF Viewer_internal-pdf-viewer_pdf_", "WebKit built-in PDF_internal-pdf-viewer_pdf_"]

    FILED_PLATFORM_SLOT: str = "Win32"
    FILED_LANGUAGE_SLOT: str = "en"
    FILED_LANGUAGES_SLOT: str = "en"
    FILED_CONNECTION_TYPE_SLOT: str = "4g"
    FILED_INNER_WIDTH_WIN_POS_SLOT: int = 1920
    FILED_INNER_HEIGHT_WIN_POS_SLOT: int = 947
    FILED_HOOK_ATTRIBUTE_SLOT: int = 0
    FILED_PROXY_FLAG_SLOT: int = 1
    FILED_SCREEN_LEFT_WIN_POS_SLOT: int = 0
    FILED_SCREEN_TOP_WIN_POS_SLOT: int = 0
    FILED_PERFORMANCE_SLOT: int = 1295771500
    FILED_EMULATOR_ATTR_SLOT: int = 0
    FILED_AUDIO_LIST_SLOT: List[str] = [
        "probably",
        "probably",
        "probably",
        "maybe"
    ]
    FILED_VIDEO_LIST_SLOT: List[str] = [
        "probably",
        "probably",
        "probably"
    ]
    FILED_BROWSER_KERNEL_TYPE_0_SLOT: int = 2
    FILED_BROWSER_KERNEL_TYPE_1_SLOT: int = 2
    FILED_CHROME_VER_SLOT: str = "11111111111111111111111111111110100111"
    FILED_FIREFOX_VER_SLOT: str = "111111111111111111111111111111111111111"
    FILED_CODE_HASH_SLOT: int = 937019376
    FILED_TIMEZONE_OFFSET_SLOT: int = -420
    FILED_DEBUGER_MODE_SLOT: int = 0
    FILED_BEAUTIFY_SOURCE_SLOT: bool = True
    FILED_INCOGNITO_MODE_SLOT: int = 0
    FILED_RUNNING_VIRTUAL_MACHINE_SLOT: bool = False
    FILED_MOBILE_DEVICES_SLOT: bool = False
    FILED_FAKE_UA_SLOT: bool = False
    FILED_DFP_SLOT: str = ""
    FILED_WEB_SCANNER_SLOT: str = ""
    
    def to_array(self):
        data = self.dict()
        
        hasil = [ None for c in data.keys()]
        
        for key, value in data.items():
            index = body_dict[key]
            hasil[index] = value
            
        return hasil
        
    
    
    def serialize(self):
        index_true = [ 28, 15, 13, 25, 3, 37, 5, 26, 6, 21, 32, 8, 35, 27, 1, 12, 10, 0, 20, 2, 34, 11, 30, 22, 23, 4, 38, 24, 14, 29, 9, 7, 17, 19, 18, 36, 33, 31, 16]
        data = self.to_array()
        
        belakangBack = []
        
        for c in range(0, body_dict['FILED_BODY_TOTAL_SLOTS_NUM_SLOT']):
            true_index = index_true[c]
            body_value = data[true_index]
            tipe = body_dict['properties'][str(true_index)]['type']
            panjang = body_dict['properties'][str(true_index)]['length']
            
            if tipe == 291:
                belakangBack = belakangBack + self.encode_1(panjang, body_value)
            
            elif tipe == 2051:
                body_len = len(body_value)
                belakangBack = belakangBack + self.encode_1(panjang, body_len)
                belakangBack = belakangBack + self.encode_2(body_value)
            
            elif tipe == 1938:
                body_len = len(body_value)
                belakangBack = belakangBack + self.parse_1(body_len)
                
                for c2 in range(0, body_len):
                    belakangBack = belakangBack + self.parse_1(len(body_value[c2]))        
                    belakangBack = belakangBack + self.encode_2(body_value[c2])
            
            elif tipe == 2169:
                val = body_value[0]
                belakangBack = belakangBack + self.parse_1(val)
                
                if val > 16:
                    limit = 16
                else:
                    limit = val
                
                for c3 in range(0, limit):
                    belakangBack = belakangBack + self.parse_1(len(body_value[c3 + 1]))
                    belakangBack = belakangBack + self.encode_2(body_value[c3 + 1])
                    
        
        belakangMod = len(belakangBack) % 16
        if belakangMod:
            limit = 16 - belakangMod
            
            for c in range(0, limit):
                belakangBack.append(limit)
                    
        return belakangBack
    

def get_time_mili():
    
    return int(time.time_ns() / 1000)



class HeadAf(Serialize):
    FILED_VERSION_SLOT: str = '2.4.1-2'
    FILED_START_TIME_STAMP_SLOT: int = Field(default_factory=get_time_mili)
    FILED_BODY_CHECKSUM_SLOT: int = 2780
    FILED_BODY_LENGTH_SLOT: int = 576
    FILED_ALGORITHM_INDICATOR_SLOT: int = 2
    FILED_VERSION_WATERMARK_SLOT: int = 3957671804
    
    data_sequence: List[int] = []
    
    def __init__(self, body_af: BodyAf = None) -> None:
        
        if not body_af:
            body_af = BodyAf()
        
        sequence = body_af.serialize()
        
        
        data = {
            'data_sequence': sequence,
            'FILED_BODY_CHECKSUM_SLOT': self.get_checksum(sequence),
            'FILED_BODY_LENGTH_SLOT': len(sequence)
            
        }
        
        super().__init__(**data)
        
    
    def to_array(self):
        data = self.dict(exclude={'data_sequence'})
        
        hasil = [ None for c in data.keys()]
        
        for key, value in data.items():
            index = head_dict[key]
            hasil[index] = value
            
        return hasil
    
    
    def serialize(self):
        datahead = self.to_array()
        head_index = [ 0, 1, 2, 3, 4, 5]
        
        head_back = []
        
        for counter in range(0, head_dict['FILED_HEAD_TOTAL_SLOTS_NUM_SLOT']):
        
            true_index = head_index[counter]
            head_value = datahead[true_index]
            tipe = head_dict['properties'][str(true_index)]['type']
            tipe_len = head_dict['properties'][str(true_index)]['length']
            
            if tipe == 291:
                head_back = head_back + self.encode_1(tipe_len, head_value)
            
            elif tipe == 2051:
                value_len = len(head_value)
                head_back = head_back + self.encode_1(tipe_len, value_len)
                head_back = head_back + self.encode_2(head_value)
        
        return head_back
            
    
    def get_checksum(self, data):
        hasil = 0
        counter = 0
        
        while counter < len(data):
            hasil = hasil + (15 & data[counter]) & 4294967295
            counter += 1
        return hasil
    
    def create_af_ac_enc(self):
        
        encript_sequence = encript_af(self.data_sequence)
        head_seq = self.serialize()
        
        final_seq = head_seq + encript_sequence
        final_seq = bytes(final_seq)
        
        return b64encode(final_seq)
    
    

    
    
if __name__ == '__main__':
    
    body = BodyAf()
    hasil = body.serialize()
    print(hasil[: 100], len(hasil))
    
    head = HeadAf(body)
    hasil = head.create_af_ac_enc()
    print(hasil, len(hasil))