from enum import Enum

class CustomerActions(Enum):
    ADDON_CANCELLATION = "Addon Cancellation"
    ADDON_PURCHASE = "Addon Purchase"
    CANCELLATION = "Cancellation"
    CONTRACTION = "Contraction"
    DOWNGRADE = "Downgrade"
    EXPANSION = "Expansion"
    NEW_SUBSCRIPTION = "New Subscription"
    PLAN_CHANGE = "Plan Change"
    UPGRADE = "Upgrade"