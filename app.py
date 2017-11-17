from flask import Flask,request,jsonify,current_app
from flask_cors import CORS, cross_origin
import requests
import json
import xml.etree.ElementTree as ET
app = Flask(__name__)
CORS(app)

url = "http://apicpsm.inet.co.th/CortexAPI/Default.aspx"
headers = {
    'authorization': "Basic Y2xvdWRhZG1pbl9jc3A6VkQxQGRtMW4=",
    'content-type': "application/xml",
    'cache-control': "no-cache",
    'postman-token': "30d50e5a-b18b-1c02-2595-c268a10baad2"
    }


@app.route('/Getuser',methods=['POST'])
def Getuser():
    data = request.json
    customername = data['cus']
    payload = """<?xml version=\"1.0\" encoding=\"utf-8\"?>\r\n<request action=\"find\" version=\"1.0\">\r\n <customer>\r\n \t<name>"""+customername+"""</name>\r\n \t<user/>\r\n \t</customer>\r\n</request>"""
    response = requests.request("POST", url, data=payload, headers=headers)
    root = ET.fromstring(response.text)
    # i=1
    json = []
    for test in root.findall('customer/user') :
        json.append({"name": test.find('name').text, 
            "fullname": test.find('fullname').text,
            "id": test.find('id').text,
            "upn": test.find('upn').text,
            "status": test.find('status').text,
            "approvalpending": test.find('approvalpending').text,
            })
        # name.append(test.find('name').text)
        # fullname.append(test.find('fullname').text)
    # print json
    return jsonify({"data": json})

@app.route('/GetCustomer',methods=['POST'])
def GetCustomer():
    payload = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\r\n<request action=\"find\" version=\"1.0\">\r\n <customer/>\r\n</request>"
    response = requests.request("POST", url, data=payload, headers=headers)
    root = ET.fromstring(response.text)
    # i=1
    name=[]
    fullname=[]
    ID=[]
    primarydomain=[]
    status=[]
    approvalpending=[]
    json = []
    for test in root.findall('customer') :
        json.append({"name": test.find('name').text, 
            "fullname": test.find('fullname').text,
            "id": test.find('id').text,
            "primarydomain": test.find('primarydomain').text,
            "status": test.find('status').text,
            "approvalpending": test.find('approvalpending').text,
            })
        # name.append(test.find('name').text)
        # fullname.append(test.find('fullname').text)
    # print json
    return jsonify({"data": json})

@app.route('/Getservicecus',methods=['POST'])
def Getservicecus():
    # customername = 'jam'
    data = request.json
    customername = data['cus']
    # payload = """<?xml version=\"1.0\" encoding=\"utf-8\"?>
    # \r\n<request action=\"GET\" trace=\"false\"  version=\"1.0\">\r\n 
    # <customer>\r\n \t<name>"""+customername+"""</name>\r\n   <!-- <user>-->\r\n\t  <!--<name>user01_tacom</name>-->\r\n\t  <!--<service>-->\r\n\t  <!--\t<name>reseller</name>-->\r\n\t  \t<service>\r\n                <name>HostedAppsandDesktops</name>\r\n\t  \t<offerings>\r\n\t  \t\t<offering/>\r\n\t  \t</offerings>\r\n\t  \t</service>\r\n\t  <!--</service>-->\r\n    <!--</user>-->\r\n </customer>\r\n</request>"""
    payload = """<?xml version=\"1.0\" encoding=\"utf-8\"?>
    \r\n<request action=\"GET\" trace=\"false\"  version=\"1.0\">\r\n 
    <customer>\r\n \t<name>"""+customername+"""</name>\r\n\t  \t<service>\r\n                
    <name>HostedAppsandDesktops</name>\r\n\t  \t<offerings>\r\n\t  
    \t\t<offering/>\r\n\t  \t</offerings>\r\n\t  \t</service>\r\n 
    </customer>\r\n</request>"""

    response = requests.request("POST", url, data=payload, headers=headers)
    root = ET.fromstring(response.text)
    i=1
    name=[]
    types=[]
    desktop =[]
    app = []
    for test in root.findall('customer/service/offerings/offering') :
        # name.append(test.find('displayname').text.replace("-SharedServer",""))
        # types.append(test.find('type').text)
        if('Windows' in test.find('name').text) :
            desktop.append({"name": test.find('name').text,
                "displayname": test.find('displayname').text,
                "enabled": test.find('enabled').text
                })
        else :
            app.append({"name": test.find('name').text,
                "displayname": test.find('displayname').text,
                "enabled": test.find('enabled').text
                })
    # print desktop
        # print('Windows' in test.find('name').text)
    return jsonify({"datadesktop": desktop, "dataapp": app, "lengthDesk": len(desktop)})
    # return response.text

