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
    cities = ['chicago', 'new york city', 'washington']
    while True:
        city = input("Enter a city to be explored (chicago, new york city, washington):\n").strip().lower()
        if city in cities:
            break
        else:
            print("City name is not valid. Please enter one of the specified cities.")
    print('\n')
    
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all','january','february','march','april','may','june']
    while True:
        month = input("Which month(s) would you like to explore (all,january,february,march,april,may,june):\n").strip().lower()
        if month in months:
            break
        else:
            print("You have entered an incorrect month.Please enter one of the specified months")
    print('\n')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_of_week = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    while True:
        day = input("Which of the day(s) of the week would you like to explore (all,monday,tuesday,wednesday,thursday,friday,saturday,sunday):\n").strip().lower()
        if day in day_of_week:
            break
        else:
            print("You have entered an incorrect day.Please enter one of the specified day_of_week")
    print('\n')

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
    # load data for specified city into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time and End Time columns to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    # extract month and day of week from Start Time to create 'month' and 'day_of_week' columns
    df['month'] = df['Start Time'].dt.month
    
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    
    # filter data by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        df = df[df['month'] == month]
        
    # filter data by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most common month: {}'.format(popular_month))

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most common day of week: {}'.format(popular_day))

    # TO DO: display the most common start hour
    popular_start_hour = df['hour'].mode()[0]
    print('Most common start hour: {}:00'.format(popular_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('{} is the most commonly used start station'.format(most_common_start_station))


    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('{} is the most commonly used end station'.format(most_common_end_station))


    # TO DO: display most frequent combination of start station and end station trip
    df['trip_route'] = df['Start Station'] + ' to ' + df['End Station']
    most_freq_trip_route = df['trip_route'].mode()[0]
    print('The most frequent trip route is from {}'.format(most_freq_trip_route))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time was: {} seconds'.format(total_travel_time))

    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('The average travel time was: {} seconds'.format(average_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    # Set the display option to show all columns
    pd.set_option("display.max_columns", 200)

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('These are the recorded users:\n {}'.format(user_types))
    print('\n')
    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('These are the recorded gender:\n {}'.format(gender_count))
    except:
        print('The gender parameter is not included in this city\'s data\n')

    # TO DO: Display earliest, most recent, and most common year of birth      
    #convert birth year from float to int
    try:
        df['Birth Year'] = df['Birth Year'].astype(int)
        earliest = df['Birth Year'].min()
        recent = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]
        print('The youngest user was born in the year {}'.format(earliest))
        print('The oldest user was born in the year {}'.format(recent))
        print('The most occuring year of birth was the year {}'.format(most_common_year))
    except:
        print('The birth year parameter is not included in this city\'s data')
        
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    # Ask if user wants to see raw data
    start = 0
    while True:
        display_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
        if display_data == 'yes':
            print('Displaying 5 rows of trip data\n')
            print(df.iloc[start:(start+5)])
            start += 5
        else:
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
