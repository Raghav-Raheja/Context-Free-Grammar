import nltk


assignment_grammar = nltk.CFG.fromstring("""
S -> NP VP
VP -> V NP NP | V TO VP ADVP | V ADVP  
ADVP -> ADV | V ADV | ADV ADVP | ADV ADJ
NP -> Prop | Prop N | NU N | Det ADJ N | N
ADV -> "now" | "ago" | "not" | "always"
ADJ -> "naive" | "nice"
V -> "go" | "had" | "came" | "visit" | "may" | "are"
Prop -> "We" | "She" | "me" | "You" | "Their"
Det -> "a"
N -> "yesterday" | "days" | "kids" | "party" 
TO -> "to"
NU -> "two"
""")

parser = nltk.RecursiveDescentParser(assignment_grammar)

sent1 = 'We had a nice party yesterday'.split()
sent2 = 'She came to visit me two days ago'.split()
sent3 = 'You may go now'.split()
sent4 = 'Their kids are not always naive'.split()

sent5 = 'Their kids had a nice party yesterday'.split()
sent6 = 'You are not always nice'.split() 
sent7 = 'Their kids may go now'.split()
sent8 = 'Their party had kids yesterday'.split()

for tree1 in parser.parse(sent1):
    print(tree1)

for tree2 in parser.parse(sent2):
    print(tree2)

for tree3 in parser.parse(sent3):
    print(tree3)
    
for tree9 in parser.parse(sent4):
    print(tree9)
    
for tree5 in parser.parse(sent5):
    print(tree5)

for tree6 in parser.parse(sent6):
    print(tree6)

for tree7 in parser.parse(sent7):
    print(tree7)
    
for tree8 in parser.parse(sent8):
    print(tree8)    

P_assignment_grammar = nltk.PCFG.fromstring("""
S -> NP VP [1]
VP -> V NP NP [0.25]| V TO VP ADVP [0.25]| V ADVP [0.50]
ADVP -> ADV [0.25]| V ADV [0.25]| ADV ADVP [0.25]| ADV ADJ [0.25]
NP -> Prop [0.43]| Prop N [0.1425]| NU N [0.1425]| Det ADJ N [0.1425]| N [0.1425]
ADV -> "now" [.25]| "ago" [.25]| "not" [.25]| "always" [.25]
ADJ -> "naive" [.5]| "nice" [.5]
V -> "go" [.166]| "had" [.166]| "came" [.166]| "visit" [.166]| "may" [.166]| "are" [.166]
Prop -> "We" [.2]| "She" [.2]| "me" [.2]| "You" [.2]| "Their" [.2]
Det -> "a" [1]
N -> "yesterday" [.25]| "days" [.25]| "kids" [.25]| "party" [.25]
TO -> "to" [1]
NU -> "two" [1]
""")

P_parser = nltk.ViterbiParser(P_assignment_grammar)

P_sent1 = 'We had a nice party yesterday'.split()
P_sent2 = 'She came to visit me two days ago'.split()
P_sent3 = 'You may go now'.split()
P_sent4 = 'Their kids are not always naive'.split()

P_sent5 = 'Their kids had a nice party yesterday'.split()
P_sent6 = 'You are not always nice'.split() 
P_sent7 = 'Their kids may go now'.split()
P_sent8 = 'Their party had kids yesterday'.split()

for treeP1 in P_parser.parse(P_sent1):
    print(treeP1)
    
for treeP2 in P_parser.parse(P_sent2):
    print(treeP2) 
   
for treeP3 in P_parser.parse(P_sent3):
    print(treeP3)

for treeP4 in P_parser.parse(P_sent4):
    print(treeP4)   
    
for treeP5 in P_parser.parse(P_sent5):
    print(treeP5)  

for treeP6 in P_parser.parse(P_sent6):
    print(treeP6)  

for treeP7 in P_parser.parse(P_sent7):
    print(treeP7) 

for treeP8 in P_parser.parse(P_sent8):
    print(treeP8)     