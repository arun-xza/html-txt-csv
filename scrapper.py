from urllib.request import urlopen
from bs4 import BeautifulSoup

import csv
from datetime import datetime
import re

# specify the url
quote_page = "url" #college faculty profile link from the website

page = urlopen(quote_page)
soup = BeautifulSoup(page, "html.parser")
found = soup.get_text()
with open('scrap.txt', 'w') as outfile:
    print( found, file = outfile)

page = urlopen(quote_page)
soup = BeautifulSoup(page, "html.parser")
found = soup.get_text()
with open('scrap.txt', 'a') as outfile:
    print( found, file = outfile)

# query the website and return the html to the variable ‘page’

# parse the html using beautiful soup and store in variable `soup`

# # Take out the <div> of name and get its value
# name_box = soup.find("strong", attrs={"class": "Faculty Name: "})
# # strip() is used to remove starting and trailing
# name = name_box.text.strip()
# #print (name)
#print (name)
# # Take out the <div> of name and get its value
# name_box = soup.find_all("strong")
# # strip() is used to remove starting and trailing
# print (name_box)

# # open a csv file with append, so old data will not be erased
# with open("try2.csv", "a") as csv_file:
#  writer = csv.writer(csv_file)
#  writer.writerow([found,datetime.now()])

##get all texts from the page

##save it to a file


##converting from text to csv
# data = []
# with open('outfile.txt') as fin:
#     row = {}
#     for line in fin:
#         key, val = line.strip().split(":")
#         row[key] = val
#         if key == 'Offset From Attachment At Top':
#             data.append(row)
#             row = {}
#
# fieldnames = data[0].keys()
# with open('test.csv') as fout:
#     cw = csv.DictWriter(fout, fieldnames)
#     cw.writerows(data)
#

errors = []                       # The list where we will store results.
linenum = 0
substr = "Name:".lower()          # Substring to search for.
substr1 = "Designation:".lower()
substr2 = "Email:".lower()
substr3 = "ContactNo:".lower()
substr31 = "Contact No:".lower()
substr32 = "Contact No&".lower()
substr4 = "Qualification:".lower()
substr5 = "Specialisation:".lower()
with open ('scrap.txt', 'rt') as myfile:
    for line in myfile:
        linenum += 1
        if line.lower().find(substr) != -1:    # if case-insensitive match,
            errors.append(line)

        elif  line.lower().find(substr1) != -1:
            # errors.append(line.strip('\n'))
            errors.append(line)
        elif  line.lower().find(substr2) != -1:
            # errors.append(line.strip('\n'))
            errors.append(line)
        elif  line.lower().find(substr3) != -1:
            # errors.append(line.strip(','))
            errors.append(line)
        elif line.lower().find(substr31) != -1:
            # errors.append(line.strip(','))
            errors.append(line)
        elif line.lower().find(substr32) != -1:
            # errors.append(line.strip(','))
            errors.append(line)
        elif  line.lower().find(substr4) != -1:
            # errors.append(line.strip('\n'))
            errors.append(line)
        elif  line.lower().find(substr5) != -1:
             # errors.append(line.strip('\n'))
             errors.append(line)
for err in errors:
    fp = open("rawextract.txt","a")
    fp.write(err)
    fp.close()
    print(err)

import re



with open('rawextract.txt') as myfile, open("extract.txt","w") as writer :

    for m in re.findall('Faculty Name:.*\n*Designation:.*\n*Email:.*\nContactNo:.*\n*Qualification:.*\n*Area of Interest / Specialisation:.*\n.*', myfile.read()):
        writer.write(m)
        print(m)
writer.close()
#
# with open('rawextract.txt') as myfile, open("extract.txt","a") as writer :
#     for m in re.findall('Faculty Name:.*\n*Designation:.*\n*Email:.*\nContact No:.*\n*Qualification:.*\n*Area of Interest / Specialisation:.*', myfile.read()):
#         writer.write(m)
#         print(m)
# writer.close()
#
# with open('rawextract.txt') as myfile, open("extract.txt", "a") as writer:
#     for m in re.findall('Faculty Name:.*\n*Designation:.*\n*Email:.*\nContact No&.*\n*Qualification:.*\n*Area of Interest / Specialisation:.*', myfile.read()):
#         writer.write(m)
#         print(m)
# writer.close()

###################################################CHECK MODULE
###################################################
# errors = []
# str1 = "Name"
# fp = open("rawextract.txt")
# check = 0
# linenum = 0
# for i,line in enumerate(fp):
#     if str1 in line:
#         check = i
#         continue
#     if "ContactNo" in line and (i == check + 3):
#         print ("OK")
#     else:
#         print ("NOT OK")

