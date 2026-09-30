"""
Created on Sun Aug 27 22:54:05 2023

@author: miche
"""
import re
#We need to specify a pattern
simplepattern= re.compile(r"miche\.")
simplestring="miche.turco.miche."
matches=simplepattern.finditer(simplestring)
for match in matches:
    print(match)
#The function finditer uses the re module to find an expression in a string
#The pattern can be defined trough simpler ways:
    # .  any character
    # \w any word character [A-Za-z0-9_]
    # \W any non word character
    # \d any digit
    # \D not a digit
    # \s whitespace (space, tab, newline)
    # \S not a whitespace
    # \b word boundary (after a whitespace)
    # \B not a word boundary 
    # ^ beggining of a string
    # $ end of a string

#The pattern requires:
    #3 uppercase or lowercase letters
    #3-5 digits
    #1 symbol
pattern1= re.compile("^[A-Za-z]{3}[0-9]{3,5}[^A-Za-z0-9]{1}$")
print(pattern1.search("ABC3456!"))
print(pattern1.search("AB3456!"))
#If the character "^" is in the square brackets, every sequence 
#not in the brackets will be included in the pattern

#The pattern only requires the string to be 10 characters long
pattern2 =re.compile("^.{10}$")
print(pattern2.search("1234567890"))

#The pattern is useful to identify an email address
mailpattern = re.compile("^[A-za-z0-9\.\-_]+@{1}[A-za-z0-9\.\-_]+\.{1}[A-Za-z]{2,3}$")
print(mailpattern.search(("mymail.-2@gmail.it")))
print("\n")
#In this pattern, we understand that some characters need to be escaped with a backslash "\":
    # "."  "^"  "("   ")"  "$"  "*"  "+"  "["  "]"  "{"  "}"  "?"  "\"  "|"

#The pattern requires the string to be a phone number
phonepatternsimple = re.compile(r"\d\d\d.\d\d\d.\d\d\d\d")
#This first pattern accept every separator because of the dot
phonepattern = re.compile(r"\d{3}[-_.]+\d{3}[._-]+\d{4}")
#This pattern instead requires the specific character
phonenumber= "389_453_7700 320.---.842..2413"
matchingnumbers=phonepatternsimple.finditer(phonenumber)
#Quantifiers:
    # * 0 or more
    # + 1 or more
    # ? 0 or 1
    # {3} exact number, {3,4} range of numbers
for match in matchingnumbers:
    print(match)
    print("\n")
matchingnumbers=phonepattern.finditer(phonenumber)
for match in matchingnumbers:
    print(match)
    print("\n")

names=""" 
Mr. Turco
Mrs Rossi
Ms Giusi
Mrs. Blu
"""
#This pattern requires the strings to be formal names
formal_name=re.compile(r"[Mm][rs]?[s]?\.?\s[A-Za-z]+")
formal_name_with_groups=re.compile(r"((Mr|Ms|Mrs)\.?\s[A-Za-z]+)")
matchingnames=formal_name.finditer(names)
for match in matchingnames:
    print(match)
    print("\n")
#With brackets (), we can specify a group of characters required for our pattern.
#With the slash |, we can specify more than a group of characters

#This pattern requires the strings to be urls
urls="""
https://www.google.com
http://coremys.com
https://youtube.com
https://www.nasa.gov"""
urlspattern=re.compile(r"https?://(www\.)?(([A-Za-z]+)(.com|.gov))")
matchingurls=urlspattern.finditer(urls)
for match in matchingurls:
    print(match.group(0))
    print("\n")
#The entire string that matches is the group 0 of the match, that can be accessed
#with the .group method. All the other groups can be accessed too.
adjustedurls=urlspattern.sub(r"\2", urls)
print(adjustedurls)
print("\n")
#With the sub method, we can directly access the url we need. Every match in the string
#is substituted with the groups selected.

#There are other useful methods. Finditer return the match with addittional info,
#while findall only returns the groups.
matchingnames=formal_name_with_groups.findall(names)
print(matchingnames)
print("\n")

#The match method determines whether the regoular expression matches at the
#beginning of a string, while with search we include also the matches in between.
sentence="Start with a sentence"
matches=(re.compile(r"a")).match(sentence)
print(matches)
matches=(re.compile(r"a")).search(sentence)
print(matches)

#If there is the need to match a word that can contain both lower and 
#uppercase characters, we have to use flags:
matches=(re.compile(r"start", re.I)).search(sentence)
print(matches)


print("AAAAAAAAAAA")




