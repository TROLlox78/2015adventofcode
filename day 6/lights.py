# file=open('lights.txt','r')
# import re
# statedic={}
#
# def flipstate(check):
#     if statedic[check]==1:
#         return 0
#     elif statedic[check]==0:
#         return 1
# def format_line(file):
#
#     if file[:8]=='turn off':
#         turn_number_off(file)
#     elif file[:7]=='turn on':
#         turn_number_on(file)
#     elif file[:6]=='toggle':
#         flipnumber(file)
#
#
# def turn_number_on(line):
#     # von https://www.geeksforgeeks.org/python-extract-numbers-from-string/
#     temp = re.findall(r'\d+', line)
#     res = list(map(int, temp))
#     x1=res[0]
#     y1=res[1]
#     x2=res[2]
#     y2=res[3]
#     for i in range(x1, x2 + 1):
#         for j in range(y1, y2 + 1):
#             i = str(i)
#             j = str(j)
#             craft = i + ',' + j
#             statedic.update({craft:1})
# def turn_number_off(line):
#     temp = re.findall(r'\d+', line)
#     res = list(map(int, temp))
#     x1=res[0]
#     y1=res[1]
#     x2=res[2]
#     y2=res[3]
#     for i in range(x1, x2 + 1):
#         for j in range(y1, y2 + 1):
#             i = str(i)
#             j = str(j)
#             craft = i + ',' + j
#             statedic.update({craft:0})
# def flipnumber(line):
#     temp = re.findall(r'\d+', line)
#     res = list(map(int, temp))
#     x1=res[0]
#     y1=res[1]
#     x2=res[2]
#     y2=res[3]
#     for i in range(x1, x2 + 1):
#         for j in range(y1, y2 + 1):
#             i = str(i)
#             j = str(j)
#             craft = i + ',' + j
#             statedic.update({craft:flipstate(craft)})
#
# # GENERATE DICTONARY :(
# for i in range(0,1000):
#     for j in range(0,1000):
#         i=str(i)
#         j=str(j)
#         creft=i+','+j
#         statedic.update({creft:0})
# # RUN PROGRAM
# for i in range(0,301):
#     line = file.readline()
#     format_line(line)
#
# print(statedic)
# print(len(statedic))
# count=0
# for z in statedic.values():
#     count+=z
# print('count: ',count)

# PART 2
file=open('lights.txt','r')
import re
statedic={}

def flipstate(check):
    if statedic[check]==1:
        return 0
    elif statedic[check]==0:
        return 1
def format_line(file):

    if file[:8]=='turn off':
        turn_number_off(file)
    elif file[:7]=='turn on':
        turn_number_on(file)
    elif file[:6]=='toggle':
        flipnumber(file)


def turn_number_on(line):
    # auf https://www.geeksforgeeks.org/python-extract-numbers-from-string/
    temp = re.findall(r'\d+', line)
    res = list(map(int, temp))
    x1=res[0]
    y1=res[1]
    x2=res[2]
    y2=res[3]
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            i = str(i)
            j = str(j)
            craft = i + ',' + j
            x = statedic[craft]
            if x >= 0:
                x += 1
            statedic.update({craft:x})
def turn_number_off(line):
    temp = re.findall(r'\d+', line)
    res = list(map(int, temp))
    x1=res[0]
    y1=res[1]
    x2=res[2]
    y2=res[3]
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            i = str(i)
            j = str(j)
            craft = i + ',' + j
            x=statedic[craft]
            if x > 0:
                x-=1
            statedic.update({craft:x})
def flipnumber(line):
    temp = re.findall(r'\d+', line)
    res = list(map(int, temp))
    x1=res[0]
    y1=res[1]
    x2=res[2]
    y2=res[3]
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            i = str(i)
            j = str(j)
            craft = i + ',' + j
            x = statedic[craft]
            if x >= 0:
                x += 2
            statedic.update({craft:x})

# GENERATE DICTONARY :(
for i in range(0,1000):
    for j in range(0,1000):
        i=str(i)
        j=str(j)
        creft=i+','+j
        statedic.update({creft:0})
# RUN PROGRAM
for i in range(0,301):
    line = file.readline()
    format_line(line)

print(statedic)
print(len(statedic))
count=0
for z in statedic.values():
    count+=z
print('count: ',count)