cypher = input()
Key = input()
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
message = ''
for i in range(len(cypher)):
    shift = alpha[cypher[i]] - alpha[Key[i]] % 26
    message += alpha[shift]
    key += alpha[shift]