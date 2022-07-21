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
    # MAKE TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        try:
            city = input("Enter name city (you can see chicago, new_york_city, washington: ").lower()
            if city in CITY_DATA:
                break
            else:
                print("You should enter name city in the right format, try with chicago, new_york_city, washington")
        except:
            print("You should enter name city in the right format, try with chicago, new_york_city, washington")
    
    # TO DO SOMETHING: get user input for month (all, january, february, ... , june)
    
    month_data = { 'january', 'february', 'march', 'april', 'may', 'june'}
    
    while True:
        try:
            month = input("Enter a month (you can see january, february, march, april, may, june) or all: ").lower()
            if month in month_data or all:
                break
            else:
                    print("You should enter month in the right format, try with january, february, march, april, may, june")
        except:
                    print("You should enter month in the right format, try with january, february, march, april, may, june") 
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    week_data = { 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'}
    
    while True:
        try:
            day = input("Enter a week day (you can see monday, tuesday, wednesday, thursday, friday, saturday, sunday) or all: ").lower()
            if day in week_data or all:
                break
            else:
                print("You should enter week day in the right format, try with monday, tuesday, wednesday, thursday, friday, saturday, sunday")
        except:
            print("You should enter week day in the right format, try with monday, tuesday, wednesday, thursday, friday, saturday, sunday")

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
# load data file into a dataframe

    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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
        df = df[df['day_of_week'] == day.title()]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:', popular_month)

    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('Most Popular Day of Week:', popular_day_of_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    
    df['Start and End Station Trip'] = df['Start Station'] + ' - ' + df['End Station']
    popular_start_station_and_end_station = df['Start and End Station Trip'].mode()[0]
    print('Most Popular Start and End Station:', popular_start_station_and_end_station)

    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print('-'*40)


def trip_duration_stats(df):
    
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The sum of Trip Duration is: ',df['Trip Duration'].sum(),'seconds')

    # TO DO: display mean travel time
    
    print('The mean of Trip Duration is: ',round(df['Trip Duration'].mean(),1),'seconds')
    
    

    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    
    try:
        gender = df['Gender'].value_counts()
        print(gender)
            
    except:
        print("You can't see gender information for Washington") 

    # TO DO: Display earliest, most recent, and most common year of birth
    
    
    try:
        print('The earliest year of birth is: ', int(df['Birth Year'].min()))
        print('The most recent year of birth is: ', int(df['Birth Year'].max()))
        print('The most common year of birth is: ', int(df['Birth Year'].mode()))   
    except:
         print("You can't see Birth Year information for Washington") 
    
 
    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print('-'*40)

    
def display_raw_data(df):
    
    """ Your docstring here """
    i = 0
    raw = input("Wish you see 5 more rows of data? yes or no: ").lower() # TO DO: convert the user input to lower case using lower() function
    pd.set_option('display.max_columns',200)

    while True:            
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df[i:(i+5)]) # TO DO: appropriately subset/slice your dataframe to display next five rows
            raw = input("Wish you see 5 more rows of data? yes or no: ").lower() # TO DO: convert the user input to lower case using lower() function
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()
    

def main():
    
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
