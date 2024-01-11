# coding=utf-8
import sqlite3
import sys
import re
from model import Model
from housebelongs import Housebelongs
from celeb import Celeb
class House(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists house(
        id integer primary key autoincrement,
        pic text
                    );""")
        self.con.commit()
        self.dbCeleb=Celeb()
        self.dbHousebelongs=Housebelongs()
    def getallbypic(self,pic):
        self.cur.execute("select * from house where pic = ?",(pic,))

        row=self.cur.fetchall()
        return row
    def getall(self):
        self.cur.execute("select * from house")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from house where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyid(self,myid):
        self.cur.execute("select * from house where id = ?",(myid,))
        row=dict(self.cur.fetchone())
        print(row["id"], "row id")
        job=self.cur.fetchall()
        return row
    def create(self,params):
        print("ok")
        myhash={}
        print("M Y H A S H")
        print(myhash,myhash.keys())
        myid=None
        monhash={"pic":str(params["pic"])}
        c={"name":str(params["name"]),"pic":""}
        celeb=self.dbCeleb.create(c)

        try:
          pics=self.getallbypic(monhash["pic"])
          if len(pics) == 0:
            self.cur.execute("insert into house (pic) values (:pic)",monhash)
            self.con.commit()
            myid=str(self.cur.lastrowid)
          else:
            myid=pics[0]["id"]
        except Exception as e:
          print("my error"+str(e))
        hey=self.dbHousebelongs.create({"celeb_id": celeb["celeb_id"],"house_id": myid})
        azerty={}
        azerty["house_id"]=myid
        azerty["notice"]="votre house a été ajouté"
        return azerty




