// Mantid Repository : https://github.com/mantidproject/mantid
//
// Copyright &copy; 2014 ISIS Rutherford Appleton Laboratory UKRI,
//   NScD Oak Ridge National Laboratory, European Spallation Source,
//   Institut Laue - Langevin & CSNS, Institute of High Energy Physics, CAS
// SPDX - License - Identifier: GPL - 3.0 +
#pragma once

#include "MantidAPI/Algorithm.h"
#include "MantidAPI/WorkspaceGroup.h"
#include "MantidAlgorithms/DllConfig.h"

namespace Mantid {
namespace Algorithms {

/** Stitch1DMany : Stitches multiple Matrix Workspaces together into a single
 output.
 */
class MANTID_ALGORITHMS_DLL Stitch1DMany final : public API::Algorithm {
public:
  /// Algorithm's name for identification. @see Algorithm::name
  const std::string name() const override { return "Stitch1DMany"; }
  /// Algorithm's version for identification. @see Algorithm::version
  int version() const override { return 1; }
  const std::vector<std::string> seeAlso() const override { return {"Rebin", "Stitch1D"}; }
  /// Algorithm's category for identification. @see Algorithm::category
  const std::string category() const override { return "Reflectometry"; }
  /// Summary of algorithm's purpose
  const std::string summary() const override { return "Stitches histogram matrix workspaces together"; }
  /// Validates algorithm inputs
  std::map<std::string, std::string> validateInputs() override;

  /// Performs the Stitch1D algorithm at a specific workspace index
  void doStitch1D(std::vector<API::MatrixWorkspace_sptr> &toStitch, const std::vector<double> &manualScaleFactors,
                  API::Workspace_sptr &outWS, std::string &outName);

  /// Performs the Stitch1DMany algorithm at a specific period
  void doStitch1DMany(const size_t period, const bool useManualScaleFactors, std::string &outName,
                      std::vector<double> &outScaleFactors, const int indexOfReference, const bool storeInADS = true);

private:
  /// Overwrites Algorithm method.
  void init() override;
  /// Pass groups in as they are to this algorithm
  bool checkGroups() override { return false; }
  /// Overwrites Algorithm method.
  void exec() override;

  // A 2D matrix holding workspaces obtained from each workspace list/group
  std::vector<std::vector<API::MatrixWorkspace_sptr>> m_inputWSMatrix;

  std::vector<double> m_startOverlaps;
  std::vector<double> m_endOverlaps;
  std::vector<double> m_params;
  std::vector<double> m_scaleFactors;
  std::vector<double> m_manualScaleFactors;
  API::Workspace_sptr m_outputWorkspace;

  bool m_scaleRHSWorkspace = true;
  bool m_useManualScaleFactors = false;
  size_t m_scaleFactorFromPeriod = 1;
  size_t m_indexOfReference = 0;
};

} // namespace Algorithms
} // namespace Mantid
