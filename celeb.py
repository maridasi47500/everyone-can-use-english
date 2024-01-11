# coding=utf-8
import sqlite3
import sys
import re
from model import Model
class Celeb(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists celeb(
        id integer primary key autoincrement,
        name text,
            pic text
                    );""")
        self.con.commit()
        #self.con.close()
    def getallbyname(self,name):
        self.cur.execute("select * from celeb where name = ?",(name,))

        row=self.cur.fetchall()
        return row
    def getall(self):
        self.cur.execute("select * from celeb")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from celeb where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyid(self,myid):
        self.cur.execute("select * from celeb where id = ?",(myid,))
        row=dict(self.cur.fetchone())
        print(row["id"], "row id")
        job=self.cur.fetchall()
        return row
    def create(self,params):
        print("ok")
        myhash={"name":params["name"],"pic":""}
        myid=None
        try:
          w=self.getallbyname(params["name"])
          if len(w) == 0:
            self.cur.execute("insert into celeb (name,pic) values (:name,:pic)",myhash)
            self.con.commit()
            myid=str(self.cur.lastrowid)
          else:
            myid=str(w[0]["id"])
        except Exception as e:
          print("my error"+str(e))
        azerty={}
        azerty["celeb_id"]=myid
        azerty["notice"]="votre celeb a été ajouté"
        return azerty




