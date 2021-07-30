'''A regular expression (RE, regex, regexes, regex pattern) is a special sequence of characters that helps you match or find other strings or sets of strings, using a specialized syntax held in a pattern. Instead of giving characters for matching and parsing strings, we can use regexes to match patterns.
Its a really smart way to look through text while searching for something.
We need to import the library re

re.search() returns a boolean value based on whether the string matches.
re.findall() actually extracts the matching string. It returns a list of all the possible matches.'''

# Greedy matching happens :  the repeat characters + and * push outwards to find the largest possible match
# To make it NOT Greedy, we add a ? at the end. This returns the shortest match.
import re

x = open("assets/regex_sum_1160002.txt","r")

y = re.findall('[0-9]+',x.read())

sum=0
for i in y:
    sum = sum+int(i)
print(sum)
