###############################################################################
#                         Liquid Film Cooling Model					          #
# Basic 0D analytical film cooling model based energy balance by Shine et al. #
#                                                                   	      #
# Creator:  Joanthan Neeser                                        		      #
# Date:     06.02.2022                                             		      #
# Version:  1.1 														      #                                      
###############################################################################


import numpy as np
import thermo
import os

from CEAClass import CEA
from FilmCooling import FilmCooling
import PropLibrary as proplib

# Validation input parameters for model from Shine et al.
# validation value based on table 2 with a target model film length of 1.02 m 
# coolant injection velocity needed to be estimated

# CEA input
fuel               = 'RP-1'                    # choose existing fuel or oxidiser from rocketcea or create new fuel or oxidiser blend in PropLibrary
ox                 = 'AIR'

# Operating point of combustion chamber 
eta_combustion     = 0.945
MR                 = 40								  # injector mixture ratio
m_dot              = 0.29                            # total mass flow [kg/s]
m_dot_f            = m_dot / (MR + 1)
m_dot_ox           = m_dot - m_dot_f
Pc                 = 1e5                             # Chamber pressure [Pa]
eps                = 40 							  # expansion ratio

# Film coolant input
cooling_fluid      = ['h2o']                    	# needs to be str
coolant_mass_frac  = [1]
m_dot_c            = 0.08                	  # mass flow of film coolant
inlet_temp         = 298.15                     	  # inlet temperature [K]
inlet_pressure     = 12.5e5                           # Cooling channel inlet pressure [Pa]
injection_velocity = 5								  # [m/s]
chamber_diameter   = 73.6e-3					      # [m]
injector_diameter  = 1e-3							  # [m]


# calculate hot gas properties from NASA CEA
cea = CEA(fuel, ox, Pc) 
cea.metric_cea_output('throat', MR, eps)

# set temperature to the exact value in table 2
# cea settings used to get close enough 
cea.Tc = 1230

# coolant Properties from thermo library
coolant = thermo.Mixture(cooling_fluid, ws=coolant_mass_frac, P=inlet_pressure, T=inlet_temp)     

# film cooling model
film = FilmCooling(cea, coolant, injection_velocity, injector_diameter, chamber_diameter, m_dot, m_dot_c)
film.film_length()

print('liquid film cooling length: ', np.round(film.liquid_film_length * 1000,3), ' mm')