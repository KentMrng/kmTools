import os

from PySide2 import QtCore, QtGui, QtWidgets
from shiboken2 import wrapInstance

from maya import cmds
from maya import OpenMayaUI as omui
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

from kmLib.utils.qt import HorizontalLine


class MainWindow(MayaQWidgetDockableMixin, QtWidgets.QDialog):
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)

        self.script_path = os.path.join(os.path.dirname(__file__), 'scripts')

        self.setWindowTitle('Command Box')
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
    
        self.create_widgets()
        self.create_layouts()
        self.create_connections()
        
        self.refresh()
    
    def create_widgets(self):
        # Scripts Layout
        self.filter_lineEdit = QtWidgets.QLineEdit()
        self.filter_lineEdit.setPlaceholderText('Filter')
        self.filter_lineEdit.setMinimumWidth(180)
        self.filter_lineEdit.setMinimumHeight(25)
        
        self.filter_clear_btn = QtWidgets.QPushButton('Clear')
        self.filter_clear_btn.setMaximumHeight(22)
    
        self.scripts_list = QtWidgets.QListView()
        
        self.run_btn = QtWidgets.QPushButton('Run')
        
        # Action Layout
        self.refresh_btn = QtWidgets.QPushButton()
        self.refresh_btn.setFlat(True)
        self.refresh_btn.setIcon(QtGui.QIcon(':QR_refresh.png'))
        
        self.separator1 = HorizontalLine()
        
        self.add_btn = QtWidgets.QPushButton()
        self.add_btn.setFlat(True)
        self.add_btn.setIcon(QtGui.QIcon(':setEdAddCmd.png'))
        
        self.rem_btn = QtWidgets.QPushButton()
        self.rem_btn.setFlat(True)
        self.rem_btn.setIcon(QtGui.QIcon(':setEdRemoveCmd.png'))
        
        self.edit_btn = QtWidgets.QPushButton()
        self.edit_btn.setFlat(True)
        self.edit_btn.setIcon(QtGui.QIcon(':setEdEditMode.png'))
        
        self.separator2 = HorizontalLine()
        
        self.trash_btn = QtWidgets.QPushButton()
        self.trash_btn.setFlat(True)
        self.trash_btn.setIcon(QtGui.QIcon(':smallTrash.png'))
        
    
    def create_layouts(self):
        main_layout = QtWidgets.QHBoxLayout(self)
        main_layout.setContentsMargins(2, 2, 2, 2)   
        main_layout.setSpacing(2)     
        
        command_layout = QtWidgets.QVBoxLayout()
        
        filter_layout = QtWidgets.QHBoxLayout()
        filter_layout.setSpacing(2)
        filter_layout.addWidget(self.filter_lineEdit)
        filter_layout.addWidget(self.filter_clear_btn)

        action_layout = QtWidgets.QVBoxLayout()
        action_layout.addStretch(0)
        # action_layout.setContentsMargins(2, 2, 2, 2)
        # action_layout.setSpacing(2)
        action_layout.addWidget(self.refresh_btn)
        action_layout.addWidget(self.separator1)
        action_layout.addWidget(self.add_btn)
        action_layout.addWidget(self.rem_btn)
        action_layout.addWidget(self.edit_btn)
        action_layout.addWidget(self.separator2)
        action_layout.addWidget(self.trash_btn)
        action_layout.addStretch(0)
        
        command_layout.addLayout(filter_layout)
        command_layout.addWidget(self.scripts_list)
        command_layout.addWidget(self.run_btn)
        
        main_layout.addLayout(command_layout)
        main_layout.addLayout(action_layout)
    
    def create_connections(self):
        self.filter_clear_btn.clicked.connect(self.clear_filter)
        self.refresh_btn.clicked.connect(self.refresh)
        self.add_btn.clicked.connect(self.add_script)
        self.rem_btn.clicked.connect(self.rem_script)
        self.edit_btn.clicked.connect(self.edit_script)
        self.trash_btn.clicked.connect(self.open_trash)
        
    def clear_filter(self):
        self.filter_lineEdit.clear()
    
    def refresh(self):
        print('TODO: refresh()')
    
    def add_script(self):
        print('TODO: add_script()')

    def rem_script(self):
        print('TODO: rem_script()')
        
    def edit_script(self):
        print('TODO: edit_script()')
    
    def open_trash(self):
        print('TODO: open_trash()')


def show():
    try:
        ui.close()
        ui.deleteLater()
    except:
        pass

    ui = MainWindow()
    ui.show(dockable=True)

'''
import kmTools.commandBox.mainUI as cmdBx
reload(cmdBx)

cmdBx.show()
'''