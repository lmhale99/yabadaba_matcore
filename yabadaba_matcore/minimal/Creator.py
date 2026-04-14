from yabadaba.record import Record

class Creator(Record):

    """
    Class for Material Core "creator" fields
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'creator'

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'creator'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """
        
        self._add_value('str', 'name', valuerequired=True,
                        description='The name of the author who generated the data.')
        self._add_value('str', 'affiliation', valuerequired=True,
                        description='The affiliation of the author who generated the data.')
        
    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True