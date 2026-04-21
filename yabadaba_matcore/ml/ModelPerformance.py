from yabadaba.record import Record

class ModelPerformance(Record):

    """
    Class for Material Core ml "model-performance" fields
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'model_performance'

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'model-performance'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """
        
        self._add_value('str', 'validation',
                        valuerequired = True,
                        description = 'A description of the approach used to determine the reliability of the obtained machine learning results.')
        
        self._add_value('str', 'uncertainty_quantification',
                        modelpath = 'uncertainty-quantification',
                        description = 'The method or process used to identify and measure the range of possible outcomes to assess the reliability of machine learning model predictions.')

    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True