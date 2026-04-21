from yabadaba.record import Record

from .ComputationParameter import ComputationParameter

class MDComputation(Record):

    """
    Class for Material Core MD "computation" fields
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'md_computation'

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'md-computation'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """
        
        self._add_value('str', 'mode',
                        valuerequired = True,
                        allowedvalues = (
                            'Static',
                            'Minimization',
                            'Equilibrium dynamics', 
                            'Nonequilibrium dynamics',
                            'Free energy'),
                        allowcustomvalue = True,
                        description = 'The type of the molecular dynamics simulation performed.')
        
        self._add_value('str', 'algorithm',
                        allowedvalues = (
                            'Simplex',
                            'Damped dynamics',
                            'FIRE',
                            'Steepest descent',
                            'Conjugate gradients',
                            'BFGS',
                            'Simulated annealing',
                            'SGLD',
                            'Leap frog',
                            'Runge-Kutta',
                            'Velocity Verlet', 
                            'Verlet',
                            'Harmonic',
                            'Metadynamics',
                            'PMF', 
                            'Thermodynamic integration',
                            'Umbrella sampling'),
                        allowcustomvalue = True,
                        description = 'The computational method used to perform the computation.')
        
        self._add_value('recordlist', 'computation_parameter',
                        recordclass = ComputationParameter,
                        modelpath = 'computation-parameter',
                        description = 'The interactions between the system being modeled and the rest of the world maintained during the computation.')
        
        self._add_value('str', 'initialization',
                        description = 'Information on the conditions set at the start of the simulation.')
        
    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True
