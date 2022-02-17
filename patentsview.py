import requests
import csv
import datetime
import os
import math
import json

base_dir = os.getcwd()
url = "https://www.patentsview.org/api/patents/query"

keys = ["date", "year", "month", "EE", "INSTRUMENTS", "CHEMISTRY", "MECHE", "ALL"]
result = []
fName = os.path.join(base_dir, "reults.csv")
oFile = open(fName, 'w', newline='', encoding='utf-8')
writer = csv.DictWriter(oFile, fieldnames=keys)
writer.writeheader()

EE = ["F21H", "F21K", "F21L", "F21S", "F21V", "F21W", "F21Y", "H01B", "H01C", "H01F", "H01G", "H01H", "H01J", "H01K", "H01M", "H01R", "H01T", "H02B", "H02G", "H02H", "H02J", "H02K", "H02M", "H02N", "H02P", "H05B", "H05C", "H05F", "H99Z", "G09F", "G09G", "G11B", "H04N", "H04N", "H04N", "H04N", "H04N", "H04N", "H04N", "H04N", "H04N", "H04R", "H04S", "H05K", "G08C", "H01P", "H01Q", "H04B", "H04H", "H04J", "H04K", "H04M", "H04N", "H04Q", "H04L", "H04N", "H04W", "H03B", "H03C", "H03D", "H03F", "H03G", "H03H", "H03J", "H03K", "H03L", "H03M", "G06C", "G06D", "G06E", "G06F", "G06G", "G06J", "G06K", "G06M", "G06N", "G06T", "G10L", "G11C", "G06Q", "H01L"]
INSTRUMENTS = ["G02B", "G02C", "G02F", "G03B", "G03C", "G03D", "G03F", "G03G", "G03H", "H01S", "G01B", "G01C", "G01D", "G01F", "G01G", "G01H", "G01J", "G01K", "G01L", "G01M", "G01N", "G01N", "G01N", "G01N", "G01N", "G01N", "G01N", "G01N", "G01N", "G01N", "G01N", "G01N", "G01N", "G01N", "G01N", "G01N", "G01N", "G01N", "G01N", "G01N", "G01N", "G01P", "G01Q", "G01R", "G01S", "G01V", "G01W", "G04B", "G04C", "G04D", "G04F", "G04G", "G04R", "G12B", "G99Z", "G01N", "G05B", "G05D", "G05F", "G07B", "G07C", "G07D", "G07F", "G07G", "G08B", "G08G", "G09B", "G09C", "G09D", "A61B", "A61C", "A61D", "A61F", "A61G", "A61H", "A61J", "A61L", "A61M", "A61N", "H05G"]
CHEMISTRY = ["A61K", "A61Q", "C07B", "C07C", "C07D", "C07F", "C07H", "C07J", "C40B", "C07G", "C07K", "C12M", "C12N", "C12P", "C12Q", "C12R", "C12S", "A61K", "A61K", "A61K", "A61K", "A61K", "A61K", "A61K", "A61K", "A61K", "A61K", "A61K", "A61K", "A61K", "A61K", "A61K", "A61K", "A61K", "A61K", "A61K", "A61K", "A61K", "A61K", "A61K", "A61P", "C08B", "C08C", "C08F", "C08G", "C08H", "C08K", "C08L", "A01H", "A21D", "A23B", "A23C", "A23D", "A23F", "A23G", "A23J", "A23K", "A23L", "C12C", "C12F", "C12G", "C12H", "C12J", "C13B", "C13B", "C13B", "C13B", "C13B", "C13B", "C13B", "C13D", "C13F", "C13J", "C13K", "A01N", "A01P", "C05B", "C05C", "C05D", "C05F", "C05G", "C06B", "C06C", "C06D", "C06F", "C09B", "C09C", "C09D", "C09F", "C09G", "C09H", "C09J", "C09K", "C10B", "C10C", "C10F", "C10G", "C10H", "C10J", "C10K", "C10L", "C10M", "C10N", "C11B", "C11C", "C11D", "C99Z", "B22C", "B22D", "B22F", "C01B", "C01C", "C01D", "C01F", "C01G", "C03C", "C04B", "C21B", "C21C", "C21D", "C22B", "C22C", "C22F", "B05C", "B05D", "B32B", "C23C", "C23D", "C23F", "C23G", "C25B", "C25C", "C25D", "C25F", "C30B", "B81B", "B81C", "B82B", "B82Y", "B01B", "B01D", "B01D", "B01D", "B01D", "B01D", "B01D", "B01D", "B01D", "B01D", "B01D", "B01D", "B01D", "B01D", "B01D", "B01D", "B01D", "B01D", "B01D", "B01D", "B01D", "B01D", "B01D", "B01D", "B01D", "B01D", "B01D", "B01D", "B01D", "B01D", "B01D", "B01D", "B01F", "B01J", "B01L", "B02C", "B03B", "B03C", "B03D", "B04B", "B04C", "B05B", "B06B", "B07B", "B07C", "B08B", "C14C", "D06B", "D06C", "D06L", "F25J", "F26B", "H05H", "A62C", "B01D", "B01D", "B01D", "B01D", "B01D", "B01D", "B01D", "B01D", "B09B", "B09C", "B65F", "C02F", "E01F", "F01N", "F23G", "F23J", "G01T"]
MECHE = ["B25J", "B65B", "B65C", "B65D", "B65G", "B65H", "B66B", "B66C", "B66D", "B66F", "B67B", "B67C", "B67D", "A62D", "B21B", "B21C", "B21D", "B21F", "B21G", "B21H", "B21J", "B21K", "B21L", "B23B", "B23C", "B23D", "B23F", "B23G", "B23H", "B23K", "B23P", "B23Q", "B24B", "B24C", "B24D", "B25B", "B25C", "B25D", "B25F", "B25G", "B25H", "B26B", "B26D", "B26F", "B27B", "B27C", "B27D", "B27F", "B27G", "B27H", "B27J", "B27K", "B27L", "B27M", "B27N", "B30B", "F01B", "F01C", "F01D", "F01K", "F01L", "F01M", "F01P", "F02B", "F02C", "F02D", "F02F", "F02G", "F02K", "F02M", "F02N", "F02P", "F03B", "F03C", "F03D", "F03G", "F03H", "F04B", "F04C", "F04D", "F04F", "F23R", "F99Z", "G21B", "G21C", "G21D", "G21F", "G21G", "G21H", "G21J", "G21K", "A41H", "A43D", "A46D", "B31B", "B31C", "B31D", "B31F", "B41B", "B41C", "B41D", "B41F", "B41G", "B41J", "B41K", "B41L", "B41M", "B41N", "C14B", "D01B", "D01C", "D01D", "D01F", "D01G", "D01H", "D02G", "D02H", "D02J", "D03C", "D03D", "D03J", "D04B", "D04C", "D04G", "D04H", "D05B", "D05C", "D06G", "D06H", "D06J", "D06M", "D06P", "D06Q", "D21B", "D21C", "D21D", "D21F", "D21G", "D21H", "D21J", "D99Z", "A01B", "A01C", "A01D", "A01F", "A01G", "A01J", "A01K", "A01L", "A01M", "A21B", "A21C", "A22B", "A22C", "A23N", "A23P", "B02B", "B28B", "B28C", "B28D", "B29B", "B29C", "B29D", "B29K", "B29L", "B99Z", "C03B", "C08J", "C12L", "C13B", "C13B", "C13B", "C13B", "C13C", "C13G", "C13H", "F41A", "F41B", "F41C", "F41F", "F41G", "F41H", "F41J", "F42B", "F42C", "F42D", "F22B", "F22D", "F22G", "F23B", "F23C", "F23D", "F23H", "F23K", "F23L", "F23M", "F23N", "F23Q", "F24B", "F24C", "F24D", "F24F", "F24H", "F24J", "F25B", "F25C", "F27B", "F27D", "F28B", "F28C", "F28D", "F28F", "F28G", "F15B", "F15C", "F15D", "F16B", "F16C", "F16D", "F16F", "F16G", "F16H", "F16J", "F16K", "F16L", "F16M", "F16N", "F16P", "F16S", "F16T", "F17B", "F17C", "F17D", "G05G", "B60B", "B60C", "B60D", "B60F", "B60G", "B60H", "B60J", "B60K", "B60L", "B60M", "B60N", "B60P", "B60Q", "B60R", "B60S", "B60T", "B60V", "B60W", "B61B", "B61C", "B61D", "B61F", "B61G", "B61H", "B61J", "B61K", "B61L", "B62B", "B62C", "B62D", "B62H", "B62J", "B62K", "B62L", "B62M", "B63B", "B63C", "B63G", "B63H", "B63J", "B64B", "B64C", "B64D", "B64F", "B64G"]

