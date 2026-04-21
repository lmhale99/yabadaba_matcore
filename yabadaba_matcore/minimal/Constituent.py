from yabadaba.record import Record

class Constituent(Record):

    """
    Class for Material Core "constituent" fields
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'constituent'

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'constituent'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """
        
        self._add_value('str', 'species',
                        valuerequired = True,
                        description = 'A chemical element included in the material.')
        
        self._add_value('str', 'concentration',
                        valuerequired = True,
                        description = 'The fraction of the material composed of this element.')

    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True