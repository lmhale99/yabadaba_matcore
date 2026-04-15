# MatCore extension for yabadaba


This package defines records associated with the [Material Core Standard (MatCore)](https://matcore.org/) schema. Both the standard and the code are currently in the development stage.  Feedback on the standard can be submitted to the MatCore website.

Basic documentation is in the numbered Jupyter Notebooks, as well as documentation for the [yabadaba package](https://github.com/usnistgov/yabadaba). 

__NOTE__: Currently, this package uses features in the upcoming yabadaba version 0.4. If you wish to try things for yourself, download and istall yabadaba from the development repository at https://github.com/lmhale99/yabadaba.  The new version of yabadaba will be released once the new features are tested and the documentation is updated.

## Code Development Progress

Done:
- Record classes added for the minimal MatCore and the MatCore-MD schemas.
- Basic documentation showing current functionality.
- User-defined elements with simple values now supported.

To do:
- Need to add records for the remaining schemas.
- Need to add allowedvalues lists to the terms with recommended standard values.  The new yabadaba now has an allowcustomvalue setting that supports having this list without explicit value checking.
- MatCore data entry would be best supported with some sort of GUI as there are lots of required values and related values.  The current non-GUI Python way works best for generating similar records or transforming/updating all records en masse.
