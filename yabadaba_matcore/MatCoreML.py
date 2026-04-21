
from .MatCore import MatCore
from .ml.MLTask import MLTask
from .ml.MLModel import MLModel
from .ml.TrainingData import TrainingData
from .ml.TrainingMethod import TrainingMethod
from .ml.ModelPerformance import ModelPerformance

class MatCoreML(MatCore):

    """
    Class for managing MatCore-ML records
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'matcore_ml'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """
        super()._init_values()

        self._add_value('recordlist', 'ml_task',
                        recordclass = MLTask,
                        valuerequired = True,
                        modelpath = 'ml-task',
                        description = 'Characterization of the machine learning process performed.')
        
        self._add_value('recordsubset', 'ml_model',
                        recordclass = MLModel,
                        valuerequired = True,
                        modelpath = 'ml-model',
                        description = 'A comprehensive description of the machine learning approach and architecture used.')
        
        self._add_value('recordlist', 'training_data',
                        recordclass = TrainingData,
                        modelpath = 'training-data',
                        description = 'The information used for parameterizing the machine learning model.')
        
        self._add_value('recordsubset', 'training_method',
                        recordclass = TrainingMethod,
                        modelpath = 'training-method',
                        description = 'The approach used to determine the machine learning model\'s free parameters.')
        
        self._add_value('recordsubset', 'model_performance',
                        recordclass = ModelPerformance,
                        modelpath = 'model-performance',
                        description = 'An assessment of the reliability of the machine learning results.')
        
        self._add_value('str', 'interpretability_method',
                        modelpath = 'interpretability-method',
                        description = 'A technique used to understand the cause-and-effect relationships within the machine learning model\'s inputs and outputs.')

    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True
