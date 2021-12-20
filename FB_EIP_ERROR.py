

                        #sg    #min     #max
sg1799DictMinMax    = {101 : [125 ,   126],
                       110 : [173  ,  186],
                       111 : [187  ,  190],
                       201 : [122  ,  124],
                       210 : [157  ,  168],
                       211 : [169  ,  172],
                       301 : [121  ,  121],
                       310 : [141  ,  152],
                       311 : [153  ,  156],
                       401 : [120  ,  120],
                       410 : [127  ,  136],
                       411 : [138  ,  140],
                       600 : ['null' ,  'null'],
                       700 : [207  ,  216],
                       701 : [217  ,  222]
                       }


with open('outputFBEIP.txt', 'w') as f:
    for sg in sg1799DictMinMax.keys():
            ipAddresses = sg1799DictMinMax[sg]
            if type(ipAddresses[1]) == int and type(ipAddresses[0]) == int :
                length = ipAddresses[1] - ipAddresses[0]
                min = ipAddresses[0]
                #print(ipAddresses)
                #print(length)
                for i in range(length+1):
                    if i == 0:
                        f.write(f'EIP_Error_SG{sg} : = IO_1799_CARD_IN[{min + i}].State <> 0 OR \n')

                    elif i != length :
                        f.write(f'IO_1799_CARD_IN[{min + i}].State <> 0 OR \n')

                    else:
                        f.write(f'IO_1799_CARD_IN[{min + i}].State <> 0 ; \n')
            f.write('\n \n \n ')



