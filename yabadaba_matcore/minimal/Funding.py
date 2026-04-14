from yabadaba.record import Record

class Funding(Record):

    """
    Class for Material Core "funding" fields
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'funding'

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'funding'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """
        
        self._add_value('str', 'award_title', valuerequired=True, modelpath='award-title',
                        description='Name of the grant that provided funding to generate the dataset.')
        self._add_value('str', 'funder', valuerequired=True,
                        description='The name of the funding agency that provided money and/or resources to generate the dataset.')
        self._add_value('str', 'award_number', modelpath='award-number',
                        description='A funder identifier for the grant.')
        
    
    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True