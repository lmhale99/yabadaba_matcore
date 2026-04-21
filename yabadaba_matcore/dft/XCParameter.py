from yabadaba.record import Record


class XCParameter(Record):

    """
    Class for Material Core DFT "xc-parameter" fields
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'xc_parameter'

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'xc-parameter'

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
                        description = 'The designation of the exchange-correlation parameter.')
        
        self._add_value('str', 'value',
                        valuerequired = True,
                        description = 'The data associated with the exchange-correlation parameter.')
        
        self._add_value('str', 'unit',
                        valuerequired = True,
                        description = 'A standardized string or identifier that defines the dimension or measurement system of the associated value.')
        
        self._add_value('str', 'description',
                        description = 'An explanation of the meaning, source, or purpose of the parameter.')

    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True