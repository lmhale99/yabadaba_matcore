
from .MatCore import MatCore
from .pf.ProblemSpecification import ProblemSpecification
from .pf.DomainAndMesh import DomainAndMesh
from .pf.NumericalMethod import NumericalMethod
from .pf.Variables import Variables

class MatCorePF(MatCore):

    """
    Class for managing MatCore-PF records
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'matcore_pf'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """
        super()._init_values()

        self._add_value('str', 'physical_phenomena',
                        valuerequired = True,
                        modelpath = 'physical-phenomena',
                        allowedvalues = (
                            'Isothermal solidification',
                            'Directional solidification',
                            'Isothermal annealing',
                            'Sintering',
                            'Twinning',
                            'Grain growth',
                            'Spinodal decomposition'),
                        allowcustomvalue = True,
                        description = 'Material process being modeled; description of the overarching processes and mechanisms being modeled/simulated.')
        
        self._add_value('recordsubset', 'problem_specification',
                        recordclass = ProblemSpecification,
                        valuerequired = True,
                        modelpath = 'problem-specification',
                        description = 'The fundamental mathematical and physical framework governing the phase field simulation, including the governing equations, thermodynamic free energy models, and time-evolution state.')
        
        self._add_value('recordsubset', 'domain_and_mesh',
                        recordclass = DomainAndMesh,
                        valuerequired = True,
                        modelpath = 'domain-and-mesh',
                        description = 'A comprehensive description of the machine learning approach and architecture used.')
        
        self._add_value('recordlist', 'numerical_method',
                        recordclass = NumericalMethod,
                        modelpath = 'numerical-method',
                        description = 'The information used for parameterizing the machine learning model.')
        
        self._add_value('recordlist', 'variables',
                        recordclass = Variables,
                        description = 'The approach used to determine the machine learning model\'s free parameters.')
        

    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True
