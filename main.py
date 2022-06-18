devices = [
    'ssw001.fn1', 'fsw001.tn1', 'ssw002.fn1', 'ssw002.tn1',
     'ssw003.fn1', 'fsw001.vn1', 'ssw002.vn1', 'fsw001.fn1',
    'fsw003.vn1'
]

output = {}
device_type = []
all_devices = []
sites = []
fn1 = []
tn1 = []
vn1 = []
ssw = []
fsw = []
ssw_dictionary_fn1 = {}
fsw_dictionary_fn1 = {}
ssw_dictionary_tn1 = {}
fsw_dictionary_tn1 = {}
ssw_dictionary_vn1 = {}
fsw_dictionary_vn1 = {}
nested_dict_fn1 = []
nested_dict_tn1 = []
nested_dict_vn1 = []

for i in devices:
    device_type.append(i[0:3])
    device_type = list(set(device_type))

for i in devices:
    sites.append(i[7:])
    sites = list(set(sites))

for i in devices:
    if i[7:] == 'fn1':
        fn1.append(i)
        output['fn1'] = fn1
    if i[7:] == 'tn1':
        tn1.append(i)
        output['tn1'] = tn1
    if i[7:] == 'vn1':
        vn1.append(i)
        output['vn1'] = vn1

for key, value in output.items():
    if key == 'fn1':
        for x in value:
            if x[0:3] == 'ssw':
                ssw.append(x)
            if x[0:3] == 'fsw':
                fsw.append(x)

        ssw_dictionary_fn1['ssw'] = ssw
        nested_dict_fn1.append(ssw_dictionary_fn1)

        fsw_dictionary_fn1['fsw'] = fsw
        nested_dict_fn1.append(fsw_dictionary_fn1)



        output['fn1'] = nested_dict_fn1

        ssw = []
        fsw = []


    elif key == 'tn1':
        for x in value:
            if x[0:3] == 'ssw':
                ssw.append(x)
            if x[0:3] == 'fsw':
                fsw.append(x)

        ssw_dictionary_tn1['ssw'] = ssw
        nested_dict_tn1.append(ssw_dictionary_tn1)

        fsw_dictionary_tn1['fsw'] = fsw
        nested_dict_tn1.append(fsw_dictionary_tn1)

        output['tn1'] = nested_dict_tn1

        ssw = []
        fsw = []

    if key == 'vn1':
        for x in value:
            if x[0:3] == 'ssw':
                ssw.append(x)
            if x[0:3] == 'fsw':
                fsw.append(x)

        ssw_dictionary_vn1['ssw'] = ssw
        nested_dict_vn1.append(ssw_dictionary_vn1)

        fsw_dictionary_vn1['fsw'] = fsw
        nested_dict_vn1.append(fsw_dictionary_vn1)
        output['vn1'] = nested_dict_vn1

        ssw = []
        fsw = []


site_name = input("Which site do you want to get the devices from?: ")
device_choice = input("Which type of device do you want to get?: ")
# print(site_name)
# print(output['fn1'])
# print(output)
for i in output[site_name]:
    for x,y in i.items():
        if x == device_choice:
            print(y)

# test_dict = [{'ssw': ['ssw002.vn1']}, {'fsw': ['fsw001.vn1', 'fsw003.vn1']}]
# print(test_dict)
# for i in test_dict:
#     for x, y in i.items():
#         print(x, y)




