from yabadaba.record import Record

from .Pseudopotential import Pseudopotential

class CoreElectronModel(Record):

    """
    Class for Material Core DFT "core-electron-model" fields
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'core_electron_model'

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'core-electron-model'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """
        
        self._add_value('str', 'type', valuerequired=True,
                        allowedvalues=('All Electron', 'LAPW', 'Pseudopotential', 'PAW'), allowcustomvalue=True,
                        description='The method used to model the electrons.')
        self._add_value('recordlist', 'pseudopotential', recordclass=Pseudopotential,
                        description=' For type "Pseudopotential", or type "PAW", additional information about the pseudopotentials.')
        
    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True