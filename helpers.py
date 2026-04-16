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
        
        # Prioritize longer matches (3, 2, then 1) to avoid the greedy trap
        for length in [3, 2, 1]:
            # Slide a window across the buffer from left to right
            for i in range(len(buffer) - length + 1):
                current_window = buffer[i:i+length]
                
                result = category_to_mappers(current_window)
                
                if result != "UNKNOWN":
                    print(f"\tMatch found:\t{current_window} -> {result}")
                    
                    # Splice the new result into the buffer
                    buffer = buffer[:i] + [result] + buffer[i+length:]
                    print(f"\tBuffer Update:\t{buffer}\n")
                    
                    reduced = True
                    break
            
            if reduced:
                break
                
    return buffer