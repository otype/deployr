# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""

# Deploy task
#
# Used for deploying GenAPIs
#
DEPLOY_TASK = 'DEPLOY'

# Deploy confirmation task
#
# Used for responding back after a GenAPI deployment
#
DEPLOY_CONFIRMATION_TASK = 'DEPLOY_CONFIRMATION'

# Undeploy task
#
# Used for undeploying GenAPIs
#
UNDEPLOY_TASK = 'UNDEPLOY'

# Undeploy confirmation task
#
# Used for responding back after undeployment of a GenAPI
#
UNDEPLOY_CONFIRMATION_TASK = 'UNDEPLOY_CONFIRMATION'

# Loadbalance deploy task
#
# Used for registering a deployed GENAPI in the loadbalancer
#
LOADBALANCE_UPDATE_TASK = 'LOADBALANCE_UPDATE'

# Loadbalance deploy confirmation task
#
# Used for registering a deployed GENAPI in the loadbalancer
#
LOADBALANCE_UPDATE_CONFIRMATION_TASK = 'LOADBALANCE_UPDATE_CONFIRMATION'

# Loadbalance undeploy task
#
# Used for deleting a deployed GENAPI in the loadbalancer
#
LOADBALANCE_UNDEPLOY_TASK = 'LOADBALANCE_UNDEPLOY'

# Loadbalance undeploy confirmation task
#
# Used for deleting a deployed GENAPI in the loadbalancer
#
LOADBALANCE_UNDEPLOY_CONFIRMATION_TASK = 'LOADBALANCE_UNDEPLOY_CONFIRMATION'