from yabadaba.record import Record

class TrainingData(Record):

    """
    Class for Material Core ml "training-data" fields
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'training_data'

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'training-data'

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
                        description = 'Name of the training dataset used to train in the machine learning model.')
        
        self._add_value('str', 'contents',
                        valuerequired = True,
                        description = 'Description of the information included in the training dataset.')
        
        self._add_value('str', 'source',
                        description = 'Location from which the training data was obtained.')
        
        self._add_value('str', 'size',
                        description = 'Number of items in the training dataset.')
        
        self._add_value('str', 'data_preprocessing',
                        modelpath = 'data-preprocessing',
                        description = 'Approach used for preliminary refining of raw, unformatted, or incomplete information into a structured and clean state suitable for modeling or analysis.')
        
        self._add_value('str', 'missing_data',
                        modelpath = 'missing-data',
                        description = 'Documentation of incomplete, null, or unrecorded entries within a feature set that hinder algorithm training.')
        
        self._add_value('str', 'missing_data_strategy',
                        modelpath = 'missing-data-strategy',
                        description = 'Approach used for filling in or removing blank, null, or unknown entries in a dataset.')
        
        self._add_value('str', 'outlier_handling',
                        modelpath = 'outlier-handling',
                        description = 'Approach to identifying and addressing extreme observations that deviate significantly from the general distribution to ensure they do not disproportionately skew model training.')
        
        self._add_value('str', 'dataset_split',
                        modelpath = 'dataset-split',
                        description = 'A description of how information used to train the machine learning model was divided into subsets as part of the training process.')
        
    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True