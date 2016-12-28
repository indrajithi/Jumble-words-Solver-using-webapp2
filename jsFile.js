var total = document.getElementById("tst").innerHTML[0];
var words = document.getElementById("tst").innerHTML;
words = words.substring(14,words.len);
wordIn = document.getElementsByName("wordIn")[0].value;

 if(total == 0){
document.getElementById("tst").innerHTML="<div class=\"alert alert-danger\">No words found!";
}

 if(total > 0){
  var str = document.getElementById("tst").innerHTML;
  var str2= "<div class=\"alert alert-success\">" + total +" Words found! </strong> <br>"+words+"</div>";
   document.getElementById('tst').innerHTML=str2;
  // document.getElementById("tst").innerHTML="";
  
}
if (total == "-")
    document.getElementById("tst").innerHTML="<div class=\"alert alert-danger\">Invalid Srting!</div>";
if (wordIn =="" || wordIn==null){
    document.getElementById("tst").innerHTML="<div class=\"alert alert-info\">Enter a String!</div>";
   
}
