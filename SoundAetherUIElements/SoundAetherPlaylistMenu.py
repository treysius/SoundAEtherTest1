# Form implementation generated from reading ui file 'SoundAetherPlaylistMenu.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SAEMainMenu(object):
    def setupUi(self, SAEMainMenu):
        SAEMainMenu.setObjectName("SAEMainMenu")
        SAEMainMenu.setFixedSize(400, 300)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(143, 143, 143))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        SAEMainMenu.setPalette(palette)
        self.line = QtWidgets.QFrame(parent=SAEMainMenu)
        self.line.setGeometry(QtCore.QRect(80, 230, 320, 20))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(parent=SAEMainMenu)
        self.line_2.setGeometry(QtCore.QRect(70, 0, 20, 300))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(parent=SAEMainMenu)
        self.line_3.setGeometry(QtCore.QRect(0, 50, 80, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.label = QtWidgets.QLabel(parent=SAEMainMenu)
        self.label.setGeometry(QtCore.QRect(20, 10, 40, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(194, 137, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(194, 137, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.DisconnectButton = QtWidgets.QPushButton(parent=SAEMainMenu)
        self.DisconnectButton.setGeometry(QtCore.QRect(320, 250, 70, 20))
        self.DisconnectButton.setObjectName("DisconnectButton")
        self.ServerIDLabel = QtWidgets.QLabel(parent=SAEMainMenu)
        self.ServerIDLabel.setGeometry(QtCore.QRect(100, 250, 215, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ServerIDLabel.setFont(font)
        self.ServerIDLabel.setObjectName("ServerIDLabel")
        self.label_2 = QtWidgets.QLabel(parent=SAEMainMenu)
        self.label_2.setGeometry(QtCore.QRect(90, 270, 171, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(194, 137, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(194, 137, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        self.label_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(19)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setLineWidth(1)
        self.label_2.setObjectName("label_2")
        self.BackToPlaylistButton = QtWidgets.QPushButton(parent=SAEMainMenu)
        self.BackToPlaylistButton.setGeometry(QtCore.QRect(290, 10, 101, 23))
        self.BackToPlaylistButton.setObjectName("BackToPlaylistButton")
        self.PlaylistNumber = QtWidgets.QLabel(parent=SAEMainMenu)
        self.PlaylistNumber.setGeometry(QtCore.QRect(90, 10, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(22)
        self.PlaylistNumber.setFont(font)
        self.PlaylistNumber.setObjectName("PlaylistNumber")
        self.PlayButton = QtWidgets.QPushButton(parent=SAEMainMenu)
        self.PlayButton.setGeometry(QtCore.QRect(330, 70, 60, 23))
        self.PlayButton.setObjectName("PlayButton")
        self.PauseButton = QtWidgets.QPushButton(parent=SAEMainMenu)
        self.PauseButton.setGeometry(QtCore.QRect(330, 100, 60, 23))
        self.PauseButton.setObjectName("PauseButton")
        self.ResumeButton = QtWidgets.QPushButton(parent=SAEMainMenu)
        self.ResumeButton.setGeometry(QtCore.QRect(330, 130, 60, 23))
        self.ResumeButton.setObjectName("ResumeButton")
        self.StopSongButton = QtWidgets.QPushButton(parent=SAEMainMenu)
        self.StopSongButton.setGeometry(QtCore.QRect(330, 160, 60, 23))
        self.StopSongButton.setObjectName("StopSongButton")
        self.MusicList = QtWidgets.QListWidget(parent=SAEMainMenu)
        self.MusicList.setGeometry(QtCore.QRect(90, 51, 231, 181))
        self.MusicList.setObjectName("MusicList")
        self.line_2.raise_()
        self.line_3.raise_()
        self.line.raise_()
        self.label.raise_()
        self.DisconnectButton.raise_()
        self.ServerIDLabel.raise_()
        self.label_2.raise_()
        self.BackToPlaylistButton.raise_()
        self.PlaylistNumber.raise_()
        self.PlayButton.raise_()
        self.PauseButton.raise_()
        self.ResumeButton.raise_()
        self.StopSongButton.raise_()
        self.MusicList.raise_()

        self.retranslateUi(SAEMainMenu)
        QtCore.QMetaObject.connectSlotsByName(SAEMainMenu)

    def retranslateUi(self, SAEMainMenu):
        _translate = QtCore.QCoreApplication.translate
        SAEMainMenu.setWindowTitle(_translate("SAEMainMenu", "Playlist Menu"))
        self.label.setText(_translate("SAEMainMenu", "Æ"))
        self.DisconnectButton.setText(_translate("SAEMainMenu", "Disconnect"))
        self.ServerIDLabel.setText(_translate("SAEMainMenu", "ServerID: ###.###.#.##"))
        self.label_2.setText(_translate("SAEMainMenu", "SoundÆther"))
        self.BackToPlaylistButton.setText(_translate("SAEMainMenu", "Back To Playlists"))
        self.PlaylistNumber.setText(_translate("SAEMainMenu", "Playlist"))
        self.PlayButton.setText(_translate("SAEMainMenu", "Play"))
        self.PauseButton.setText(_translate("SAEMainMenu", "Pause"))
        self.ResumeButton.setText(_translate("SAEMainMenu", "Resume"))
        self.StopSongButton.setText(_translate("SAEMainMenu", "Stop"))
