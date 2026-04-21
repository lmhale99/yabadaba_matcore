from yabadaba.record import Record

from .Constituent import Constituent

class Material(Record):

    """
    Class for Material Core "material" fields
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'material'

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'material'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """
        
        self._add_value('str', 'phase',
                        valuerequired = True,
                        allowedvalues = (
                            'Amorphous',
                            'Crystal',
                            'Quasicrystal',
                            'Molecule',
                            'Liquid',
                            'Gas',
                            'Plasma'),
                        allowcustomvalue = True,
                        description = 'The structure of the material included in the dataset.')
        self._add_value('str', 'description',
                        description = 'An explanation of the nature of the material, e.g. a crystal structure designation, a chemical formula for a molecule, etc.')
        self._add_value('recordlist', 'constituent',
                        recordclass = Constituent,
                        valuerequired = True,
                        description = 'A chemical element included in the material and its concentration.')
        self._add_value('str', 'microstructure',
                        description = 'The arrangement of phases, grains and defects in a material.')
    
    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True

