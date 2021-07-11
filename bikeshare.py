import time
import pandas as pd
import numpy as np
import calendar

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
    print('\nHello! Let\'s explore some US bikeshare data!')

    # create default values for month and day variables
    month = " "
    day = " "

    # get user input for city (chicago, new york city, washington) using while loop to handle invalid answers
    while True:
            city = input("\nWould you like to see data for Chicago, New York City or Washington?\n").lower()
            if city not in CITY_DATA:
                print("\nOoops. That's not a valid answer. Please try again.\n")
                continue
            else:
                print("\nLoading all available data for {}...\n".format(city.title()))
                break

    # get user input for month (all, january, february, ... , june)
    while True:
            month = input("\nWould you like to see data for all months or would you like to filter by month? Please type 'all', 'january', 'february', 'march', 'april', 'may', or 'june'.\n").lower()
            if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
                print("\nOoops. That's not a valid answer. Please try again.\n")
                continue
            else:
                break
    if month == 'all':
                print("\nLoading all unfiltered data available...\n")
    else:
            print("\nLoading all available data for {}...\n".format(month.title()))

     # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
            day = input("\nWould you like data for all days of the week or would you like filter by day? Please type 'all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' or 'sunday'.\n").lower()
            if day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
                print("\nOoops. That's not a valid answer. Please try again.\n")
                continue
            else:
                break
    if day == 'all':
                print("\nLoading all unfiltered data available...\n")
    else:
            print("\nLoading all available data for {}...\n".format(day.title()))

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
    # load data file into a DataFrame
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    # filter by month to create a new DataFrame
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new DataFrame
        df = df[df['day_of_week'] == day.title()]

    return df

def raw_data(df):
    """Displays first 5 lines of raw data upon user request"."""

    # user input to see if they want to see 5 lines of raw data
    view_raw_data = input("\nWould you like to see 5 lines of raw data? Please type 'y' or 'n'.\n").lower()
    start_loc = 0
    while view_raw_data == 'y':
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_raw_data = input("\nWould you like to view five more lines of raw data? Please type 'y' or 'n'.\n").lower()
        if view_more_data == 'n':
            break
    else:
        if view_raw_data not in ('y', 'n'):
            print("\nOops. That's not a valid answer. Please type 'y' or 'n'.\n")
            view_raw_data = input("\nWould you like to see 5 lines of raw data? Please type 'y' or 'n'.\n").lower()

print('-'*40)


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    popular_month_name = calendar.month_name[popular_month]
    print("Most Popular Month:", popular_month_name)

    # display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print("Most Popular Day of Week:", popular_day_of_week)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("Most Popular Start Hour:", popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode(0)[0]
    print("Most Popular Start Station:", popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode(0)[0]
    print("Most Popular End Station:", popular_end_station)

    # display most frequent combination of start station and end station trip
    df['popular_station_combination'] = df['Start Station'] + " - " + df['End Station']
    print("Most Popular Start and End Station Combination:", format((df['popular_station_combination'].mode()[0])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_duration = df['Trip Duration'].sum()
    print("Total Duration: ", total_duration)

    # display mean travel time
    average_duration = df['Trip Duration'].mean()
    print("Average Duration: ", average_duration)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    if "User Type" in df.columns:
        user_type_counts = df['User Type'].value_counts()
        print("Breakdown by User Type:\n",user_type_counts)
    else:
        print("\n'User Type' data not available\n")

    # Display counts of gender
    if "Gender" in df.columns:
        gender_count = df['Gender'].value_counts()
        print("\nBreakdown by Gender:\n",gender_count)
    else:
        print("\n'Gender' data not available\n")

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year = int(df['Birth Year'].min().astype)
        most_recent_birth_year = int(df['Birth Year'].max().astype)
        most_common_birth_year = int(df['Birth Year'].mode()[0].astype)
        print("\nEarliest Birth Year: ", earliest_birth_year)
        print("Most Recent Birth Year:" , most_recent_birth_year)
        print("Most Common Birth Year: ", most_common_birth_year)
    else:
        print("'Birth Year' data not available")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
