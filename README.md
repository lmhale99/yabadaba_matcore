# MatCore extension for yabadaba


This package defines records associated with the [Material Core Standard (MatCore)](https://matcore.org/) schema. Both the standard and the code are currently in the development stage.  Feedback on the standard can be submitted to the MatCore website.

Basic documentation is in the numbered Jupyter Notebooks, as well as documentation for the [yabadaba package](https://github.com/usnistgov/yabadaba). 

__NOTE__: Currently, this package uses features in the upcoming yabadaba version 0.4. If you wish to try things for yourself, download and istall yabadaba from the development repository at https://github.com/lmhale99/yabadaba.  The new version of yabadaba will be released once the new features are tested and the documentation is updated.

## Code Development Progress

Done:
- Record classes added for MatCore, MatCore-MD, and all component schemas except for PF.
- Basic documentation showing current functionality.
- User-defined elements with simple values now supported.

To do:
- yabadaba float and floatarray values need updating to allow for alternate representations of complex values.  Currently, values in the model become subsets containing value, unit, error, and shape fields.  Customization requires allowing for custom paths to unit and error, or optionally not displaying unit and shape values when fixed.