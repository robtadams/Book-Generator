var = open("List of adjectives.txt")
adj = var.read().split('\n')
var.close()
adj = adj[1:]
for i in range(0, len(adj)):
    adj[i] = adj[i].capitalize()
