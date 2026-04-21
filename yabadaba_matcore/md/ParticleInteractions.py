from yabadaba.record import Record

from .Source import Source

class ParticleInteractions(Record):

    """
    Class for Material Core MD "particle-interactions" fields
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'particle_interactions'

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'particle-interactions'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """
        
        self._add_value('str', 'model_type',
                        valuerequired = True,
                        modelpath = 'model-type',
                        description = 'The kind of potential used to compute the particle interactions.')
        
        self._add_value('str', 'bonding_type',
                        valuerequired = True,
                        modelpath = 'bonding-type',
                        allowedvalues = (
                            'Reactive',
                            'Bonded fixed',
                            'Bonded mutable'),
                        allowcustomvalue = True,
                        description = 'Specifies whether the bonds between particles are immutable or can be broken.')
        
        self._add_value('str', 'theory_level',
                        valuerequired = True,
                        modelpath = 'theory-level',
                        allowedvalues = (
                            'Classical physics-based',
                            'Classical machine-learning',
                            'Tight-binding',
                            'Ab initio',
                            'Ab initio machine learning'),
                        allowcustomvalue = True,
                        description = 'The rigor with which the atomic interactions are modeled.')
        
        self._add_value('recordlist', 'source',
                        recordclass = Source,
                        description = 'Information that uniquely identifies the origin of the particle interaction model (e.g. a journal article, or a repository containing an implementation or parameter set).')
        
    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True
