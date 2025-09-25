import time
from termcolor import colored
from data import JOURNEY_IN_DAYS
from data import COST_FOOD_HUMAN_COPPER_PER_DAY 
from data import COST_FOOD_HORSE_COPPER_PER_DAY 
from data import COST_TENT_GOLD_PER_WEEK
from data import COST_HORSE_SILVER_PER_DAY
from data import COST_INN_HUMAN_SILVER_PER_NIGHT
from data import COST_INN_HORSE_COPPER_PER_NIGHT 

import math

##################### O03 #####################

def copper2silver(amount:int) -> float:
    return amount / 10

def silver2gold(amount:int) -> float:
    return amount / 5

def copper2gold(amount: int) -> float:
    silver = copper2silver(amount)
    return silver2gold(silver)

def platinum2gold(amount:int) -> float:
    return amount * 25

def getPersonCashInGold(personCash:dict) -> float:
    copper = copper2gold(personCash.get("copper", 0))
    silver = silver2gold(personCash.get("silver", 0))
    gold = personCash.get("gold", 0)
    platinum = platinum2gold(personCash.get("platinum", 0))

    total = copper + silver + gold + platinum
    return round(total, 2)

##################### O05 #####################

def getJourneyFoodCostsInGold(people: int, horses: int, days: int = JOURNEY_IN_DAYS) -> float:
    total_copper = (
        people * COST_FOOD_HUMAN_COPPER_PER_DAY * days
        + horses * COST_FOOD_HORSE_COPPER_PER_DAY * days
    )
    return copper2gold(total_copper)

##################### O06 #####################

def getFromListByKeyIs(lst: list, key: str, value: any) -> list:
    return [item for item in lst if item.get(key) == value]


def getAdventuringPeople(people: list) -> list:
    return getFromListByKeyIs(people, "adventuring", True)


def getShareWithFriends(friends: list) -> list:
    return getFromListByKeyIs(friends, "shareWith", True)


def getAdventuringFriends(friends: list) -> list:
    share_with = getShareWithFriends(friends)
    return getAdventuringPeople(share_with)


##################### O07 #####################
def getNumberOfHorsesNeeded(people:int) -> int:
    """
    2 personen per paard.
    """
    horses = people // 2
    if people % 2 != 0:  
        horses += 1
    return horses


def getNumberOfTentsNeeded(people:int) -> int:
    tents = people // 3
    if people % 3 != 0:
        tents += 1
    return tents


def getTotalRentalCost(horses:int, tents:int) -> float:
    weeks = JOURNEY_IN_DAYS // 7
    if JOURNEY_IN_DAYS % 7 != 0:
        weeks += 1

    tent_cost_gold = tents * COST_TENT_GOLD_PER_WEEK * weeks

    horse_cost_silver = horses * COST_HORSE_SILVER_PER_DAY * JOURNEY_IN_DAYS
    horse_cost_gold = silver2gold(horse_cost_silver)

    return round(tent_cost_gold + horse_cost_gold, 2)

##################### O08 #####################

def getItemsAsText(items:list) -> str:
    teksten = []
    for item in items:
        aantal = item["amount"]
        eenheid = item["unit"]
        naam = item["name"]
        if eenheid:
            teksten.append(f"{aantal}x {aantal}{eenheid} {naam}")
        else:
            teksten.append(f"{aantal}x {naam}")

    if len(teksten) == 0:
        return ""
    if len(teksten) == 1:
        return teksten[0]
    return ", ".join(teksten[:-1]) + " & " + teksten[-1]


def getItemsValueInGold(items:list) -> float:
    total_gold = 0
    for item in items:
        price = item.get("price", {"amount": 0, "type": "copper"})
        amount = item.get("amount", 1)
        price_amount = price.get("amount", 0)
        price_type = price.get("type", "copper")
        
        if price_type == "copper":
            gold_value = copper2gold(price_amount)
        elif price_type == "silver":
            gold_value = silver2gold(price_amount)
        else:  
            gold_value = price_amount
        
        total_gold += gold_value * amount
    
    return round(total_gold, 2)


##################### O09 #####################

def getCashInGoldFromPeople(people: list) -> float:
    totaal = 0
    for persoon in people:
        totaal += getPersonCashInGold(persoon["cash"])
    return round(totaal, 2)

##################### O10 #####################

def getInterestingInvestors(investors: list) -> list:
    result = []
    for inv in investors:
        if inv["profitReturn"] <= 10:
            result.append(inv)
    return result

def getAdventuringInvestors(investors: list) -> list:
    result = []
    for inv in getInterestingInvestors(investors):
        if inv["adventuring"] == True:
            result.append(inv)
    return result

def getTotalInvestorsCosts(investors: list, gear: list) -> float:
    total_cost = 0
    for inv in investors:
        if inv["adventuring"]:  
            horse_cost = COST_HORSE_SILVER_PER_DAY * JOURNEY_IN_DAYS
            tent_cost = COST_TENT_GOLD_PER_WEEK * math.ceil(JOURNEY_IN_DAYS / 7)
            food_cost = getJourneyFoodCostsInGold(1, 1, JOURNEY_IN_DAYS)
            gear_cost = getItemsValueInGold(gear)
            total_cost += (silver2gold(horse_cost) +
                           tent_cost + food_cost + gear_cost)
    return round(total_cost, 2)


##################### O11 #####################

def getMaxAmountOfNightsInInn(leftoverGold: float, people: int, horses: int) -> int:
    cost_one_night = getJourneyInnCostsInGold(1, people, horses)
    if cost_one_night <= 0:
        return 0
    
    nights = int(leftoverGold // cost_one_night)
    return nights

def getJourneyInnCostsInGold(nightsInInn: int, people: int, horses: int) -> float:
    people_silver_total = people * COST_INN_HUMAN_SILVER_PER_NIGHT * nightsInInn
    people_gold = silver2gold(people_silver_total)
    horse_copper_total = horses * COST_INN_HORSE_COPPER_PER_NIGHT * nightsInInn
    horse_gold = copper2gold(horse_copper_total)
    total_gold = people_gold + horse_gold
    return round(total_gold, 2)

##################### O13 #####################
def getInvestorsCuts(profitGold: float, investors: list) -> list:
    cuts = []
    for inv in investors:
        cut = profitGold * (inv['profitReturn'] / 100)  # procent naar goud
        cuts.append(round(cut, 2))
    return cuts


def getAdventurerCut(profitGold: float, investorsCuts: list, fellowship: int) -> float:
    total_investor_cuts = sum(investorsCuts)
    leftover = profitGold - total_investor_cuts
    if fellowship > 0:
        return round(leftover / fellowship, 2)
    return 0.0

##################### O14 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################

def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()