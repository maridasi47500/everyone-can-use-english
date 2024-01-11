import re
class Myroute:
  def __init__(self,route,mystr):
    self.str=mystr
    self.route=route
    #ecrire :number dans la route pour un nombre
    #ecrire :string dans la route pour une chaine
  def check(self):
    return re.match(("^"+self.route+"$").replace(":number","(\\d+)").replace(":string","(\\w+)"),self.str)
  def findall(self):
    return re.findall(("^"+self.route+"$").replace(":number","(\\d+)").replace(":string","(\\w+)"),self.str)
  def myparams(self):
    for x in self.route.split("/"):
       for y in x.split("("):
           for z in y.split("("):
               try:
                   h=z.index(")")
                   i=z.split(")")[0]
               except:
                   paspremier=False
                   for w in y.split(":"):
                       if paspremier:
                          print("param name:",w)
                       paspremier=True
