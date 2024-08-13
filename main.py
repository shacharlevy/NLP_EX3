import json
import time
import benepar
import nltk
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer, ENGLISH_STOP_WORDS
from sklearn.feature_selection import SelectKBest

benepar.download('benepar_en3')
parser = benepar.Parser("benepar_en3")  # todo: uncomment this line once you have benepar installed
nltk.download('punkt')


def identify_explicit_and_implicit_that_clauses(filename):
    # todo: implement this function
    print(f'looking for explicit and implicit "that" usages in {filename}')

    # todo: note that we're looking for sentences where the optional "that" is used (or omitted)
    #  as a subordinating conjunction between main and subordinate clause; we say that the usage is "explicit" in cases
    #  where "that" is used but could be omitted, and "implicit", where it's omitted but could be used

    # todo: example sentences:
    #  in my head, i feel that i ended our friendship fairly (explicit)
    #  some people argue that all you need to know is calories in vs calories out, end of story (explicit)
    #  you’re correct, i believe it would be an active exhaust that changes in volume based on drive mode (implicit)
    #  we agree this specific suggestion is much better (implicit)
    data = load_data(filename)

    explicit_set = set()
    implicit_set = set()

    i = 1
    for sentence_text in data.split('\n'):
        i+=1
        try:
            tree = parser.parse(sentence_text)
            explicit, implicit = False, False
            for subtree in tree.subtrees():
                if check_explicit(subtree):
                    explicit_set.add(sentence_text)
                    explicit = True
                if check_implicit(subtree):
                    implicit_set.add(sentence_text)
                    implicit = True
                if implicit and explicit:
                    break

            if i % 1000 == 0:
                print(f' {i} - len exp: {len(explicit_set)} , len imp: {len(implicit_set)} total time: {round(time.time()-start, 0) / 60} min')
        except Exception as e:
            continue

    return explicit_set, implicit_set


def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()

    return data


def check_implicit(subtree):
    if subtree.label() == 'VP':
        left_child = subtree[0] if len(subtree) > 0 else None
        if left_child and left_child.label() in ['VB', 'VBD', 'VBP', 'VBZ', 'VBG', 'VBN']:
            right_child = subtree[1] if len(subtree) > 1 else None
            if right_child and right_child.label() == 'SBAR':
                left_son = right_child[0] if len(right_child) > 0 else None
                if left_son and left_son.label() == 'S':
                    return True
    return False


def check_explicit(subtree):
    if subtree.label() == 'VP':
        left_child = subtree[0] if len(subtree) > 0 else None
        if left_child and left_child.label() in ['VB', 'VBD', 'VBP', 'VBZ', 'VBG', 'VBN']:
            right_child = subtree[1] if len(subtree) > 1 else None
            if right_child and right_child.label() == 'SBAR':
                left_son = right_child[0] if len(right_child) > 0 else None
                if left_son and left_son.label() == 'IN' and left_son[0] == 'that':
                    return True
    return False


def extract_features(explicit, implicit):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(list(explicit) + list(implicit))
    y = np.array([0] * len(explicit) + [1] * len(implicit))
    selector = SelectKBest(k=15)
    selector.fit_transform(X, y)
    feature_indices = selector.get_support(indices=True)
    feature_names = np.array(vectorizer.get_feature_names_out())
    selected_words = feature_names[feature_indices]
    print("Top 15 words distinguishing between explicit and implicit sentences:")
    print(selected_words)


if __name__ == '__main__':
    start = time.time()

    with open('config.json', 'r') as json_file:
        config = json.load(json_file)

    explicit, implicit = identify_explicit_and_implicit_that_clauses(config['input_filename'])
    print(f'found {len(explicit)} explicit, and {len(implicit)} implicit cases')
    with open(config['explicit_filename'], 'w', encoding='utf-8') as fout:
        fout.write('\n'.join(explicit))
    with open(config['implicit_filename'], 'w', encoding='utf-8') as fout:
        fout.write('\n'.join(implicit))

    print(f'total time: {round(time.time()-start, 0)} sec')