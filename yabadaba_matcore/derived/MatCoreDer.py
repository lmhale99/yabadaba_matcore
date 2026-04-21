from yabadaba.record import Record

from .DerivedProperty import DerivedProperty

class MatCoreDer(Record):

    """
    Class for managing the MatCore-Der fields
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'matcore_der'
    
    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """

        self._add_value('recordlist', 'derived_property',
                        recordclass = DerivedProperty,
                        valuerequired = True,
                        modelpath = 'derived-property',
                        description = 'Details of a quantity related to material behavior computed based on a computational materials science (CMS) calculation covered by the MatCore standard.')
        

    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True
