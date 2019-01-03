"""
Data Loading and cleaning scripts
"""
import pandas as pd
import os


def load_secom_features(data_path, filename="secom.data"):
    """Loads secom data with exception of datetime in labels

    Parameters
    ----------
    data_path: str
        Directory containing data file

    filename: str, opt
        Filename of secom dataset. Defaults to 'secom.data'

    Returns
    -------
    secom_x: pd.DataFrame
        secom data
    """
    secom_x = pd.read_csv(os.path.join(data_path, filename), delimiter=" ", header=None)
    secom_x = secom_x.add_prefix("s_data_")
    return secom_x


def load_secom_labels(data_path, filename="secom_labels.data", feature_engineer=True):
    """Loads secom_labels.data and optionally provides feature engineering

    Parameters
    ----------
    data_path: str
        Directory containing data file

    filename: str, opt
        Filename of secom labels. Defaults to 'secom_labels.data'

    feature_engineer: bool, opt
        Perform initial feature engineer. Drops unneeded columns. Defaults to True


    Returns
    -------
    secom_y: pd.DataFrame
        secom labels
    """
    secom_y = pd.read_csv(os.path.join(data_path, filename), delimiter=" ", header=None)

    secom_y[1] = pd.to_datetime(secom_y[1])

    # Rename columns of clarity
    secom_y.columns = ["target", "datetime"]

    secom_y["datetime"] = pd.to_datetime(secom_y["datetime"])

    if feature_engineer is True:
        secom_y["datetime_ordinal_eng"] = secom_y["datetime"].apply(lambda d: d.toordinal())
        secom_y = secom_y.drop("datetime", axis=1)

    secom_y = secom_y.add_prefix("s_label_")

    return secom_y


def load_vendor_json(data_path, filename="vendordata.json", feature_engineer=True):
    """Loads vendor_json and optionally provides feature engineering

    Parameters
    ----------
    data_path: str
        Directory containing data file

    filename: str, opt
        Filename of vendor data. Defaults to 'vendordata.json'

    feature_engineer: bool, opt
        Perform initial feature engineer. Drops unneeded columns. Defaults to True


    Returns
    -------
    secom_json: pd.DataFrame
        Dataframe from JSON dataframe
    """
    secom_json = pd.read_json(os.path.join(data_path, filename)).sort_index()

    if feature_engineer is True:
        secom_json["datetime_ordinal"] = pd.to_datetime(secom_json["datetime"]) \
                                         .apply(lambda d: d.toordinal())

    return secom_json


def combine_data_sources(secom_data, secom_labels, vendor_data):
    """Merge all three dataframes together. Return data and labels as separate dataframes

    Parameters
    ----------
    secom_data: pd.DataFrame
    secom_labels: pd.DataFrame
    vendor_data: pd.DataFrame

    Returns
    -------
    merged_df: pd.DataFrame

    """

    merged_df = secom_data.merge(secom_labels, left_index=True, right_index=True) \
                            .merge(vendor_data, left_index=True, right_index=True)

    return merged_df

