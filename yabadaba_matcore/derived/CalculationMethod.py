from yabadaba.record import Record

from .CalculationParameter import CalculationParameter

class CalculationMethod(Record):

    """
    Class for Material Core derived "calculation-method" fields
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'calculation_method'

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'calculation-method'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """
        
        self._add_value('str', 'description',
                        valuerequired = True,
                        description = 'Description of the method used to obtain the derived property.')
        
        self._add_value('recordlist', 'calculation_parameter',
                        recordclass = CalculationParameter,
                        modelpath = 'calculation-parameter',
                        description = 'A parameter associated with the specified calculation method.')
        
    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True