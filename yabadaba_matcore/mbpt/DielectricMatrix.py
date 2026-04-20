from yabadaba.record import Record

class DielectricMatrix(Record):

    """
    Class for Material Core mbpt "dielectric-matrix" fields
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'dielectric_matrix'

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'dielectric-matrix'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """
        
        self._add_value('float', 'planewave_basis_cutoff', valuerequired=True,
                        modelpath='planewave-basis-cutoff', unit='Ry',
                        description='For a planewave code, the basis set cutoff employed for the dielectric matrix. This is the same as the kinetic energy cutoff.')
        self._add_value('str', 'local_orbital_basis_set', valuerequired=True, modelpath='local-orbital-basis-set',
                        description='For local orbital codes, the name of the basis set.')
        self._add_value('str', 'frequency',
                        allowedvalues=('Hybertsen-Louie', 'Godby-Needs', 'Full frequency real axis',
                                       'Full frequency imaginary axis', 'Contour deformation', 'Spacetime'),
                        allowcustomvalue=True,
                        description='The method used to handle the frequency dependence of the Green\'s function, the screened Coulomb interaction, and their product.')
        self._add_value('int', 'response_basis_size', modelpath='response-basis-size',
                        description='For sum-over-states methods, the number of bands used in the sum. For linear-response methods, the number of dielectric eigenvalues.')
        self._add_value('intarray', 'q_points', valuerequired=True, modelpath='q-points', shape=(3,),
                        description='Brillouin zone grid used for sampling the dielectric matrix.')
        self._add_value('str', 'coulomb_truncation', modelpath='coulomb-truncation',
                        allowedvalues=('Ismail-Beigi', 'Rozzi', 'Spencer-Alavi'),
                        allowcustomvalue=True,
                        description='Method used to eliminate long-range Coulomb interactions between periodic replicas in supercell calculations.')
        
    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True