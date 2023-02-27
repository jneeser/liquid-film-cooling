# Liquid Film Cooling Model
This program is an implementation of the anayltical 0D liquid film cooling model propsed by [Shine et al](https://www.researchgate.net/publication/256718300_A_new_generalised_model_for_liquid_film_cooling_in_rocket_combustion_chambers).
The model relies on an energy balance between the convective and radiative heat transfer of the combustion gases and the evaporation of the coolant. The model produces an
estimate of the liquid film length and assumes that the temperature rise of the wall under the liquid film is very small. 

## Cooling Fluid 
Currently only single component liquids are supported. This makes automatically calculating the enthalpy of evaporation and the boiling point easier. For mixtures a new
method needs to be implemented or values hard coded. 


## CEA Implementation
This model uses the CEA implementation of [RocketCEA](https://rocketcea.readthedocs.io/en/latest/). This requires Fortran compilers and can be installed using the method outlined in 
PyRocket. Restrictions on the DLR network may apply. If you prefer to use another implementation of CEA, then simply writer a wrapper class that used the same name spaces as in the CEAClass.py file.
Or replace instances of where the current CEA class is used with your own. 

## Engine Sizing Tool
A complementary engine sizing tool is also provided. Input desired thrust and nozzle exit condition and appropriate mass flows and chamber dimensions will be estimated.
This routine is not validated. Use at your own risk!

## Validation
Validation data from the paper by Shine et al. is used in the runValidation.py file to recreate the film length data of experiments in table 2 of the paper. 

