from yabadaba.record import Record

class BSEHamiltonian(Record):

    """
    Class for Material Core mbpt "bse-hamiltonian" fields
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'bse_hamiltonian'

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'bse-hamiltonian'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """
        
        self._add_value('int', 'number_valence_bands',
                        modelpath = 'number-valence-bands',
                        description = 'Number of valence bands included in the BSE Hamiltonian.')
        
        self._add_value('int', 'number_conduction_bands',
                        modelpath = 'number-conduction-bands',
                        description = 'Number of conduction bands included in the BSE Hamiltonian.')
        
        self._add_value('intarray', 'k_point_mesh',
                        modelpath = 'k-point-mesh',
                        shape = (3,),
                        description = 'Brillouin zone grid used for building the BSE Hamiltonian.')
        
        self._add_value('floatarray', 'exciton_momentum',
                        modelpath = 'exciton-momentum',
                        shape = (3,),
                        description = 'Crystal momentum of the exciton in the BSE calculation.')
        
        self._add_value('str', 'exciton_multiplicity',
                        modelpath = 'exciton-multiplicity',
                        allowedvalues = (
                            'Singlet',
                            'Triplet'),
                        allowcustomvalue = True,
                        description = 'Specification whether the BSE calculation is performed for singlet or triplet excitons.')
        
        self._add_value('str', 'diagonalization', 
                        allowedvalues = (
                            'Tamm-Dancoff',
                            'Full diagonalization'),
                        allowcustomvalue = True,
                        description = 'Approximation method used to diagonalize the BSE Hamiltonian.')
        
        self._add_value('int', 'number_lowest_eigenvalues',
                        modelpath = 'number-lowest-eigenvalues',
                        description = 'Number of lowest eigenvalues computed by solving the BSE Hamiltonian.')
        
    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True