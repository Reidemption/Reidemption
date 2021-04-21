def intro():
    print("""Welcome to the Leet Speak Translator

If you have a file that is written in leet
speak, we can translate it back to normal
English for you.

Just give me the name of the file you want
to have translated, and the name you want
for the translated file.""")

def main():
    intro()
    filein=input("Leet file name? ")
    fileout=input("English file name? ")
    fin=open(filein,'r')
    fout=open(fileout, 'w')
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-!,' :.?"
    leetspeak="48CD3FGHIJK1MN0PQR57UVWXYZ@bcd3fghijk1mn0pqr57uvwxyz-!,' :.?"
    newstr = ''
    for line in fin:
        for char in line:
            for i in range(len(alphabet)):
                if char == leetspeak[i]:
                    if char == '0':
                        newstr += 'o'
                        break
                    elif char == '3':
                        newstr += 'e'
                        break
                    elif char == 'L':
                        newstr += 'l'
                        break
                    elif char == '5':
                        newstr+= 's'
                        break
                    elif char == '7':
                        newstr+= 't'
                        break
                    else:
                        newstr+=alphabet[i]
                        break
                else:
                    newstr+=''
    print(newstr)
    fin.close()
    fout.close()
main()

                
    
    
        
