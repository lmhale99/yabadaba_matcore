from yabadaba.record import Record

from .XCParameter import XCParameter

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
        
        self._add_value('str', 'type', valuerequired=True,
                        allowedvalues=('LDA', 'GGA', 'Meta GGA', 'Hybrid', 'ML'), allowcustomvalue=True,
                        description='The mathematical form of the exchange-correlation functional.')
        self._add_value('str', 'description',
                        description='Explanatory text providing more information about the type of the exchange-correlation method used including any relevant identifying information.')
        self._add_value('recordlist', 'xc_parameter', recordclass=XCParameter, modelpath='xc-parameter',
                        description='A fixed variable associated with the specified exchange-correlation functional method.')
        
    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True