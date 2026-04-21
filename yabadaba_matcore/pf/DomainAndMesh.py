from yabadaba.record import Record

class DomainAndMesh(Record):

    """
    Class for Material Core pf "domain-and-mesh" fields
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'domain_and_mesh'

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'domain-and-mesh'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """
        
        self._add_value('str', 'dimensionality',
                        valuerequired = True,
                        allowedvalues = (
                            '1D',
                            '2D',
                            '3D'),
                        allowcustomvalue = True,
                        description = 'The spatial dimensions of the computational domain.')
        
        self._add_value('str', 'coordinate_system',
                        modelpath = 'coordinate-system',
                        allowedvalues = (
                            'Cartesian',
                            'Cylindrical',
                            'Spherical'),
                        allowcustomvalue = True,
                        description = 'The structured framework used to uniquely determine and standardize the position of the points in space and the symmetry assumed.')
        
        self._add_value('str', 'mesh_type',
                        modelpath = 'mesh-type',
                        allowedvalues = (
                            'Regular',
                            'Cartesian',
                            'Rectilinear',
                            'Skewed',
                            'Curvilinear',
                            'Unstructured',
                            'Adaptive Mesh Refinement',
                            'Meshless'),
                        allowcustomvalue = True,
                        description = 'The topology or distribution of the discrete grid points.')
        
        self._add_value('floatarray', 'domain_size',
                        modelpath = 'domain-size',
                        description = 'Specification of the computational region extents.')
        
        self._add_value('strlist', 'boundary_conditions',
                        modelpath = 'boundary-conditions',
                        allowedvalues = (
                            'NoFlux',
                            'Periodic',
                            'Fixed',
                            'Free',
                            'Dirichlet',
                            'Neumann'),
                        allowcustomvalue = True,
                        description = 'Constraints applied to the computational domain perimeter.')
        
        self._add_value('strlist', 'initial_conditions',
                        modelpath = 'initial-conditions',
                        description = 'The spatial distribution of the field variables at the start of the simulation.')

    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True