from typing import Optional

from .MatCore import MatCore
from .md.MDComputation import MDComputation
from .md.ParticleInteractions import ParticleInteractions
from .md.ChargeInteractions import ChargeInteractions
from .md.MagneticInteractions import MagneticInteractions
from .md.ThermodynamicConstraint import ThermodynamicConstraint

class MatCoreMD(MatCore):

    """
    Class for managing Material Core MD Standard records
    """

    ########################## Basic metadata fields ##########################

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'matcore_md'

    ####################### Define Values and attributes #######################

    def _init_values(self):
        """
        Method that defines the value objects for the Record.  This should
        call the super of this method, then use self._add_value to create new Value objects.
        Note that the order values are defined matters
        when build_model is called!!!
        """
        super()._init_values()

        self._add_value('recordlist', 'md_computation', recordclass=MDComputation,
                        valuerequired=True, modelpath='md-computation',
                        description='The form of molecular dynamics performed.')
        self._add_value('str', 'particle_style', valuerequired=True, modelpath='particle-style',
                        description='The nature of the discrete entities used in the molecular dynamics simulation.')
        self._add_value('recordlist', 'particle_interactions', recordclass=ParticleInteractions,
                        valuerequired=True, modelpath='particle-interactions',
                        description='The model used to describe the potential energy surface of the system.')
        self._add_value('recordlist', 'charge_interactions', recordclass=ChargeInteractions,
                        modelpath='charge-interactions',
                        description='The model used to describe the interactions between charged particles.')
        self._add_value('recordlist', 'magnetic_interactions', recordclass=MagneticInteractions,
                        modelpath='magnetic-interactions',
                        description='The model used to describe the interactions between magnetic spins.')
        self._add_value('recordlist', 'thermodynamic_constraint', recordclass=ThermodynamicConstraint,
                        modelpath='thermodynamic-constraint',
                        description='Macroscopic physical restriction imposed on the simulation, such as a statistical mechanics ensemble.')
        

    @property
    def defaultname(self) -> Optional[str]:
        """str: The name to default to, usually based on other properties"""
        return self.matcore_id

    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True

    def add_md_computation(self, **kwargs):
        """Adds a md_computation to the record"""
        self.get_value('md_computation').append(**kwargs)
    
    def add_particle_interactions(self, **kwargs):
        """Adds a particle_interactions to the record"""
        self.get_value('particle_interactions').append(**kwargs)

    def add_charge_interactions(self, **kwargs):
        """Adds a charge_interactions to the record"""
        self.get_value('charge_interactions').append(**kwargs)

    def add_magnetic_interactions(self, **kwargs):
        """Adds a magnetic_interactions to the record"""
        self.get_value('magnetic_interactions').append(**kwargs)

    def add_thermodynamic_constraint(self, **kwargs):
        """Adds a thermodynamic_constraint to the record"""
        self.get_value('thermodynamic_constraint').append(**kwargs)



    def md_computation_df(self):
        """Generates a pandas DataFrame of the md_computation information"""
        return self.get_value('md_computation').metadata_df()
    
    def particle_interactions_df(self):
        """Generates a pandas DataFrame of the particle_interactions information"""
        return self.get_value('particle_interactions').metadata_df()
    
    def charge_interactions_df(self):
        """Generates a pandas DataFrame of the charge_interactions information"""
        return self.get_value('charge_interactions').metadata_df()
    
    def magnetic_interactions_df(self):
        """Generates a pandas DataFrame of the magnetic_interactions information"""
        return self.get_value('magnetic_interactions').metadata_df()
    
    def thermodynamic_constraint_df(self):
        """Generates a pandas DataFrame of the thermodynamic_constraint information"""
        return self.get_value('thermodynamic_constraint').metadata_df()
    