from flask import Flask,request,jsonify,current_app
from flask_cors import CORS, cross_origin
import requests
import json
import xml.etree.ElementTree as ET
app = Flask(__name__)
CORS(app)



@app.route('/Getservice',methods=['POST'])
def Getservice():
    payload = ("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<request action=\"GET\" version=\"1.0\">\n <customer>\n \t<name>CSP</name>\n  " +
          "<service>\n\t  <name>HostedAppsandDesktops</name>\n\t  \n    </service>\n </customer>\n</request>")
    response = requests.request("POST", url, data=payload, headers=headers)
    root = ET.fromstring(response.text)
    i=1
    name=[]
    types=[]
    json =[]
    for test in root.findall('customer/service/offerings/offering') :
        name.append(test.find('name').text.replace("-SharedServer",""))
        types.append(test.find('type').text)
    return jsonify({"name": name, "type": types})

@app.route('/provisionappcus',methods=['POST'])
def provisionappcus():
    data = request.json
    customername = data['cus']
    app = data['app']
    payload = """<?xml version=\"1.0\" encoding=\"utf-8\"?>
\r\n<request action=\"SET\" version=\"1.0\">
\r\n <customer>
\r\n \t<name>"""+customername+"""</name>
\r\n    <service>
\r\n\t  <name>HostedAppsandDesktops</name>
\r\n\t  <offerings>"""
    services = ''
    for service in app :
      services +="""<offering><name>"""+service+"""-SharedServer</name><displayname>"""+service+"""</displayname><type>Citrix App</type><enabled>True</enabled></offering> """
    tail = """</offerings></service></customer></request>"""
    payload += services + tail
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text

@app.route('/provisionappuser',methods=['POST'])
def provisionappuser():
    data = request.json
    customername = data['cus']
    username = data['user']
    app = data['app']
    payload = """<?xml version=\"1.0\" encoding=\"utf-8\"?>
\r\n<request action=\"SET\" version=\"1.0\">
\r\n <customer>
\r\n \t<name>"""+customername+"""</name>
\r\n \t<user>
\r\n\t\t<name>"""+username+"""</name>
\r\n    <service>
\r\n\t  <name>HostedAppsandDesktops</name>
\r\n\t  <offerings>"""
    services = ''
    for service in app :
      services +="""<offering><name>"""+service+"""-SharedServer</name><displayname>"""+service+"""</displayname><type>Citrix App</type><enabled>True</enabled></offering> """
    tail = """</offerings></service></user></customer></request>"""
    payload += services + tail
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text

@app.route('/de-provisionappcus',methods=['POST'])
def deprovisionappcus():
    data = request.json
    customername = data['cus']
    app = data['app']
    payload = """<?xml version=\"1.0\" encoding=\"utf-8\"?>
\r\n<request action=\"SET\" version=\"1.0\">
\r\n <customer>
\r\n \t<name>"""+customername+"""</name>
\r\n    <service>
\r\n\t  <name>HostedAppsandDesktops</name>
\r\n\t  <offerings>"""
    services = ''
    for service in app :
      services +="""<offering><name>"""+service+"""-SharedServer</name><displayname>"""+service+"""</displayname><type>Citrix App</type><enabled>False</enabled></offering> """
    tail = """</offerings></service></customer></request>"""
    payload += services + tail
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text

@app.route('/de-provisionappuser',methods=['POST'])
def deprovisionappuser():
    data = request.json
    customername = data['cus']
    username = data['user']
    app = data['app']
    payload = """<?xml version=\"1.0\" encoding=\"utf-8\"?>
\r\n<request action=\"SET\" version=\"1.0\">
\r\n <customer>
\r\n \t<name>"""+customername+"""</name>
\r\n \t<user>
\r\n\t\t<name>"""+username+"""</name>
\r\n    <service>
\r\n\t  <name>HostedAppsandDesktops</name>
\r\n\t  <offerings>"""
    services = ''
    for service in app :
      services +="""<offering><name>"""+service+"""-SharedServer</name><displayname>"""+service+"""</displayname><type>Citrix App</type><enabled>False</enabled></offering> """
    tail = """</offerings></service></user></customer></request>"""
    payload += services + tail
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text

@app.route('/deletecus',methods=['POST'])
def deletecus():
    data = request.json
    customername = data['cus']
    payload = """<?xml version=\"1.0\" encoding=\"utf-8\"?>
\r\n<request action=\"DELETE\" version=\"1.0\">
\r\n <customer>
\r\n \t<name>""" + customername + """</name>
\r\n </customer>
\r\n</request>"""

    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text

