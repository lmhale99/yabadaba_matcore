
from .MatCore import MatCore
from .dft.XCFunctional import XCFunctional
from .dft.CoreElectronModel import CoreElectronModel
from .dft.ValenceElectronModel import ValenceElectronModel
from .dft.KPointMesh import KPointMesh
from .dft.SelfConsistentFieldConvergence import SelfConsistentFieldConvergence

class MatCoreDFT(MatCore):

    """
    Class for managing MatCore-DFT records
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'matcore_dft'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """
        super()._init_values()

        self._add_value('recordlist', 'xc_functional',
                        recordclass = XCFunctional,
                        valuerequired = True,
                        modelpath = 'xc-functional',
                        description = 'Approximation used to describe the electron exchange and electron correlation energies')
        
        self._add_value('recordsubset', 'core_electron_model',
                        recordclass = CoreElectronModel,
                        valuerequired = True,
                        modelpath = 'core-electron-model',
                        description = 'Model of the electrons used in the calculation.')
        
        self._add_value('recordsubset', 'valence_electron_model',
                        recordclass = ValenceElectronModel,
                        valuerequired = True,
                        modelpath = 'valence-electron-model',
                        description = 'The elementary functions used for expanding electronic wave functions.')
        
        self._add_value('strlist', 'calculation_physics',
                        modelpath = 'calculation-physics',
                        allowedvalues = (
                            'Relativistic effects',
                            'Spin polarization',
                            'Noncollinear spin polarization',
                            'On-site correlation',
                            'Van der Waals'),
                        allowcustomvalue = True,
                        description = 'Additional phenomena included beyond the standard DFT calculation.')
        
        self._add_value('recordsubset', 'k_point_mesh',
                        recordclass = KPointMesh,
                        modelpath = 'k-point-mesh',
                        description = 'For periodic systems, a grid of points sampled within the Brillouin zone, used to approximate integrals and calculate electronic properties by discretizing the wavefunction across reciprocal space.')
        
        self._add_value('recordsubset', 'self_consistent_field_convergence',
                        recordclass = SelfConsistentFieldConvergence,
                        modelpath = 'self-consistent-field-convergence',
                        description = 'Method and termination criteria defining the precision of self-consistent solution of the Kohn-Sham equations.')
        
        self._add_value('float', 'relaxation_tolerance_energy',
                        modelpath = 'relaxation-tolerance-energy',
                        #unit = 'eV',
                        description = 'Total energy convergence criterion for atomic relaxation.')
        
        self._add_value('float', 'relaxation_tolerance_forces',
                        modelpath = 'relaxation-tolerance-forces',
                        #unit = 'eV/angstrom',
                        description = 'Maximum force convergence criterion for atomic relaxation.')
        
        self._add_value('strlist', 'comment',
                        description = 'Additional information on the DFT calculation. For example, non-self-consistent constraints, such as details about imposed state occupation or moment freezing.')

    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True
