import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

city =''
month =''
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    #get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        cities= ['chicago', 'new york', 'washington']
        city = input("which city data would you like to see? \n Chicago, Washington or New York\n").lower()
        if city in cities:
            print('you have selected {} as your city of choice'.format(city))
            break
        else:
            print(' please enter one of the cities stated above')
    
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
        month = input("\nN.B data only available for the first six months.\nwhat month(s) would you like to see \n type 'all' if you're intrested in everything\n").lower()
        if month in months:
            print('you have chosen {}'.format(month))
            break
        else:
            print('please type in a valid month')
        
 
    #get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' 'sunday', 'all']
        day = input("\nwhat day are you interested in? \ntype 'all' if you're interested in everything\n").lower()
        if day in days:
             print("You have chosen {} as your day.".format(city))
             print(f"\nYou have chosen to view data for city: {city.upper()}, month/s: {month.upper()} and day/s: {day.upper()}.")
             break
        else:
            print('please type in a valid day')
            
    print('-'*50)
    return city, month, day


def load_data(city,month,day):
    
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # loading data file into a dataframe
    print("\n....data loading, please be patient")
    df = pd.read_csv(CITY_DATA[city])
      # converting start time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month,day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    #Filtered by month if applicable
    if month != 'all':
        #index of the months list to get the corresponding integer
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
      
        #Filtered by month to create the new dataframe
        df = df[df['month'] == month]
        #print("============", df) 
    #Filtering by day of week, 
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]  
        #print("------------------", df) 
    return df
    

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #the most common month of travel
    pop_month = df['month'].mode()

    print('the most poular month of travel is {}'.format(pop_month))

    #the most common day of week
    pop_day_of_week = df['day_of_week'].mode()

    print('The most popular day of travel is {}'.format(pop_day_of_week))

    # display the most common start hour
    pop_start_hour = df['hour'].mode()
    print('The most popular start hour is {}'.format(pop_start_hour))
    
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #displaying most commonly used start station
    pop_start_station = df['Start Station'].mode()
    print('The most commonly used start station is {}'.format(pop_start_station))

    #displaying most commonly used end station
    pop_end_station = df['End Station'].mode()
    print('The most commonly used end station is {}'.format(pop_end_station))

    # displaying most frequent combination of start station and end station trip
    # created a new column by combining the start and end station
    #Used mode to display most frequent combination of start station and end station trip
    df['Start to End Station'] = df['Start Station'] + ' ' + 'TO' + ' ' +  df['End Station']
    pop_combination = df['Start to End Station'].mode()
    print('The most common start to end station is {}'.format(pop_combination))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #displaying total travel time
    tot_travel_time = df['Trip Duration'].sum()
    #duration in minutes and seconds format
    minute, second = divmod(tot_travel_time, 60)
    #the duration in hour and minutes format
    hour, minute = divmod(minute, 60)
    print("The total trip duration: {} hour(s) {} minute(s) {} second(s)".format(hour, minute, second))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is {}.'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    #Displaying counts of user types
    count_user_types = df['User Type'].value_counts()
    print('Count of User Types:\n {}'.format(count_user_types))

    #Displaying counts of gender
    if city == 'chicago':
        print('The Gender Count is:')
        print(df['Gender'].value_counts())
    elif city == 'new york': 
        print('The Gender Count is:')
        print(df['Gender'].value_counts())
    else:
        print('\n Your chosen city does not have stats for gender')
       
    #Display earliest, most recent, and most common year of birth
    if city == 'chicago':
        most_common_year = df['Birth Year'].mode()
        print('The Most Common Birth Year is : {}'.format(most_common_year))
        most_recent_year = df['Birth Year'].max()
        print('The Youngest User was born {}'.format(most_recent_year))
        earliest_year = df['Birth Year'].min()
        print('The Oldest User was born {}'.format(earliest_year))
    elif city == 'new york':
        most_common_year = df['Birth Year'].mode()
        print('The Most Common Birth Year is : {}'.format(most_common_year))
        most_recent_year = df['Birth Year'].max()
        print('The Youngest User was born {}'.format(most_recent_year))
        earliest_year = df['Birth Year'].min()
        print('The Oldest User was born {}'.format(earliest_year))
    else:
        print('\nYo;ur chosen city does not have stats for Year of Birth')
     
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)
    
    
def display_data(df):
    ''' 
    Displays the data set used for the analysis in steps of five rows based on users intrest
    
    Args:
    (dataframe) df 
    '''
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while view_data == 'yes':
        print(df.iloc[start_loc :-1])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


           
if __name__ == "__main__":
	main()
