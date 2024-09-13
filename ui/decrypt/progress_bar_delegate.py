from PyQt6 import QtWidgets, QtCore

class ProgressBarDelegate(QtWidgets.QStyledItemDelegate):

    def paint(self, painter, option, index):
        progress_bar_option = QtWidgets.QStyleOptionProgressBar()
        progress_bar_option.rect = option.rect
        # progress_bar_option.state = QtWidgets.QStyle.State_Horizontal
        progress_bar_option.direction = QtCore.Qt.LayoutDirection.LeftToRight
        # progress_bar_option.fontMetrics = QtWidgets.QApplication.fontMetrics()

        progress_bar_option.minimum = 0
        progress_bar_option.maximum = 100
        # progress_bar_option.textAlignment = QtCore.Qt.AlignCenter
        progress_bar_option.textVisible = True

        progress_bar_option.progress = 66
        progress_bar_option.text = 'demo'

        # QtWidgets.QApplication.style().drawControl(QtWidgets.QStyle.CE_ProgressBar,
        #                                         progress_bar_option,  painter)
        style = option.widget.style()
        style.drawControl(QtWidgets.QStyle.ControlElement.CE_ProgressBar, progress_bar_option, painter)
        return