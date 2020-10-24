import copy
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
    if token.get('automatic_failure', False):
        if not fatherMateo:
            result['tokens_resolved'].append(token.get('label', ''))
            result['automatic_failure'] = True
            return result
    
    # Token is an automatic success
    if token.get('automatic_success') or fatherMateo:
        result['tokens_resolved'].append(token.get('label', ''))
        result['automatic_success']: True
        return result
    
    # Token is cancelled
    if token.get('symbol', False) and cards.get('counterspell', False):
        result['effects_resolved'].append('counterspell')
        return result


    ###################################################################
    # Apply Modifier                                                  #
    ###################################################################    
    result = recallTheFuture(token, cards, result)
    result = ritualCandles(token, cards, result)

    if not isTokenIgnored(token, cards, character):
        result['tokens_resolved'].append(token.get('label', ''))
        result['modifier'] += token.get('modifier', 0)
    
    ###################################################################
    # Recurse for draw again conditions                               #
    ###################################################################
    if shouldDrawAgain(token, cards, character):
        recursive_results = []
        bag_deep_copy = copy.deepcopy(bag) # clone bag
        for i in range(len(bag_deep_copy)): # remove the first copy of the current token
            if(bag_deep_copy[i].get('label', '') == token.get('label', '')):
                del bag_deep_copy[i]
                break
        for token in bag_deep_copy:
            result_deep_copy = copy.deepcopy(result)
            recursive_result = resolveToken(token, bag_deep_copy, cards, character, result_deep_copy)
            recursive_results.append(recursive_result)
        return recursive_results
    else:
        return [result]

# checks to see if the character is father mateo and the token is an auto-fail or elder sign
# returns boolean
def fatherMateoConstructor(character, token):
    return character.get('name', '') == "Father Mateo" and (token.get('label', '') == "automatic_failure" or token.get('label', '') == "Elder Sign")

# checks to see if the character is jim culver and the token is a skull
# returns boolean
def jimCulverConstructor(character, token):
    return 


# Check for copies of Recall The Future and apply their modifiers
def recallTheFuture(token, cards, result):
    if cards.get('recall_the_future', '') == token.get('label', '') and not 'recall_the_future' in result.get('effects_resolved', []):
        result['modifier'] += 2
        result['effects_resolved'].append('recall_the_future')

    if cards.get('recall_the_future_second_copy', '') == token.get('label', '') and not 'recall_the_future_second_copy' in result.get('effects_resolved', []):
        result['modifier'] += 2
        result['effects_resolved'].append('recall_the_future_second_copy')

    return result

# Check for copies of Ritual Candles and apply their modifiers
def ritualCandles(token, cards, result):
    if cards.get('ritual_candles', '') == token.get('label', '') and not 'ritual_candles' in result.get('effects_resolved', []):
        result['modifier'] += 1
        result['effects_resolved'].append('ritual_candles')

    if cards.get('ritual_candles_second_copy', '') == token.get('label', '') and not 'ritual_candles_second_copy' in result.get('effects_resolved', []):
        result['modifier'] += 1
        result['effects_resolved'].append('ritual_candles_second_copy')

    return result

# Checks for card conditions that would ignore the modifier for a given test
def isTokenIgnored(token, cards, character):
    ignored = False
    if cards.get('defiance', '') == token.get('label', ''):
        ignored = True
    if cards.get('defiance_level_2') and token.get('symbol', False):
        ignored = True
    if character.get('name', '') == "Jim Culver" and token.label == "Skull":
        # technically this treats the modifier as 0, but they're mathematically the same
        ignored = True
    return ignored

# checks for conditions that would draw an additional token
def shouldDrawAgain(token, cards, character):
    should = False
    if token.get('draw_again', False):
        should = True
    return should