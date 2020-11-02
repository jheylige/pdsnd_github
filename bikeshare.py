import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

city_names = ['chicago', 'new york city', 'washington']
month_names = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
day_names = ['all', 'sunday', 'monday', 'tuesday',
             'wednesday', 'thrusday', 'friday', 'saturday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid input
    try:
        city = input('Which city would you like to select? Chicago, New York City or Washington? ').lower()
        while (city not in city_names):
            print("You entered an invalid city please try again")
            city = input("Enter valid city name: ").lower()
        print("You selected ", city, " thank you!")
    except e:
        print("An exception occurred {}".format(e))

    # TO DO: get user input for month (all, january, february, ... , june)
    try:
        month = input('Which month would you like to filter? (from January up to June or all) ').lower()
        while (month not in month_names):
            print('This is not a valid month, please try again')
            month = input("Enter valid month name: ").lower()
        print("You selected ",month," thank you!")
    except e:
        print("An exception occurred {}".format(e))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    try:
        day = input('Which day of week would you like to select (Monday up to Sunday or all) ').lower()
        while (day not in day_names):
            print('this is not a valid day , please try again!')
            day = input("Enter valid day name: ").lower()
        print("You selected ",day," thank you!")
    except e:
        print("An exception occurred {}".format(e))

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

    df = pd.read_csv(CITY_DATA[city])

    # Converted the Start and End Time columns to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract out month & day and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':

    # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':

    # filter by day of week to create the new dataframe
        df[df['day_of_week'] == day.title()]


    return df

import calendar # Import the calendar module

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Create a column for month, day of week and hour from Start Time column in DateTime format
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    month = df['Start Time'].dt.month
    day_of_week = df['Start Time'].dt.weekday_name
    hour = df['Start Time'].dt.hour

    # TO DO: display the most common month
    common_month= df['month'].mode()[0]
    common_month = calendar.month_name[common_month]
    print('The most common month is',common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    common_day = calendar.day_name[common_day]
    print('The most common day is',common_day)

    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    common_hour_count = hour.value_counts().max()
    print('The most common start hour is {} and count is {}'.format(common_start_hour,common_hour_count))

    print("\nThe results took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Create a column for start station, end station
    df['Start Station'] = df['Start Station'].mode()[0]
    df['End Station'] = df['End Station'].mode()[0]

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most popular start station is {}".format(common_start_station))

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print("The most popular end station is {}".format(common_end))

    # TO DO: display most frequent combination of start station and end station trip
    popular_trip=df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print("The most popular trip from start to end is: \n {}".format(popular_trip))

    print("\nThe results took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['Trip Duration'] = df['Trip Duration'].mode()[0]

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum() / 60 / 60 /24
    print("The total travel time is {} seconds".format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = (df['Trip Duration'].mean()) / 60
    print("The average travel time is {} minutes".format(mean_travel_time))

    print("\nThe results took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        user_type = df['User Type'].value_counts()
        print('Count of users by type:\n',user_type)

    # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print('\nGender count:\n', gender)

    # TO DO: Display earliest, most recent, and most common year of birth
        birth_year = df['Birth Year']
        print("\nEarliest year of birth:", birth_year.min())
        print("Most recent year of birth:", birth_year.max())
        print("Popular year of birth:", birth_year.mode()[0])

    except KeyError:
        print("No data available for Washington")

    print("\nThe results took %s seconds." % (time.time() - start_time))
    print('-'*40)


    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    i = 0
    while view_data in ['yes'] and i+5 < df.shape[0]:
        print(df.iloc[i:i+5])
        i += 5
        view_data = input('Do you wish to continue? Please enter yes or no: ').lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart the analysis? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
