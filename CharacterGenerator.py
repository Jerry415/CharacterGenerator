import random
import sys
import os

# GLOBAL VARIABLES
max_hench = 0
loyalty = 0
reaction = 0
mis_att = 0
str_hit = 0
str_dam = 0
learn_spell = 0
spell_def = 0
spell_bon = 0
cha_reaction = 0
bonus_HP = 0


# DIE SIMULATOR FOR ANY SIDED DIE -- EVEN ODD DIES, D3, D5, ECT.
def die(side):
    die_roll = random.randrange(1, side + 1)
    return die_roll


# STAT GENERATOR. REROLLS 1'S, 2'S AND 3'S ======================================================
def stat():
    total = 0
    stop = 0
    while stop <= 2:
        roll = die(6)
        #REROLL 1'S & 2'S
        if roll > 2:
            total += roll
            stop += 1
    return total


# ROLLS STRENGTH STAT AND CHECKS FOR FIGHTER STRENGTH BONUSES ====================================
def strength(modi, race):
    str_hit = str_dam = eighteen = 0
    strength = stat()

    if race == 4:
        strength -= 1

    # IF THE CHARACTER IS A RANGER AND STRENGTH IS UNDER 13, SETS STRENGTH
    # TO 13.
    if modi == 2:
        if strength < 13:
            strength = 13

    # CHECK FOR FIGHTER'S EXCEPTIONAL STRENGTH BONUS.
    # IF NOT A FIGHTER THEN ASSIGNS REGULAR STRENGTH BONUSES.
    if modi == 1 and strength == 18:
        eighteen = die(100)
        if eighteen <= 50:
            str_hit = 1
            str_dam = 3
        elif 51 <= eighteen <= 75:
            str_hit = 2
            str_dam = 3
        elif 76 <= eighteen <= 90:
            str_hit = 2
            str_dam = 4
        elif 91 <= eighteen <= 99:
            str_hit = 2
            str_dam = 5
        else:
            str_hit = 3
            str_dam = 6
    elif strength == 18:
        str_hit = 1
        str_dam = 2
    elif strength == 17:
        str_hit = 1
        str_dam = 1
    elif strength == 16:
        str_dam = 1


    # PRINTS THE STRENGTH RESULTS ON THE CONSOLE
    if modi == 1 and strength == 18:
        print("Strength: \t\t{}/{}\tHit +{}, Dam +{}"
              .format(strength, eighteen,str_hit, str_dam))
    elif 17 <= strength <= 18:
        print("Strength: \t\t{}\tHit +{}, Dam +{}".format(strength, str_hit, str_dam))
    elif strength == 16:
        print("Strength: \t\t{}\tDam +{}".format(strength, str_dam))
    else:
        print("Strength: \t\t{}".format(strength))


# ROLLS DEXTERITY AND CHECKS FOR BONUSES =======================================================
def dexterity(modi, race):
    dext = stat()

    # CHECKS TO SEE IF CLASS MINIMUM REQUIREMENT IS MET.  IF NOT, SETS
    # THE STAT TO THE MINIMUM REQUIREMENT.

    if (race == 2 or race == 5) and dext < 18:
        dext += 1

    if modi == 2:
        if dext < 13:
            dext = 13

    dex_react = 0
    ac_mod = 0
    if dext == 18:
        dex_react = 2
        mis_att = 2
        ac_mod = 4
    elif dext == 17:
        dex_react = 2
        mis_att = 2
        ac_mod = 3
    elif dext == 16:
        dex_react = 1
        mis_att = 1
        ac_mod = 2
    elif dext == 15:
        ac_mod = 1
    else:
        dex_react = 0
        mis_att = 0
        ac_mod = 0

    # PRINTS DEXTERITY BONUS RESULTS
    if 16 <= dext <= 18:
        print("Dexterity: \t\t{}\tInitiative: +{}, Missile Weapon +{}, AC Adjustment -{}"
              .format(dext, dex_react, mis_att, ac_mod))
    elif dext == 15:
        print("Dexterity: \t\t{}\tAC Adjustment -{}"
              .format(dext, ac_mod))
    else:
        print("Dexterity: \t\t{}".format(dext))

    return ac_mod


