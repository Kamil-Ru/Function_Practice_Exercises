# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def paper_doll(text):
    a = ''
    for x in range(len(text)):
        a += text[x] *3
    return a

# test

print(paper_doll('text'))
print(paper_doll('Hello'))
print(paper_doll('Mississippi'))