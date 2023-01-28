"""Module contains custom clickable item view class"""
from typing import List

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QListView, QDialog, QGridLayout, QPushButton


# TODO: add types
class ClickableItemsView(QDialog):
    """Class implements custom clickable item view"""
    def __init__(self, item_list: List, selected_items: List[str]):
        super().__init__()
        grid = QGridLayout()
        grid.setSpacing(10)
        self.setLayout(grid)
        self.selected_items: List[str] = selected_items
        self.item_list: List = item_list
        self.model: QStandardItemModel = QStandardItemModel()

        btn_ok = QPushButton('OK', self)
        btn_ok.clicked.connect(self.ok_pressed)
        btn_cancel = QPushButton('Cancel', self)
        btn_cancel.clicked.connect(self.cancel_pressed)
        btn_clear_all = QPushButton('Clear all', self)
        btn_clear_all.clicked.connect(self.clear_all)

        self.view: QListView = self.init_items()

        grid.addWidget(self.view, 0, 0)
        grid.addWidget(btn_clear_all, 0, 1)
        grid.addWidget(btn_ok, 1, 1)
        grid.addWidget(btn_cancel, 1, 2)
        self.setModal(True)
        self.show()

    def init_items(self) -> QListView:
        """Method init items"""
        for table in self.item_list:
            item = QStandardItem(table)
            item.setCheckState(0)
            if item.text() in self.selected_items:
                item.setCheckState(2)
            item.setCheckable(True)
            self.model.appendRow(item)

        view = QListView()
        view.setModel(self.model)
        return view

    def ok_pressed(self) -> None:
        """Method saves changes which user made in UI and closes form"""
        amount = self.model.rowCount()
        checked_tables = []
        for idx in range(amount):
            item = self.model.item(idx, 0)
            if item.checkState() == 2:
                checked_tables.append(item.text())
        self.selected_items = checked_tables
        self.init_items()
        self.close()

    def clear_all(self) -> None:
        """Method clears all"""
        amount = self.model.rowCount()
        for idx in range(0, amount - 1):
            item = self.model.item(idx, 0)
            if item.checkState() == 2:
                # TODO: fix: expected type CheckState, got int instead
                item.setCheckState(0)
        self.selected_items = []
        self.init_items()

    def cancel_pressed(self) -> None:
        """Method closes form"""
        self.close()