# ROLLS INTELLIGENCE AND CHECKS FOR BONUSES ===================================================
def intelligence(modi, race):
    learn_spell = 0
    lang = 0
    intell = stat()

    if race == 3 and intell < 18:
        intell += 1

    if intell == 18:
        learn_spell = 85
        lang = 7
    elif intell == 17:
        learn_spell = 75
        lang = 6
    elif intell == 16:
        learn_spell = 70
        lang = 5
    elif intell == 15:
        learn_spell = 65
        lang = 4
    elif intell == 14:
        learn_spell = 60
        lang = 4
    elif intell == 13:
        learn_spell = 55
        lang = 3
    elif intell == 12:
        learn_spell = 50
        lang = 3
    elif intell == 11:
        learn_spell = 45
        lang = 2
    elif intell == 10:
        learn_spell = 40
        lang = 2
    elif intell == 9:
        learn_spell = 35
        lang = 2
    else:
        lang = 1

    if modi == 5 and (9 <= intell <= 18):
        print("Intelligence: \t{}\tLearn Spell {}%, Languages {}"
              .format(intell, learn_spell, lang))
    else:
        print("Intelligence: \t{}\tLanguages {}".format(intell, lang))


# ROLLS THE WISDOM STAT AND CHECKS FOR BONUSES =========================================
def wisdom(modi, race):
    wisd = stat()

    if race == 5:
        wisd -= 1

    if modi == 2:
        if wisd < 14:
            wisd =14

    if wisd == 18:
        spell_def = 4
        spell_bon = 4
    elif wisd == 17:
        spell_def = 3
        spell_bon = 3
    elif wisd == 16:
        spell_def = 2
        spell_bon = 2
    elif wisd == 15:
        spell_def = 1
        spell_bon = 2
    elif wisd == 14 or wisd == 13:
        spell_bon = 1

    if modi == 3 and (15 <= wisd <= 18):
        print("Wisdom: \t\t{}\tMagic Defense +{}, Bonus Spell Level {}"
              .format(wisd, spell_def, spell_bon))
    elif modi == 3 and (13 <= wisd <= 14):
        print("Wisdom: \t\t{}\tBonus Spell Level {}"
              .format(wisd, spell_bon))
    elif 15 <= wisd <= 18:
        print("Wisdom: \t\t{}\tMagic Defense {}".format(wisd, spell_def))
    else:
        print("Wisdom: \t\t{}".format(wisd,))


# ROLLS THE CONSTITUTION STAT ====================================================================
def constitution(modi, race):
    const = stat()

    if race == 1 and const < 18:
        const += 1
    elif race == 2:
        const -= 1

    if modi == 2:
        if const < 14:
            const = 14

    if modi <= 2 and const == 18:
        bonus_HP = 4
    elif modi <= 2 and const == 17:
        bonus_HP = 3
    elif 16 <= const <= 18:
        bonus_HP = 2
    elif const == 15:
        bonus_HP = 1
    else:
        bonus_HP = 0

    if 15 <= const <= 18:
        print("Constitution: \t{}\tHP Adjustment +{}".format(const, bonus_HP))
    else:
        print("Constitution: \t{}".format(const))
    return bonus_HP

# ROLLS FOR CHARISMA AND CHECKS FOR BONUSES. =====================================================
def charisma(race):
    char = stat()

    if race == 1:
        char -= 1

    if char == 18:
        max_hench = 15
        loyalty = 8
        cha_reaction = 7
    elif char == 17:
        max_hench = 10
        loyalty = 6
        cha_reaction = 6
    elif char == 16:
        max_hench = 8
        loyalty = 4
        cha_reaction = 5
    elif char == 15:
        max_hench = 7
        loyalty = 3
        cha_reaction = 3
    elif char == 14:
        max_hench = 6
        loyalty = 1
        cha_reaction = 2
    elif char == 13:
        max_hench = 5
        cha_reaction = 1
    elif char == 12:
        max_hench = 5
    else:
        max_hench = 4

    if 14 <= char <= 18:
        print("Charisma: \t\t{}\tMax Henchmen {}, Loyalty Base +{}, Reaction Adjustment +{}"
              .format(char, max_hench, loyalty, cha_reaction))
    elif char == 13:
        print("Charisma: \t\t{}\tMax Henchmen {}, Reaction Adjustment +{}"
              .format(char, max_hench, cha_reaction))
    elif char == 12:
        print("Charisma: \t\t{}\tMax Henchmen".format(char, max_hench))
    else:
        print("Charisma: \t\t{}".format(char))
