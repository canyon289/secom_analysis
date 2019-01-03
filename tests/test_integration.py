"""
Integration tests for data load. Assumes data is available in relative path

../data

Tests are written specifically for input data files to check that there's no loading
or merge errors
"""
import pytest

from secom import data


@pytest.fixture()
def data_path():
    return "../data"


def test_load_secom_labels(data_path):
    df = data.load_secom_labels(data_path)
    assert df.shape[0] == 1567


def test_load_secom_features(data_path):
    df = data.load_secom_features(data_path)
    assert df.shape[0] == 1567


def test_load_vendor_json(data_path):
    df = data.load_vendor_json(data_path)
    assert df.shape[0] == 1567


def test_combine_data_sources(data_path):
    secom_data = data.load_secom_labels(data_path)
    secom_labels = data.load_vendor_json(data_path)
    vendor_data = data.load_secom_features(data_path)
    df = data.combine_data_sources(secom_data, secom_labels, vendor_data)
    assert df.shape[0] == 1567
