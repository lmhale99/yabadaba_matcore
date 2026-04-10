from yabadaba.record import Record

class File(Record):
    """
    Class for Material Core "file" fields
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'file'

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'file'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """
        
        self._add_value('str', 'name', valuerequired=True,
                        description='The file name.')
        self._add_value('str', 'description',
                        description='A brief description of the file and its contents.')
        self._add_value('str', 'contents',
                        description='The text and/or data contained in the file. Not required in case a link to the file is provided instead.')
        self._add_value('str', 'link',
                        description='A URI pointing to a permanent location of the file online.')
