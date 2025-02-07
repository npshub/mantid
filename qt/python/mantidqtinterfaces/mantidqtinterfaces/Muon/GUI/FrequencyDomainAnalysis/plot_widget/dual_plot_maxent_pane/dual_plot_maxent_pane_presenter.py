# Mantid Repository : https://github.com/mantidproject/mantid
#
# Copyright &copy; 2021 ISIS Rutherford Appleton Laboratory UKRI,
#   NScD Oak Ridge National Laboratory, European Spallation Source,
#   Institut Laue - Langevin & CSNS, Institute of High Energy Physics, CAS
# SPDX - License - Identifier: GPL - 3.0 +
from mantidqtinterfaces.Muon.GUI.Common.plot_widget.base_pane.base_pane_presenter import BasePanePresenter
from mantidqt.utils.observer_pattern import GenericObserverWithArgPassing, GenericObserver, GenericObservable
from mantidqtinterfaces.Muon.GUI.FrequencyDomainAnalysis.frequency_context import FREQ, FIELD, GAUSS, MHz


FREQ_X_LABEL = f'Maxent ({MHz}) and Counts'
FIELD_X_LABEL =  f'Maxent ({GAUSS}) and Counts'


class DualPlotMaxentPanePresenter(BasePanePresenter):

    def __init__(self, view, model, context, figure_presenter):
        super().__init__(view, model, context, figure_presenter)
        # view set up
        self._data_type = [FREQ_X_LABEL, FIELD_X_LABEL]
        self._sort_by = ["Maxent + Groups/detectors"]
        self.update_view()
        self._view.enable_plot_type_combo()
        self._view.hide_plot_diff()
        self._view.enable_tile_plotting_options()
        self._view.hide_plot_raw()
        self._view.disable_tile_plotting_options()
        self._view.set_is_tiled_plot(True)
        self._view.set_slot_for_selection_changed(self.update_selection)
        # sync view and model
        self._model.set_selection(self.view.get_selection_for_plot)
        # private memeber
        self._maxent_ws_name = None
        # connections
        self.method_changed =  GenericObserverWithArgPassing(self.change_time_plot)
        self.period_changed =  GenericObserverWithArgPassing(self.change_period)
        self.new_data_observer = GenericObserverWithArgPassing(
            self.handle_maxent_data_updated)
        self.reconstructed_data_observer = GenericObserverWithArgPassing(
            self.handle_reconstructed_data_updated)
        self.instrument_observer = GenericObserver(self.clear)
        self.update_freq_units = GenericObservable()
        self.update_x_label_observer = GenericObserver(self._update_pane)

    def change_time_plot(self, method):
        self._model.set_if_groups(method=="Groups")
        self.clear()

    def change_period(self, period):
        self._model.set_period(period)

    def handle_maxent_data_updated(self, name):
        if name is None:
            return
        self._maxent_ws_name = name
        self._model.set_run_from_name(name)
        self.add_data_to_plots()

    def handle_time_data_updated(self):
        return self._model.get_workspace_list_and_indices_to_plot()

    def add_data_to_plots(self):
        workspaces, indices = self.handle_time_data_updated()
        workspaces, indices = self._model.add_reconstructed_data(workspaces, indices)
        if self._maxent_ws_name:
            workspaces += [self._maxent_ws_name]
            indices += [0]
        self.add_list_to_plot(workspaces, indices, hold=False, autoscale=True)
        # force the maxent plot to have sensible start values
        self._figure_presenter._options_presenter.set_selection_by_index(1)
        self._figure_presenter.set_plot_range(self.context._frequency_context.range())

    def handle_reconstructed_data_updated(self, data_dict):
        self._model.clear_data()
        if "table" in data_dict.keys() and "ws" in data_dict.keys():
            self._model.set_reconstructed_data(data_dict["ws"], data_dict["table"])
        self._view.update_selection(self._model.create_options())
        self.update_selection()

    def update_selection(self):
        self._model.set_selection(self.view.get_selection_for_plot)
        self.add_data_to_plots()

    def clear(self):
        self._model.clear_data()
        self._maxent_ws_name = None
        self._view.update_selection([])
        self.clear_subplots()

    def get_plot_type(self):
        plot_type = self._view.get_plot_type()
        if GAUSS in plot_type:
            return FIELD
        else:
            return FREQ

    def handle_data_type_changed(self):
        """
        Handles the data type being changed in the view by plotting the workspaces corresponding to the new data type
        """
        self.context._frequency_context.x_label = self.get_plot_type()
        # update plot -> will update range too
        self.handle_maxent_data_updated(self.context._frequency_context.switch_units_in_name(self._maxent_ws_name))
        self.update_freq_units.notify_subscribers()

    def _update_pane(self):
        if self.context.frequency_context.unit() == GAUSS:
            self._view.set_plot_type(FIELD_X_LABEL)
        else:
            self._view.set_plot_type(FREQ_X_LABEL)
        self._figure_presenter.set_plot_range(self.context.frequency_context.range())
        if self._maxent_ws_name is None:
            return
        new_ws_name = self.context._frequency_context.switch_units_in_name(self._maxent_ws_name)
        self.handle_maxent_data_updated(new_ws_name)
