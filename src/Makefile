.NOTPARALLEL:
# Disable all of make's built-in rules (similar to Fortran's implicit none)
MAKEFLAGS += --no-builtin-rules --no-builtin-variables

# Compiler settings
fortran_compiler ?= gfortran 
# compiler_flags := /debug /Od /Qdiag-disable:10448 /check:all /traceback
# compiler_flags := /Qdiag-disable:10448 /nologo /debug:full /O2 /assume:buffered_io /fpp /DDebug /reentrancy:threaded /free /warn:all /real-size:64 /Qauto /fpe:0 /fp:strict /fpconstant /module:"Debug\\" /object:"Debug\\" /Fd"Debug\vc160.pdb" /check:pointer /check:bounds /check:uninit /check:format /check:output_conversion /check:stack /libs:static /threads /Qmkl:sequential /c

# Select the operating system
ifeq ($(OS),Windows_NT)
    # Windows
    compiler_flags := /Qdiag-disable:10448 /nologo /debug:full /O2 /assume:buffered_io /fpp /DDebug /reentrancy:threaded /free /warn:all /real-size:64 /Qauto /fpe:0 /fp:strict /fpconstant /check:pointer /check:bounds /check:uninit /check:format /check:output_conversion /check:stack /libs:static /threads #/Qmkl:sequential /c
    EXE = .exe
else
    # Assume Linux
    compiler_flags := -O0 -g -traceback -check all -warn all -free -fpp
    EXE = .out
endif 

# set the files to remove
remove_files_command := rm -f

# list of all source files
source_files := ./GlobalConstants.FOR \
        ./Soilmodels/A3DLinearElasticity.f \
        ./Soilmodels/A3DMohrCoulombStandard.f \
        ./GeoMath.FOR \
        ./MatrixMath.FOR \
        ./FileIO.for \
        ./String.for \
        ./Counters.FOR \
        ./Feedback.for \
        ./ReadCalculationData.FOR \
        ./ElemCalcTETRA.FOR \
        ./ElemCalcQUAD.FOR \
        ./Soilmodels/A3DBingham.f \
        ./ReadMaterialData.FOR \
        ./ElemCalcTRI.FOR \
        ./getversion.for \
        ./InitialiseKernel.FOR \
        ./ElemCalc.FOR \
        ./MeshInfo.FOR \
        ./ReadGeometryData.FOR \
        ./ISORT.FOR \
        ./ElemConnections.FOR \
        ./Particle.FOR \
        ./MPMData.FOR \
        ./RotBoundCond.FOR \
        ./MPMStresses.FOR \
        ./MPMDynViscousBoundary.FOR \
        ./TwoLayerFormulation.FOR \
        ./MPMDYN2PhaseSP.FOR \
        ./MPMDYN3PhaseSP.FOR \
        ./MPMDynContact.FOR \
        ./ReadMPMData.FOR \
        ./WriteMPMData.FOR \
        ./MPMMeshAdjustment.FOR \
        ./MPMConvPhase.FOR \
        ./WriteTestData.FOR \
        ./MPMEmptyElements.FOR \
        ./InitialiseElementType.for \
        ./AdjustParticleDiscretisation.FOR \
        ./MPMInit.FOR \
        ./MPMDYNBTSig.FOR \
        ./RigidBody.f \
        ./LagrangianPhase.FOR \
        ./Liquid.FOR \
        ./ExternalSoilModel.for \
        ./MPMStrainSmoothing.FOR \
        ./MPMDYNStresses.FOR \
        ./MPMDYNConvPhase.FOR \
        ./MPMExcavation.FOR \
        ./BuildBJacDet.FOR \
        ./BuildDElastic.FOR \
        ./BuildLoad.FOR \
        ./GetPrinStress.FOR \
        ./GetStrain.FOR \
        ./timing.for \
        ./ReadOutputData.FOR \
        ./WriteVTKASCII.FOR \
        ./WriteVTKBinary.FOR \
        ./WriteVTKOutput.FOR \
        ./WriteVTK2Layer.FOR \
        ./WriteNodalData.FOR \
        ./WriteResultData.FOR \
        ./ErrorHandler.for \
        ./MPMDynamicExplicit.FOR \
        ./MPMConstruction.FOR \
        ./Kernel.for \
        ./Anura3D.for

# Target executable
TARGET := Anura3D$(EXE)

all:
	@echo "Compiling in order..."
	for file in $(source_files); do \
		$(fortran_compiler) $(compiler_flags) -c $$file || exit 1; \
	done
	@echo "Linking..."
	$(fortran_compiler) $(compiler_flags) *.o -o $(TARGET)

# Phony target for cleaning
.PHONY: clean
clean:
	$(remove_files_command) *.o *.mod *genmod*.f90 *.pdb *.ilk $(TARGET)
