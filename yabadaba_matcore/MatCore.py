from typing import Optional

from yabadaba.record import Record

from .minimal.Creator import Creator
from .minimal.Material import Material
from .minimal.Computation import Computation
from .minimal.Citation import Citation
from .minimal.Funding import Funding
from .minimal.RelatedContent import RelatedContent
from .minimal.Provenance import Provenance

class MatCore(Record):

    """
    Class for managing Material Core Standard records
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'matcore'

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'root'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """

        self._add_value('recordlist', 'creator', recordclass=Creator, valuerequired=True,
                        description='The author who generated the data and institutional affiliation.')
        self._add_value('str', 'title', valuerequired=True,
                        description='A single sentence description of the dataset.')
        self._add_value('date', 'creation_date', valuerequired=True, modelpath='creation-date',
                        description='The calendar date when the dataset was created.')
        self._add_value('str', 'description', valuerequired=True,
                        description='A synopsis of the dataset, its contents, and purpose.')
        self._add_value('str', 'disclaimer',
                        description='A statement of applicability provided by the creator(s) informing users of the intended use and/or limitations of this dataset.')
        self._add_value('recordlist', 'material', recordclass=Material, valuerequired=True,
                        description='A description of the chemical composition and structure of a substance in this dataset.')
        self._add_value('recordlist', 'computation', recordclass=Computation, valuerequired=True,
                        description='A description of a computer simulation used to generate data in the dataset.')
        self._add_value('recordlist', 'citation', recordclass=Citation, 
                        description='Information that uniquely identifies a source being acknowledged.')
        self._add_value('recordlist', 'funding', recordclass=Funding, 
                        description='Information about received monetary support or other resources to generate the dataset.')
        self._add_value('recordlist', 'related_content', recordclass=RelatedContent, modelpath='related-content',
                        description='Other datasets that are connected to the current one in some manner.')
        self._add_value('recordlist', 'provenance', recordclass=Provenance, 
                        description='History of the dataset, detailing its origins and transformations.')
        self._add_value('str', 'matcore_id', valuerequired=True, modelpath='matcore-id',
                        description='An identifier for the dataset.')
        self._add_value('date', 'matcore_date', valuerequired=True, modelpath='matcore-date',
                        description='The calendar date when this MatCore document was created.')
        self._add_value('str', 'license', valuerequired=True,
                        description='A contract defining the terms and conditions under which the dataset can be used.')

    @property
    def defaultname(self) -> Optional[str]:
        """str: The name to default to, usually based on other properties"""
        return self.matcore_id

    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True

    def add_creator(self, **kwargs):
        """Adds a creator to the record"""
        self.get_value('creator').append(**kwargs)
    
    def add_material(self, **kwargs):
        """Adds a material to the record"""
        self.get_value('material').append(**kwargs)

    def add_computation(self, **kwargs):
        """Adds a computation to the record"""
        self.get_value('computation').append(**kwargs)

    def add_citation(self, **kwargs):
        """Adds a citation to the record"""
        self.get_value('citation').append(**kwargs)

    def add_funding(self, **kwargs):
        """Adds a funding to the record"""
        self.get_value('funding').append(**kwargs)

    def add_related_content(self, **kwargs):
        """Adds a related_content to the record"""
        self.get_value('related_content').append(**kwargs)

    def add_provenance(self, **kwargs):
        """Adds a provenance to the record"""
        self.get_value('provenance').append(**kwargs)



    def creator_df(self):
        """Generates a pandas DataFrame of the creator information"""
        return self.get_value('creator').metadata_df()
    
    def material_df(self):
        """Generates a pandas DataFrame of the material information"""
        return self.get_value('material').metadata_df()
    
    def computation_df(self):
        """Generates a pandas DataFrame of the computation information"""
        return self.get_value('computation').metadata_df()
    
    def citation_df(self):
        """Generates a pandas DataFrame of the citation information"""
        return self.get_value('citation').metadata_df()
    
    def funding_df(self):
        """Generates a pandas DataFrame of the funding information"""
        return self.get_value('funding').metadata_df()
    
    def related_content_df(self):
        """Generates a pandas DataFrame of the related_content information"""
        return self.get_value('related_content').metadata_df()
    
    def provenance_df(self):
        """Generates a pandas DataFrame of the provenance information"""
        return self.get_value('provenance').metadata_df()