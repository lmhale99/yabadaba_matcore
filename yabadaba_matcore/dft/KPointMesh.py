from yabadaba.record import Record


class KPointMesh(Record):

    """
    Class for Material Core DFT "k-point-mesh" fields
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'k_point_mesh'

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'k-point-mesh'

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
                            'Monkhorst-Pack',
                            'Gamma centered',
                            'Irregular'),
                        allowcustomvalue = True,
                        description = 'The choice of how k-points are distributed on the mesh.')
        
        self._add_value('intarray', 'number-of-points',
                        modelpath = 'number-of-points',
                        shape = (3,),
                        description = 'How many k-points are included along each reciprocal lattice vector.')
        
        self._add_value('floatarray',
                        'k-point-spacing',
                        modelpath = 'k-point-spacing',
                        shape = (3,),
                        #unit = '1/angstrom',
                        description = 'Separation between k-points along each reciprocal lattice vector direction.')
        
        self._add_value('floatarray', 'shift',
                        shape = (3,),
                        #unit = '1/angstrom',
                        description = 'Translation of the k-point mesh along the reciprocal lattice vector directions.')
        
        self._add_value('str', 'smearing_type',
                        modelpath = 'smearing-type',
                        allowedvalues = (
                            'None',
                            'None - tetrahedron',
                            'None - Blöchl-corrected tetrahedron',
                            'Gaussian', 
                            'Fermi',
                            'Methfessel-Paxton'),
                        allowcustomvalue = True,
                        description = 'The choice of method for assigning fractional occupancies of electronic states and/or facilitating reciprocal space integrations.')
        
        self._add_value('float',
                        'smearing_width',
                        modelpath = 'smearing-width',
                        #unit = 'eV',
                        description = 'A parameter that controls the broadening of the electron energy levels near the Fermi level.')
        
        self._add_value('int', 'methfessel_paxton_order',
                        modelpath = 'methfessel-paxton-order',
                        description = 'For smearing-type “Methfessel-Paxton”, level of polynomial approximation used in the Methfessel-Paxton smearing method.')
        
    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True