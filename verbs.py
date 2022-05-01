var = open("List of sVerbs.txt")
verbs = var.read().split('\n')
var.close()
for i in range(0, len(verbs)):
    verbs[i] = verbs[i].capitalize()
    verbs[i] = verbs[i].strip()
