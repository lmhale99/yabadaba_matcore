from yabadaba.record import Record

class MBPTMethod(Record):

    """
    Class for Material Core mbpt "mbpt-method" fields
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'mbpt_method'

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'mbpt-method'

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
                            'GW',
                            'BSE',
                            'GW/BSE'),
                        allowcustomvalue = True,
                        description = 'The nature of the MBPT calculation performed.')
        
        self._add_value('str', 'self_consistency',
                        valuerequired = True,
                        modelpath =' self-consistency',
                        allowedvalues = (
                            'G0W0',
                            'GW0',
                            'G0W',
                            'scGW',
                            'QSGW',
                            'BSE0',
                            'scBSE',
                            'scGW+BSE'),
                        allowcustomvalue = True,
                        description = 'Specifies the level of iterative updating applied to the Green\'s function (G), the screened Coulomb interaction (W), or the excitonic Hamiltonian during the calculation. This property identifies whether the MBPT equations are solved in a \'one-shot\' perturbative manner or through an iterative cycle where the electronic or excitonic quasiparticle states are updated to reach a self-consistent solution.')
        
    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True