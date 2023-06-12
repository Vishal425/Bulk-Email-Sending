
# # Create your views here.
# from django.shortcuts import render
# from django.views.generic.edit import CreateView
# from django.urls import reverse_lazy
# from .models import Upload
# class UploadView(CreateView):
#     model = Upload
#     fields = ['upload_file', ]
#     success_url = reverse_lazy('fileupload')
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['documents'] = Upload.objects.all()
#         return context



from django.shortcuts import render, redirect

from .forms import TutorialForm

from .models import Tutorial

from io import StringIO

import pandas as pd

#from .models import Tutorial

from django.db import connection

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd
from email import encoders
from email.mime.base import MIMEBase
from string import Template
import time
import re


import logging
logger = logging.getLogger(__name__)

def tutorialList(request):
    tutorials = Tutorial.objects.all()
    return render(request, r'C:\Users\vishal.lote\Desktop\Project Reports\reports\Email_Send\email_send\file_upload\templates\file_upload\list.html', { 'tutorials' : tutorials})

def uploadTutorial(request):
    try:
        if request.method == 'POST':  
            form = TutorialForm(request.POST, request.FILES)
            
            if form.is_valid():

                #Taking the HTML and EXCEL files from POST request 
                
                # sql_query = request.POST['title'] #Sql query from title form  

                # print(sql_query)
 
                # dfs=pd.read_sql_query(sql_query,connection)

                # print(dfs.head(10))

   
                                   

                html_raw_data=request.FILES.get('feature_image').read().decode("utf-8") 

                excel_raw_data = pd.read_excel(request.FILES.get('attachment'))


                #Sending mail using above file request

                #Sending email Main code 

                def email_func(email,Name):
                    port = 587
                    # port = 465
                    smtp_server = "vgipl.in"
                    # smtp_server = "smtp.gmail.com"

                    # sender_email = "virtualgalaxyinfotechpvtltd@gmail.com"
                    sender_email = "virtualdigital@vgipl.in"
                    receiver_email = email
                    password = 'VgiplDM#1997'#input("Type your password and press enter:")#virtualgalaxyinfotechpvtltd@gmail.com#Virtual$1997galaxy
                    # password = 'tcwuzkqhttaoigkh'#input("Type your password and press enter:")
                    # sender_email ="prashant.nagmote@vgipl.in"
                    # receiver_email = email
                    # password = 'Virtual@%09'#Virtual%08' #input("Type your password and press enter:")

                    context = ssl.create_default_context() ##we used this line only other port not gmail server

                    message = MIMEMultipart("alternative")
                    message["Subject"] = "e-Banker Core Banking Solution for Nidhi Company"
                    message["From"] = "Virtual Galaxy Infotech Pvt. Ltd <{}>".format(str(sender_email))
                    message["To"] = receiver_email
                
                    #Providing Html file  
                    fname = html_raw_data
                    # html_file = open(fname, 'r', encoding='utf-8')
                    # source_code = html_file.read() 
                   
                    # html_ = Template((fname)).safe_substitute(code="Hello  " +Name)#read_data['Name'][i]
                    html_ = Template((fname)).safe_substitute(code=" ")#read_data['Name'][i]

                    part2 = MIMEText(html_, "html")

                    message.attach(part2)
                    try:
                        with smtplib.SMTP(smtp_server ,port) as server:
                            server.starttls(context=context)
                        
                        # server = smtplib.SMTP('smtp.gmail.com: 587')
                        # server.ehlo()
                        # server.starttls()
                        # # Perform operations via server
                        # server.login(sender_email, password)
                        # server.sendmail(sender_email, receiver_email, message.as_string())
                        # server.close()                    
                            server.login(sender_email, password)
                            server.sendmail(sender_email, receiver_email, message.as_string())
                        print('message send sucessfully')
                    except Exception as e:
                        logging.error(e)

                    

                #Code for function calling and Email validations
                Invalid_Email=[]
                try:
                    read_data=excel_raw_data
                    for i in range(len(read_data)):
                        print('this is the name',read_data['Name'][i])
                        print('this is the email',read_data['Email'][i])

                        # Make a regular expression for validating an Email
                        try:
                            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                            if (re.match(regex, read_data['Email'][i])):
                                email_func(read_data['Email'][i],read_data['Name'][i])
                                
                            else:
                                Invalid_Email.append(read_data['Email'][i])
                        except Exception as e:
                            logging.error(e)

                except Exception as e:
                    logging.error(e)

                finally:
                    invalid_df=pd.DataFrame(Invalid_Email,columns=['Invalid_EmailId'])
                    invalid_df.to_excel('Invalid_email_id_'+str(i)+'.xlsx',index=False)                 
                    
                #
                form.save()
                return redirect('tutorial_list')
        else:
            form = TutorialForm()
        return render(request, r'C:\Users\vishal.lote\Desktop\Project Reports\reports\Email_Send\email_send\file_upload\templates\file_upload\upload.html', {'form' : form})
    
    except Exception as e:
        logging.error(e)



def deleteTutorial(request, pk):
    try:
        if request.method == 'POST':
            tutorial = Tutorial.objects.get(pk=pk)
            tutorial.delete()
        return redirect('tutorial_list')
    except Exception as e:
        logging.error(e)


#

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'