from apyori import apriori

if __name__ == "__main__":

    transactions = [
        ['beer', 'sugar'],
        ['beer', 'nuts'],
        ['ham', 'nuts', 'sugar'],
        ['beer', 'cheese'],
        ['cheese', 'ham'],
        ['beer', 'butter'],
    ]

    results = list(
        apriori(transactions, min_support=1 / len(transactions), min_confidence=0.5, min_lift=1 * len(transactions) / 4,
                max_length=3))

    for result in results:
        if len(list(result)[0]) > 2:
            print(list(list(result)[0]))
