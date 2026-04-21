from yabadaba.record import Record

from .GoverningEquation import GoverningEquation
from .FreeEnergy import FreeEnergy

class ProblemSpecification(Record):

    """
    Class for Material Core pf "problem-specification" fields
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'problem_specification'

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'problem-specification'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """
        
        self._add_value('str', 'time_dependence',
                        valuerequired = True,
                        modelpath = 'time-dependence',
                        allowedvalues = (
                            'Property prediction',
                            'Transient evolution',
                            'Steady state',
                            'Stationary',
                            'Thermodynamic equilibrium'),
                        allowcustomvalue = True,
                        description = 'Description of the time-evolution state targeted by the simulation.')
        
        self._add_value('recordlist', 'governing_equation',
                        recordclass = GoverningEquation,
                        modelpath = 'governing-equation',
                        description = 'The specific phase field equation used to evolve a field variable.')
        
        self._add_value('recordsubset', 'free_energy',
                        recordclass = FreeEnergy,
                        modelpath = 'free-energy',
                        description = 'The thermodynamic free energy function used in the system.')
        
        self._add_value('strlist', 'additional_energy_contribution',
                        modelpath = 'additional-energy-contribution',
                        allowedvalues = (
                            'Elasticity',
                            'Plasticity',
                            'Electrical',
                            'Magnetic',
                            'Fluid-Solid-Interaction',
                            'Solid-Solid-Interaction'),
                        allowcustomvalue = True,
                        description = 'Physical contributions to the free energy function.')

    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True