from yaml import dump

"""
This file contains all models.
"""


class Text:
    """
    The class representing a text-object.

    A text is formally a collection of sentences with some extra metadata.
    """

    def __init__(self):
        """
        Default constrcutor
        """
        self.title = ""
        self.title_translation = ""
        self.language = "und" # Und is the default for the undefined language
        self.plain_text = ""
        self.rich_text = ""
        self.delta = {}
        self.metadata = {}
        self.phrases = []

    def add_phrase(self, phrase):
        """
        Adds a phrase to the text-object

        :param phrase:
        :return:
        """
        if not (isinstance(phrase, Phrase)):
            raise Exception("Wrong argument to add_phrase. Expected Phrase instance")

        self.phrases.append(phrase)

    def add_metadata(self, key, value):
        """
        Adds a metadata key-value pair.

        :param key:
        :param value:
        :return:
        """

        if key is not None and value is not None:
            self.metadata[key] = value
        else:
            raise Exception("Wrong argument to add_metadata. Expected a key-value pair as argument one and two")

    def to_dict(self):
        return {
            'title': self.title,
            'title_translation': self.title_translation,
            'language': self.language,
            'plain_text': self.plain_text,
            'rich_text': self.rich_text,
            'delta': self.delta,
            'metadata': self.metadata,
            'phrases': map(lambda phr: phr.to_dict(), self.phrases)
        }

    def __str__(self):
        return dump(self.to_dict())

    def __iter__(self):
        return self.phrases.__iter__()

class Phrase:
    """
    The class representing a phrase-object.

    A phrase is a collection of words.
    """

    def __init__(self):
        """
        Default constructor.
        """
        self.phrase = ""
        self.free_translation = ""
        self.free_translation2 = ""
        self.comment = ""
        self.offset = 0
        self.duration = 0
        self.senses = []
        self.words = []

    def add_word(self, word):
        """
        Adds a word to the phrase.

        :param word:
        :return: Nothing
        """
        if not (isinstance(word, Word)):
            raise Exception("Bad argument to add_word, expected a word instance")

        self.words.append(word)

    def to_dict(self):
        return {
            'phrase': self.phrase,
            'free_translation': self.free_translation,
            'free_translation2': self.free_translation2,
            'comment': self.comment,
            'offset': self.offset,
            'duration': self.duration,
            'senses': self.senses,
            'words': map(lambda wrd: wrd.to_dict(), self.words)
        }

    def __str__(self):
        return dump(self.to_dict())

    def __iter__(self):
        return self.words.__iter__()


class Word:
    """
    The class representing a Word.

    A word is a collection of morphemes and an associated POS-tag.
    """

    def __init__(self):
        """
        Default constructor.
        """
        self.word = ""
        self.ipa = ""
        self.pos = ""
        self.stem_morpheme = None
        self.morphemes = []

    def add_morpheme(self, morpheme):
        if not (isinstance(morpheme, Morpheme)):
            raise Exception("Wrong argument to add_morpheme, expected Morpheme instance")

        self.morphemes.append(morpheme)

    def to_dict(self):
        return {
            'word': self.word,
            'ipa': self.ipa,
            'pos': self.pos,
            'stem_morpheme': self.stem_morpheme,
            'morphemes': map(lambda mrph: mrph.to_dict(), self.morphemes)
        }

    def __str__(self):
        return dump(self.to_dict())

    def __iter__(self):
        return self.morphemes.__iter__()


class Morpheme:
    """
    The class representing a morpheme.

    A morpheme is the tiniest building block of the typecraft xml-format.

    It is comprised of a text-content and a set of glosses.
    """

    def __init__(self):
        self.morpheme = ""
        self.meaning = ""
        self.baseform = ""
        self.glosses = []

    def to_dict(self):
        return {
            'morpheme': self.morpheme,
            'baseform': self.baseform,
            'meaning': self.meaning,
            'glosses': self.glosses
        }

    def __str__(self):
        return dump(self.to_dict())
