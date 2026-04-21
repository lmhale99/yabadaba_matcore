
from .MatCoreDFT import MatCoreDFT
from .mbpt.MBPTMethod import MBPTMethod
from .mbpt.DielectricMatrix import DielectricMatrix
from .mbpt.BSEHamiltonian import BSEHamiltonian

class MatCoreMBPT(MatCoreDFT):

    """
    Class for managing MatCore-MBPT records
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'matcore_mbpt'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """
        super()._init_values()

        self._add_value('recordlist', 'mbpt_method',
                        recordclass = MBPTMethod,
                        valuerequired = True,
                        modelpath = 'mbpt-method',
                        description = 'The many-body perturbation theory (MBPT) approach used and associated settings.')
        
        self._add_value('str', 'starting_point',
                        valuerequired = True,
                        modelpath = 'starting-point',
                        allowedvalues = (
                            'LDA',
                            'GGA',
                            'Meta GGA',
                            'Hybrid GGA',
                            'DFT+U'),
                        allowcustomvalue = True,
                        description = 'The density functional theory (DFT) exchange-correlation functional used to generate Kohn-Sham wavefunctions and eigenvalues for the Green\'s function and the screened Coulomb interaction.')
        
        self._add_value('recordsubset', 'dielectric_matrix',
                        recordclass = DielectricMatrix,
                        valuerequired = True,
                        modelpath = 'dielectric-matrix',
                        description = 'Information on the dielectric matrix used to compute the screened Coulomb interaction W.')
        
        self._add_value('int', 'gw_bands',
                        modelpath = 'gw-bands',
                        description = 'Number of bands for which the GW correction is evaluated.')
        
        self._add_value('recordsubset', 'bse_hamiltonian',
                        recordclass = BSEHamiltonian,
                        modelpath = 'bse-hamiltonian',
                        description = 'A collective descriptor for the parameters defining the construction, dimensionality, and solution method of the effective excitonic Bethe-Salpeter Hamiltonian that is being solved in a BSE calculation. It characterizes the Hilbert space size and the physical constraints (momentum and spin) applied during the diagonalization.')
        
        self._add_value('str', 'bse_kernel_truncation',
                        modelpath = 'bse-kernel-truncation',
                        allowedvalues = (
                            'Ismail-Beigi',
                            'Rozzi',
                            'Spencer-Alavi'),
                        allowcustomvalue = True,
                        description = 'Method used to eliminate long-range Coulomb interactions between periodic replicas in the BSE Coulomb kernel.')

    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True
