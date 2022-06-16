devices = [
    'ssw001.fn1', 'fsw001.tn1', 'ssw002.fn1', 'ssw002.tn1',
     'ssw003.fn1', 'fsw001.vn1', 'ssw002.vn1'
]
output = {}
device_type = []
new_list = []
all_devices = []
for i in devices:
    device_type.append(i[0:3])
for i in device_type:

    if i not in new_list:
        new_list.append(i)

for i in devices:
    each_device = i.split('.')
    output[each_device[1]] = i
print(output)
