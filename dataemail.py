""" import re

f = open("*.txt", "r")
fr = re.sub('Subject:.*\n.*.*\n.*\n.*\n.*Reply-to:.*','', f.read())
print(fr) """


#import necessary modules
""" import csv
import re
from csv import DictReader

with open('messages.csv','rt')as f:
  data = DictReader(f)


  for row in data:
        print(row)  """

""" import mailbox
import email.utils

mbox = mailbox.mbox('mail.mbox')
for message in mbox:
    print (message['Content-Type']) """

"""
import mailbox

 def showMbox(mboxPath):
    box = mailbox.mbox(mboxPath)
    for msg in box:
        print (msg['Subject'])
        
        showPayload(msg)

        print('')
        print ('**********************************')
        print ('')


def showPayload(msg):
    payload = msg.get_payload()

    if msg.is_multipart():
        div = ''
        for subMsg in payload:
            print (showPayload(subMsg))
    else:
        print (msg.get_content_type())
        print (payload[:200])


if __name__ == '__main__':
    showMbox('mail.mbox') """


import os
import re
import csv

def rename_files(): 
    i = 0
      
    for filename in os.listdir("emails/"): 
        dst ="mensagen" + str(i) + ".txt"
        src ='emails/'+ filename 
        dst ='emails/'+ dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
        i += 1

def list_files ():
    csv_columns = ['conteudo','fraude']
    dict_emails = {'conteudo':'', 'fraude': 0}
    from pathlib import Path

    # List all files in directory using pathlib
    basepath = Path('emails/')
    files_in_basepath = (entry for entry in basepath.iterdir() if entry.is_file())
    #data_file = open('dataset.txt', 'w')
    data_file = open('dataset.csv', 'w')
    for item in files_in_basepath:
        
        print(item.name)
        arquivo = 'emails/' + item.name
        f = open(arquivo)
        fr = re.sub('.*:.*','', f.read())
        dict_emails['conteudo'] = fr

        writer = csv.DictWriter(data_file, fieldnames=csv_columns)
        writer.writeheader()

        writer.writerow(dict_emails)
        
    data_file.close()

    

#rename_files()
list_files()
