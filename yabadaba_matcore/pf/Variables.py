from yabadaba.record import Record

from .ModelParameter import ModelParameter
from .FieldVariable import FieldVariable

class Variables(Record):

    """
    Class for Material Core pf "variables" fields
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'variables'

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'variables'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """
        
        self._add_value('recordlist', 'model_parameter',
                        recordclass = ModelParameter,
                        modelpath = 'model-parameter',
                        description = 'A specific, adjustable, or calibrated numeric value that controls certain aspects of the simulation.')
        
        self._add_value('recordlist', 'field_variable',
                        recordclass = FieldVariable,
                        modelpath = 'field-variable',
                        description = 'A specific, adjustable, or calibrated numeric value that controls certain aspects of the simulation.')

    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True