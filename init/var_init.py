
def init(question, answer, clues):
    return {
        "question"  : question,
        "answer"    : answer,
        "clues"     : clues,
        "ask"       : "{} ".format(question)
    }


indices = ["Quiz --indice", "quiz --indice", "quiz -i", "Quiz -i"]