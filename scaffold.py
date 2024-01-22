# -*- coding: utf-8 -*-

import sys
import os
print(sys.argv[1])


filename=sys.argv[1].lower()
myclass=(filename).capitalize()
modelname=(filename).capitalize()
marouteget="\"/%s\"" % filename
maroutenew="\"/%s_new\"" % filename
maroutecreate="\"/%s_create\"" % filename
marouteget2="\\\"/%s\\\"" % filename
myhtml="my"+filename+"html"
myfavdirectory=filename
index = 2 
createtable=""
columns="("
values="("
myparam=","
items=sys.argv
formulaire="<form method=\"post\" action=\"/create_"+items[1]+"\">"
myitem="<div class=\"my_"+items[1]+"\">"
pageindex="<h1>tous les "+items[1]+"</h1>"
pageindex="<ul>"
pageindex="<%=render_collection(collection=params['{hey}'], partial='{hey}/_{hey}.html', as_='book')%>".format(hey=items[1])
pageindex="</ul>"
while index < (len(items)):

    try:
      print(index, items[index])
      paramname=items[index]
      print(items[(index+1)])
    except:
      myparam=""
    index += 1
    columns+="{paramname}{myparam}".format(myparam=myparam,paramname=paramname)
    values+=":{paramname}{myparam}".format(myparam=myparam,paramname=paramname)
    formulaire+="\r\n<div class=\"field\">"
    formulaire+="\r\n<label for=\"champ_{hey}_{paramname}\">{paramname}</label>".format(hey=filename,paramname=paramname)
    formulaire+="\r\n<input type=\"text\" id=\"champ_{hey}_{paramname}\" name=\"{paramname}\" />".format(hey=filename,paramname=paramname)
    formulaire+="\r\n</div>"
    myitem+="\r\n<div class=\"hey\">"
    myitem+="\r\n<b>{paramname}:</b>".format(paramname=paramname)
    myitem+="\r\n<%=hey['{paramname}']%>".format(hey=filename,paramname=paramname)
    myitem+="\r\n</div>"

    createtable+="""        {paramname} text{myparam}
    """.format(myparam=myparam,paramname=paramname)
formulaire+="\r\n<div class=\"actions\">"
formulaire+="\r\n<input type=\"submit\" id=\"valider_{paramname}\" value=\"creer {paramname}\" name=\"valider_{paramname}\"/>".format(paramname=filename)
formulaire+="\r\n</div>"
formulaire+="\r\n</form>"
myitem+="\r\n</div>"
columns+=")"
values+=")"
mystr="""# coding=utf-8
import sqlite3
import sys
import re
from model import Model
class {modelname}(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute(\"\"\"create table if not exists {filename}(
        id integer primary key autoincrement,
"""
mystr+=createtable

mystr+="""                );\"\"\")
        self.con.commit()
        #self.con.close()
    def getall(self):
        self.cur.execute("select * from {filename}")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

"""
mystr+="""        self.cur.execute("delete from {filename} where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyid(self,myid):
        self.cur.execute("select * from {filename} where id = ?",(myid,))
        row=dict(self.cur.fetchone())
        print(row["id"], "row id")
        job=self.cur.fetchall()
        return row
    def create(self,params):
        print("ok")
        myhash={myhash}
        for x in params:
            if 'confirmation' in x:
                continue
            if 'envoyer' in x:
                continue
            if '[' not in x and x not in ['routeparams']:
                #print("my params",x,params[x])
                try:
                  myhash[x]=str(params[x].decode())
                except:
                  myhash[x]=str(params[x])
        print("M Y H A S H")
        print(myhash,myhash.keys())
        myid=None
        try:
          self.cur.execute("insert into {filename} {columns} values {values}",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        azerty={notice}
        azerty["{filename}_id"]=myid
        azerty["notice"]="votre {filename} a été ajouté"
        return azerty




"""
if not os.path.isfile(filename+".py"):
  f = open(filename+".py", "w") 
  res=(mystr.format(modelname=modelname,filename=filename,columns=columns,values=values,myhash={},notice={}))
  print(res)
  f.write(res)
  f.close()
if not os.path.isfile("form_new_"+filename+".html"):
  f = open("form_new_"+filename+".html", "w") 
  f.write(formulaire)
  f.close()
if not os.path.isfile("all_"+filename+".html"):
  f = open("all_"+filename+".html", "w") 
  f.write(pageindex)
  f.close()
if not os.path.isfile("_"+filename+".html"):
  f = open("_"+filename+".html", "w") 
  f.write(myitem)
  f.close()


with open("./route.py", "r") as f:
  contents = f.readlines()


#index=[i for i in range(len(contents)) if "class S(BaseHTTPRequestHandler):" in contents[i]][0]
#contents.insert(index, scriptfunc.format(myfavdirectory=myfavdirectory,myclass=filename,myhtml=myhtml))
#contents.insert(1, "global {myclass}\n".format(myclass=filename))
#contents.insert(1, "import {myclass}\n".format(myclass=filename))
#contents.insert(1, "from {myclass} import {myclass}page\n".format(myclass=filename))
#myrouteget="\"/{myclass}\":{myclass}func,\n"
#index=[i for i in range(len(contents)) if "myroutes = {" in contents[i]][0]
#contents.insert((index+1), myrouteget.format(myclass=filename))
#index=[i for i in range(len(contents)) if "def reloadmymodules" in contents[i]][0]
#contents.insert((index+1), "    reload({myclass})\n".format(myclass=filename))
#index=[i for i in range(len(contents)) if "__mots__={" in contents[i]][0]
#contents.insert((index+1), "    \"/{myclass}\":{\"partiedemesmots\":\"{myclass}\"},\n".replace("{myclass}",filename))

#with open("./script.py", "w") as f:
#    contents = "".join(contents)
#    f.write(contents)

#os.system("mkdir %s" % myfavdirectory)
#pathhtml="%s/%s.html" % (myfavdirectory, myhtml)
#os.system("touch %s" % pathhtml)

#if os.path.isfile(pathhtml):
#    with open(pathhtml, "w") as f:
#        urlayout="""<h1>Layout de la route {myclass}</h1>
#<p><a href="{marouteget}">nous sommes ici (essayez ce lien)</a></p>
#<p>Entrez du texte sur cette page</p>
#"""
#          f.write(urlayout.format(marouteget=marouteget,myclass=filename))
#
#  #print("ma route get %s a été ajoutée. Maintenant vous pouvez essayer d'y acceder" % marouteget)
