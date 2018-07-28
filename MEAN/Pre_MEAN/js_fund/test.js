function userLanguages(userlist)
{

  for(i=0;i<userlist.length;i++)
      {
          var langlist = ""
          for(j=0;j<userlist[i].languages.length;j++)
          {
              if(j < userlist[i].languages.length-1)
              {
                  langlist += userlist[i].languages[j]
                  langlist += ", "
              }
              else
              {
                  langlist += "and "
                  langlist += userlist[i].languages[j]
                  langlist += "." + "\n"
              }

          }
          console.log(userlist[i].fname + " " + userlist[i].lname + " knows " + langlist )
    }
}