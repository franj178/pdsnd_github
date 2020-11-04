import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #def an empty city variable, used to store users city input
    city = ''
    #while loop to assure the correct input from the user
    while city not in CITY_DATA.keys():
        print('Choose one of the following cities names to analyze the US bikeshare data.')
        print('1. Chicago')
        print('2. New York city')
        print('3. Washington')
        print('\nPlease insert the name of your selected city:')
        #convert the input into lower case, to compare with the keys of CITY_DATA
        city = input().lower()
        if city not in CITY_DATA.keys():
            print('\nYour input was incorrect, use the full name of the city, as shown above, please try again!')
            print('\nThe program is restarting')
    print(f"\nYou have chosen {city.title()} as the city you want to analyze.")
        
    # TO DO: get user input for month (all, january, february, ... , june)
    MONTHS = {'january','february','march','april','may','june','all'}
    month = ''
    while month not in MONTHS:
        print('\nPlease select the month you want to analyze: january, february, march, april, june or all the avaible months.')
        print('Remember, the accepted input is the month name, not case sensitive.')
        #convert the input into lower case, to compare with the MONTHS list
        month = input().lower()
        if month not in MONTHS:
            print('Your input is incorrect, please try again.')
    print(f"\nYou have chosen {month.title()} as your month.")
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    DAYS = ['monday','tuesday','wednesday','thrusday','friday','saturday','sunday','all']
    day = ''
    while day not in DAYS:
        print('\nPlease select the day you want to analyze: monday, tuesday, wednesday, thursday, friday, saturday, sunday or all the avaible days.')
        print('Remember, the accepted input is the day name, not case sensitive.')
        #convert the input into lower case, to compare with the DAYS list
        day = input().lower()
        if day not in DAYS:
            print("\nInvalid input. Please try again using one of the accepted input formats.")
            print("\nRestarting...")

    print(f"\nYou have chosen {day.title()} as your day.")
    print(f"\nYou have chosen to view data for city: {city.upper()}, month/s: {month.upper()} and day/s: {day.upper()}.")
    
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
        
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    print("\nLoading data...")
    df = pd.read_csv(CITY_DATA[city])
       
    #Start time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #month and day 
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
        
    #month filter
    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1
        # df with the filter applied
        df = df[df['month'] == month]
        
    #day filter
    if day != 'all':
        #df with the filter applied
        df = df[df['day_of_week'] == day.title()]
     
    #returns the filtered df with the selected values
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print(f"Most Common Month (1 = January,...,6 = June): {common_month}")
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print(f"\nMost Common Day: {common_day}")

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print(f"\nMost Common Start Hour: {common_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f"The most commonly used start station: {common_start_station}")

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f"\nThe most commonly used end station: {common_end_station}")

    # TO DO: display most frequent combination of start station and end station trip
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    combination = df['Start To End'].mode()[0]
    print(f"\nThe most frequent combination of trips are from {combination}.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    minute, second = divmod(total_travel, 60)
    hour, minute = divmod(minute, 60)
    print(f"The total travel time is {hour} hours, {minute} minutes and {second} seconds.")

    # TO DO: display mean travel time
    average_duration = round(df['Trip Duration'].mean())
    mins, sec = divmod(average_duration, 60)
    if mins > 60:
        hrs, mins = divmod(mins, 60)
        print(f"\nThe mean travel time is {hrs} hours, {mins} minutes and {sec} seconds.")
    else:
        print(f"\nThe mean travel time is {mins} minutes and {sec} seconds.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print(f"The types of users by number are the following:\n\n{user_type}")

    # TO DO: Display counts of gender
    # try if there is no column for gender
    try:
        gender = df['Gender'].value_counts()
        print(f"\nThe types of users by gender are the following:\n\n{gender}")
    except:
        print("\nThere is no 'Gender' column in the current file.")

    # TO DO: Display earliest, most recent, and most common year of birth
    #try in case there is no year of birth, check for the 'Birth Year' data, if not, print exception.
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print(f"\nThe earliest year of birth: {earliest}\n\nThe most recent year of birth: {recent}\n\nThe most common year of birth: {common_year}")
    except:
        print("There are no birth years details in the current file.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Displays 5 rows of data from the csv file for the selected city.
    Args:
        param1 (df): The data frame you wish to work with.
    Returns:
        None.
    """
    YES_NO = ['yes', 'no']
    rdata = ''
    counter = 0
    while rdata not in YES_NO:
        print("\nDo you wish to view the raw data?")
        print("\nAccepted responses:\n-yes\n-no")
        rdata = input().lower()
        #the raw data from the df is displayed if user select 'yes'
        if rdata == "yes":
            print(df.head())
        elif rdata not in YES_NO:
            print("\nPlease check your input.")
            print("Input does not seem to match any of the accepted responses.")
            print("\nRestarting...\n")

    #continue to view data?
    while rdata == 'yes':
        print("Do you wish to view more raw data?")
        counter += 5
        rdata = input().lower()
        #If user says yes display 5 next rows
        if rdata == "yes":
             print(df[counter:counter+5])
        elif rdata != "yes":
             break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

#THIS FILE IS MODIFIED TO BE USED ON GIT PROJECT