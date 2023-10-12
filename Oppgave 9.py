
Liste = ["I", "dag", "er", "jeg", "så", "lykkelig", "så", "lykkelig", "så", "lykkelig", "det", "hele",
"endte", "dejligt", "jeg", "synger", "og", "er", "glad", "Ja", "alting", "endte", "lykkeligt", "så",
"lykkeligt", "så", "lykkeligt", "i", "dag", "er", "jeg", "så", "lykkelig", "som", "dagen", "den",
"er", "lang"]

antall_ord = len(" ".join(Liste).split()) #Finner ut hvor mange ord det er i listen

print("det er", antall_ord, "ord i listen")

sa = len("sa".join(Liste).split()) #Finner ut hvor mange så det er i listen
lykkelig = len("lykelig".join(Liste).split()) #Finner ut hvor mange lykkelig det er i listen
dag = len("dag".join(Liste).split()) #Finner ut hvor mange dag det er i listen

print('det er', sa, 'så i listen,', lykkelig, 'lykelig i listen,', dag, 'dag i listen')