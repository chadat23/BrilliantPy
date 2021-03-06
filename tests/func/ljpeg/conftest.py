import numpy as np
import pytest


@pytest.fixture()
def rgb_numpy_photo(data_folder_path):
    return np.load(str(data_folder_path / 'ljpeg' / 'F-18.ppm.pickle.np'))
