def analyzeResults(results):
    denominator = len(results)
    tests = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
    # tokens = ['+1', '0', '-1', '-2', '-3', '-4', '-5', '-6', '-7', '-8', 'Blessing', 'Curse', 'Skull', 'Cultist', 'Tablet', 'Elder Thing', 'Autofail', 'Elder Sign']
    test_results = {}
    for test in tests:
        successful_results = len(list(filter(lambda r: test + r.get('modifier', 0) >= 0, results)))
        test_results[str(test)] = (successful_results * 100) / denominator
    
    return test_results
