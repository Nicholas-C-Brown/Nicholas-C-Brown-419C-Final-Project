
from nltk.stem import PorterStemmer
import string

def compile(data):

    ps = PorterStemmer()

    stopwords = []
    punctuationextra = "‘‘’“”â€1234567890(){}[]\n"

    jobdict = {}

    # Read list of stopwords
    stopfile = open("stopwords.txt","r")
    for line in stopfile:
        line = line.replace("\n","")
        stopwords.append(line)

    for jobname, desc in data.items():
        desc = desc.lower()

        # split into words by white space
        tokens = desc.split()

        # remove punctuation (and other weird characters) from each word
        table = str.maketrans('', '', string.punctuation + punctuationextra)
        stripped = [w.translate(table) for w in tokens]

        # create array for filtered file
        filtered = []

        # remove stopwords
        for w in stripped:
            if w not in stopwords:
                filtered.append(w)

        # remove empty strings
        while '' in filtered:
            filtered.remove('')

        stemmed = []
        for word in filtered:

            stemmed_word = ps.stem(word)
            if "\\" not in stemmed_word:
                stemmed.append(stemmed_word)

        jobdict[jobname] = stemmed

    return jobdict
