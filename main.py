from version_dynamique import brute_force




actions =[
  {"name":"Action-1" ,"cost" : 20, "benefice" : 5 },
  {"name":"Action-2" ,"cost" : 30, "benefice" : 10 }, 
  {"name":"Action-3" ,"cost" : 50,"benefice" : 15 },
  {"name":"Action-4" ,"cost" : 70,"benefice" : 20 },
  {"name":"Action-5" ,"cost" : 60,"benefice" : 17 },
  {"name":"Action-6" ,"cost" : 80,"benefice" : 25 },
  {"name":"Action-7" ,"cost" : 22,"benefice" : 7 },
  {"name":"Action-8" ,"cost" : 26,"benefice" : 11 },
  {"name":"Action-9" ,"cost" : 48,"benefice" : 13 },
  {"name":"Action-10" ,"cost" : 34,"benefice" : 27 },
  {"name":"Action-11" ,"cost" : 42,"benefice" : 17 },
  {"name":"Action-12" ,"cost" : 110, "benefice" : 9 },
  {"name":"Action-13" ,"cost" : 38, "benefice" : 23 },
  {"name":"Action-14" ,"cost" : 14,"benefice" : 1 },
  {"name":"Action-15" ,"cost" : 18,"benefice" : 3 },
  {"name":"Action-16" ,"cost" : 8,"benefice" : 8 },
  {"name":"Action-17" ,"cost" : 4,"benefice" : 12 },
  {"name":"Action-18" ,"cost" : 10,"benefice" : 14 },
  {"name":"Action-19" ,"cost" : 24,"benefice" : 21 },
  {"name":"Action-20" , "cost" : 114,"benefice" : 18 }
    
]

budget = 200

if __name__ == "__main__":
    
    brute = brute_force(actions, budget)
    print(f"La meilleur solution est {brute[0]} ")
        
        
