from yabadaba.record import Record

class FieldVariable(Record):

    """
    Class for Material Core PF "field-variable" fields
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'field_variable'

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'field-variable'

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
                        description = 'The designation of the field variable.')
        
        self._add_value('str', 'type',
                        valuerequired = True,
                        description = 'The kind of data associated with the field variable.')
        
        self._add_value('str', 'unit',
                        valuerequired = True,
                        allowedvalues = (
                            'Scalar',
                            'Vector',
                            'Tensor'
                        ),
                        allowcustomvalue = True,
                        description = 'A standardized string or identifier that defines the dimension or measurement system of the associated value.')
        
        self._add_value('str', 'description',
                        description = 'An explanation providing further clarification on the field variable.')
        
    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True
    