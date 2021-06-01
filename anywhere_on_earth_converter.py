from simpleimage import SimpleImage
import pytz
from pytz import timezone, tzinfo
from datetime import datetime, timedelta
utc = pytz.utc
utc.zone

tz1 = 'Time-Zones/TimeZone1.png'
tz2 = 'Time-Zones/TimeZone2.png'
tz3 = 'Time-Zones/TimeZone3.png'
tz4 = 'Time-Zones/TimeZone4.png'


def main():
    space()
    print("                   Welcome to Code in Place's very own Anywhere on Earth (AoE) Time Zone Converter!\n\n               The Anywhere on earth (AoE) time zone is Code In Place's chosen time zone to create assignment\n          deadlines for all the students taking Code In Place. This is useful because there are students from all\n                    over the world up to 140 countries on 7 continents taking this course, making\n                 the Anywhere on Earth time zone a perfect choice to account for all possible time zones. ")
    space()
    print("You can choose from two features! You can choose the time & date your assignment is due OR the current time & date in Anywhere on Earth")
    print("")

    assignment_time = input("Would you like to know when your Assignment is due Anywhere on Earth(AoE)? Yes or No: " + new_line())
    current_conversion = input("Would you like to know what the current time is Anywhere on Earth(AoE)? Yes or No: " + new_line())
    show_time_zone_data()

    choose_feature(assignment_time, current_conversion)
    feature_selection(assignment_time, current_conversion)

def show_time_zone_data():
    showImg = get_file()
    orig = SimpleImage(showImg)
    orig.show()
    orig2 = SimpleImage(tz2)
    orig2.show()
    orig3 = SimpleImage(tz3)
    orig3.show()
    orig3 = SimpleImage(tz4)
    orig3.show()

def get_file():
    # Read image file path from user, or use the default file
    filename = input("First find your Time Zone!\nMake sure to spell your time zone exactly as shown on the list.\nIf there is a space in the time zone use an underscore where indicated.\n\n To see the list of all usable time zones press enter and after seeing the list press enter again to continue : ")
    print('')
    if filename == '':
        filename1 = tz1
    return filename1

def feature_selection(present, incoming):
    if present == 'Yes' and incoming == 'No':
        return due_date()
    elif present == 'Yes' and incoming == 'No':
        return current_time()
    elif present == 'Yes' and incoming == 'Yes':
        current_time(), due_date()
    space()

def current_time():
    get_file()
    chosen_time_zone = str(input('What is your Time Zone? '))
    chosen_date = str(input('What is todays date? Please use this format: YYYY-MM-DD '))
    chosen_time = str(input('What is todays time? Please use 24 Hour format: 00:00: '))
    tri_space()
    time_zone = timezone(chosen_time_zone)

    time_and_date = chosen_date + " " + chosen_time

    check_daylight_savings = time_zone.localize(datetime.strptime(time_and_date, '%Y-%m-%d %H:%M'))

    your_time_zone = check_daylight_savings.astimezone(time_zone)

    utc_time = check_daylight_savings.astimezone(utc)

    #format time zone to show timezone acronym
    format_your_time_zone = your_time_zone.strftime('%Y-%m-%d %H:%M %Z%z')
    format_UTC = utc_time.strftime('%Y-%m-%d %H:%M %Z%z')

    #remove timezone info to do arithmetic without aware offsets and retrieve Anywhere On Earth Time.
    time_zone_removed = check_daylight_savings.replace(tzinfo=None).astimezone(utc)
    time_zone_state = time_zone_removed.replace(tzinfo=utc_time.tzinfo)
    aoe_subtraction = utc_time.replace(tzinfo=time_zone_removed.tzinfo) - timedelta(hours=12)

    anywhere_on_earth_time = aoe_subtraction.strftime('%Y-%m-%d %H:%M')
    #
    space()

    print("     If the time in " + chosen_time_zone + " is:  " + format_your_time_zone + " hours\n")
    print("     And time in Universal Time Coordinated(UTC) is:  " + format_UTC + " hours\n")
    print("     Then time Anywhere On Earth(AoE) is: " + str(anywhere_on_earth_time) + " AoE UTC-1200 hours Anywhere on Earth, Baker Island. \n\n                      Anywhere On Earth(AoE)the last place on earth where the date ends!\n                It is located in the remote Baker Islands and is the last designated timezone\n                                 in the globe before the end of each date")


def due_date():
    get_file()
    chosen_time_zone = str(input('What is your Time Zone? '))
    chosen_date = str(input('What date is your assignment due in Anywhere On Earth(AoE)? Please use this format: YYYY-MM-DD '))
    chosen_time = str(input('What time is your assignment due in Anywhere On Earth(AoE)? Please use 24 Hour format: 00:00: '))
    tri_space()
    time_zone = timezone(chosen_time_zone)

    time_and_date = chosen_date + " " + chosen_time

    str_time_date = str(time_and_date)

    given_datetime = utc.localize(datetime.strptime(str_time_date, '%Y-%m-%d %H:%M'))

    retrieved_utc = given_datetime + timedelta(hours=12)

    convert_to_tz = retrieved_utc.astimezone(time_zone)

    format_tz = convert_to_tz.strftime('%Y-%m-%d %H:%M %Z%z')

    print(" ")
    print("     If the due date of your assignment is "  + time_and_date + " hours in Anywhere On Earth(AoE) time")
    print("         Then your assignment is due on: " + str(format_tz) + " " + chosen_time_zone + " time" + "\n\n\n                            Attn: All hours are based on 24 Hour date time\n\n                     Anywhere On Earth(AoE)the last place on earth where the date ends!\n                It is located in the remote Baker Islands and is the last designated timezone\n                                 in the globe before the end of each date.")

def choose_feature(future, current):
    space()
    space()

    space()

    if (future == 'yes' or 'Yes'): 
        return 'Yes'
    else: 
        return 'No'
    if (current == 'yes' or 'Yes'):
        return 'Yes'
    elif (current and future == 'no' or 'No'):
        print("Please choose one of these two features to convert your time or you can choose when your are ready. Thank You.")

    
    
def space():
    print(" ")
    print(" ")

def tri_space():
    print(" ")
    print(" ")
    print(" ")

def new_line():
    newline = "\n\n\n"
    return newline


if __name__ == '__main__':
    main()