s

# FUNCTION THAT GENERATES A CHARACTER =========================================================
def character_stat_generator(choice, who, alignment, level, race):
    print ("\n\nCharacter Name:", who)

    # GENERATES HIT POINTS EVEN IF THE CHARACTER IS NOT 1ST LEVEL.
    def hit_points_generator(start, level, choice):
        if choice <= 2 and level > 9:
            hit_points_gen = start
            die_roll_HP = 9
            after_nine = (level - 9) * 3
            while die_roll_HP > 1:
                hit_points_gen += die(start)
                die_roll_HP -= 1
            return hit_points_gen + after_nine
        elif choice <= 2 and level <= 9:
            hit_points_gen = start
            while level > 1:
                hit_points_gen += die(start)
                level -= 1
            return hit_points_gen
        elif choice == 3 and level > 9:
            hit_points_gen = start
            die_roll_HP = 9
            after_nine = (level - 9) * 2
            while die_roll_HP > 1:
                hit_points_gen += die(start)
                die_roll_HP -= 1
            return hit_points_gen + after_nine
        elif choice == 3 and level <= 9:
            hit_points_gen = start
            while level > 1:
                hit_points_gen += die(start)
                level -= 1
            return hit_points_gen
        elif choice == 4 and level > 10:
            hit_points_gen = start
            die_roll_HP = 10
            after_nine = (level - 10) * 2
            while die_roll_HP > 1:
                hit_points_gen += die(start)
                die_roll_HP -= 1
            return hit_points_gen + after_nine
        elif choice == 4 and level <= 10:
            hit_points_gen = start
            while level > 1:
                hit_points_gen += die(start)
                level -= 1
            return hit_points_gen
        elif choice == 5 and level > 10:
            hit_points_gen = start
            die_roll_HP = 10
            after_nine = (level - 10) * 1
            while die_roll_HP > 1:
                hit_points_gen += die(start)
                die_roll_HP -= 1
            return hit_points + after_nine
        elif choice == 5 and level <= 10:
            hit_points_gen = start
            while level > 1:
                hit_points_gen += die(start)
                level -= 1
            return hit_points_gen


    hit_points_level = 0
    # PRINTS THE CHOSEN CHARACTER CLASS
    if choice == 1:
        print("Character Class: Fighter")
        start_hp = 10
        hit_points_level = hit_points_generator(start_hp, level, choice)
    elif choice == 2:
        print("Character Class: Ranger")
        start_hp = 10
        hit_points_level = hit_points_generator(start_hp, level, choice)
    elif choice == 3:
        print("Character Class: Cleric")
        start_hp = 8
        hit_points_level = hit_points_generator(start_hp, level, choice)
    elif choice == 4:
        print("Character Class: Thief")
        start_hp = 6
        hit_points_level = hit_points_generator(start_hp, level, choice)
    elif choice == 5:
        print("Character Class: Magic User")
        start_hp = 4
        hit_points_level = hit_points_generator(start_hp, level, choice)

    print("Level:", str(level))

    # PRINTS THE ALIGNMENT
    if alignment == 1:
        print("Alignment: Lawful Good")
    elif alignment == 2:
        print("Alignment: Neutral Good")
    elif alignment == 3:
        print("Alignment: Chaotic Good")
    elif alignment == 4:
        print("Alignment: Lawful Neutral")
    elif alignment == 5:
        print("Alignment: Neutral")
    elif alignment == 6:
        print("Alignment: Chaotic Neutral")
    elif alignment == 7:
        print("Alignment: Lawful Evil")
    elif alignment == 8:
        print("Alignment: Neutral Evil")
    elif alignment == 9:
        print("Alignment: Chaotic Evil")


    if race == 1:
        print("Race: Dwarf")
    elif race == 2:
        print("Race: Elf")
    elif race == 3:
        print("Race: Gnome")
    elif race == 4:
        print("Race: Halfling")
    elif race == 5:
        print("Race: Human")



    # PRINTS OUT RANDOM STATS FOR THE NPC
    print(" ")
    strength(choice, race)
    armor_adj = dexterity(choice, race)
    intelligence(choice, race)
    wisdom(choice, race)
    con_bonus = constitution(choice, race)
    charisma(race)

    # STARTING ARMOR CLASS
    armor_class = 10 - armor_adj

    # STARTING HIT POINTS
    hit_points = con_bonus * adjust_HP_bonus + hit_points_level

    print("\nHit Points: {}".format(hit_points))
    print("Armor Class: {}".format(armor_class))




