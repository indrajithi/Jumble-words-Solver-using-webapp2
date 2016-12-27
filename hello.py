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
    tmpString = ""
    found = 0
    for line in file:
     if is_anargam(wd_in,line.strip()):
        found += 1
        tmpString += line.strip() + ", " 
    return tmpString, found

class MainPage(webapp2.RequestHandler):
    def get(self):
        queryString = cgi.escape(self.request.get("wordIn"))

        outWords,total = anargamFind(queryString)
        self.response.headers["Content-Type"] = "text/html"
        self.response.write("""
          <!DOCTYPE html>
<html lang="en">
<head>
  <title>Python Webapp</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>
<body>
<script>
var found = {};

   // alert("success");

</script>
<div class="container">
              <form action="/" method="get">
                 <input type="text" name="wordIn" value={}><br>
                <input type="submit" class="btn btn-success"value="Find"><br>
               <h3>{} Words Found: {}</h3>
              </form>
</div>
            </body>
          </html>""".format(total,queryString,total, outWords))

routes = [('/', MainPage)]

my_app = webapp2.WSGIApplication(routes, debug=True)