######################################################################last working csv
# import pandas as pd
#
# with open('rawextract.txt', 'r') as records:
#     lines = [(line.split(':'))[1] for line in records.readlines()]
#     col_titles = ('Name', 'Designation','Email','Contact','Qualification','Specialisation')
#     data = pd.np.array(lines).reshape((len(lines) // 6, 6))
#     pd.DataFrame(data, columns=col_titles).to_csv("output.csv", index=False)


# import csv, collections
#
# with open('extract.txt', 'r') as record_fields, open('log.csv', 'w') as out_file:
#     records, fieldnames, record = [], collections.OrderedDict(), {}
#     for field in record_fields:
#         name, _, value = field.strip().partition(": ")
#         if name == "Faculty Name" and record:
#             records.append(record)
#             record = {}
#         if name not in record: record[name] = value
#         fieldnames[name] = None
#     records.append(record)
#
#     writer = csv.DictWriter(out_file, fieldnames=fieldnames.keys())
#     writer.writeheader()
#     writer.writerows(records)

import itertools, csv
data = [i.strip('\n').split(': ') for i in open('extract.txt')]
new_data = [[a, list(b)] for a, b in itertools.groupby(data, key=lambda x:x[0] == 'Faculty Name')]
header = [c for b in new_data[:2] for c, _ in b[-1]]
a, b, *d = [[new_data[i][-1][-1][-1], *[' '.join(c) for _, *c in new_data[i+1][-1]]] for i in range(0, len(new_data), 2)]
with open('professors.csv', 'w') as f:
  write = csv.writer(f)
  write.writerows([header, a, b, d[0][:6]])


    # substr = "Designation".lower()  # Substring to search for.
    # with open('outfile.txt', 'rt') as myfile:
    #     for line in myfile:
    #         linenum += 1
    #         if line.lower().find(substr) != -1:  # if case-insensitive match,
    #             errors.append("Line " + str(linenum) + ": " + line.rstrip('\n'))
    # for err in errors:
    #     print(err)

##using pandas
# import pandas
# etxt_file = r"test.txt"
# txt = open(try1.txt, "r")
# txt_string = txt.read()
#
#
# txt_lines = txt_string.split("\n")
# txt_dict = {}
#
#
# for txt_line in txt_lines:
#     k,v = txt_line.split(":")
#     k = k.strip()
#     v = v.strip()
#     if txt_dict.has_key(k):
#         list = txt_dict.get(k)
#     else:
#         list = []
#     list.append(v)
#     txt_dict[k]=list
#
# print (pandas.DataFrame.from_dict(txt_dict, orient="index"))
#
# # import csv
# import re
#
# fieldnames = ['Faculty name', 'Designation', 'Email', 'ContactNo', 'Qualification', 'Specialization']
#
# #re_fields = re.compile(r'({})\s+:\s(.*)'.format('|'.join(fieldnames)), re.I)
#
# with open('filtered.txt') as f_input, open('output.csv', 'wb') as f_output:
#     csv_output = csv.DictWriter(f_output, fieldnames)
#     csv_output.writeheader()
#     start = False
#
#     for line in f_input:
#         line = line.strip()
#
#         if len(line):
#             if 'name' in line:
#                 if start:
#                     start = False
#                     block.append(line)
#                     text_block = '\n'.join(block)
#
#                     for field, value in re_fields.findall(text_block):
#                         entry[field.upper()] = value
#
#                     # if line[0] == '*':
#                     #     entry['COMPUTER NAME'] = block[1]
#                     #     entry['STATUS'] = block[2]
#                     # else:
#                     #     entry['COMPUTER NAME'] = entry['NAME']
#                     #     entry['STATUS'] = 'Online'
#                     #
#                     csv_output.writerow(entry)
#
#                 else:
#                     start = True
#                     entry = {}
#                     block = [line]
#             elif start:
#                 block.append(line)

#
# #
#  import pandas
#
# # etxt_file = r"test.txt"
# # txt = open(txt_file, "r")
# with open("filtered.txt", 'r') as txt, open("csvfile", 'w') as etxt:
#     txt_string = txt.read()
#     txt_lines = txt_string.split("\n")
#     txt_dict = {}
#
#     for txt_line in txt_lines:
#
#        # k,v = txt_line.split(":")
#         for (k, v) in [txt_line.split(":")]:
#             k = k.strip()
#             v = v.strip()
#         if k in txt:
#         # if txt_dict.has_key(k):
#            list = txt_dict.get(k)
#         else:
#             list = []
#         list.append(v)
#         txt_dict[k]=list
#
# print (pandas.DataFrame.from_dict(txt_dict, orient="index"))
#
# for (k,v) in [s.split("=")]:
#     print(k,v)
#
#

