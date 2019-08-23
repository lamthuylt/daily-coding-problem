'''
This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have `s` as a prefix.

For example, given the query string `de` and the set of strings [`dog`, `deer`, `deal`], return [`deer`, `deal`].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
'''

"""
Data structure #1: List

["dog", "deer", "deal"]
"""

def find(query, dictionary):
    suggestions = []    
    for word in dictionary:
        if query == word[:len(query)]:
            suggestions.append(word)
    return suggestions



""" 
Data structure #2: Tree

       "root"
           \
           "d" 
         /    \
       "o"    "e"
       /      / \
     "g"    "e"  "a"
    /       /     \
 "dog"    "r"     "l"
         /          \
      "deer"      "deal"
"""
suggestions = []

class Node:
    def __init__(self, val):
        self.val = val
        self.children = []
    
    
    def add(self, remaining, word):
        flag_exist = False
        
        for child in self.children:
            if (remaining[0] == child.val) and (len(remaining[1:]) >= 1):         
                child.add(remaining[1:], word)
                flag_exist = True

        if flag_exist == False:
            self.children.append(Node(remaining[0]))
            # add child node containing each character of remaining            
            if len(remaining[1:]) >= 1:  
                self.children[-1].add(remaining[1:], word)
            # add child node containing the whole word to the end of each branch 
            if len(remaining[1:]) == 0:
                self.children[-1].children.append(Node(word))


    def fillSuggestionsList(self):
        if self.children == []:
            suggestions.append(self.val)
        else:
            for child in self.children:
                child.fillSuggestionsList()
             
            
    def find(self, query):
        # if query is empty or query is checked and does exist, return all possible query strings
        if query == '':
            self.fillSuggestionsList()
            return suggestions
        # check the existance of query character by character
        for child in self.children:
            if query[0] == child.val:
                return child.find(query[1:])
        # return None if query does not exist
        return None
                
            
if __name__ == "__main__":
    # data strucutre 1
    dictionary = ["dog", "deer", "deal"]
    print('Suggestions by DS#1: {}'.format(find('de', dictionary)))
    
    # data structure 2
    root = Node("root")
    for word in dictionary:     
        root.add(word, word)
    print('Suggestions by DS#2: {}'.format(root.find('de')))

