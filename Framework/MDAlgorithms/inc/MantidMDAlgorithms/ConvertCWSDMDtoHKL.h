// Mantid Repository : https://github.com/mantidproject/mantid
//
// Copyright &copy; 2015 ISIS Rutherford Appleton Laboratory UKRI,
//   NScD Oak Ridge National Laboratory, European Spallation Source,
//   Institut Laue - Langevin & CSNS, Institute of High Energy Physics, CAS
// SPDX - License - Identifier: GPL - 3.0 +
#pragma once

#include "MantidAPI/Algorithm.h"
#include "MantidAPI/IMDEventWorkspace_fwd.h"
#include "MantidDataObjects/PeaksWorkspace.h"
#include "MantidGeometry/MDGeometry/MDTypes.h"
#include "MantidKernel/Matrix.h"
#include "MantidKernel/System.h"
#include "MantidKernel/V3D.h"
#include "MantidMDAlgorithms/DllConfig.h"

namespace Mantid {
namespace MDAlgorithms {

/** ConvertCWSDMDtoHKL : TODO: DESCRIPTION
 */
class MANTID_MDALGORITHMS_DLL ConvertCWSDMDtoHKL final : public API::Algorithm {
public:
  /// Algorithm's name
  const std::string name() const override { return "ConvertCWSDMDtoHKL"; }

  /// Summary of algorithms purpose
  const std::string summary() const override {
    return "Convert constant wavelength single crystal diffractomer's data"
           "in MDEventWorkspace and in unit of Q-sample to the HKL space "
           "by UB matrix.";
  }

  /// Algorithm's version
  int version() const override { return (1); }

  /// Algorithm's category for identification
  const std::string category() const override { return "Diffraction\\ConstantWavelength"; }

private:
  /// Initialisation code
  void init() override;

  /// Execution code
  void exec() override;

  void exportEvents(const API::IMDEventWorkspace_sptr &mdws, std::vector<Kernel::V3D> &vec_event_qsample,
                    std::vector<signal_t> &vec_event_signal, std::vector<detid_t> &vec_event_det);

  void convertFromQSampleToHKL(const std::vector<Kernel::V3D> &q_vectors, std::vector<Kernel::V3D> &miller_indices);

  API::IMDEventWorkspace_sptr createHKLMDWorkspace(const std::vector<Kernel::V3D> &vec_hkl,
                                                   const std::vector<signal_t> &vec_signal,
                                                   const std::vector<detid_t> &vec_detid);

  void addMDEvents(std::vector<std::vector<coord_t>> &vec_q_sample, std::vector<float> &vec_signal);

  void saveMDToFile(const std::vector<std::vector<coord_t>> &vecEventQsample, const std::vector<float> &vecEventSignal);

  void saveEventsToFile(const std::string &filename, std::vector<Kernel::V3D> &vecEventPos,
                        const std::vector<signal_t> &vecEventSignal, const std::vector<detid_t> &vecEventDetid);

  void getUBMatrix();

  void getRange(const std::vector<Kernel::V3D> &vec_hkl, std::vector<double> &extentMins,
                std::vector<double> &extentMaxs);

  API::IMDEventWorkspace_sptr m_outputWS;

  Kernel::Matrix<double> m_UB;
};

} // namespace MDAlgorithms
} // namespace Mantid
