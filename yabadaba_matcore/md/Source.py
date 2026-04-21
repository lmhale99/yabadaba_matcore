from yabadaba.record import Record

class Source(Record):

    """
    Class for Material Core MD "source" fields
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'source'

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'source'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """
        
        self._add_value('str', 'reference',
                        valuerequired = True,
                        description = 'The origin of the particle interaction model implementation used, such as an interatomic potential repository (e.g. OpenKIM or the NIST IPR), a code (like LAMMPS), or a publication.')
        
        self._add_value('str', 'doi',
                        description = 'The digital object identifier (DOI) for the source.')
        
        self._add_value('str', 'link',
                        description = 'A URI pointing to a permanent location of the source.')

    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True
    