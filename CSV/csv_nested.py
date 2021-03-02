import json
import csv
import pandas as pd

with open('C:/Users/SSS2015046/Desktop/test1.json', 'r') as js:
    jdata = json.load(js)

output = {}
result = [ ]
# print(jdata['glossary']['title'])
# output['glossary_title'] = str(jdata['glossary']['title'])
# output['GlossDiv_title'] = str(jdata['glossary']['GlossDiv']['title'])

for k,v in jdata['glossary'].items():
    output['glossary_title'] = str(jdata['glossary']['title'])
    for k,v in jdata['glossary']['GlossDiv'].items():
        output['GlossDiv_title'] = str(jdata['glossary']['GlossDiv']['title'])
        for k,v in jdata['glossary']['GlossDiv']['GlossList']['GlossEntry'].items():
            output[k] = str(jdata['glossary']['GlossDiv']['GlossList']['GlossEntry'][k])
        if output[k] == 'GlossDef':
            # print(output[k])
            for k, v in jdata['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossDef'].items():
                output[k]=str(jdata['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossDef'][k])
    print(output[k])
        # if output[k] == 'para':


# result.append(output)
#         # print(output)
# df = pd.DataFrame(result)
# print(df)
# df.to_csv('C:/Users/SSS2015046/Desktop/jsontocsv1.csv', index=False)




# import json
# import csv
# import pandas as pd
#
# with open('C:/Users/SSS2015046/Desktop/test1.json', 'r') as js:
#     jdata = json.load(js)
#
# output = {}
# result = [ ]
# # print(jdata['glossary']['title'])
# output['glossary_title'] = str(jdata['glossary']['title'])
# output['GlossDiv_title'] = str(jdata['glossary']['GlossDiv']['title'])
# # for k,v in jdata['glossary'].items():
# #     output[k] = str(jdata['glossary'][k])
# #     for k,v in jdata['glossary']['GlossDiv'].items():
# #         output[k] = str(jdata['glossary']['GlossDiv'][k])
# #         for k,v in jdata['glossary']['GlossDiv']['GlossList'].items():
# #             output[k] = str(jdata['glossary']['GlossDiv']['GlossList'][k])
# #             for k,v in jdata['glossary']['GlossDiv']['GlossList']['GlossEntry'].items():
# #                 output[k] = str(jdata['glossary']['GlossDiv']['GlossList']['GlossEntry'][k])
# for k, v in jdata['glossary']['GlossDiv']['GlossList']['GlossEntry'].items():
#     output[k] = str(jdata['glossary']['GlossDiv']['GlossList']['GlossEntry'][k])
#
#
#
# # output['GlossDef_para'] = str(jdata['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossDef'][para])
# result.append(output)
# # output['GlossDef_GlossSeeAlso'] = str(jdata['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossDef']['GlossSeeAlso'])
#
#     # output['GlossDef_GlossSeeAlso'] = str(jdata['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossDef']['GlossSeeAlso'].items())
#
# # for k, v in jdata['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossDef'].items():
# #     output[k] = str(jdata['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossDef'][k])
# #       result.append(output)
# df = pd.DataFrame(result)
# print(df)
# df.to_csv('C:/Users/SSS2015046/Desktop/jsontocsv2.csv', index=False)








































import json
import csv
import pandas as pd

with open('C:/Users/SSS2015046/Desktop/test1.json', 'r') as js:
    jdata = json.load(js)

output = { }
result = [ ]
# print(jdata['glossary']['title'])
# output['glossary_title'] = str(jdata['glossary']['title'])
# output['GlossDiv_title'] = str(jdata['glossary']['GlossDiv']['title'])

for k,v in jdata['glossary'].items():
    output['glossary_title'] = str(jdata['glossary']['title'])
    for k,v in jdata['glossary']['GlossDiv'].items():
        output['GlossDiv_title'] = str(jdata['glossary']['GlossDiv']['title'])
        for k,v in jdata['glossary']['GlossDiv']['GlossList']['GlossEntry'].items():
            output[k] = str(jdata['glossary']['GlossDiv']['GlossList']['GlossEntry'][k])
            for k,v in jdata['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossDef'].items():
                output['GlossDef_para'] = str(jdata['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossDef']['para'])
                if output[k] == 'GlossDef_para':
                    print(output[k])
                elif output[k] == 'GlossDef_GlossSeeAlso':
                    output['GlossDef_GlossSeeAlso'] = str(jdata['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossDef']['GlossSeeAlso'])
                    print(output['GlossDef_GlossSeeAlso'])
# print(output)

            # print(output['GlossDef'])
        # if output[k] == 'A meta-markup language, used to create markup languages such as DocBook.':
        #     output['GlossDef_para'] = str(jdata['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossDef']['para'])
        #     # print(output['GlossDef_para'])
        #     # print(output['GlossSeeAlso'])
        # else:
        #     pass
            # for k, v in jdata['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossDef'].items():
            #     output[k]=str(jdata['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossDef'][k])
    # print(output[k])
        # if output[k] == 'para':
#     result.append(output)
#         # print(output)
#     df = pd.DataFrame(result)
#     print(df)
# df.to_csv('C:/Users/SSS2015046/Desktop/jsontocsv1.csv', index=False)

# print(output)
# result.append(output)
# df = pd.DataFrame(result)
# print(df)

# for k,v in jdata['glossary'].items():
#     output['glossary_title']=str(jdata['glossary']['title'])
#     for k,v in jdata['glossary']['GlossDiv'].items():
#         output['GlossDiv_title']=str(jdata['glossary']['GlossDiv']['title'])
#         for k,v in jdata['glossary']['GlossDiv']['GlossList']['GlossEntry'].items():
#             output[k]=str(jdata['glossary']['GlossDiv']['GlossList']['GlossEntry'][k])
#             # output['GlossDef']=str(jdata['glossary']['GlossDiv']['GlossList']['GlossEntry']
#             # output['GlossEntry'] = str(jdata['glossary']['GlossDiv']['GlossEntry']['GlossDef'])
#             for k,v in jdata['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossDef'].items():
#                 output[k]=str(jdata['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossDef'][k])
#                 for k, v in jdata['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossDef'].items():
#                     output[lossDef] = str(jdata['glossary']['GlossDiv']['GlossList']['GlossSee'])



# output['GlossDef_para'] = str(jdata['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossDef']['para'])

    # output['GlossDef_GlossSeeAlso'] = str(jdata['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossDef']['GlossSeeAlso'].items())

# for k, v in jdata['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossDef'].items():
#     output[k] = str(jdata['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossDef'][k])
#     result.append(output)
# result.append(output)
# df = pd.DataFrame(result)
# # print(df)
# df.to_csv('C:/Users/SSS2015046/Desktop/jsontocsv1.csv', index=False)