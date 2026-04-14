from yabadaba.record import Record

class RelatedContent(Record):

    """
    Class for Material Core "related-content" fields
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'related_content'

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'related-content'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """
        
        self._add_value('strlist', 'links', valuerequired=True,
                        description='A list of permanent pointers to related datasets (such as MatCore IDs, DOIs, URIs, etc.)')
        self._add_value('str', 'description',
                        description='Explanation of the relationship between the related content and the current dataset.')
        
    
    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True