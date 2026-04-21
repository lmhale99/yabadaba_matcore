from yabadaba.record import Record

class ChargeInteractions(Record):

    """
    Class for Material Core MD "charge-interactions" fields
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'charge_interactions'

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'charge-interactions'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """
        
        self._add_value('str', 'charge_origin',
                        valuerequired = True,
                        modelpath = 'charge-origin',
                        allowedvalues = (
                            'Semi empirical',
                            'Quantum',
                            'Electronic population',
                            'Electronegativity',
                            'Tabulated'),
                        allowcustomvalue = True,
                        description = 'Nature of the particle charges.')
        
        self._add_value('str', 'charge_style',
                        valuerequired = True,
                        modelpath = 'charge-style',
                        allowedvalues = (
                            'Coulomb full',
                            'Coulomb screened'),
                        allowcustomvalue = True,
                        description = 'The nature of the charges associated with the particles, such as total or effective charges.')
        
        self._add_value('str', 'charge_variability',
                        valuerequired = True,
                        modelpath = 'charge-variability',
                        allowedvalues = (
                            'Fixed',
                            'QEq',
                            'EEM',
                            'iEL/SCF',
                            'FlucQ',
                            'Drude'),
                        allowcustomvalue = True,
                        description = 'Attribute specifying the method for dynamically varying the local electric charge associated with discrete entities.')
        
        self._add_value('str', 'long_range_electrostatics',
                        modelpath = 'long-range-electrostatics',
                        allowedvalues = (
                            'None',
                            'Direct',
                            'Ewald',
                            'PME',
                            'PPPM',
                            'Reaction'),
                        allowcustomvalue = True,
                        description = 'Method used to compute long-range electrostatic interactions.')
        
        self._add_value('str', 'electric_dipole',
                        modelpath = 'electric-dipole',
                        allowedvalues = (
                            'Stockmayer',
                            'Screened',
                            'Long range'),
                        allowcustomvalue = True,
                        description = 'Attribute specifying the type of interaction associated with the local electric dipoles associated with particles.')
        
        self._add_value('str', 'electric_dipole_variability',
                        modelpath = 'electric-dipole-variability',
                        allowedvalues = (
                            'Induced',
                            'Isotropic',
                            'Anisotropic'),
                        allowcustomvalue = True,
                        description = 'Attribute specifying the method for dynamically varying the local electric charge associated with discrete entities.')
        
    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True
    