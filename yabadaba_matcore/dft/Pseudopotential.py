from yabadaba.record import Record

class Pseudopotential(Record):

    """
    Class for Material Core DFT "pseudopotential" fields
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'pseudopotential'

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'pseudopotential'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """
        self._add_value('str', 'name',
                        valuerequired = True,
                        description = 'The name of the pseudopotential.')
        
        self._add_value('str', 'description', 
                        description = 'Explanatory text about the pseudopotential including any relevant identifying information.')
        
        self._add_value('str', 'type',
                        valuerequired = True,
                        allowedvalues = (
                            'Norm conserving',
                            'Ultrasoft'),
                        allowcustomvalue = True,
                        description = 'The physical form of the pseudopotential.')
        
        self._add_value('int', 'number_of_valence_electrons',
                        valuerequired = True,
                        modelpath = 'number-of-valence-electrons',
                        description = 'The number of electrons treated explicitly.')
        
        self._add_value('str', 'repository', 
                        description = 'The database from which the pseudopotential was obtained.')
        
        self._add_value('str', 'version',
                        description = 'The version of the pseudopotential.')
        
        self._add_value('str', 'doi',
                        description = 'The digital object identifier (DOI) for the pseudopotential.')
        
        self._add_value('str', 'unique_identifier',
                        modelpath = 'unique-identifier',
                        description = 'A hash or other token providing a digital signature for the pseudopotential.')
        
    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True