def chisquare(input, col1, col2):
    """ 

    Given a a pandas dataframe (input) and the name of 2 columns (col1, col2), computes chi2 test for each pairwise combination of col1 and returns p value
    col1 must be the fixed variable (es. Group)

    Arguments:
        input: a pandas DataFrame
        col1: name of the column with the fixed variable (es. Group)
        col2: name of the column with the dependent variable (es. Sex)

    Prints: 
        chi2 square p value for each pairwise combinations of col1
    Returns:
        pandas DataFrame with columns 'Variable1', 'Variable2', and 'p-value'
    """
    import itertools
    import pandas as pd
    from scipy.stats import chi2_contingency

    series1 = input[str(col1)]
    series2 = input[str(col2)]

    contingency = pd.crosstab(series2, series1)

    x = list(itertools.combinations(
        range(0, series1.nunique()), 2))
    print("Pairwise chi2 test comparison for combinations of: ",
          str(col1), " and variable: ", str(col2))

    results = []

    for i in x:
        a, b = i
        c, p, dof, expected = chi2_contingency(contingency.iloc[:, [a, b]])
        print("chi2 test between: ", contingency.columns[a],
              " and ", contingency.columns[b])
        print("pvalue: ", p)
        results.append([contingency.columns[a], contingency.columns[b], p])
        print("\n")

    return pd.DataFrame(results, columns=['Variable1', 'Variable2', 'p-value'])


def fisher_test(input, col1, col2):
    """ 

    Given a a pandas dataframe (input) and the name of 2 columns (col1, col2), computes Fisher's exact test for each pairwise combination of col1 and returns p value
    col1 must be the fixed variable (es. Group)

    Arguments:
        input: a pandas DataFrame
        col1: name of the column with the fixed variable (es. Group)
        col2: name of the column with the dependent variable (es. Sex)

    Prints: 
        Fisher's exact test p value for each pairwise combinations of col1
    Returns:
        pandas DataFrame with columns 'Variable1', 'Variable2', and 'p-value'
    """
    import itertools
    import pandas as pd
    from scipy.stats import fisher_exact

    series1 = input[str(col1)]
    series2 = input[str(col2)]

    contingency = pd.crosstab(series2, series1)

    x = list(itertools.combinations(
        range(0, series1.nunique()), 2))
    print("Pairwise Fisher's exact test comparison for combinations of: ",
          str(col1), " and variable: ", str(col2))

    results = []

    for i in x:
        a, b = i
        table = contingency.iloc[:, [a, b]].values
        _, p = fisher_exact(table)
        print("Fisher's exact test between: ", contingency.columns[a],
              " and ", contingency.columns[b])
        print("pvalue: ", p)
        results.append([contingency.columns[a], contingency.columns[b], p])
        print("\n")

    return pd.DataFrame(results, columns=['Variable1', 'Variable2
