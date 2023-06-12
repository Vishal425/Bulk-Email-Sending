#!/usr/bin/env python
# coding: utf-8

# In[32]:


#Sending email Main code 
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd
from email import encoders
from email.mime.base import MIMEBase
from string import Template
import time
#kamalkumarnagrale@gmail.com
read_data=pd.read_excel(r'C:\Users\vishal.lote\Documents\My Received Files\PY-SAURABH DUBEY (LAPTOP)\Email_Send\Testing Data1.xlsx')
for i in range(len(read_data)):
    print('this is the name',read_data['Name'][i])
    print('this is the email',read_data['Email'][i])
    port = 587  # For starttls
    smtp_server = "vgipl.in"
    sender_email = "virtualdigital@vgipl.in"
    receiver_email = str(read_data['Email'][i])
    password = 'Virtual%08' #input("Type your password and press enter:")
    # message = """\
    # This is the testing mail """
    #body = "This is an email with attachment sent from Python"

    context = ssl.create_default_context() ##

    message = MIMEMultipart("alternative")
    message["Subject"] = "E banker Core Banking Solutions for Nidhi Companys"
    message["From"] = "Virtual Galaxy Infotech Pvt.Ltd <{}>".format(str(sender_email))
    message["To"] = receiver_email
    #message["Bcc"] = receiver_email  # Recommended for mass emails



    # # Add body to email
    #message.attach(MIMEText(body, "plain"))



    """Step 1 for file attachment"""
    # #Add the pdf or file path you want to attach
    # filename = "D:\Python_Project\py\Dataset&Report\LIST-OF-SACCOS-AUDITED.pdf"  # In same directory as script

    # # Open PDF file in binary mode
    # with open(filename, "rb") as attachment:
    #     # Add file as application/octet-stream
    #     # Email client can usually download this automatically as attachment
    #     part = MIMEBase("application", "octet-stream")
    #     part.set_payload(attachment.read())

    # # Encode file in ASCII characters to send by email    
    # encoders.encode_base64(part)

    # # Add header as key/value pair to attachment part
    # part.add_header(
    #     "Content-Disposition",
    #     f"attachment; filename= {filename}",
    # )

    # message.attach(part)




    # Create the plain-text and HTML version of your message

    """ Step2   Body part attachment in text format"""
    #This is the Body text
    # text = """\
    # Hi,
    # This is the testing mail from python
    # https://vgipl.com/"""


    #This is the html attachments
    """Step3 for Html attachment """
    # html = """\
    # <html>
    #   <body>
    #     <p>Hi,<br>
    #        How are you?<br>
    #        <a href="https://vgipl.com/">Virtual Galaxy</a> 
    #        has many great tutorials.
    #     </p>
    #   </body>
    # </html>
    # """
    fname = r"C:\Users\vishal.lote\Documents\My Received Files\PY-SAURABH DUBEY (LAPTOP)\Email_Send\nidhi_email_page_03.html"
    html_file = open(fname, 'r', encoding='utf-8')
    source_code = html_file.read() 
    html_ = Template((source_code)).safe_substitute(code="Hello" +   read_data['Name'])#read_data['Name'][i]


    # Turn these into plain/html MIMEText objects
    # part1 = MIMEText(text, "plain")
    part2 = MIMEText(html_, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    # message.attach(part1)
    message.attach(part2)

    with smtplib.SMTP(smtp_server, port) as server:
        #server.ehlo()  # Can be omitted
        server.starttls(context=context)
        #server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    print('message send sucessfully')


# In[42]:



#Sending email Main code 
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd
from email import encoders
from email.mime.base import MIMEBase
from string import Template
import time
import re
def email_func(email,Name):
    port = 587
    smtp_server = "vgipl.in"
    sender_email = "virtualdigital@vgipl.in"
    receiver_email = email
    password = 'Virtual%08' #input("Type your password and press enter:")

    context = ssl.create_default_context() ##

    message = MIMEMultipart("alternative")
    message["Subject"] = "e-Banker Core Banking Solutions for Nidhi Companys"
    message["From"] = "Virtual Galaxy Infotech Pvt.Ltd <{}>".format(str(sender_email))
    message["To"] = receiver_email
   
    fname = r"D:\Python_Project\py\web_scraping\Email_Send\nidhi_email_page_02.html"
    html_file = open(fname, 'r', encoding='utf-8')
    source_code = html_file.read() 
    html_ = Template((source_code)).safe_substitute(code="Hello  " +Name)#read_data['Name'][i]

    part2 = MIMEText(html_, "html")

    message.attach(part2)
    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=context)
        
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print('message send sucessfully')
    except Exception as e:
        print(e)

#Code for function calling and Email validations
Invalid_Email=[]
Sending_Email=[]
try:
    read_data=pd.read_excel('D:\Python_Project\py\web_scraping\Email_Send\Testing Data.xlsx')
    for i in range(len(read_data)):
        print('this is the name',read_data['Name'][i])
        print('this is the email',read_data['Email'][i])
        # Make a regular expression
        # for validating an Email
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.match(regex, read_data['Email'][i])):
            email_func(read_data['Email'][i],read_data['Name'][i])
            sender_email.append(read_data['Email'][i])
    
        else:
            Invalid_Email.append(read_data['Email'][i])
except Exception as e:
    print(e)
finally:
    invalid_df=pd.DataFrame(Invalid_Email,columns=['Invalid_EmailId'])
    invalid_df.to_excel('Invalid_email_id.xlsx',index=False)
    Sending_Email_df=pd.DataFrame(Sending_Email,columns=['Sending_Email'])
    Sending_Email_df.to_excel('Sending_Email_id.xlsx',index=False)


# In[30]:


# #Code for convertion of  pdf file into the Excel file 
# # importing required modules
# import PyPDF2
 
# # creating a pdf file object
# pdfFileObj = open(r'D:\Python_Project\py\Dataset&Report\LIST-OF-SACCOS-AUDITED.pdf', 'rb')
 
# # creating a pdf reader object
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# Saccos_name=[]
# for i in range(0,68):
   
#     # creating a page object
#     pageObj = pdfReader.getPage(i)

#     # extracting text from page
#     A=(pageObj.extractText())
#     chunks = A.split('\n')
#     for j in range(len(chunks)):
#         #print(chunks[j])
#         if 'SACCO' in chunks[j]:
#             Saccos_name.append(chunks[j])

# import pandas as pd
# read_data=pd.Series(Saccos_name)
# read_data.to_csv(r'D:\Python_Project\py\web_scraping\Email_Send\email_send\Saccos_pdf_data.csv',index=False)


# # In[ ]:




