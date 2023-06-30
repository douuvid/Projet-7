# #1) commencer par la formule cout + interet

# def formule___(cout: int, benef: float):
#     i = 1
#     benef = 1 + benef / 100  # Convert the percentage benefit to a decimal value
#     result = cout * benef

#     return f"L'action-{i} vaut : {result}"

# print(formule___(20, 5))

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
max_budget = 500

def formule(actions):
    results = []
    i = 1
    for action in actions:
        cost = action["cost"]
        benefit = action["benefice"]
        value = round(cost * (1 + benefit / 100), 2)
        result = f"L'action-{i} vaut : {value} avec un taux de {benefit}% apres deux ans"
        results.append(result)
        i += 1
        
    return results


results = formule(actions)
sorted_results = sorted(results, key=lambda x: float(x.split("vaut : ")[1].split(" ")[0]), reverse=True)

for result in sorted_results:
    print(result)


    
