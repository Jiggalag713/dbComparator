"""Module contains class intended for storing default variables"""
from typing import List
from configuration.system_config import SystemConfig


class DefaultValues:
    """Class intended for storing default variables"""
    def __init__(self):
        self.system_config: SystemConfig = SystemConfig()
        self.checks_customization = {'check_schema': True,
                                     'fail_fast': False,
                                     'check_reports': True,
                                     'check_entities': True,
                                     'use_dataframes': True,
                                     'report_check_type': 'detailed'}
        self.default_excluded_tables: List[str] = ['databasechangelog',
                                                   'download',
                                                   'migrationhistory',
                                                   'mntapplog',
                                                   'reportinfo',
                                                   'synchistory',
                                                   'syncstage',
                                                   'synctrace',
                                                   'synctracelink',
                                                   'syncpersistentjob',
                                                   'forecaststatistics',
                                                   'migrationhistory']
        self.default_excluded_columns: List[str] = ['archived',
                                                    'addonFields',
                                                    'hourOfDayS',
                                                    'dayOfWeekS',
                                                    'impCost',
                                                    'id']
        self.constants = {
            'comparing_step': 10000,
            'depth_report_check': 7,
            'retry_attempts': 5,
            'table_timeout': 5,
            'strings_amount': 1000
        }
        self.schema_columns: List[str] = []
        # self.schema_columns: List[str] = ['TABLE_CATALOG',
        #                                   'TABLE_NAME',
        #                                   'COLUMN_NAME',
        #                                   'ORDINAL_POSITION',
        #                                   'COLUMN_DEFAULT',
        #                                   'IS_NULLABLE',
        #                                   'DATA_TYPE',
        #                                   'CHARACTER_MAXIMUM_LENGTH',
        #                                   'CHARACTER_OCTET_LENGTH',
        #                                   'NUMERIC_PRECISION',
        #                                   'NUMERIC_SCALE',
        #                                   'DATETIME_PRECISION',
        #                                   'CHARACTER_SET_NAME',
        #                                   'COLLATION_NAME',
        #                                   'COLUMN_TYPE',
        #                                   'COLUMN_KEY',
        #                                   'EXTRA',
        #                                   'COLUMN_COMMENT',
        #                                   'GENERATION_EXPRESSION']

    def set_default_values(self, line_edits, checkboxes, radio_buttons) -> None:
        """Method sets default values to some UI elements on main window."""
        self.line_edits_default_values(line_edits)
        self.check_boxes_default_values(checkboxes)
        self.radio_buttons_default_values(radio_buttons)

    def line_edits_default_values(self, line_edits) -> None:
        """Method sets default values for line_edits"""
        line_edits.excluded_tables.setText(','.join(self.default_excluded_tables))
        line_edits.excluded_tables.setCursorPosition(0)
        line_edits.excluded_columns.setText(','.join(self.default_excluded_columns))
        line_edits.excluded_columns.setCursorPosition(0)

    def check_boxes_default_values(self, checkboxes) -> None:
        """Method sets default values for check_boxes"""
        checkboxes.get('check_schema').setChecked(self.checks_customization.get('check_schema'))
        checkboxes.get('fail_fast').setChecked(self.checks_customization.get('fail_fast'))
        checkboxes.get('check_reports').setChecked(self.checks_customization.get('check_reports'))
        checkboxes.get('check_entities').setChecked(self.checks_customization.get('check_entities'))
        checkboxes.get('use_dataframes').setChecked(self.checks_customization.get('use_dataframes'))

    @staticmethod
    def radio_buttons_default_values(radio_buttons) -> None:
        """Method sets default values for radio_buttons"""
        radio_buttons.get('day_summary_mode').setChecked(True)
        radio_buttons.get('section_summary_mode').setChecked(False)
        radio_buttons.get('detailed_mode').setChecked(False)
