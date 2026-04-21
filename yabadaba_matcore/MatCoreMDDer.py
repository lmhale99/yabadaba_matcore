from .MatCoreMD import MatCoreMD
from .derived.MatCoreDer import MatCoreDer


class MatCoreMDDer(MatCoreMD, MatCoreDer):

    """
    Class for managing MatCore-MD-Der records
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'matcore_md_der'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """
        MatCoreMD._init_values(self)
        MatCoreDer._init_values(self)
