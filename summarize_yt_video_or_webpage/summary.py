from string import punctuation
import statistics
import nltk
nltk.download('punkt')
nltk.download('stopwords')


class Summarizer:

    MAX_WORD_IN_SENTENCE = 30

    def __init__(self, text, text_for_the_model=None):
        self.text = text
        if text_for_the_model == None:
            self.model_text = text
        else:
            self.model_text = text_for_the_model
        self.__word_frequencies = {}
        self.__stopwords = nltk.corpus.stopwords.words('english')
        self.__punctuation = punctuation
        self.__sentence_scores = {}
        self.sentence_median_score = 0

    def __rank_words(self):
        words = nltk.word_tokenize(self.model_text)
        # convert words to numbers (freq word -> bigger number)
        for word in words:
            if word not in self.__stopwords and word not in self.__punctuation:
                if word not in self.__word_frequencies.keys():
                    self.__word_frequencies[word] = 1
                else:
                    self.__word_frequencies[word] += 1

        maximum_frequency = max(self.__word_frequencies.values())
        for word in self.__word_frequencies.keys():
            self.__word_frequencies[word] = self.__word_frequencies[word] / maximum_frequency

    def __rank_sentencies(self, sentence_list):
        for sent in sentence_list:
            for word in nltk.word_tokenize(sent.lower()):
                if word in self.__word_frequencies.keys():
                    if len(sent.split(' ')) < Summarizer.MAX_WORD_IN_SENTENCE:
                        if sent not in self.__sentence_scores.keys():
                            self.__sentence_scores[sent] = self.__word_frequencies[word]
                        else:
                            self.__sentence_scores[sent] += self.__word_frequencies[word]
                else:
                    pass
                    #not relevant word (model created on different text)

    def __calculate_median_score(self):
        self.sentence_median_score = statistics.median(self.__sentence_scores.values())


    def create_model(self):
        self.__rank_words()
        self.__rank_sentencies()

    def create_summary(self) ->str:
        sentence_list = nltk.sent_tokenize(self.text)
        self.__rank_words()
        self.__rank_sentencies(sentence_list)

        #print sentencies what has bigger score than the median element
        self.__calculate_median_score()

        summary = ""
        for sent in sentence_list:
            if sent in self.__sentence_scores.keys():
                if self.sentence_median_score < self.__sentence_scores[sent]:
                    summary += sent
        return summary

    def print_summary(self):
        print(self.create_summary())