from yabadaba.record import Record

class MagneticInteractions(Record):

    """
    Class for Material Core MD "magnetic-interactions" fields
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'magnetic_interactions'

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'magnetic-interactions'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """
        
        self._add_value('str', 'spin_style',
                        valuerequired = True,
                        modelpath = 'spin-style',
                        allowedvalues = (
                            'Classical spin dynamics',
                            'Coupled spinlattice dynamics',
                            'Ab initio spin dynamics',
                            'Tight binding spin dynamics',
                            'Quantum spin dynamics'),
                        allowcustomvalue = True,
                        description = 'The nature of the magnetic spins associated with the particles.')

        self._add_value('str', 'magnetic_dipole',
                        modelpath = 'magnetic-dipole',
                        description = 'Attribute specifying the type of interaction (spin Hamiltonian) between the magnetic dipoles associated with particles.')
        
    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True
    