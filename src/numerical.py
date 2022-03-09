import numpy as np


def df_filter_constant(Dataframe, Ignore, VarThreshold=0.01):
    """Find and remove columns which do not have a variance bigger
    than the given threshold.
    :param Dataframe: Dataframe to be scanned for
    constant columns.
    :type Dataframe: pandas Dataframe

    :param Ignore: List of columns to be ignored,
    columns will end up in returned dataframe
    regardless of variance.
    :type Ignore: array-like

    :param Varthreshold: All columns with less or equal
    this variance will not
    end up in returned data frame.

    :raises KeyError: Raises error, when Ignore contains
    keywords that Dataframe does not contain

    :return: Copy of Dataframe, where all columns with variance
     less than given treshold are discarded
    :rtype: pandas.Dataframe
    """

    NewDf = Dataframe

    for key in Ignore:
        try:
            NewDf[key]

        except KeyError as e:
            print(e, "Column to be ignored not found in dataframe")

    for key in Dataframe.columns.values:

        if key in Ignore:
            continue

        if np.var(NewDf[key]) <= VarThreshold:
            NewDf = NewDf.drop(key, axis=1)

    return NewDf


def plot_relevant_columns(Dataframe, xAxis, figsize=(14, 10), VarTreshold=0):

    """Plot columns with Variance bigger than the
    given threshold.

    :param Dataframe: Dataframe to be plotted.
    :type Dataframe: pandas Dataframe

    :param xAxis: column to be used for the xAxis
    of the plots
    :type xAxis: Key for dataframe (most likely string)

    :param Varthreshold: All columns with less or
    equal this variance will not
    end up in returned data frame.
    Default is 0, so only constant columns will be discarded
    :type Varthreshold: float

    :param figsize: Size of figure
    :type figsize: tuple

    :return: None
    :rtype: None
    """
    try:
        NewDF = df_filter_constant(Dataframe, [xAxis], VarThreshold=VarTreshold)
    except KeyError as e:
        print(e, "Specified x-axis not found in dataframe")

    NewDF.plot(x=xAxis, subplots=True, figsize=figsize)