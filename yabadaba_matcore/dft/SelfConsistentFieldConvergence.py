from yabadaba.record import Record


class SelfConsistentFieldConvergence(Record):

    """
    Class for Material Core DFT "self-consistent-field-convergence" fields
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'self_consistent_field_convergence'

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'self-consistent-field-convergence'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """
        
        self._add_value('str', 'method',
                        allowedvalues=('Simple mixing', 'Pulay mixing', 'Blocked Davidson', 'DIIS', 'BFGS'),
                        allowcustomvalue=True,
                        description='The self-consistent field mixing and/or extrapolation scheme for the iterative solution of the Kohn-Sham equations.')
        self._add_value('float', 'tolerance', valuerequired=True,
                        description='Convergence criterion for the self-consistent loop.')

        
    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True