@app.route('/GetservicecusforDe',methods=['POST'])
def GetservicecusforDe():
    # customername = 'jam'
    data = request.json
    customername = data['cus']
    # payload = """<?xml version=\"1.0\" encoding=\"utf-8\"?>
    # \r\n<request action=\"GET\" trace=\"false\"  version=\"1.0\">\r\n 
    # <customer>\r\n \t<name>"""+customername+"""</name>\r\n   <!-- <user>-->\r\n\t  <!--<name>user01_tacom</name>-->\r\n\t  <!--<service>-->\r\n\t  <!--\t<name>reseller</name>-->\r\n\t  \t<service>\r\n                <name>HostedAppsandDesktops</name>\r\n\t  \t<offerings>\r\n\t  \t\t<offering/>\r\n\t  \t</offerings>\r\n\t  \t</service>\r\n\t  <!--</service>-->\r\n    <!--</user>-->\r\n </customer>\r\n</request>"""
    payload = """<?xml version=\"1.0\" encoding=\"utf-8\"?>
    \r\n<request action=\"GET\" trace=\"false\"  version=\"1.0\">\r\n 
    <customer>\r\n \t<name>"""+customername+"""</name>\r\n\t  \t<service>\r\n                
    <name>HostedAppsandDesktops</name>\r\n\t  \t<offerings>\r\n\t  
    \t\t<offering/>\r\n\t  \t</offerings>\r\n\t  \t</service>\r\n 
    </customer>\r\n</request>"""

    response = requests.request("POST", url, data=payload, headers=headers)
    root = ET.fromstring(response.text)
    i=1
    name=[]
    types=[]
    desktop =[]
    app = []
    for test in root.findall('customer/service/offerings/offering') :
        # name.append(test.find('displayname').text.replace("-SharedServer",""))
        # types.append(test.find('type').text)
        if (test.find('enabled').text == 'True'):
            if('Windows' in test.find('name').text) :
                desktop.append({"name": test.find('name').text,
                    "displayname": test.find('displayname').text,
                    "inuse": test.find('inuse').text
                    })
            else :
                app.append({"name": test.find('name').text,
                    "displayname": test.find('displayname').text,
                    "inuse": test.find('inuse').text
                    })
    # print desktop
        # print('Windows' in test.find('name').text)
    return jsonify({"datadesktop": desktop, "dataapp": app, "lengthDesk": len(desktop)})
    # return response.text

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
        # name.append(test.find('displayname').text.replace("-SharedServer",""))
        # types.append(test.find('type').text)
        
        json.append({"name": test.find('name').text,
            "displayname": test.find('displayname').text
            })
    return jsonify({"data": json})

@app.route('/GetserviceAll',methods=['POST'])
def GetserviceAll():
    payload = ("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<request action=\"GET\" version=\"1.0\">\n <customer>\n \t<name>CSP</name>\n  " +
          "<service>\n\t  <name>HostedAppsandDesktops</name>\n\t  \n    </service>\n </customer>\n</request>")
    response = requests.request("POST", url, data=payload, headers=headers)
    root = ET.fromstring(response.text)
    # i=1
    dataIn =[]
    desktopIn =[]
    data = []
    desktop =[]
    i = 0
    k=0
    for test in root.findall('customer/service/offerings/offering') :
        # name.append(test.find('displayname').text.replace("-SharedServer",""))
        # types.append(test.find('type').text)
        if (not('Windows' in test.find('name').text)) :
            dataIn.append({"name": test.find('name').text,
              "displayname": test.find('displayname').text,
              "pic": '../../static/'+test.find('displayname').text+'.png'
              })
            i=i+1
        else :
            desktopIn.append({"name": test.find('name').text,
              "displayname": test.find('displayname').text
              })
            k = k+1

        if (dataIn !=[] and ((i-k)%8 == 7 and (i-k)!= 0) or (i-k) == len(root.findall('customer/service/offerings/offering'))-1-k) :
            data.append(dataIn)
            dataIn = []
        if (desktopIn !=[] and (k%8 ==7 and k !=0) or (i-k) == len(root.findall('customer/service/offerings/offering'))-1-k) :
           desktop.append(desktopIn)
           desktopIn = []
    return jsonify({"data": data,"desktop": desktop})

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
      services +="""<offering><name>"""+service['name']+"""</name><displayname>"""+service['displayname']+"""</displayname><type>Citrix App</type><enabled>True</enabled></offering> """
    tail = """</offerings></service></customer></request>"""
    payload += services + tail
    response = requests.request("POST", url, data=payload, headers=headers)
    root = ET.fromstring(response.text)
    word = 'jam'
    json =[]
    status = 'complete'
    for test in root.findall('error') :
        # name.append(test.find('displayname').text.replace("-SharedServer",""))
        # types.append(test.find('type').text)
        status = 'fail'
        json.append({"id": test.find('id').text,"message": test.find('message').text})
    return jsonify({"data": json,"status": status})

