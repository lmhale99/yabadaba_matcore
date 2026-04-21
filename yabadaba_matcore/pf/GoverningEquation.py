from yabadaba.record import Record

class GoverningEquation(Record):

    """
    Class for Material Core pf "governing-equation" fields
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'governing_equation'

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'governing-equation'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """
        self._add_value('str', 'type',
                        valuerequired = True,
                        allowedvalues = (
                            'CH',
                            'AC',
                            'GP',
                            'FID',
                            'PFC',
                            'Fluid',
                            'Muilti',
                            'Coupled',
                            'Diffuse'),
                        allowcustomvalue = True,
                        description = 'The mathematical classification of the phase field equation.')
        
        self._add_value('str', 'evolved_variable',
                        valuerequired = True,
                        modelpath = 'evolved-variable',
                        description = 'The name of the field-variable that this equation solves for.')
        
        self._add_value('strlist', 'driving_energy',
                        modelpath = 'driving-energy',
                        description = 'A free energy component that acts as a forcing term in this equation.')

    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True