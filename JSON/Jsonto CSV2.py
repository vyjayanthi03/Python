# import json
# import pandas as pd
#
# with open('C:/Users/SSS2015046/Desktop/json_test1.json', 'r') as j:
#     jdata = json.load(j)
#
# result = []
# data = jdata['quiz']
#
# for k,v in data.items():
#     output = {}
#     # print(v)
#     # print(k,v)
#     category = k
#     # print(category)
#
#     for  i in v:
#         q_data = v[i]
#         output = {}
#         question = q_data['question']
#         # print(category,question)
#         output['question']=category,question
#         print(output)


        #
        # options = q_data['options']
        # # print(category,options[0],options[1],options[2],options[3])
        # output['options']=category,options[0],options[1],options[2],options[3]
        #
        # answer = q_data['answer']
        #
        #
        # # print(category,answer)
        # output['answer'] = category,answer
# result.append(output)
#
# df = pd.DataFrame(result)
# print(result)
# df.to_csv('C:/Users/SSS2015046/Desktop/json_test1.csv', index = False)
#








import json
import threading
import pandas as pd

with open('C:/Users/SSS2015046/Desktop/json_test1.json', 'r') as j:
    jdata = json.load(j)
result = []

                                        #sport
for data in jdata['quiz']['sport']['q1']: #sport
    output = {}
    output['sport(question)'] = jdata['quiz']['sport']['q1']['question']
    for datasport in jdata['quiz']['sport']['q1']['options']:
        output['sport(options[1])'] = jdata['quiz']['sport']['q1']['options'][0]
        for data1 in jdata['quiz']['sport']['q1']['options']:
            output['sport(options[2])'] = jdata['quiz']['sport']['q1']['options'][1]
            for data1 in jdata['quiz']['sport']['q1']['options']:
                output['sport(options[3])'] = jdata['quiz']['sport']['q1']['options'][2]
                for data1 in jdata['quiz']['sport']['q1']['options']:
                    output['sport(options[4])'] = jdata['quiz']['sport']['q1']['options'][3]
                    for data1 in jdata['quiz']['sport']['q1']:
                        output['sport(answer)'] = jdata['quiz']['sport']['q1']['answer']

                                                    #mathsq1
                        for datamathsq1 in jdata['quiz']['maths']['q1']:  # mathsq1
                            output['mathsq1(question)'] = jdata['quiz']['maths']['q1']['question']
                            for data1 in jdata['quiz']['sport']['q1']['options']:
                                output['mathsq1(options[1])'] = jdata['quiz']['maths']['q1']['options'][0]
                                for data1 in jdata['quiz']['sport']['q1']['options']:
                                    output['mathsq1(options[2])'] = jdata['quiz']['maths']['q1']['options'][1]
                                    for data1 in jdata['quiz']['sport']['q1']['options']:
                                        output['mathsq1(options[3])'] = jdata['quiz']['maths']['q1']['options'][2]
                                        for data1 in jdata['quiz']['sport']['q1']['options']:
                                            output['mathsq1(options[4])'] = jdata['quiz']['maths']['q1']['options'][3]
                                            for data1 in jdata['quiz']['maths']['q1']:
                                                output['mathsq1(answer)'] = jdata['quiz']['maths']['q1']['answer']

                                                                #mathsq2
                                                for datamathsq2 in jdata['quiz']['maths']['q2']:  # mathsq2
                                                    output['mathsq2(question)'] = jdata['quiz']['maths']['q2']['question']
                                                    for data2 in jdata['quiz']['maths']['q2']['options']:
                                                        output['mathsq2(options[1])'] = jdata['quiz']['maths']['q2']['options'][0]
                                                        for data2 in jdata['quiz']['maths']['q2']['options']:
                                                            output['mathsq2(options[2])'] = jdata['quiz']['maths']['q2']['options'][1]
                                                            for data2 in jdata['quiz']['maths']['q2']['options']:
                                                                output['mathsq2(options[3])'] = jdata['quiz']['maths']['q2']['options'][2]
                                                                for data2 in jdata['quiz']['maths']['q2']['options']:
                                                                     output['mathsq2(options[4])'] = jdata['quiz']['maths']['q2']['options'][3]
                                                                     for data2 in jdata['quiz']['maths']['q2']:
                                                                         output['mathsq2(answer)'] = jdata['quiz']['maths']['q2']['answer']
result.append(output)
df = pd.DataFrame(result)
print(df)
df.to_csv('C:/Users/SSS2015046/Desktop/json_test1.csv', index=False)