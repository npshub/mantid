// Mantid Repository : https://github.com/mantidproject/mantid
//
// Copyright &copy; 2019 ISIS Rutherford Appleton Laboratory UKRI,
//   NScD Oak Ridge National Laboratory, European Spallation Source,
//   Institut Laue - Langevin & CSNS, Institute of High Energy Physics, CAS
// SPDX - License - Identifier: GPL - 3.0 +
#pragma once

#include "IndirectDataValidationHelper.h"
#include "IndirectMomentsModel.h"
#include "MantidAPI/AnalysisDataService.h"
#include "MantidFrameworkTestHelpers/WorkspaceCreationHelper.h"
#include <cxxtest/TestSuite.h>
#include <gmock/gmock.h>

using namespace MantidQt::CustomInterfaces;

class IndirectMomentsModelTest : public CxxTest::TestSuite {
public:
  /// Needed to make sure everything is initialized
  IndirectMomentsModelTest() = default;

  void setUp() override { m_model = std::make_unique<IndirectMomentsModel>(); }

  void test_algorrithm_set_up() {
    // The Moments algorithm is a python algorithm and so can not be called in
    m_workspace = WorkspaceCreationHelper::create2DWorkspace(5, 4);
    Mantid::API::AnalysisDataService::Instance().addOrReplace("Workspace_name_sqw", m_workspace);
    m_model->setInputWorkspace("Workspace_name");
    m_model->setEMin(-0.4);
    m_model->setEMax(0.4);
    m_model->setScale(false);
  }

  void test_output_workspace() {
    m_model->setInputWorkspace("Workspace_name_sqw");
    auto outputWorkspaceName = m_model->getOutputWorkspace();
    TS_ASSERT(outputWorkspaceName == "Workspace_name_Moments");
  }

private:
  MatrixWorkspace_sptr m_workspace;
  std::unique_ptr<IndirectMomentsModel> m_model;
};
