from yabadaba.record import Record

class MLModel(Record):

    """
    Class for Material Core ml "ml-model" fields
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'ml_model'

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'ml-model'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """
        
        self._add_value('str', 'algorithm', valuerequired=True,
                        description='The machine learning method used.')
        self._add_value('strlist', 'target_variable', valuerequired=True,
                        modelpath='target-variable',
                        description='The desired output or answer the machine learning model aims to predict.')
        self._add_value('strlist', 'input_feature', modelpath='input-feature',
                        description='Information provided to the machine learning method.')
        self._add_value('str', 'model_architecture', modelpath='model-architecture',
                        description='A description of the network topology used by the specified algorithm.')
        self._add_value('str', 'model_size', modelpath='model-size',
                        description='A measure of the magnitude of the machine learning architecture.')
        
        
    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True