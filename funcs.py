import urllib.request
import json
import re

def getData(usr):
    if(bool(re.search('[а-яА-Я]', usr))):
        result = result = 'Извините, Ваш идентификатор не записан в базу данных SocShield.'
    else:
        link = "https://www.socshield.online/telegram/tmain.php?hu="+usr
        response = urllib.request.urlopen(link)
        data = json.loads(response.read())

        if (data['lastname']==''):
            link = "https://www.socshield.online/telegram/tmainshort.php?hu="+usr
            response = urllib.request.urlopen(link)
            data = json.loads(response.read())
            if(data['lastname']==''):
                result = 'Извините, Ваш идентификатор не записан в базу данных SocShield.'
            else:
                result = 'Здравствуйте, '+data['lastname']+' '+data['firstname']+' '+data['patronymic']+'! Ваш документ документ истек. Обратитесь в ближайший отдел медико-социальной экспертизы для выдачи нового документа.'
        else:
            result = 'Здравствуйте, '+data['lastname']+' '+data['firstname']+' '+data['patronymic']+'! Ваш документ '+data['docnum']+' действителен до '+data['edate']+'.'
    return result

def getPension(usr):

    if(bool(re.search('[а-яА-Я]', usr))):
        result = result = 'Извините, Ваш идентификатор не записан в базу данных SocShield.'
    else:
        link = "https://www.socshield.online/telegram/tsocial.php?hu="+usr
        response = urllib.request.urlopen(link)
        data = json.loads(response.read())
        if(data['pension']!=None):
            result = 'Назначенное государственное пособие составляет '+data['pension']+' тенге.'
        else: result = 'Срок Вашего документа истек или идентификатор SocShield недействиелен'
    return result

def getHelp(usr):
    if(bool(re.search('[а-яА-Я]', usr))):
        result = result = 'Извините, Ваш идентификатор не записан в базу данных SocShield.'
    else:
        link = "https://www.socshield.online/telegram/thelp.php?hu="+usr
        response = urllib.request.urlopen(link)
        data = json.loads(response.read())
        if(data['status']=='Инвалид I группы' or data['status']=='Инвалид детства I группы'): page = 'inv1.php'
        elif(data['status']=='Инвалид II группы' or data['status']=='Инвалид детства II группы'): page = 'inv2.php'
        elif(data['status']=='Инвалид III группы' or data['status']=='Инвалид детства III группы'): page = 'inv3.php'
        elif(data['status']=='Ребенок-инвалид'): page = 'dinv.php'
        else: page = ''

        if(page!=''): result = 'https://www.socshield.online/pages/infopages/'+page
        else: result = ''
    return result