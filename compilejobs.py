from urllib.request import urlopen
from nltk.stem import PorterStemmer
import string

def compile(data):

    ps = PorterStemmer()

    stopwords = []
    punctuationextra = "‘‘’“”â€1234567890(){}[]\n"

    bagofwords = []

    # Read list of stopwords
    stopurl = urlopen("https://people.ok.ubc.ca/bowenhui/analytics/asgns/a2/stopwords.txt")
    for line in stopurl:
        # remove \n from word
        line = line[0:len(line) - 1]
        # convert to string
        line = ch = str(line, 'utf-8')
        # add it to the list of stopwords
        stopwords.append(line)

    for jobnum, desc in data.items():
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

        bagofwords.append(stemmed)

    return bagofwords
