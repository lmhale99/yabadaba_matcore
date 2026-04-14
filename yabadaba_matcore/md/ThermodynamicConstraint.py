from yabadaba.record import Record

from .TDParameter import TDParameter

class ThermodynamicConstraint(Record):

    """
    Class for Material Core MD "thermodynamic-constraint" fields
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'thermodynamic_constraint'

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'thermodynamic-constraint'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """
        
        self._add_value('str', 'system', valuerequired=True,
                        description='The collection of particles to which the constraint is applied.')
        self._add_value('str', 'type',
                        description='The nature of the imposed thermodynamic constraint.')
        self._add_value('str', 'method',
                        description=' The name of the approach used to impose the constraint.')
        self._add_value('str', 'description',
                        description='Explanatory text about the constraint and method used to impose it.')
        self._add_value('recordlist', 'td_parameter', recordclass=TDParameter, modelpath='td-parameter',
                        description='A fixed variable associated with the specified thermodynamic constraint.')
        
    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True
    
    def add_td_parameter(self, **kwargs):
        """Adds a td_parameter to the record"""
        self.get_value('td_parameter').append(**kwargs)

    def td_parameter_df(self):
        """Generates a pandas DataFrame of the td_parameter information"""
        return self.get_value('td_parameter').metadata_df()
