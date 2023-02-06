import pytest
from PyQt5.QtWidgets import QRadioButton


def test_save_configuration(default_main):
    assert True


def test_write_to_file():
    assert True


def test_serialize_check_customization_state():
    assert True


@pytest.mark.parametrize("expected", ['day-sum', 'section-sum', 'detailed'])
def test_get_check_type_checked(config_serialization, expected):
    radio_buttons = {
        'day-sum': QRadioButton('Day summary'),
        'section-sum': QRadioButton('Section summary'),
        'detailed': QRadioButton('Detailed')
    }
    radio_buttons.get(expected).setChecked(True)
    assert config_serialization.get_check_type(radio_buttons) == expected


def test_host_properties_to_json():
    assert True


def test_system_variables_to_json():
    assert True


def test_variables_to_json():
    assert True


def test_get_value():
    assert True


def test_load_configuration():
    assert True


def test_deserialize_config():
    assert True


def test_load_radio_buttons_state():
    assert True