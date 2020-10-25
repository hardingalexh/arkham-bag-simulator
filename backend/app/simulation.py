import copy

# For a given bag and token, resolve and return a list of all possible resolutions
def resolveToken(token, bag, cards, character, result=None):
    ###################################################################
    # Instantiate intial result dict                                  #
    ###################################################################
    if result == None:
        result = {
        'tokens_resolved': [], # a list of which tokens were resolved (by label)
        'effects_resolved': [], # a list of one-time effects that have already been resolved
        'modifier': 0, # the numeric modifier to apply to the test
        'automatic_success': False, # indicates that a condition causes the test to automatically succeed
        'automatic_failure': False # indicates that a condition causes the test to automatically succeed
    }
    ###################################################################
    # Check for automatic success, automatic failure, or cancellation #
    ###################################################################
    fatherMateo = fatherMateoConstructor(character, token)
    # Token is automatic_failure
    if token.automatic_failure:
        if not fatherMateo:
            result['tokens_resolved'].append(token.label)
            result['automatic_failure'] = True
            return [result]
    
    # Token is an automatic success
    if token.automatic_success or fatherMateo:
        result['tokens_resolved'].append(token.label)
        result['automatic_success']: True
        return [result]
    
    # Token is cancelled
    if token.symbol and cards.counterspell:
        result['effects_resolved'].append('counterspell')
        return [result]


    ###################################################################
    # Apply Modifier                                                  #
    ###################################################################    
    result = recallTheFuture(token, cards, result)
    result = ritualCandles(token, cards, result)

    if not isTokenIgnored(token, cards, character):
        result['tokens_resolved'].append(token.label)
        result['modifier'] += token.modifier
    
    ###################################################################
    # Recurse for draw again conditions                               #
    ###################################################################
    if shouldDrawAgain(token, cards, character):
        recursive_results = []
        bag_deep_copy = copy.deepcopy(bag) # clone bag
        for i in range(len(bag_deep_copy)): # remove the first copy of the current token
            if(bag_deep_copy[i].label == token.label):
                del bag_deep_copy[i]
                break
        for token in bag_deep_copy:
            result_deep_copy = copy.deepcopy(result)
            recursive_result = resolveToken(token, bag_deep_copy, cards, character, result_deep_copy)
            recursive_results += recursive_result
        return recursive_results
    else:
        return [result]

# checks to see if the character is father mateo and the token is an auto-fail or elder sign
# returns boolean
def fatherMateoConstructor(character, token):
    return character == "Father Mateo" and (token.label == "automatic_failure" or token.label == "Elder Sign")

# Check for copies of Recall The Future and apply their modifiers
def recallTheFuture(token, cards, result):
    if cards.recall_the_future == token.label and not 'recall_the_future' in result.get('effects_resolved', []):
        result['modifier'] += 2
        result['effects_resolved'].append('recall_the_future')

    if cards.recall_the_future_second_copy == token.label and not 'recall_the_future_second_copy' in result.get('effects_resolved', []):
        result['modifier'] += 2
        result['effects_resolved'].append('recall_the_future_second_copy')

    return result

# Check for copies of Ritual Candles and apply their modifiers
def ritualCandles(token, cards, result):
    if cards.ritual_candles == token.label and not 'ritual_candles' in result.get('effects_resolved', []):
        result['modifier'] += 1
        result['effects_resolved'].append('ritual_candles')

    if cards.ritual_candles_second_copy == token.label and not 'ritual_candles_second_copy' in result.get('effects_resolved', []):
        result['modifier'] += 1
        result['effects_resolved'].append('ritual_candles_second_copy')

    return result

# Checks for card conditions that would ignore the modifier for a given test
def isTokenIgnored(token, cards, character):
    ignored = False
    if cards.defiance == token.label:
        ignored = True
    if cards.defiance_second_copy == token.label:
        ignored = True
    if cards.defiance_level_2 and token.symbol:
        ignored = True
    if character == "Jim Culver" and token.label == "Skull":
        # technically this treats the modifier as 0, but they're mathematically the same
        ignored = True
    return ignored

# checks for conditions that would draw an additional token
def shouldDrawAgain(token, cards, character):
    should = False
    if token.draw_again:
        should = True
    return should