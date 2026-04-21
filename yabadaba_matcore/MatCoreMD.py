
from .MatCore import MatCore
from .md.MDComputation import MDComputation
from .md.ParticleInteractions import ParticleInteractions
from .md.ChargeInteractions import ChargeInteractions
from .md.MagneticInteractions import MagneticInteractions
from .md.ThermodynamicConstraint import ThermodynamicConstraint

class MatCoreMD(MatCore):

    """
    Class for managing MatCore-MD records
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

        self._add_value('recordlist', 'md_computation',
                        recordclass = MDComputation,
                        valuerequired = True,
                        modelpath = 'md-computation',
                        description = 'The form of molecular dynamics performed.')
        
        self._add_value('str', 'particle_style',
                        valuerequired = True,
                        modelpath = 'particle-style',
                        allowedvalues = (
                            'Atom',
                            'Radical',
                            'United atom',
                            'Bead',
                            'Coarse grained',
                            'Mesoscale',
                            'Classical electron'),
                        allowcustomvalue = True,
                        description = 'The nature of the discrete entities used in the molecular dynamics simulation.')
        
        self._add_value('recordlist', 'particle_interactions',
                        recordclass = ParticleInteractions,
                        valuerequired = True,
                        modelpath = 'particle-interactions',
                        description = 'The model used to describe the potential energy surface of the system.')
        
        self._add_value('recordlist', 'charge_interactions',
                        recordclass = ChargeInteractions,
                        modelpath = 'charge-interactions',
                        description = 'The model used to describe the interactions between charged particles.')
        
        self._add_value('recordlist', 'magnetic_interactions',
                        recordclass = MagneticInteractions,
                        modelpath = 'magnetic-interactions',
                        description = 'The model used to describe the interactions between magnetic spins.')
        
        self._add_value('recordlist', 'thermodynamic_constraint',
                        recordclass = ThermodynamicConstraint,
                        modelpath = 'thermodynamic-constraint',
                        description = 'Macroscopic physical restriction imposed on the simulation, such as a statistical mechanics ensemble.')
        
    @property
    def _defaultextensible(self) -> bool:
        """bool: Default value for extensible for this record class."""
        return True
