# HUFFMAN CODING : COMPRESSION TECHNIQUE

text=input('Please enter the text for compression')
len_text=len(text)
print('Entered text :')
print(text)

#Characters and Frequencies finding

letters=[]
only_letters=[]
for letter in text:
    if letter not in letters:
        freq=text.count(letter) 
        letters.append(freq)
        letters.append(letter)
        only_letters.append(letter)
    
# start of the huffman tree

nodes=[]
while len(letters)>0:
    nodes.append(letters[0:2])
    letters=letters[2:]

nodes.sort()
huffman_tree =[]
huffman_tree.append(nodes)

#Tree Building

def combine(nodes):
    pos=0
    newnode=[]

    if len(nodes)>1:
        nodes.sort()
        nodes[pos].append('0')
        nodes[pos+1].append('1')
        combined_node1=(nodes[pos][0]+nodes[pos+1][0])
        combined_node2=(nodes[pos][1]+nodes[pos+1][1])
        newnode.append(combined_node1)
        newnode.append(combined_node2)
        newnodes= []
        newnodes.append(newnode)
        newnodes=newnodes+nodes[2:]
        nodes=newnodes
        huffman_tree.append(nodes)
        combine(nodes)
        return huffman_tree

newnodes =combine(nodes)


#reversing the order of huffman tree
huffman_tree.sort(reverse=True)

#Removing similar elements in the tree
checklist=[]
for level in huffman_tree:
    for node in level:
        if node not in checklist:
            checklist.append(node)
        else :
            level.remove(node)
c=0
for level in huffman_tree:
    print(c,":",level)
    c=c+1


#Binary coding
letter_bin=[]
if len(only_letters)==1:
    letter_code=[only_letters[0],"0"]
    letter_bin.append(letter_code*len(text))
else:
    for letter in only_letters:
        lettercode=''
        for node in checklist:
            if len(node)>2 and letter in node[1]:
                lettercode=lettercode+node[2]
        letter_code=[letter,lettercode]
        letter_bin.append(letter_code)

#printing dictionary
print("The huffman code dictionary is as follows :") 

for letter in letter_bin:
    print(letter[0],letter[1])

#creating two lists from letter_bin so that index function can be applied

code=[]
codeword=[]
for i in range(0,len(letter_bin)):
    code.append(letter_bin[i][1])

for i in range(0,len(letter_bin)):
    codeword.append(letter_bin[i][0])

#printing the compressed text
compressed_text=''
for character in text:
    compressed_text=compressed_text+code[codeword.index(character)]
    
print('The compressed text is :',compressed_text)
