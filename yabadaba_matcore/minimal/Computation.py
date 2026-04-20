from yabadaba.record import Record

from .Software import Software
from .SimulationConditions import SimulationConditions

class Computation(Record):

    """
    Class for Material Core "computation" fields
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'computation'

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'computation'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """
        
        self._add_value('str', 'method_class', valuerequired=True, modelpath='method-class',
                        allowedvalues=('Electronic', 'Atomistic', 'Mesoscopic', 'Continuum',
                                       'Data-driven'), allowcustomvalue=True,
                        description='The general category to which the computational technique belongs.')
        self._add_value('str', 'method',
                        allowedvalues=('CC', 'QMC', 'DFT', 'MBPT', 'MC', 'MD',
                                       'DDD', 'KMC', 'CGMD', 'PF', 'ML'),
                                       allowcustomvalue=True,
                        description='The computational materials science (CMS) approach used in the computation.')
        self._add_value('recordsubset', 'simulation_conditions', 
                        recordclass=SimulationConditions, valuerequired=True,
                        modelpath='simulation-conditions',
                        description='The interactions between the system being modeled and the rest of the world maintained during the computation.')
        self._add_value('recordlist', 'software', recordclass=Software, valuerequired=True,
                        description='Identification of a computer package used to perform the calculations.')
        
    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True
