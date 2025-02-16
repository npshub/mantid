set(SRC_FILES
    src/Communicator.cpp
    src/ExecutionMode.cpp
    src/IO/Chunker.cpp
    src/IO/EventLoader.cpp
    src/IO/EventParser.cpp
    src/IO/EventsListsShmemManager.cpp
    src/IO/EventsListsShmemStorage.cpp
    src/IO/MultiProcessEventLoader.cpp
    src/IO/NXEventDataLoader.cpp
    src/IO/EventLoaderChild.cpp
    src/Request.cpp
    src/StorageMode.cpp
    src/ThreadingBackend.cpp
    src/IO/EventLoaderHelpers.cpp
)

set(INC_FILES
    inc/MantidParallel/Collectives.h
    inc/MantidParallel/Communicator.h
    inc/MantidParallel/ExecutionMode.h
    inc/MantidParallel/IO/Chunker.h
    inc/MantidParallel/IO/EventDataPartitioner.h
    inc/MantidParallel/IO/EventLoader.h
    inc/MantidParallel/IO/EventLoaderHelpers.h
    inc/MantidParallel/IO/EventParser.h
    inc/MantidParallel/IO/EventsListsShmemManager.h
    inc/MantidParallel/IO/EventsListsShmemStorage.h
    inc/MantidParallel/IO/MultiProcessEventLoader.h
    inc/MantidParallel/IO/NXEventDataLoader.h
    inc/MantidParallel/IO/NXEventDataSource.h
    inc/MantidParallel/IO/PulseTimeGenerator.h
    inc/MantidParallel/Nonblocking.h
    inc/MantidParallel/Request.h
    inc/MantidParallel/Status.h
    inc/MantidParallel/StorageMode.h
    inc/MantidParallel/ThreadingBackend.h
)

set(TEST_FILES
    ChunkerTest.h
    CollectivesTest.h
    CommunicatorTest.h
    EventDataPartitionerTest.h
    EventLoaderTest.h
    EventParserTest.h
    ExecutionModeTest.h
    NonblockingTest.h
    ParallelRunnerTest.h
    PulseTimeGeneratorTest.h
    RequestTest.h
    StorageModeTest.h
    ThreadingBackendTest.h
)

if(COVERAGE)
  foreach(loop_var ${SRC_FILES} ${INC_FILES})
    set_property(GLOBAL APPEND PROPERTY COVERAGE_SRCS "${CMAKE_CURRENT_SOURCE_DIR}/${loop_var}")
  endforeach(loop_var)
endif()

# Add the target for this directory
add_library(Parallel ${SRC_FILES} ${INC_FILES})
add_library(Mantid::Parallel ALIAS Parallel)
add_dependencies(Parallel EventParallelLoader Mantid::Kernel)

target_include_directories(
  Parallel PUBLIC $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/inc> $<INSTALL_INTERFACE:include/Mantid>
)

# Set the name of the generated library
set_target_properties(Parallel PROPERTIES OUTPUT_NAME MantidParallel COMPILE_DEFINITIONS IN_MANTID_PARALLEL)

if(${CMAKE_SYSTEM_NAME} MATCHES "Darwin")
  set_target_properties(Parallel PROPERTIES INSTALL_RPATH "@loader_path/../MacOS;@loader_path/../Frameworks")
elseif(${CMAKE_SYSTEM_NAME} STREQUAL "Linux")
  set_target_properties(Parallel PROPERTIES INSTALL_RPATH "\$ORIGIN/../${LIB_DIR}")
endif()

# Add to the 'Framework' group in VS
set_property(TARGET Parallel PROPERTY FOLDER "MantidFramework")

target_link_libraries(Parallel PUBLIC Mantid::Kernel Boost::serialization)

if(UNIX AND NOT APPLE)
  target_link_libraries(Parallel PRIVATE rt)
endif()

# Add executable for Nexus parallel loader child process
add_executable(EventParallelLoader ${SRC_FILES} ${INC_FILES})

target_include_directories(
  EventParallelLoader PUBLIC $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/inc> $<INSTALL_INTERFACE:include/Mantid>
)
add_dependencies(EventParallelLoader Mantid::Kernel)
# set the name of generated executable
set_target_properties(
  EventParallelLoader PROPERTIES OUTPUT_NAME MantidNexusParallelLoader COMPILE_DEFINITIONS IN_MANTID_PARALLEL
)

if(${CMAKE_SYSTEM_NAME} MATCHES "Darwin")
  set_target_properties(EventParallelLoader PROPERTIES INSTALL_RPATH "@loader_path/../MacOS;@loader_path/../Frameworks")
elseif(${CMAKE_SYSTEM_NAME} STREQUAL "Linux")
  set_target_properties(EventParallelLoader PROPERTIES INSTALL_RPATH "\$ORIGIN/../${LIB_DIR}")
endif()

# Add to the 'Framework' group in VS
set_property(TARGET EventParallelLoader PROPERTY FOLDER "MantidFramework")

target_link_libraries(
  EventParallelLoader
  PUBLIC Mantid::Kernel
  PRIVATE Boost::serialization
)

if(UNIX AND NOT APPLE)
  target_link_libraries(EventParallelLoader PRIVATE rt)
endif()

# Add the unit tests directory
add_subdirectory(test)

# Installation settings
if(CONDA_ENV)
  set(TARGET_EXPORT_NAME "MantidParallelTargets")
  mtd_install_framework_lib(TARGETS Parallel EXPORT_NAME ${TARGET_EXPORT_NAME})
else()
  mtd_install_targets(TARGETS Parallel INSTALL_DIRS ${LIB_DIR} ${WORKBENCH_LIB_DIR})
endif()

mtd_install_targets(TARGETS EventParallelLoader INSTALL_DIRS ${LIB_DIR} ${WORKBENCH_LIB_DIR})
