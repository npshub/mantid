// Mantid Repository : https://github.com/mantidproject/mantid
//
// Copyright &copy; 2015 ISIS Rutherford Appleton Laboratory UKRI,
//   NScD Oak Ridge National Laboratory, European Spallation Source,
//   Institut Laue - Langevin & CSNS, Institute of High Energy Physics, CAS
// SPDX - License - Identifier: GPL - 3.0 +
#pragma once

#include "ConvFitDataView.h"
#include "ConvFitModel.h"
#include "IndirectFitDataPresenter.h"

namespace MantidQt {
namespace CustomInterfaces {
namespace IDA {

class ConvFitAddWorkspaceDialog;

class MANTIDQT_INDIRECT_DLL ConvFitDataPresenter : public IndirectFitDataPresenter {
  Q_OBJECT
public:
  ConvFitDataPresenter(IIndirectFitDataModel *model, IIndirectFitDataView *view);

signals:
  void modelResolutionAdded(std::string const &name, WorkspaceID const &workspaceID);

protected:
  void addTableEntry(FitDomainIndex row) override;

private:
  std::unique_ptr<IAddWorkspaceDialog> getAddWorkspaceDialog(QWidget *parent) const override;
};

} // namespace IDA
} // namespace CustomInterfaces
} // namespace MantidQt
