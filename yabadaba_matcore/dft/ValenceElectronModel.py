from yabadaba.record import Record

from .LocalizedOrbitalsBasisSet import LocalizedOrbitalsBasisSet

class ValenceElectronModel(Record):

    """
    Class for Material Core DFT "valence-electron-model" fields
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'valence_electron_model'

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'valence-electron-model'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """
        
        self._add_value('strlist', 'type', valuerequired=True,
                        allowedvalues=('Plane waves', 'LAPW', 'Localized orbitals', 'PAW'), allowcustomvalue=True,
                        description='The choice of a basis set to expand electronic wave functions.')
        self._add_value('recordlist', 'localized_orbital_basis_set', recordclass=LocalizedOrbitalsBasisSet,
                        modelpath='localized-orbital-basis-set',
                        description='For type "Localized orbitals", additional information about the localized orbital basis set.')
        self._add_value('float', 'kinetic_energy_cutoff', modelpath='kinetic-energy-cutoff', unit='eV',
                        description=' For type not "Localized orbitals", the maximum kinetic energy of the plane waves included in the calculation of wave functions.')
        self._add_value('float', 'charge_density_cutoff', modelpath='charge-density-cutoff', unit='eV',
                        description='For type not "Localized orbitals", the energy value used to truncate the plane wave expansion of the electron charge density,')
        
    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True