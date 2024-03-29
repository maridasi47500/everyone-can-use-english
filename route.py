from directory import Directory
from render_figure import RenderFigure
from myscript import Myscript
from user import User
from myrecording import Myrecording
from book import Book
from phrase import Phrase
from program import Myprogram
from macroword import Macroword
from phraseatrou import Phraseatrou
from maphrase import Maphrase
from mot import Mot
from text import Text


from film import Film
from mypic import Pic
from javascript import Js
from stylesheet import Css
import re
import traceback
import sys

class Route():
    def __init__(self):
        self.dbUsers=User()
        self.Program=Directory("premiere radio")
        self.Program.set_path("./")
        self.mysession={"notice":None,"email":None,"name":None}
        self.dbScript=Myscript()
        self.dbBook=Book()
        self.dbFilm=Film()
        self.dbMot=Mot()
        self.dbPhrase=Phrase()
        self.dbText=Text()
        self.dbMaphrase=Maphrase()
        self.dbPhraseatrou=Phraseatrou()
        self.dbMacro=Macroword()
        self.execProgram=Myprogram()
        self.dbRecording=Myrecording()
        self.render_figure=RenderFigure(self.Program)
        self.getparams=("id",)
    def set_post_data(self,x):
        self.post_data=x
    def get_post_data(self):
        return self.post_data
    def set_my_session(self,x):
        print("set session",x)
        self.Program.set_my_session(x)
        self.render_figure.set_session(self.Program.get_session())
    def set_redirect(self,x):
        self.Program.set_redirect(x)
        self.render_figure.set_redirect(self.Program.get_redirect())
    def render_some_json(self,x):
        self.Program.set_json(True)
        return self.render_figure.render_some_json(x)
    def render_my_json(self,x):
        self.Program.set_json(True)
        return self.render_figure.render_my_json(x)
    def set_json(self,x):
        self.Program.set_json(x)
        self.render_figure.set_json(self.Program.get_json())
    def set_notice(self,x):
        print("set session",x)
        self.Program.set_session_params({"notice":x})
        self.render_figure.set_session(self.Program.get_session())
    def set_session(self,x):
          print("set session",x)
          self.Program.set_session(x)
          self.render_figure.set_session(self.Program.get_session())
    def get_this_get_param(self,x,params):
          print("set session",x)
          hey={}
          for a in x:
              hey[a]=params[a][0]
          return hey
          
    def get_this_route_param(self,x,params):
          print("set session",x)
          return dict(zip(x,params["routeparams"]))
          
    def logout(self,search):
        self.Program.logout()
        self.set_redirect("/")
        return self.render_figure.render_redirect()
    def chat(self,search):
        hi=self.dbScript.getall()
        self.render_figure.set_param("scripts",hi)
        return self.render_figure.render_figure("welcome/chat.html")
    def welcome(self,search):
        return self.render_figure.render_figure("welcome/index.html")
    def audio_save(self,search):
        myparam=self.get_post_data()(params=("recording",))
        hi=self.dbRecording.create(myparam)
        return self.render_some_json("welcome/hey.json")
    def allscript(self,search):
        #myparam=self.get_post_data()(params=("name","content",))
        hi=self.dbScript.getall()
        self.render_figure.set_param("scripts",hi)
        return self.render_figure.render_figure("welcome/allscript.html")
    def lancerscript(self,search):
        myparam=search["myid"][0]
        hi=self.dbScript.getbyid(myparam)
        print(hi, "my script")
        a=self.scriptpython(hi["name"]).lancer()
        return self.render_some_json("welcome/monscript.json")

    def new1(self,search):
        myparam=self.get_post_data()(params=("name","pic",))
        #x=self.dbHouse.create(myparam)
        print(hey)
        return self.render_some_json("welcome/mypic.json")
    def edit_phraseatrou(self,params):
        getparams=("id",)
        print("get param, action see my new",getparams)
        myparam=self.get_this_route_param(getparams,params)
        x=self.dbPhraseatrou.getbyid(myparam["id"])
        self.render_figure.set_param("phraseatrou",x)
        return self.render_figure.render_figure("phraseatrou/form_edit_phraseatrou.html")
    def edit_phrase(self,params):
        getparams=("id",)
        print("get param, action see my new",getparams)
        myparam=self.get_this_route_param(getparams,params)
        x=self.dbPhrase.getbyid(myparam["id"])
        self.render_figure.set_param("phrase",x)
        return self.render_figure.render_figure("phrase/editphrase.html")
    def voir_livre(self,params):
        getparams=("id",)
        print("get param, action see my new",getparams)
        myparam=self.get_this_route_param(getparams,params)
        x=self.dbBook.getbyid(myparam["id"])
        print(x,"book")
        self.render_figure.set_param("book",x)
        return self.render_figure.render_figure("book/voirlivre.html")
    def update_phraseatrou(self,search):
        myparam=self.get_post_data()(params=("text_en","text_trou","id",))
        x=self.dbPhraseatrou.update(myparam)
        self.render_figure.set_param("redirect","/phraseatrou")
        return self.render_some_json("welcome/redirect.json")
    def update_phrase(self,search):
        myparam=self.get_post_data()(params=("text_fr","text_en","id",))
        x=self.dbPhrase.update(myparam)
        self.render_figure.set_param("redirect","/phrase")
        return self.render_some_json("welcome/redirect.json")
    def create_mot(self,search):
        myparam=self.get_post_data()(params=("mot","alphabet",))
        x=self.dbMot.create(myparam)
        self.render_figure.set_param("redirect","/api")
        return self.render_some_json("welcome/redirect.json")
    def create_maphrase(self,search):
        myparam=self.get_post_data()(params=("text",))
        x=self.dbMaphrase.create(myparam)
        self.render_figure.set_param("redirect","/maphrase")
        return self.render_some_json("welcome/redirect.json")
    def create_book(self,search):
        myparam=self.get_post_data()(params=("title","author",))
        x=self.dbBook.create(myparam)
        self.render_figure.set_param("redirect","/books")
        return self.render_some_json("welcome/redirect.json")
    def create_text(self,search):
        myparam=self.get_post_data()(params=("text","recording",))
        x=self.ddText.create(myparam)
        self.render_figure.set_param("redirect","/text")
        return self.render_some_json("welcome/redirect.json")
    def create_film(self,search):
        myparam=self.get_post_data()(params=("title","date_sortie",))
        x=self.dbFilm.create(myparam)
        self.render_figure.set_param("redirect","/films")
        return self.render_some_json("welcome/redirect.json")
    def create_phraseatrou(self,search):
        myparam=self.get_post_data()(params=("text_en","text_trou",))
        x=self.dbPhraseatrou.create(myparam)
        self.render_figure.set_param("redirect","/phraseatrou")
        return self.render_some_json("welcome/redirect.json")
    def create_phrase(self,search):
        myparam=self.get_post_data()(params=("text_fr","text_en",))
        x=self.dbPhrase.create(myparam)
        self.render_figure.set_param("redirect","/phrase")
        return self.render_some_json("welcome/redirect.json")
    def create_macros(self,search):
        myparam=self.get_post_data()(params=("nom","fichier",))
        x=self.dbMacro.create(myparam)
        self.render_figure.set_param("redirect","/macros")
        return self.render_some_json("welcome/redirect.json")
    def monscript(self,search):
        myparam=self.get_post_data()(params=("name","content",))
        hey=self.dbCommandline.create(myparam)
        hi=self.dbScript.create(myparam)
        print(hey,hi)
        return self.render_some_json("welcome/monscript.json")
    def enregistrer(self,search):
        print("hello action")
        self.render_figure.set_param("enregistrer",True)
        return self.render_figure.render_figure("welcome/radio.html")
    def elibrary(self,search):
        print("hello action")
        #self.render_figure.set_param("houses",self.dbHouse.getall())
        self.execProgram(["sh","monscrit/elibrary.sh"])
        return self.render_figure.render_figure("welcome/index.html")
    def hello(self,search):
        print("hello action")
        #self.render_figure.set_param("houses",self.dbHouse.getall())
        return self.render_figure.render_figure("welcome/index.html")
    def passage(self,myscrit):
        filename=myscrit["title"][0].replace(".mp3","").split("/")[-1]
        current_dateTime=datetime.now()
        self.render_figure.set_param("title", song["title"])
        self.render_figure.set_param("artist", song["artist"])
        self.render_figure.set_param("filename", song["filename"])
        self.render_figure.set_param("time", str(song["time"]))
        return self.render_some_json(Fichier("./welcome","chansonpassages.json").lire())
    def jouerchanson(self,myscrit):
        mylist=os.listdir("../radiohaker/public/uploads")
        k=random.randrange(0,(len(mylist) - 1))
        filename=mylist[k]
        print("filename =",filename)
        self.render_figure.set_param("filename", "/uploads/"+filename)
        self.render_figure.set_param("title", song["title"])
        self.figure.set_param("artist", song["artist"])
        self.render_some_json(Fichier("./welcome","chansons.json").lire())
    def delete_user(self,params={}):
        getparams=("id",)
        myparam=self.post_data(self.getparams)
        self.render_figure.set_param("user",User().deletebyid(myparam["id"]))
        self.set_redirect("/")
        return self.render_figure.render_redirect()
    def edit_user(self,params={}):
        getparams=("id",)

        myparam=self.get_this_route_param(getparams,params)
        print("route params")
        self.render_figure.set_param("user",User().getbyid(myparam["id"]))
        return self.render_figure.render_figure("user/edituser.html")
    def seeuser(self,params={}):
        getparams=("id",)
        print("get param, action see my new",getparams)
        myparam=self.get_this_route_param(getparams,params)
        return self.render_figure.set_param("user",User().getbyid(myparam["id"]))
    def text(self,params={}):
        self.render_figure.set_param("text",self.dbText.getall())
        return self.render_figure.render_figure("text/all_text.html")
    def mot(self,params={}):
        self.render_figure.set_param("mot",self.dbMot.getall())
        return self.render_figure.render_figure("mot/all_mot.html")
    def maphrase(self,params={}):
        self.render_figure.set_param("maphrase",self.dbMaphrase.getall())
        return self.render_figure.render_figure("maphrase/all_maphrase.html")
    def books(self,params={}):
        self.render_figure.set_param("books",self.dbBook.getall())
        return self.render_figure.render_figure("book/books.html")
    def phrases(self,params={}):
        self.render_figure.set_param("phrase",self.dbPhrase.getall())
        return self.render_figure.render_figure("phrase/all_phrase.html")
    def phraseatrou(self,params={}):
        self.render_figure.set_param("phraseatrou",self.dbPhraseatrou.getall())
        return self.render_figure.render_figure("phraseatrou/all_phraseatrou.html")
    def films(self,params={}):
        self.render_figure.set_param("film",self.dbFilm.getall())
        return self.render_figure.render_figure("film/all_film.html")
    def macros(self,params={}):
        self.render_figure.set_param("macros",self.dbMacro.getall())
        return self.render_figure.render_figure("welcome/macro.html")
    def myusers(self,params={}):
        self.render_figure.set_param("users",User().getall())
        return self.render_figure.render_figure("user/users.html")
    def pic(self,params={}):
        return self.render_figure.render_figure("welcome/pic.html")
    def update_user(self,params={}):
        myparam=self.post_data(self.getparams)
        self.user=self.dbUsers.update(params)
        self.set_session(self.user)
        self.set_redirect(("/seeuser/"+params["id"][0]))
    def login(self,s):
        search=self.get_post_data()(params=("email","password"))
        self.user=self.dbUsers.getbyemailpw(search["email"],search["password"])
        print("user trouve", self.user)
        if self.user["email"]:
            self.set_session(self.user)
            self.set_session(self.user)
            self.set_json("{\"redirect\":\"/chat\"}")
        else:
            self.set_json("{\"redirect\":\"/signin\"}")
            print("session login",self.Program.get_session())
        return self.render_figure.render_json()
    def nouveau(self,search):
        return self.render_figure.render_figure("welcome/new.html")
    def chanson(self,params={}):
        myparam=self.get_post_data()(params=("title","artist","file","lyric"))


        return self.render_some_json("welcome/create.json")
    def getlyrics(self,params={}):
        getparams=("id",)

       
        myparam=self.get_this_get_param(getparams,params)
        print("my param :",myparam)
        try:
          print("hey",hey)
          if not hey:
            hey=[]
        except:
          hey=[]

        self.render_figure.set_param("lyrics",hey)
        return self.render_some_json("welcome/lyrics.json")
    def getsongs(self,params={}):
        getparams=("id",)

       
        myparam=self.get_this_get_param(getparams,params)
        print("my param :",myparam)
        try:
          print("hey",hey)
          if not hey:
            hey=[]
        except:
          hey=[]

        self.render_figure.set_param("songs",hey)
        return self.render_some_json("welcome/songs.json")
    def photoartist(self,params={}):
        myparam=self.get_post_data()(params=("pic","id",))
        return self.render_some_json("welcome/create.json")
    def cadeau(self,params={}):
        myparam=self.get_post_data()(params=("pic","name"))
        return self.render_some_json("welcome/create.json")
    def jouerjeux(self,search):
        return self.render_figure.render_figure("welcome/jeu.html")
    def monjeu(self,search):
        myparam=self.get_post_data()(params=("lyric_id",))

        print(hi)
        self.render_figure.set_param("redirect","/jouerjeux")
        return self.render_some_json("welcome/redirect.json")
    def gagnant(self,search):
        myparam=self.get_post_data()(params=("name","pic",))

        print(hi)
        return self.render_some_json("welcome/create.json")

    def signin(self,search):
        return self.render_figure.render_figure("user/signin.html")

    def save_user(self,params={}):
        myparam=self.get_post_data()(params=("businessaddress","gender","profile","metier", "otheremail", "password","zipcode", "email", "mypic","postaladdress","nomcomplet","password_confirmation"))
        self.user=self.dbUsers.create(myparam)
        if self.user["email"]:
            self.set_session(self.user)
            self.set_json("{\"redirect\":\"/welcome\"}")
            return self.render_figure.render_json()
        else:
            self.set_json("{\"redirect\":\"/e\"}")
            return self.render_figure.render_json()
    def joueraujeu(self,params={}):
        self.set_json("{\"redirect\":\"/signin\"}")
        getparams=("song_id","jeu_id")
        myparam=self.get_post_data()(params=getparams)
        self.set_session_params(myparam)
        #self.set_redirect("/signin")
        #return self.render_figure.render_redirect()
        return self.render_figure.render_my_json("{\"redirect\":\"/signin\"}")
    def run(self,redirect=False,redirect_path=False,path=False,session=False,params={},url=False,post_data=False):
        if post_data:
            print("post data")
            self.set_post_data(post_data)
            print("post data set",post_data)
        if url:
            print("url : ",url)
            self.Program.set_url(url)
        self.set_my_session(session)

        if redirect:
            self.redirect=redirect
        if redirect_path:
            self.redirect_path=redirect
        if not self.render_figure.partie_de_mes_mots(balise="section",text=self.Program.get_title()):
            self.render_figure.ajouter_a_mes_mots(balise="section",text=self.Program.get_title())
        if path and path.endswith("png"):
            self.Program=Pic(path)
            self.Program.set_path("./")
        elif path and path.endswith("jpeg"):
            self.Program=Pic(path)
            self.Program.set_path("./")
        elif path and path.endswith("gif"):
            self.Program=Pic(path)
            self.Program.set_path("./")
        elif path and path.endswith("svg"):
            self.Program=Pic(path)
            self.Program.set_path("./")
        elif path and path.endswith("jpg"):
            self.Program=Pic(path)
            self.Program.set_path("./")
        elif path and path.endswith(".jfif"):
            self.Program=Pic(path)
        elif path and path.endswith(".css"):
            self.Program=Css(path)
        elif path and path.endswith(".js"):
            self.Program=Js(path)
        elif path:
            path=path.split("?")[0]
            print("link route ",path)
            ROUTES={
                    '^/$': self.hello,
                    '^/books$': self.books,
                    '^/macros$': self.macros,
                    '^/create_macroword$': self.create_macros,
                    '^/create_book$': self.create_book,
                    '^/films$': self.films,
                    '^/maphrase$': self.maphrase,
                    '^/create_film$': self.create_film,
                    '^/book/(\d+)$': self.voir_livre,
                    '^/elibrary$': self.elibrary,
                    '^/phrase$': self.phrases,
                    '^/editphrase/(\d+)$': self.edit_phrase,
                    '^/create_phrase$': self.create_phrase,
                    '^/update_phrase$': self.update_phrase,
                    '^/phraseatrou$': self.phraseatrou,
                    '^/editphraseatrou/(\d+)$': self.edit_phraseatrou,
                    '^/create_phraseatrou$': self.create_phraseatrou,
                    '^/update_phraseatrou$': self.update_phraseatrou,
                    '^/maphrase$': self.maphrase,
                    '^/create_maphrase$': self.create_maphrase,
                    '^/api$': self.mot,
                    '^/create_mot$': self.create_mot,
                    '^/text$': self.text,
                    '^/create_text$': self.create_text,

                    }
            REDIRECT={"/save_user": "/welcome"}
            for route in ROUTES:
               print("pattern=",route)
               mycase=ROUTES[route]
               x=(re.match(route,path))
               print(True if x else False)
               if x:
                   params["routeparams"]=x.groups()
                   try:
                       self.Program.set_html(html=mycase(params))


                   except Exception:  
                       self.Program.set_html(html="<p>une erreur s'est produite "+str(traceback.format_exc())+"</p><a href=\"/\">retour à l'accueil</a>")
                   #self.Program.redirect_if_not_logged_in()
                   return self.Program
               else:
                   self.Program.set_html(html="<p>la page n'a pas été trouvée</p><a href=\"/\">retour à l'accueil</a>")
        return self.Program
