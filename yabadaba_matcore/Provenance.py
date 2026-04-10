from yabadaba.record import Record

class Provenance(Record):

    """
    Class for Material Core "provenance" fields
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'provenance'

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'provenance'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """
        
        self._add_value('str', 'event_type', valuerequired=True, modelpath='event-type',
                        description='Description of change made to the dataset.')
        self._add_value('date', 'date', valuerequired=True,
                        description='The data when the change was made.')
        self._add_value('str', 'agent', valuerequired=True,
                        description='Identity of the entity responsible for the change.')
        self._add_value('str', 'comments',
                        description='Explanation for the change in provenance.')
        self._add_value('str', 'checksum',
                        description='A digital fingerprint for the dataset of associated files.')