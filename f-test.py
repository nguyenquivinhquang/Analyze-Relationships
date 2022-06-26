import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import statsmodels.formula.api as smf
from bioinfokit.analys import stat
from scipy import stats
from utils import WriteFile
import warnings

warnings.filterwarnings('ignore')

writeFile = WriteFile("Output", "Export_relationship", isFirstTime=True)


def qf(p, df1, df2, ncp=0):
    """compute the value of quantile function over F distribution 
    for a sequence of numeric values. 

    Args:
        p (array_like):    lower tail probability
        df1 (_type_): Degree of the First Freedom
        df2 (_type_): Degree of the Secibd Freedom
        ncp (int, optional): Defaults to 0.

    Returns:
        array_like:     quantile corresponding to the lower tail probability q.

    """
    return stats.f.ppf(q=p, dfn=df1, dfd=df2, loc=0, scale=1) if ncp == 0 else stats.ncf.ppf(
        q=p, dfn=df1, dfd=df2, loc=0, scale=1)


# Forward Selection
def forward_selected(data, response):
    """_summary_

    Args:
        data (dataframe): data
        response (str): The Y column/label

    Returns:
        formula (str): Indicate y depends on which the attributes.
        model: The model which is fit formula and data
        selected (int): Number of attributes that y depend on
    """

    remaining = set(data.columns)
    remaining.remove(response)
    selected = []
    current_score = best_new_score = 0.0
    iter = 0
    while remaining and current_score == best_new_score and iter < 10000:
        scores_with_candidates = []
        for candidate in remaining:
            iter += 1
            formula = f"{response} ~ {' + '.join(selected + [candidate])} + 1"
            score = smf.ols(formula, data).fit().rsquared_adj
            scores_with_candidates.append((score, candidate))

        scores_with_candidates.sort()

        best_new_score, best_candidate = scores_with_candidates.pop()
        if current_score < best_new_score:
            remaining.remove(best_candidate)
            selected.append(best_candidate)
            current_score = best_new_score

    formula = f"{response} ~ {' + '.join(selected)} + 1"
    model = smf.ols(formula, data).fit()
    return model, formula, len(selected)


df = pd.read_csv("datasetGenerate/datasettrade-weatherCities-weatherIndian_v2.csv")
df = df.drop("Unnamed: 0", axis=1)

total_commodity = len(list(set(df["Commodity"].tolist())))

for (_count, commodity) in enumerate(list(set(df["Commodity"].tolist()))):

    df1 = df.loc[df["Commodity"] == commodity]
    df1_im = df1.drop(["YEAR", "Commodity", "Import", "Difference"], axis=1)
    Y = df1_im[["Export"]]
    X = df1_im.iloc[:, 1:]

    # Choose the suitable feature and fit the model
    model, formula, p = forward_selected(df1_im, "Export")
    model.summary()

    anova = stat()
    anova.anova_stat(df=df1_im, res_var="Export", anova_model=formula)
    anova.anova_summary

    n = X.shape[0]
    alpha = 0.05
    degree_of_freedom = n - p - 1

    # sum of squares total,
    SSTO = np.sum(np.square(Y - Y.mean()))

    # sum of squares error
    SSE = np.sum(np.square(model.resid))

    MSE = SSE / degree_of_freedom

    # Sum of residual
    SSR = SSTO - SSE
    MSR = SSR / degree_of_freedom

    writeFile.update("Commodity: " + str(commodity))
    # F test
    if ((MSR / MSE).item()) > qf(1 - alpha, p - 1, degree_of_freedom):
        writeFile.update("Y is related to all independent variables")
        writeFile.update(formula)
        writeFile.update("Param: ")
        writeFile.update(str(model.params))
    else:
        writeFile.update("Y is not related to all independent variables")

    print("{}/{}".format(_count + 1, total_commodity))
    writeFile.update("----------------------------------")
    writeFile.update("")