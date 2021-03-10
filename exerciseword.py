import docx
import os
location = "docs"
word_to_search = input("Which word do you want to search? ")
def get_all_docs_in_folder(location="."):
    """
    Get a list of all the doc files in a certain location
    :param location: the location to search for docs
    :return: a list of doc files names
    """
    all_files = os.listdir(location)
    print(all_files)
    doc_files = []
    for file in all_files:
        # we iterate over all the files in the "location" folder
        if file.endswith(".docx"):
            doc_files.append(file)
    return doc_files


def check_word_in_doc_file(word="Luigi", file_name="1.docx"):
    """
    Opens the file_nma and searches for the word inside
    :param word: the Word to seach for
    :param file_name: the docx file to search in
    :return: True if found, false if not found
    """
    fp = open(file_name, "rb")
    doc_file = docx.Document(fp)
    # go over the file by paragraph and check for word
    for paragraph in doc_file.paragraphs:
        if word in paragraph.text.lower():
            return True
    # I search in all the file and if i got here, i could not find the word
    return False


doc_list = get_all_docs_in_folder("docs")
os.chdir(location)
good_files = []
for doc_file in doc_list:
    if check_word_in_doc_file(word=word_to_search.lower(), file_name=doc_file):
        good_files.append(doc_file)
print(f"these are the good files {good_files}")