@app.route('/deleteuser',methods=['POST'])
def deletecuser():
    data = request.json
    customername = data['cus']
    username = data['user']

    payload = """<?xml version=\"1.0\" encoding=\"utf-8\"?>
\r\n<request action=\"DELETE\" version=\"1.0\">
\r\n <customer>
\r\n \t<name>""" + customername + """</name>
\r\n \t<user>
\r\n\t\t<name>"""+username+"""</name>
\r\n    </user>
\r\n </customer>
\r\n</request>"""

    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text


@app.route('/createcus',methods=['POST'])
def createcus():
    data = request.json
    customername = data['cus']
    fullname = data['full']
    disable_app = ''
    payload = ("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<request action=\"GET\" version=\"1.0\">\n <customer>\n \t<name>CSP</name>\n  " +
              "<service>\n\t  <name>HostedAppsandDesktops</name>\n\t  \n    </service>\n </customer>\n</request>")
    response = requests.request("POST", url, data=payload, headers=headers)
    root = ET.fromstring(response.text)
    for test in root.findall('customer/service/offerings/offering') :
        name = test.find('name').text
        type = test.find('type').text
        # print name, type
        disable_app += ("<offering>\n\t<name>" + name + "</name>\n\t<displayname>" + name.replace("-SharedServer","") + "</displayname>\n\t<type>" + type + """</type>
        <default>True</default>
        <enabled>False</enabled>
        <inuse>False</inuse>
    </offering>\n""")

    disable_app_head = """<service><name>HostedAppsandDesktops</name><offerings>\n"""

    disable_app_last = """</offerings>
    </service>"""

    test = disable_app_head + disable_app + disable_app_last
    text = """<?xml version=\"1.0\" encoding=\"utf-8\"?>\r\n
    <request action=\"set\" version=\"1.0\">\r\n
    <customer>\r\n
    \t    <fullname>"""+fullname+"""</fullname>\r\n
          <name>"""+customername+"""</name>\r\n  
          <code>"""+customername+"""</code>\r\n      
          <contactname>Admin"""+customername+"""</contactname>\r\n        
          <contactemail>Admin"""+customername+"""@"""+customername+""".local</contactemail>\r\n        
          <primarydomain>"""+customername+""".local</primarydomain> 
          """

    payload = text + "" + test + """\r\n</customer>\r\n</request>"""
    # print payload
    response = requests.request("POST", url, data=payload, headers=headers)

    # response = requests.request("POST", url, data=payload, headers=headers)
    return response.text

@app.route('/createuser',methods=['POST'])
def createuser():
    data = request.json
    customername = data['cus']
    fullname = data['full']
    num = int(data['user'])
    if len(customername) > 3 :
      username = customername[0]+customername[1]+customername[2]
    else:
      username = customername
    disable_app = ''
    payload = ("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<request action=\"GET\" version=\"1.0\">\n <customer>\n \t<name>CSP</name>\n  " +
              "<service>\n\t  <name>HostedAppsandDesktops</name>\n\t  \n    </service>\n </customer>\n</request>")
    response = requests.request("POST", url, data=payload, headers=headers)
    root = ET.fromstring(response.text)
    for test in root.findall('customer/service/offerings/offering') :
        name = test.find('name').text
        type = test.find('type').text
        # print name, type
        disable_app += ("<offering>\n\t<name>" + name + "</name>\n\t<displayname>" + name.replace("-SharedServer","") + "</displayname>\n\t<type>" + type + """</type>
        <default>True</default>
        <enabled>False</enabled>
        <inuse>False</inuse>
    </offering>\n""")

    disable_app_head = """<service><name>HostedAppsandDesktops</name><offerings>\n"""

    disable_app_last = """</offerings>
    </service>"""

    test = disable_app_head + disable_app + disable_app_last
    text = """<?xml version=\"1.0\" encoding=\"utf-8\"?>\r\n
    <request action=\"set\" version=\"1.0\">\r\n
    <customer>\r\n
    \t    <fullname>"""+fullname+"""</fullname>\r\n
          <name>"""+customername+"""</name>\r\n    
          <contactname>Admin"""+customername+"""</contactname>\r\n        
          <contactemail>Admin"""+customername+"""@"""+customername+""".local</contactemail>\r\n        
          <primarydomain>"""+customername+""".local</primarydomain> 
          """
    user = ""
    for i in range(num):
        user = user+"""\r\n
        <user>\r\n
          \t<name>"""+username+"""%02d</name>\r\n
          \t<password>\r\n
            \t<password>Hello%02d</password>\r\n
            \t<changeatnextlogon>False</changeatnextlogon>\r\n
          </password>\r\n
        </user>""" % ((i+1),(i+1))

    payload = text + "" + user + "" + test + """\r\n</customer>\r\n</request>"""
    # print payload
    response = requests.request("POST", url, data=payload, headers=headers)

    # response = requests.request("POST", url, data=payload, headers=headers)
    return response.text


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',threaded=True)
