import docx
import os
# docx is the library that works with word files
# os is used to change directories, get files in a directory. OS stands for Operating System

#modify this variable to search for another name
word_to_search = "Luigi"
path = "docs"

# this returns a list of all the files in the directory. Some are docx some are not
all_files = os.listdir(path)
#print(all_files)


# this is the list of only the doc files that we construct
doc_files = []

# we check for each file to see if it is a docx file or not
for file in all_files:
    # if file.startswith("~$"):
    if file.find("$") != -1:
        continue
    if file.endswith(".docx"):
        doc_files.append(file)

#print(doc_files)

# this is the third list where we store the files that contain our keyword
result_files = []

# we change the current directory to make opening the files easier
os.chdir(path)

# for each docx file, we open, go through each paragraph and search the keyword
for file_name in doc_files:
    # this is how you open a file (any file, not just word)
    f = open(file_name, "rb")

    # this is how you convert an opened generic file to a docx document (we made sure that the file is docx format)
    doc = docx.Document(f)

    # we iterate through each paragraph in the document
    for para in doc.paragraphs:
        # we check to see if the word_to_search is in this paragraph
        if word_to_search.lower() in para.text.lower():
            # we found it, so we add the file name to the list of the file names that match! we also break since there is no point to look further in this file
            result_files.append(file_name)
            break

    # close the file and move to the next one in the other step of the iteration
    f.close()

# in the end, we print the result
print("These were all the docx files that I searched: {}".format(doc_files))
print("Here is the list of files that contain the word {}: {}".format(word_to_search,result_files))

