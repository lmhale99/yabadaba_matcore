from yabadaba.record import Record

class TrainingMethod(Record):

    """
    Class for Material Core ml "training-method" fields
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'training_method'

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'training-method'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """
        
        self._add_value('str', 'training-procedure', valuerequired=True, modelpath='training-procedure',
                        description='The methodology used to determine the machine learning model\'s free parameters.')
        self._add_value('str', 'training_hyperparameters', modelpath='training-hyperparameters',
                        description='Documentation of the settings used in fitting the model.')
        self._add_value('str', 'transfer_learning', modelpath='transfer-learning',
                        description='Method used to migrate knowledge from previously mastered objectives to accelerate proficiency for the current machine learning task.')
        
        
        
    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True