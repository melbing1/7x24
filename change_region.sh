#!/bin/bash -
#===============================================================================
#
#          FILE: change_region.sh
#
#         USAGE: ./change_region.sh old-region-string new-region-string
#
#   DESCRIPTION: Takes the current region and then changes it to the new region 
#
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: Matthew Elbing (2021), 
#  ORGANIZATION: 
#       CREATED: 01/31/2021 13:42:34
#      REVISION:  ---
#===============================================================================

set -o nounset                                  # Treat unset variables as an error

grep -rl '$2' ./ | xargs sed -i 's/$2/$2/g'