classes = {"EE": EE, "INSTRUMENTS" : INSTRUMENTS, "CHEMISTRY" : CHEMISTRY, "MECHE" : MECHE}

start_year = 2020

for year in range(start_year, 2021):
    for month in range(1, 13):
        tRes = {}
        tRes["year"] = year
        tRes["month"] = month
        tRes["date"] = datetime.datetime(year, month, 1)
        print(tRes["date"])
        for i in classes:
            query = {'q':
                    { "_and":[
                        {"_gte" : {"patent_date" : "{}-{}-01".format(year,month)}},
                        {"_lte" : {"patent_date" : "{}-{}-31".format(year,month)}},
                        {"_lte" : {"app_type" : "28"}},
                        {"cpc_group_id" : classes[i]},
                        {"cpc_sequence" : "0"}
                        ]},
                    'f':
                        ["patent_number", "cpc_group_id", "cpc_sequence"],
                    'o': {"page":0,"per_page":1}}
            response = requests.post(url, data = json.dumps(query).encode()).json()
            tRes[i] = response["total_patent_count"]

        query = {'q':
                { "_and":[
                    {"_gte" : {"patent_date" : "{}-{}-01".format(year,month)}},
                    {"_lte" : {"patent_date" : "{}-{}-31".format(year,month)}},
                    {"_lte" : {"app_type" : "28"}},
                    ]},
                'f':
                    ["patent_number", "cpc_group_id", "cpc_sequence"],
                'o': {"page":0,"per_page":1}}
        response = requests.post(url, data = json.dumps(query).encode()).json()
        tRes["ALL"] = response["total_patent_count"]

        writer.writerow(tRes)


oFile.close()
