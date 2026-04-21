from yabadaba import recordmanager

# Add the modular Record styles
recordmanager.import_style('matcore', '.MatCore', __name__)

recordmanager.import_style('matcore_dft', '.MatCoreDFT', __name__)
recordmanager.import_style('matcore_md', '.MatCoreMD', __name__)
recordmanager.import_style('matcore_mbpt', '.MatCoreMBPT', __name__)
recordmanager.import_style('matcore_ml', '.MatCoreML', __name__)
recordmanager.import_style('matcore_pf', '.MatCorePF', __name__)

recordmanager.import_style('matcore_dft_der', '.MatCoreDFTDer', __name__)
recordmanager.import_style('matcore_md_der', '.MatCoreMDDer', __name__)
recordmanager.import_style('matcore_mbpt_der', '.MatCoreMBPTDer', __name__)
recordmanager.import_style('matcore_ml_der', '.MatCoreMLDer', __name__)
recordmanager.import_style('matcore_pf_der', '.MatCorePFDer', __name__)