# records = """Faculty Name: Dr. john doe///////LAST WORKING LOGIC
# Designation: Professor
# Email: johndoe@google.com
# ContactNo: 1234567, 9999999
# Qualification: M.Tech., Ph.D.
# Area of Interest / Specialisation: network security"""
#
# for record in records.split('Faculty Name'):
#     for record in records.split('Faculty Name'):
#         if record == '':
#             continue
#         fields = record.split('\n')
#
#     Faculty_Name = "NA"
#     Designation = "NA"
#     ContactNo = "NA"
#     Qualification = "NA"
#     Specialization = "NA"
#     for field in fields:
#         if field == '':
#             continue
#         field_name, field_value = field.split(':')
#         if field_name == "": # This is Faculty name, since we split on it
#             Faculty_Name = field_value
#         print(field_name )
#         if field_name == "Designation":
#             Designation = field_value
#         if field_name == "ContactNo":
#             ContactNo = field_value
#         if field_name == "Qualification":
#             Qualification = field_value
#         if field_name == "Specialization":
#             Specialization = field_value

# import csv, collections
#
# with open('extract.txt', 'r') as record_fields, open('log.csv', 'w') as out_file:
#     records, fieldnames, record = [], collections.OrderedDict(), {}
#     for field in record_fields:
#         name, _, value = field.strip().partition(": ")
#         if name == "Faculty Name" and record:
#             records.append(record)
#             record = {}
#         if name not in record: record[name] = value
#         fieldnames[name] = None
#     records.append(record)
#
#     writer = csv.DictWriter(out_file, fieldnames=fieldnames.keys())
#     writer.writeheader()
#     writer.writerows(records)


# with open('extract.txt', 'r') as records:
#     stripped = (line.strip() for line in records)
#     lines = (line.split(":") for line in stripped if line)
#     with open('log.csv', 'w') as out_file:
#         writer = csv.writer(out_file)
#         writer.writerows(lines)
# #
# #
#
# import csv, collections
#
# with open('extract.txt', 'r') as record_fields, open('log.csv', 'w') as out_file:
#     records, fieldnames, record = [], collections.OrderedDict(), {}
#     for field in record_fields:
#         name, _, value = field.strip().partition(": ")
#         if name == "Employee Name" and record:
#             records.append(record)
#             record = {}
#         if name not in record: record[name] = value
#         fieldnames[name] = None
#     records.append(record)
#
#     writer = csv.DictWriter(out_file, fieldnames=fieldnames.keys())
#     writer.writeheader()
#     writer.writerows(records)
#
#






# records = """Faculty Name: Dr. john doe
# Designation: Professor
# Email: johndoe@google.com
# ContactNo: 1234567, 9999999
# Qualification: M.Tech., Ph.D.
# Area of Interest / Specialisation: network security"""
# #
#

# with open('log.csv', 'r') as f:
#     for line in f:
#         for record in line.split('Faculty Name'):
#
#             if record == '':
#                 continue
#             fields = record.split('\n')
#             Faculty_Name = "NA"
#             Designation = "NA"
#             ContactNo = "NA"
#             Qualification = "NA"
#             Specialisation = "NA"
#             for field in fields:
#                 # if field == '':
#                 #    continue
#                 field_name, field_value = field.split(':')
#                 if field_name == "": # This is employee name, since we split on it
#                     Faculty_Name = field_value
#                     print(field_name,field_value)
#                 if field_name == "Designation":
#                    Designation = field_value
#                    print(field_name, field_value)
#                 if field_name == "ContactNo":
#                    ContactNo = field_value
#                    print(field_name, field_value)
#                 if field_name == "Qualification":
#                   Qualification = field_value
#                   print(field_name, field_value)
#                 if field_name == "Specialization":
#                     Specialization = field_value
#                     print(field_name, field_value)
#
# # #
# #
# import pandas
#
# etxt_file = r"test2.txt"
# txt = open("test.txt", "r")
# txt_string = txt.read()
#
#
# txt_lines = txt_string.split("\n")
# txt_dict = {}
#
#
# for txt_line in txt_lines:
#     k,v = txt_line.split(":")
#     k = k.strip()
#     v = v.strip()
#     if k in txt_dict:
#         list = txt_dict.get(k)
#     else:
#         list = []
#     list.append(v)
#     txt_dict[k]=list
#
# print (pandas.DataFrame.from_dict(txt_dict, orient="index"))
