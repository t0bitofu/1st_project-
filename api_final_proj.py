import requests
import json

base_url = "https://www.dictionaryapi.com/api/v3/references/ithesaurus/json/"

thesaurus_key = "3333989a-a54f-4a59-9939-473039175982"

print("WELCOME TO THE THESAURUS ARCADE!")
#print("You can choose three options: Guess the synonym (1), guess the word (2), and run a text through a thesaurus (3)")
#user_choice = input("Input a number 1 to 3:")

def call_synonym():
    user_word = input("Input a word: ")
    query = user_word + "?key="
    url = base_url + query + thesaurus_key 
    response = requests.get(url)
    json_dict = response.json()
    array = json_dict["array"]
    noun = array["0"]
    meta = "0"["meta"]
    synonym_list = meta["syns"]
    synonym = synonym_list[0]
    found_word = synonym[1]
    return found_word
    #new_text = []
    #new_text.append(found_word)

print(call_synonym())


#text = "Interesting"
#text = text.split("")

#for word in text:
#    call_synonym(word)


if user_choice == 1:
  print("hi")
elif user_choice == 2:
  print("hello")
elif user_choice == 3:
  print("hey")


