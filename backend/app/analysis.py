def analyzeResults(results, bag):
    tests = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
    # tokens = ['+1', '0', '-1', '-2', '-3', '-4', '-5', '-6', '-7', '-8', 'Blessing', 'Curse', 'Skull', 'Cultist', 'Tablet', 'Elder Thing', 'Autofail', 'Elder Sign']
    test_results = {}
    for test in tests:
        test_token_results = {}
        for token in bag:
            def token_resolved(r):
                return r.get('tokens_resolved', [{'id': 'placeholder'}])[0].id == token.id
            token_results = list(filter(token_resolved, results))
            def token_success(r):
                return (test + r.get('modifier', 0) >= 0 or r.get('automatic_success')) and not r.get('automatic_failure')
            successful_results = len(list(filter(token_success, token_results)))
            token_probability_of_success = (successful_results * 100) / len(token_results)
            test_token_results[token.id] = token_probability_of_success
        
        test_probability_of_success = sum(test_token_results.values()) / len(test_token_results)
        test_results[str(test)] = test_probability_of_success
    return test_results
