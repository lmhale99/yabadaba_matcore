from yabadaba.record import Record


class LocalizedOrbitalsBasisSet(Record):

    """
    Class for Material Core DFT "localized-orbitals-basis-set" fields
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'localized_orbitals_basis_set'

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'localized-orbitals-basis-set'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """
        
        self._add_value('str', 'type', valuerequired=True,
                        description='The designation of the set of orbital functions used for expanding electronic wave functions.')
        self._add_value('str', 'repository', 
                        description='The database from which the localized-orbital basis set was obtained.')
        self._add_value('str', 'version',
                        description='The version of the localized-orbital basis set.')
        self._add_value('str', 'doi',
                        description='The digital object identifier (DOI) for the localized-orbital basis set.')
        self._add_value('str', 'unique_identifier', modelpath='unique-identifier',
                        description='A hash or other token providing a digital signature for the localized-orbital basis set.')

        
    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True