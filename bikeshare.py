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
    while True:
        city = input("\nenter the name of city chicago, new york city, washington\n").lower()
        if city not in CITY_DATA:
            print('please enter the correct city name.')
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('enter the name for month january, february, march, april, may, june, or enter "all months').lower()
        months_list = ['january', 'february', 'march', 'april', 'may', 'june']
        if month not in months_list and month != 'all':
            print('enter the correct month name')
        else:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('enter the name for day, or enter "all" days').lower()
        days_list = ['saturday', 'sunday', 'monday' 'tuesday', 'wednesday', 'thursday', 'friday' ]
        if day not in days_list and day != 'all':
            print('enter correct day')
        else:
            break
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
        months_list = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months_list.index(month) + 1

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

    most_common_month = df['month'].mode()[0]
    print('Most Common Month:', most_common_month)

    # TO DO: display the most common day of week

    most_common_day = df['day_of_week'].mode()[0]
    print('Most Common day:', most_common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('Most Common Hour:', most_common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
                    # TO DO: display the m     # TO DO: display the most common day of week

    # TO DO: display the most common start hour

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station' , common_start_station)

      # TO DO: display most commonly used end station

    common_end_station = df['End Station'].mode()[0]

    print('The most commonly used end station, common_end_station')



    # TO DO: display most frequent combination of start station and end station trip
    start_end_station = df.groupby(['Start Station', 'End Station']).count().idxmax()
    print('\nmost commonly used combination of start station and end station trip:', start_end_station) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
          
    # TO DO: display total travel time
    total_travel_time =df['Trip Duration'].sum()      
    print('Total travel time:', total_travel_time, 'seconds','or',  total_travel_time/3600, 'hour' )
    

    # TO DO: display mean travel time
    avg_time = df['Trip Duration'].mean()
    print('average travel time:', avg_time, 'seconds', avg_time/3600, 'hour')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('counts of user types', user_types)
    

    # TO DO: Display counts of gender
    try:
       gender_types = df['Gender'].value_counts()
       print('\ngender types:\n', gender_types)
    except KeyError:
       print("\ngender types:\n unvalid data.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      earliest_year = df['Birth Year'].min()
      print('\nearliest year:', earliest_year)
    except KeyError:
      print("\nearliest year:\n unvalid data.")
    try:
       recent_year = df['Birth Year'].max()
       print('\nmost recent year:', recent_year)
    except KeyError:
      print("\nMost Recent Year:\nunvalid data.")

          
    try:
      common_year = df['Birth Year'].value_counts().idxmax()
      print('\nmost common year:', common_year)
    except KeyError:
      print("\nmost common year:\nunvalid data.")         

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
       #display 5 raws of data to user
def display_raw_data(city):
    print('\nRaw data is available to check... \n')
    display_raw = input('To View the availbale 5 raw data enter: Yes or No ').lower()
    while display_raw not in ('yes', 'no'):
        print('invalid , please try again')
        display_raw = input('To View the availbale 5 raw data enter: Yes or No ').lower()
   
# The second while loop 
    while display_raw == 'yes':
        try:
            for chunk in pd.read_csv(CITY_DATA[city], index_col = 0 ,chunksize=5):
                print(chunk)
                display_raw = input('To View the availbale raw in chuncks of 5 rows type: Yes\n').lower()
                if display_raw != 'yes':
                    print('Thank You')
                    break #breaking of for loop
            break

        except KeyboardInterrupt:
            print('Thank you.')

def main():
    while True:
        city, month, day = get_filters()

        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	 main()
