users = [
    {
      fname: "Kermit",
      lname: "the Frog",
      languages: ["Python", "JavaScript", "C#", "HTML", "CSS", "SQL"],
      interests: {
        music: ["guitar", "flute"],
        dance: ["tap", "salsa"],
        television: ["Black Mirror", "Stranger Things"]
      }
    },
    {
      fname: "Winnie",
      lname: "the Pooh",
      languages: ["Python", "Swift", "Java"],
      interests: {
        food: ["honey", "honeycomb"],
        flowers: ["honeysuckle"],
        mysteries: ["Heffalumps"]
      }
    },
    {
      fname: "Arthur",
      lname: "Dent",
      languages: ["JavaScript", "HTML", "Go"],
      interests: {
        space: ["stars", "planets", "improbability"],
        home: ["tea", "yellow bulldozers"]
      }
    }
  ]
  

  function userLanguages(userlist)
  {
    var langlist = ""
    for(i=0;i<userlist.length;i++)
        {
            langlist+= userlist[i].fname+" "+userlist[i].lname+" knows "
            for(j=0;j<userlist[i].languages.length;j++){
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
            
      }
      return langlist
  }




console.log(userLanguages(users));
