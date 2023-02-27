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

from CEAClass import CEA
from FilmCooling import FilmCooling
import PropLibrary as pl


# CEA input
fuel               = 'MMH'                    # choose existing fuel or oxidiser from rocketcea or create new fuel or oxidiser blend in PropLibrary
ox                 = 'N2O4'

# Operating point of combustion chamber 
MR                 = 1.7							  # injector mixture ratio
m_dot              = 0.056                            # total mass flow [kg/s]
m_dot_f            = m_dot / (MR + 1)
m_dot_ox           = m_dot - m_dot_f
Pc                 = 10e5                             # Chamber pressure [Pa]
eps                = 330  							  # expansion ratio

# Film coolant input
cooling_fluid      = ['CH6N2']                  # needs to be list of str
coolant_mass_frac  = [1]					  # nees to add up to 1
m_dot_c            = m_dot * 0.33                	  # mass flow of film coolant
m_dot_inj          = m_dot - m_dot_c
inlet_temp         = 288.15                     	  # inlet temperature [K]
inlet_pressure     = 12.5e5                           # Cooling channel inlet pressure [Pa]
injection_velocity = 21								  # [m/s]
chamber_diameter   = 31e-3					          # [m]
injector_diameter  = 0.5e-3							  # [m]


# calculate hot gas properties from NASA CEA
cea = CEA(fuel, ox, Pc) 
cea.metric_cea_output('throat', MR, eps)


# coolant Properties from thermo library
coolant = thermo.Mixture(cooling_fluid, ws=coolant_mass_frac, P=inlet_pressure, T=inlet_temp)     

# film cooling model
film = FilmCooling(cea, coolant, injection_velocity, injector_diameter, chamber_diameter, m_dot_inj, m_dot_c)
film.film_length()

# output
print('propellants:                   ', fuel , ' + ', ox)
print('coolant:                       ', coolant.IDs, ' mass fraction: ', coolant.ws)
print('total mass flow                ', np.round(m_dot * 1000, 3), ' g/s')
print('coolant mass flow              ', np.round(m_dot_c * 1000, 3), ' g/s')
print('coolant flow per circumference:', np.round(m_dot_c / (np.pi * chamber_diameter), 3), ' kg/(m*s)')
print('liquid film cooling length:    ', np.round(film.liquid_film_length * 1000, 3), ' mm')

