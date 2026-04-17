from dictionary import dictionary, mapper

# Gets the N, V, ADV, etc. for us
def word_to_category(word):
    word = word.lower().strip()

    return dictionary.get(word, "UNKNOWN")


# Gets the different mappings for NP, VP, etc.
def category_to_mappers(categories):
    tupled_categories = tuple(categories)

    return mapper.get(tupled_categories, "UNKNOWN")


# Splits a sentence via spaces
def tokenizer(sentence):
    words = sentence.split(" ")

    return words

"""
    Performs the tokenization via shift reduce
    What it does is it first converst the token into the category,
    and checks if there are reduction that can be performed in the 
    stack. If the stack is empty and ends with 'S', it is successful
"""
def shift_reduce(tokens):
    # First, convert all words to their starting categories
    buffer = [word_to_category(t) for t in tokens]
    print(f"\tInitial Buffer:\t{buffer}\n")

    reduced = True
    while reduced:
        reduced = False
        
        for rule_tuple, parent_phrase in mapper.items():
            rule_length = len(rule_tuple)
            
            # Slide the window looking ONLY for this specific rule
            for i in range(len(buffer) - rule_length + 1):
                current_window = tuple(buffer[i:i+rule_length])
                
                if current_window == rule_tuple:
                    print(f"\tMatch found:\t{list(current_window)} -> {parent_phrase}")
                    
                    # Splice the new result into the buffer
                    buffer = buffer[:i] + [parent_phrase] + buffer[i+rule_length:]
                    print(f"\tBuffer Update:\t{buffer}\n")
                    
                    reduced = True
                    break
            
            if reduced:
                break
                
    return buffer