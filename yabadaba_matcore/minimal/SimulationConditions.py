from yabadaba.record import Record

class SimulationConditions(Record):
    """
    Class for Material Core "simulation-conditions" fields
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'simulation-conditions'

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'simulation-conditions'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """
        
        self._add_value('str', 'type',
                        valuerequired = True,
                        allowedvalues = (
                            'Equilibrium',
                            'Nonequilibrium',
                            'Nonstandard'),
                        allowcustomvalue = True,
                        description = 'The nature of the simulation being performed, whether equilibrium, nonequilibrium, or nonstandard.')
        
        self._add_value('str', 'description',
                        description = 'Explanatory text clarifying the simulation type selection.')
        
        self._add_value('int', 'number_of_particles',
                        modelpath = 'number-of-particles',
                        description = 'A count of atoms or other discrete entities comprising the material.')
        
        self._add_value('float', 'volume',
                        #unit = 'm^3',
                        description = 'The amount of space occupied by the material.')
        
        self._add_value('float', 'mass_density',
                        modelpath = 'mass-density',
                        #unit = 'kg/m^3',
                        description = 'The total number of particles comprising the material divided by the volume it occupies.')
        
        self._add_value('floatarray', 'cell',
                        #unit = 'm',
                        shape = (3,3),
                        description = 'The domain occupied by the material in the simulation (if fixed).')
        
        self._add_value('floatarray', 'cell_reference',
                        modelpath = 'cell-reference',
                        #unit = 'm',
                        shape = (3,3),
                        description = 'The domain occupied by the material in the simulation in configuration relative to which strains are defined.')
        
        self._add_value('intarray', 'cell_periodicity',
                        modelpath = 'cell-periodicity',
                        shape = (3,),
                        description = 'Specification of whether periodic boundary conditions are applied along the cell vector directions. This applies to both cell and cell-reference.')
        
        self._add_value('float', 'temperature',
                        description = 'A measure of the hotness or coldness of an external heat bath in thermal contact with the material.')
        
        self._add_value('floatarray', 'stress',
                        #unit = 'Pa',
                        shape = (6,),
                        description = 'A uniform force per unit current area, including both normal and shear components, applied to the material during the simulation through contact with an external loading device.')
        
        self._add_value('floatarray', 'strain',
                        shape = (6,),
                        description = 'A deformation relative to a reference configuration imposed on the simulation cell expressed in the referential frame (Lagrangian strain tensor).')
        
        self._add_value('floatarray', 'strain_rate',
                        modelpath = 'strain-rate',
                        shape = (6,),
                        description = 'The derivative with respect to time of a deformation relative to a reference configuration imposed on the simulation cell expressed in the referential frame (Lagrangian strain rate tensor), which is constant throughout the simulation.')
        
        self._add_value('floatarray', 'heat_flux',
                        modelpath = 'heat-flux',
                        #unit = 'W/m^2',
                        shape = (3,),
                        description = 'The amount of thermal energy transferred to the material per unit area per unit time along a given direction.')
        
        self._add_value('floatarray', 'temperature_gradient',
                        modelpath = 'temperature-gradient',
                        #unit = 'W/m^2',
                        shape = (3,),
                        description = 'A physical quantity that describes the rate and direction of maximum temperature change per unit distance.')

    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True