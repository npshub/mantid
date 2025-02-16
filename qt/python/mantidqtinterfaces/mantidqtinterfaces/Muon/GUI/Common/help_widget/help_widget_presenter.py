# Mantid Repository : https://github.com/mantidproject/mantid
#
# Copyright &copy; 2019 ISIS Rutherford Appleton Laboratory UKRI,
#   NScD Oak Ridge National Laboratory, European Spallation Source,
#   Institut Laue - Langevin & CSNS, Institute of High Energy Physics, CAS
# SPDX - License - Identifier: GPL - 3.0 +
from mantidqtinterfaces.Muon.GUI.Common.help_widget.help_widget_view import HelpWidgetView


class HelpWidgetPresenter(object):

    def __init__(self, view):
        self._view = view

        self._view.on_manage_user_directories_clicked(self.handle_manage_user_directories)
        self._view.on_help_button_clicked(self.handle_help_button_clicked)

    def handle_manage_user_directories(self):
        self._view.show_directory_manager()

    def handle_help_button_clicked(self):
        self._view._on_help_button_clicked()


class HelpWidget(object):
    def __init__(self, doc):
        self.view = HelpWidgetView(doc)
        self.presenter = HelpWidgetPresenter(self.view)
