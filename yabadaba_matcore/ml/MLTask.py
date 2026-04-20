from yabadaba.record import Record

class MLTask(Record):

    """
    Class for Material Core ml "ml-task" fields
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'ml_task'

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'ml-task'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """
        
        self._add_value('strlist', 'type', valuerequired=True,
                        allowedvalues=('Property prediction', 'Structure prediction',
                                       'Structure generation', 'Synthesis prediction',
                                       'Material ranking', 'Clustering', 'Embedding'),
                        allowcustomvalue=True,
                        description='The nature of the machine learning task.')
        self._add_value('str', 'description',
                        description='Explanation of the machine learning task performed.')
        
    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True