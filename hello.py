import webapp2
import cgi


def is_anargam(word1, word2):
    """Returns True if anargam is found. Else return False."""
    count = 0
    word1, word2 = list(word1), list(word2)
    if len(word1) == len(word2):
          for i in word1:
                   if i in word2:
                    word2.remove(i)
                    count += 1
          if count == len(word1):
               return True
    return False


def anargamFind(wd_in):
    file = open('words.txt')
    wd_in=wd_in.lower();
    tmpString = ""
    found = 0
    for line in file:
     if is_anargam(wd_in,line.strip()):
        found += 1
        tmpString += line.strip() + ", " 
    return tmpString, found

class MainPage(webapp2.RequestHandler):
    def get(self):
        queryString = -1
        queryString = cgi.escape(self.request.get("wordIn"))
        if(queryString.isalpha()):
          outWords,total = anargamFind(queryString)
        else:
          outWords,total=(-1,-1)
        self.response.headers["Content-Type"] = "text/html"
        self.response.write("""
          <!DOCTYPE html>
<html lang="en">
<head>
  <title>Jumble Words Solver</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  <link rel="stylesheet" href="/my.css">
</head>
<body>


<div class="container" style="display: table;
  margin: auto;">

<div class="text-vertical-center">

<div class="jumbotron" style=" border:solid black 10px;">
<a style=" font-size:15px;background:white; color:black;" href="https://github.com/indrajithi/Jumble-words-Solver-using-webapp2" class="btn btn-info btn-lg">
          <span class="glyphicon glyphicon-link"></span> Fork on Github 
        </a>
<h1>Jumble Words Solver!</h1><br>
              <form action="/" method="get" >
                 <input type="text" name="wordIn" maxlength=20; style=" padding: 12px 20px;margin: 8px 0;box-sizing: border-box;font-size: 20px" value={}><br>
                <input type="submit" class="btn btn-success" style="padding: 10px 125px;font-size: 20px  ;" value="Find""><br>
               <h3 id="tst">{} Words Found: {}</h3>
              </form>
<div id="out"></div>

</div>
</div>


</div>
<script src="/jsFile.js"></script>

            </body>
          </html>""".format(queryString,total, outWords))

routes = [('/', MainPage)]

my_app = webapp2.WSGIApplication(routes, debug=True)
