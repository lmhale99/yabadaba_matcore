from yabadaba.record import Record

from .CalculationMethod import CalculationMethod

class DerivedProperty(Record):

    """
    Class for Material Core derived "derived-property" fields
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'derived_property'

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'derived-property'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """
        
        self._add_value('str', 'type', valuerequired=True, 
                        allowedvalues=('Electronic', 'Electron-phonon interactions',
                                       'Linear-response', 'Magnetic', 'Microscopy, electron',
                                       'Microscopy, scanning probe', 'NMR', 'Optical',
                                       'Spectroscopy, core-level', 'Spectroscopy, vibrational',
                                       'Transport', 'X-ray scattering'),
                        allowcustomvalue = True,
                        description='Kind of physical quantity being computed.')
        self._add_value('str', 'description', valuerequired=True,
                        description='Explanation of the derived property.')
        self._add_value('recordlist', 'calculation_method', recordclass=CalculationMethod,
                        modelpath='calculation-method', valuerequired=True,
                        description='Details regarding an approach used to obtain the derived property. Multiple approaches may be involved in the computation.')
        
    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True