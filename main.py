# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # open and read your file
   with open('./story.txt', 'r') as file:
       read_doc = file.read()


   return read_doc
#print(read_file_content('story.txt'))

def count_words():
    text = read_file_content("./story.txt")
    #Split text into words
    text_words = text.split()
    word_count = dict()

    #Create for loop to count the words
    for word in text_words:
        if word in word_count:
            word_count[word] += 1

        else:
            word_count[word] = 1

    return word_count
print(count_words())


   # return {"as": 10, "would": 20}