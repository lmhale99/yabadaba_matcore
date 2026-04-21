from yabadaba.record import Record

from .GridSpacing import GridSpacing
from .TimeStepSize import TimeStepSize

class NumericalMethod(Record):

    """
    Class for Material Core pf "numerical-method" fields
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'numerical_method'

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'numerical-method'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """
        self._add_value('str', 'spatial_discretization',
                        valuerequired = True,
                        modelpath = 'spatial-discretization',
                        allowedvalues = (
                            'FDM',
                            'FEM',
                            'FVM',
                            'LBM',
                            'Particle',
                            'Spectral'),
                        allowcustomvalue = True,
                        description = 'The numerical approach used to convert continuous governing equations into a system of algebraic equations defined over a discrete mesh or set of points within the computational domain.')
        
        self._add_value('int', 'spatial_accuracy_order',
                        modelpath = 'spatial-accuracy-order',
                        description = 'The exponent of the grid spacing parameter () determining the rate at which the discretization error approaches zero as the mesh is refined.')
        
        self._add_value('str', 'temporal_discretization',
                        modelpath = 'temporal-discretization',
                        allowedvalues = (
                            'Forward Euler',
                            'Backward Euler',
                            'Adams Bashforth',
                            'Implicit',
                            'Explicit',
                            'Crank-Nicholson',
                            'Runge-Kutta',
                            'Mixed'),
                        allowcustomvalue = True,
                        description = 'The algorithm, step-size approach, and integration order used to advance a simulation, governing equation in time.')
        
        self._add_value('int', 'temporal_accuracy_order',
                        modelpath = 'temporal-accuracy-order',
                        description = 'The exponent of the time step parameter () determining the rate at which the discretization error approaches zero as the time step tends to zero.')
        
        self._add_value('recordlist', 'grid_spacing',
                        recordclass = GridSpacing,
                        modelpath = 'grid-spacing',
                        description = 'Defines the physical distance between adjacent discretization points in a numerical domain.')
        
        self._add_value('recordlist', 'time_step_size',
                        recordclass = TimeStepSize,
                        modelpath = 'time-step-size',
                        description = 'The discrete duration of progression between consecutive stages of a simulation, determining the interval for numerical integration, resolution of transient phenomena, and stability of the governing equations.')
        
        self._add_value('strlist', 'solver',
                        description = 'Specific numerical algorithm or backend used for solving the equations.')

    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True