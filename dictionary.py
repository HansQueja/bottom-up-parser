
parts_of_speech = ["N", "V", "A", "ADV", "P"]

phrases = ["NP", "VP", "AUX", "DET", "S"]

dictionary = {
    # Original
    "user": "N", "users": "N",
    "printer": "N", "printers": "N",
    "clean": "V", "cleans": "V",
    "stopped": "V",
    "should": "AUX",
    "the": "DET", "a": "DET", "with": "P",

    # Expanded Nouns (N)
    "robot": "N", "robots": "N",
    "algorithm": "N", "algorithms": "N",
    "model": "N", "data": "N",
    
    # Expanded Verbs (V)
    "navigate": "V", "navigates": "V",
    "train": "V", "trained": "V",
    "processed": "V", "compiled": "V",
    
    # Expanded Auxiliaries (AUX)
    "will": "AUX", "can": "AUX", 
    "must": "AUX", "might": "AUX",
    
    # Expanded Determiners (DET)
    "an": "DET", "this": "DET", 
    "that": "DET", "some": "DET"
}

mapper = {
    # Foundational Noun Phrase Rules
    ("DET", "N"): "NP",
    ("DET", "ADJ", "N"): "NP",
    ("N",): "NP",

    # Prepositional Phrase Rule
    ("P", "NP"): "PP",

    # Verb Phrase Rules
    ("V",): "VP",
    ("V", "NP"): "VP",
    ("V", "NP", "PP"): "VP",

    # Sentence Rules
    ("NP", "VP"): "S",
    ("NP", "AUX", "VP"): "S"
}