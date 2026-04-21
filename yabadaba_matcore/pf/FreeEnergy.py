from yabadaba.record import Record

class FreeEnergy(Record):

    """
    Class for Material Core pf "free-energy" fields
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'free_energy'

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'free-energy'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """
        
        self._add_value('str', 'name',
                        valuerequired = True,
                        description = 'The identifier or symbol used for this specific energy functional.')
        
        self._add_value('str', 'description',
                        valuerequired = True,
                        allowedvalues = (
                            'Ideal',
                            'Regular',
                            'Flory',
                            'Calphad',
                            'Poly',
                            'Non-polynomial'),
                        allowcustomvalue = True,
                        description = 'The type/derivation of the thermodynamic bulk free energy function.')
        
        self._add_value('str', 'expression',
                        description = 'The exact mathematical formulation of the phase field functional.')
        
        self._add_value('str', 'unit',
                        description = 'The physical unit of the free energy density.')
        
        
        
    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True