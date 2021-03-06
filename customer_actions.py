from enum import Enum


class CustomerActions(Enum):
    TEST = "U0251J73N0Z"
    ADDON_PURCHASE = "B017PNTEQE5"
    EXPANSION = "B016WBNJ7P1"
    NEW_SUBSCRIPTION = "B017B9Y5A75"
    UPGRADE = "B017H9MT02G"

    ADDON_CANCELLATION = "B016WC1AFC7"
    CANCELLATION = "B0180V3NGBA"
    CONTRACTION = "B017H9L9ATE"
    DOWNGRADE = "B017H9Q1Z9S" 
    PLAN_CHANGE = "B017H9Q1Z9S" #month<->year