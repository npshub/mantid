// Mantid Repository : https://github.com/mantidproject/mantid
//
// Copyright &copy; 2018 ISIS Rutherford Appleton Laboratory UKRI,
//   NScD Oak Ridge National Laboratory, European Spallation Source,
//   Institut Laue - Langevin & CSNS, Institute of High Energy Physics, CAS
// SPDX - License - Identifier: GPL - 3.0 +
#include "MantidParallel/ExecutionMode.h"

namespace Mantid::Parallel {

/// Returns the corresponding ExecutionMode for a given StorageMode.
ExecutionMode getCorrespondingExecutionMode(StorageMode storageMode) {
  switch (storageMode) {
  case StorageMode::Cloned:
    return ExecutionMode::Identical;
  case StorageMode::Distributed:
    return ExecutionMode::Distributed;
  case StorageMode::MasterOnly:
    return ExecutionMode::MasterOnly;
  default:
    return ExecutionMode::Invalid;
  }
}

/// Returns a human-readable string representation of an ExecutionMode.
std::string toString(ExecutionMode mode) {
  switch (mode) {
  case ExecutionMode::Invalid:
    return "Parallel::ExecutionMode::Invalid";
  case ExecutionMode::Serial:
    return "Parallel::ExecutionMode::Serial";
  case ExecutionMode::Identical:
    return "Parallel::ExecutionMode::Identical";
  case ExecutionMode::Distributed:
    return "Parallel::ExecutionMode::Distributed";
  case ExecutionMode::MasterOnly:
    return "Parallel::ExecutionMode::MasterOnly";
  default:
    return "Parallel::ExecutionMode::<undefined>";
  }
}

} // namespace Mantid::Parallel