@app.route('/provisionappcuss',methods=['GET'])
def provisionappcuss():
    customername = 'jam'
    app = [{'displayname' :"7-Zip File Manager", 'name':"1_APINXCPSM_9_7-ZipFileManager"}]
    payload = """<?xml version=\"1.0\" encoding=\"utf-8\"?>
\r\n<request action=\"SET\" version=\"1.0\">
\r\n <customer>
\r\n \t<name>"""+customername+"""</name>
\r\n    <service>
\r\n\t  <name>HostedAppsandDesktops</name>
\r\n\t  <offerings>"""
    services = ''
    for service in app :
      services +="""<offering><name>"""+service['name']+"""</name><displayname>"""+service['displayname']+"""</displayname><type>Citrix App</type><enabled>True</enabled></offering> """
    tail = """</offerings></service></customer></request>"""
    payload += services + tail
    response = requests.request("POST", url, data=payload, headers=headers)
    root = ET.fromstring(response.text)
    word = 'jam'
    json =[]
    status = 'complete'
    for test in root.findall('error') :
        # name.append(test.find('displayname').text.replace("-SharedServer",""))
        # types.append(test.find('type').text)
        status = 'fail'
        json.append({"id": test.find('id').text,"message": test.find('message').text})
    return jsonify({"data": json,"status": status})


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
      services +="""<offering><name>"""+service['name']+"""</name><displayname>"""+service['displayname']+"""</displayname><type>Citrix App</type><enabled>False</enabled></offering> """
    tail = """</offerings></service></customer></request>"""
    payload += services + tail
    response = requests.request("POST", url, data=payload, headers=headers)
    root = ET.fromstring(response.text)
    word = 'jam'
    json =[]
    status = 'complete'
    for test in root.findall('error') :
        # name.append(test.find('displayname').text.replace("-SharedServer",""))
        # types.append(test.find('type').text)
        status = 'fail'
        json.append({"id": test.find('id').text,"message": test.find('message').text})
    return jsonify({"data": json,"status": status})

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

@app.route('/createcusget',methods=['GET'])
def createcusget():
    data = request.json
    customername = 'jam'
    fullname = 'jamInet'
    num = int(5)
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
        types = test.find('type').text
        display = test.find('displayname').text
        # print name, type
        disable_app += ("<offering>\n\t<name>" + name + "</name>\n\t<displayname>" + display + "</displayname>\n\t<type>" + types + """</type>
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
    current_app.logger.info(payload)
    response = requests.request("POST", url, data=payload, headers=headers)

    # text = """<?xml version=\"1.0\" encoding=\"utf-8\"?>\r\n
    # <request action=\"set\" version=\"1.0\">\r\n
    # <customer>\r\n
    # \t    <fullname>"""+fullname+"""</fullname>\r\n
    #       <name>"""+customername+"""</name>\r\n  
    #       <code>"""+customername+"""</code>\r\n      
    #       <contactname>Admin"""+customername+"""</contactname>\r\n        
    #       <contactemail>Admin"""+customername+"""@"""+customername+""".local</contactemail>\r\n        
    #       <primarydomain>"""+customername+""".local</primarydomain> 
    #       """

    # payload = text + "" + test + """\r\n</customer>\r\n</request>"""
    # # print payload
    # response = requests.request("POST", url, data=payload, headers=headers)
    # current_app.logger
    # response = requests.request("POST", url, data=payload, headers=headers)
    # return response.text
    current_app.logger.info(test)
    return test



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
        types = test.find('type').text
        display = test.find('displayname').text
        # print name, type
        disable_app += ("<offering>\n\t<name>" + name + "</name>\n\t<displayname>" + display + "</displayname>\n\t<type>" + types + """</type>
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
    # current_app.logger
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
        types = test.find('type').text
        display = test.find('displayname').text
        # print name, type
        disable_app += ("<offering>\n\t<name>" + name + "</name>\n\t<displayname>" + display + "</displayname>\n\t<type>" + types + """</type>
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
    current_app.logger.info(payload)
    response = requests.request("POST", url, data=payload, headers=headers)

    # response = requests.request("POST", url, data=payload, headers=headers)
    return response.text


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',threaded=True)