'''
THE START OF CHARACTER GENERATING!!! =======================================================================
'''
# GIVES THE CHARACTER A NAME.
name = input("What is this character's name? ")

# PROMPTS USER TO CHOSE A CHARACTER CLASS AND STORE THE
# INPUT AS AN INTEGER.


class_choice = int(input("Choose a character class: \n "
                         "\t1) Figher\n \t2) Ranger\n \t3) Cleric\n "
                         "\t4) Thief\n\t5) Magic User\n"))
while 1 > class_choice or class_choice > 5 or str(class_choice):
    print("Please enter a number from 1 to 5.")
    class_choice = int(input("Choose a character class: \n "
                         "\t1) Figher\n \t2) Ranger\n \t3) Cleric\n "
                         "\t4) Thief\n\t5) Magic User\n"))

# PROMPTS USER TO CHOSE AN ALIGNMENT FOR THE CHARACTER.

if class_choice == 2:
    align = int(input("\nAlignment? \n \t1) Lawful Good\n \t2) Neutral Good\n \t3) Chaotic Good\n"))
    while align < 1 or align > 3:
        print("Chose a number between 1 and 3")
        align = int(input("\nAlignment? \n \t1) Lawful Good\n \t2) Neutral Good\n \t3) Chaotic Good\n"))
else:
    align = int(input("\nAlignment? \n \t1) Lawful Good\n \t2) Neutral Good\n "
              "\t3) Chaotic Good\n \t4) Lawful Neutral\n "
              "\t5) Neutral\n \t6) Chaotic Neutral\n \t7) Lawful Evil\n"
              "\t8) Neutral Evil\n \t9) Chaotic Evil\n"))
    while align < 1 or align > 9:
        print("Please pick a number between 1 and 9")
        align = int(input("\nAlignment? \n \t1) Lawful Good\n \t2) Neutral Good\n "
              "\t3) Chaotic Good\n \t4) Lawful Neutral\n "
              "\t5) Neutral\n \t6) Chaotic Neutral\n \t7) Lawful Evil\n"
              "\t8) Neutral Evil\n \t9) Chaotic Evil\n"))

# GIVES THE CHARACTER A LEVEL AND ADJUSTS THE STATS ACCORDINGLY.
level = int(input("What level is this character?"))
adjust_HP_bonus = 0
if class_choice <= 3 and level > 9:
    adjust_HP_bonus = 9
else:
    adjust_HP_bonus = 10

# CHOOSES A RACE
if class_choice == 2:
    race = int(input("Choose a race: \n"
                 "\t2) Elf\n \t5) Human\n"))
    while race != 2 and race != 5:
        print("Please chose either human or elf.")
        race = int(input("Choose a race: \n"
                 "\t2) Elf\n \t5) Human\n"))
else:
    race = int(input("Choose a race: \n"
                 "\t1) Dwarf\n \t2) Elf\n \t3) Gnome\n"
                 "\t4) Human\n \t5) Halfling\n"))
    while race < 1 or race > 5:
        print("Chose a number between 1 and 5.")
        race = int(input("Choose a race: \n"
                 "\t1) Dwarf\n \t2) Elf\n \t3) Gnome\n"
                 "\t4) Halfling\n \t5) Human\n"))

# FUCNTION CALL TO GENERATE THE NPC.
character_stat_generator(class_choice, name, align, level, race)
