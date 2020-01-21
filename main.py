from flask import Flask, render_template, request, json
from flask_bootstrap import Bootstrap

import heapq as h
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize


app = Flask(__name__)




def makeTable(text_string) -> dict:

    #word frequency dictionary.
    stopWords = set(stopwords.words("english"))
    words = dict()
    for word in word_tokenize(text_string):
     if word not in stopWords:
        if word not in words.keys():
            words[word] = 1
        else:
            words[word] += 1


    return words


def sentencesScoring(sentences, words) -> dict:

    score = dict()

    for sentence in sentences:
            for word in word_tokenize(sentence.lower()):
             if word in words.keys():
              if len(sentence.split(' ')) < 40:
                if sentence not in score.keys():
                    score[sentence] = words[word]
                else:
                    score[sentence] += words[word]


    return score 


def run_summarization(text):
    
    # find word frequency and put into a dictionary
    freq_table = makeTable(text)

    # tokenize the sentences - create the array of sentences.
    #we simply use the inbuild nltk method
    sentences = sent_tokenize(text)

    # score the sentences
    score = sentencesScoring(sentences, freq_table)

    # count the sentences + determine a good summary sentence amount
    countSentences = text.count('. ') +1

    if countSentences < 5:
       treshold = 1
    elif countSentences < 10:
       treshold = 2
    elif countSentences < 25:
       treshold = 3
    elif countSentences < 40:
       treshold = 4
    elif countSentences < 90:
       treshold = 5
    elif countSentences > 500:
       treshold = 10
    else:
       treshold = 7
 
    # get sentences with the highest scores
    getbestSentences = h.nlargest(treshold, score, key=score.get)
    
    # join the best sentences together
    summary = ' '.join(getbestSentences)

    return summary



@app.route("/")
def start():
    return render_template("index.html")


@app.route('/Summarizer', methods=['POST'])
def summarize():
    longText =  request.form['longText'];
    shortText = run_summarization(longText)
    response = app.response_class(
        response=json.dumps({'status':'OK','shortTxt':shortText}),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__=="__main__":
    app.run()
