import pandas as pd
import numpy as np

#Constantes con colores para dar un mejor diseño a la hora de mostrar la info en consola
RED = "\x1b[1;31m"
GREEN = "\x1b[2;32m"
YELLOW = "\x1b[1;33m"
PURPLE = "\x1b[1;35m"
WHITE = "\x1b[1;37m"
SIMPLE_WHITE = "\x1b[0;37m"
UNDERLINED_WHITE = "\x1b[4;37m"
STRAIGHT_LINES = f"{PURPLE}{"-":->124}{SIMPLE_WHITE}"

#Leemos el dataframe principal
premier_df = pd.read_csv("PL_files//PremierLeague.csv")

def Team_name(index: int) -> str:
    """Return the corresponding string based on the specified index

    Args:
        index (int): Index of the team whose name you want to return

    Raises:
        ValueError: ValueError (Numbers out of range)

    Returns:
        str: Name of the team
    """
    if index < 1 or index > 20:
        raise ValueError("The number isn't in range")
    
    else:
        teams: dict = {1: "AFC Bournemouth", 2: "Arsenal", 3: "Aston Villa", 4: "Brentford", 5: "Brighton & Hove Albion",
                       6: "Burnley", 7: "Chelsea", 8: "Crystal Palace", 9: "Everton", 10: "Fulham",
                       11: "Liverpool" , 12: "Luton Town", 13: "Manchester City" , 14: "Manchester United", 15: "Newcastle United",
                       16: "Nottingham Forest", 17: "Sheffield United", 18: "Tottenham Hotspur", 19: "West Ham United", 20: "Wolverhampton Wanderers"}   
        
        return teams[index]
    
def index_teams() -> pd.DataFrame:
    """Return a DataFrame with team names and their numbers

    Returns:
        pd.DataFrame: Names of the teams and their index
    """
    teams = pd.read_csv("PL_files//PremierLeague.csv", usecols=["home_team_name"]).sort_values("home_team_name").drop_duplicates()
    teams.index = range(1,21)
    return teams

def Order_string(index: int) -> str:
    if index < 1 or index > 9:
        raise ValueError("The number isn't in range")
    
    else:
        order_par: dict = {1: "PTS", 2: "TEAM", 3: "W", 4: "D", 5: "L",
                       6: "GF", 7: "GA", 8: "DF", 9: "PTS"}   
        
        return order_par[index]
      
def Games_by_matchday(matchday: int) -> tuple[int, pd.DataFrame]:
    """Return matches from the entered matchday

    Args:
        matchday (int): Matchday number you want to see

    Returns:
        tuple[int, pd.DataFrame]: An integer with the matchday number and a DataFrame with the matches
    """
    matchday_ouput = premier_df[premier_df["round_number"] == matchday].drop(columns=["home_team_name" , "away_team_name"])
    return matchday, matchday_ouput

def Games_by_team(team_user: str, local_away: int) -> pd.DataFrame:
    """Return a DataFrame with the home matches, away matches, or all matches of the entered team

    Args:
        team_user (str): Team whose matches you want to see
        local_away (int): 1.Local 2.Away 3.All

    Returns:
        pd.DataFrame: Dataframe with the information
    """
    if local_away == 1:
        local_games = premier_df[(premier_df["home_team_name"] == team_user)].drop(columns=["home_team_name", "away_team_name"])
        return local_games
        
    elif local_away == 2:
        away_games = premier_df[(premier_df["away_team_name"] == team_user)].drop(columns=["home_team_name", "away_team_name"])
        return away_games
        
    elif local_away == 3:
        all_games = premier_df[(premier_df["home_team_name"] == team_user) | (premier_df["away_team_name"] == team_user)].drop(columns=["home_team_name" , "away_team_name"])
        return all_games
    
def Games_by_result(result: int, team: str) -> tuple[pd.DataFrame, int]:
    """Return a DataFrame and an integer with the wins, defeats, or draw matches of the entered team

    Args:
        result (int): 1.Win 2.Defeat 3.Draw
        team (str): Team whose matches you want to see

    Returns:
        tuple[pd.DataFrame, int]: A Dataframe with the matches and a integer with the amount
    """
    
    if result == 1:
        local_wins = (premier_df["home_team_name"] == team) & (premier_df["home_team_goals"] > premier_df["away_team_goals"])
        away_wins = (premier_df["away_team_name"] == team) & (premier_df["away_team_goals"] > premier_df["home_team_goals"])
        result_win = premier_df[(local_wins) | (away_wins)].drop(columns=["home_team_name","away_team_name"])
        return result_win, result_win.shape[0]
    
    elif result == 2:
        local_defeats = (premier_df["home_team_name"] == team) & (premier_df["home_team_goals"] < premier_df["away_team_goals"])
        away_defeats = (premier_df["away_team_name"] == team) & (premier_df["home_team_goals"] > premier_df["away_team_goals"])
        result_defeat = premier_df[(local_defeats) | (away_defeats)].drop(columns=["home_team_name","away_team_name"])
        return result_defeat, result_defeat.shape[0]
    
    elif result == 3:
        matchs_team = (premier_df["home_team_name"] == team) | (premier_df["away_team_name"] == team)
        draw = (premier_df["home_team_goals"] == premier_df["away_team_goals"])
        result_draw = premier_df[(matchs_team) & (draw)].drop(columns=["home_team_name","away_team_name"])
        return result_draw, result_draw.shape[0]

def Games_by_goals(lineament: int, amount: int) -> tuple[pd.DataFrame, int]:
    """Return a DataFrame that meets the criteria and the desired number of goals, along with an integer representing the quantity of such matches

    Args:
        lineament (int): 1.Specific goals 2.More goals than 3.Less goals than
        amount (int): Amount of goals

    Returns:
        tuple[pd.DataFrame, int]: Dataframe with the matches and an integer with the amount
    """
    
    global premier_df
    try:
        premier_df = premier_df.drop(columns=["home_team_name","away_team_name"])
    except KeyError:
        premier_df
    
    if lineament == 1:
        specific_goals = premier_df[(premier_df["home_team_goals"] + premier_df["away_team_goals"]) == amount]
        return specific_goals, specific_goals.shape[0]
    
    elif lineament == 2:
        more_goals = premier_df[(premier_df["home_team_goals"] + premier_df["away_team_goals"]) > amount]
        return more_goals, more_goals.shape[0]

    elif lineament == 3:
        less_goals = premier_df[(premier_df["home_team_goals"] + premier_df["away_team_goals"]) < amount]
        return less_goals, less_goals.shape[0]

def Ask_for_date(lineament: str) ->  tuple[int]:
    """Ask for the year, month, and day (if required) and return a tuple with these values

    Args:
        lineament (str): 'd'->Ask for  year, month and day and returns them. 'm'->Ask for  year and month and returns them. 

    Returns:
        tuple[int]: Tuple with the date
    """
    if lineament =="d":
        while True:
            year = int(input(f"{UNDERLINED_WHITE}Type year (2023 | 2024){SIMPLE_WHITE} => "))
            if not (year ==2023 or year ==2024):
                print(f"\n{YELLOW}Number out of range, try again{SIMPLE_WHITE}")
                continue
            break
        
        while True:
            if year == 2023:
                month = int(input(f"{UNDERLINED_WHITE}Type month's number (August 2023 to December 2023){SIMPLE_WHITE} => "))
                if not (month >= 8 and month <=12):
                    print(f"\n{YELLOW}Number out of range, try again{SIMPLE_WHITE}")
                    continue
                break
            
            elif year == 2024:
                month = int(input(f"{UNDERLINED_WHITE}Type month's number (January 2024 to May 2024){SIMPLE_WHITE} => "))
                if not (month >= 1 and month <=5):
                    print(f"\n{YELLOW}Number out of range, try again{SIMPLE_WHITE}")
                    continue
                break
        
        while True:
            if month ==8 or month ==10 or month ==12 or month ==1 or month ==3 or month ==5:
                day = int(input(f"{UNDERLINED_WHITE}Type day's number (01 to 31){SIMPLE_WHITE} => "))
                if not (day >=1 and day <=31): 
                    print(f"\n{YELLOW}Number out of range, try again{SIMPLE_WHITE}")
                    continue
                break
            
            elif month ==9 or month ==11 or month ==4:
                day = int(input(f"{UNDERLINED_WHITE}Type day's number (01 to 30){SIMPLE_WHITE} => "))
                if not (day >=1 and day <=30): 
                    print(f"\n{YELLOW}Number out of range, try again{SIMPLE_WHITE}")
                    continue
                break
            
            elif month ==2:
                day = int(input(f"{UNDERLINED_WHITE}Type day's number (01 to 29){SIMPLE_WHITE} => "))
                if not (day >=1 and day <=29): 
                    print(f"\n{YELLOW}Number out of range, try again{SIMPLE_WHITE}")
                    continue
                break
        return year, month, day
    
    if lineament =="m":
        while True:
            year = int(input(f"{UNDERLINED_WHITE}Type year (2023 | 2024){SIMPLE_WHITE} => "))
            if not (year ==2023 or year ==2024):
                print(f"\n{YELLOW}Number out of range, try again{SIMPLE_WHITE}")
                continue
            break
        
        while True:
            if year == 2023:
                month = int(input(f"{UNDERLINED_WHITE}Type month's number (August 2023 to December 2023){SIMPLE_WHITE} => "))
                if not (month >= 8 and month <=12):
                    print(f"\n{YELLOW}Number out of range, try again{SIMPLE_WHITE}")
                    continue
                break
            
            elif year == 2024:
                month = int(input(f"{UNDERLINED_WHITE}Type month's number (January 2024 to May 2024){SIMPLE_WHITE} => "))
                if not (month >= 1 and month <=5):
                    print(f"\n{YELLOW}Number out of range, try again{SIMPLE_WHITE}")
                    continue
                break
           
        return year, month
    

def By_day(year: int, month: int, day: int) -> pd.DataFrame:
    """Receives the date for which you want to see the matches

    Args:
        year (int): year
        month (int): month
        day (int): day

    Returns:
        pd.DataFrame: DataFrame with the matches on that date
    """
    #Cargamos el df y eliminamos dos columnas
    premier_df = pd.read_csv("PL_files//PremierLeague.csv").drop(columns=['home_team_name', 'away_team_name'])
    #Convertimos al formato estandar las filas correspondientes a a la fecha
    premier_df['starting_at'] = pd.to_datetime(premier_df['starting_at'])
    #Convertimos fecha ingresada al formato estandar
    date = pd.to_datetime(f"{year}/{month}/{day}")
    #Comparamos la fecha ingresada
    day_matches = premier_df[(premier_df['starting_at'] == date)]
    return day_matches

def By_month(year: int, month: int) -> pd.DataFrame:
    """Receives the date (year and month) for which you want to see the matches

    Args:
        year (int): year
        month (int): month

    Returns:
        pd.DataFrame: DataFrame with the matches on that month
    """
    #Cargamos el df y eliminamos dos columnas
    premier_df = pd.read_csv("PL_files//PremierLeague.csv").drop(columns=['home_team_name', 'away_team_name'])
    #Convertimos al formato estandar las filas correspondientes a a la fecha
    premier_df['starting_at'] = pd.to_datetime(premier_df['starting_at'])
    #Dependiendo el mes almacenamos en day la cantidad de dias correspondiente
    if month ==8 or month ==10 or month ==12 or month ==1 or month ==3 or month ==5:
        day = 31
    elif month ==9 or month ==11 or month ==4:
        day = 30
    elif month ==2:
        day = 29
    #Convertimos fecha ingresada al formato estandar
    date = pd.to_datetime(f"{year}/{month}/{day}")
    #Comparamos la fecha ingresada
    start = pd.Timestamp(f"{year}/{month}/01")
    end = pd.Timestamp(f"{year}/{month}/{day}")

    month_matches = premier_df[(premier_df['starting_at'] >= start) & (premier_df['starting_at'] <= end)]
    return month_matches


def Generate_table() -> pd.DataFrame:   
    """Generates a complete table with matches (W, D, L), points, goals (For, Against) and positions

    Returns:
        pd.DataFrame: DataFrame with all teams' information 
    """
    premier_df = pd.read_csv("PL_files//PremierLeague.csv")
    def Amount_matches() -> np.array:
        #Creamos dos listas en las que almacenaremos los datos de cada equipo
        wins_teams = []
        draw_teams = []
        for team in final_table['TEAM']:
            wins = 0
            draws = 0

            #Obtenemos el numero de victorias a partir del shape[0] 
            wins = premier_df[(premier_df['home_team_name'] == team) & (premier_df['home_team_goals'] > premier_df['away_team_goals']) | (premier_df['away_team_name'] == team) & (premier_df['away_team_goals'] > premier_df['home_team_goals'])].shape[0]

            #Obtenemos el numero de empates a partir del shape[0] 
            draws = premier_df[(premier_df['home_team_name'] == team) & (premier_df["home_team_goals"] == premier_df['away_team_goals']) | (premier_df['away_team_name'] == team) & (premier_df["home_team_goals"] == premier_df['away_team_goals'])].shape[0]
        
            #Creamos una lista dentro de la lista en la que cada equipo tendra su correspondiente valor
            wins_teams.append([wins])
            draw_teams.append([draws])
        
        #Convertimos las listas a arrays
        num_wins = np.array(wins_teams)
        num_draw = np.array(draw_teams)
        #Las concatenamos de manera paralela
        wins_and_draws = np.concatenate((num_wins,num_draw), axis=1)
        #Hacemos la suma de victorias y derrotas de cada fila (equipo)
        wins_and_draws = wins_and_draws.sum(axis=1)
        #Creamos un nuevo array restando la totalidad de partidos con la cantidad de victorias y derrotas
        num_defeats = np.reshape([38 - wins_and_draws], newshape=(20,1))
        #Concatenamos las 3 columnas en un array de (20,3)
        matches = np.concatenate((num_wins,num_draw, num_defeats), axis=1)
        
        return matches

    def Points() -> np.array:
        #Creamos una lista para almacenar los puntos de cada equipo
        points = []
        #Recorremos cada fila de la columna 0 y 1
        for wins, draws in zip(matches[:, 0], matches[:, 1]):
            points.append([(wins*3)+draws])
        #Convertimos la lista a un array de (20,1)
        points = np.array(points)
        
        return points
    
    def Goals_by_team() -> np.array:
        #Creamos una lista para almacenar los goles a favor de cada equipo
        total_goals_list = []
        for team in final_table['TEAM']:
            
            #Obtenemos el numero de goles a partir del sum 
            local_goals = premier_df.loc[premier_df['home_team_name'] == team, 'home_team_goals'].sum()    
            away_goals = premier_df.loc[premier_df['away_team_name'] == team, 'away_team_goals'].sum()
            
            goals = local_goals + away_goals
            total_goals_list.append([goals])
        
        #Convertimos la lista a un array de (20,1)   
        total_goals = np.array(total_goals_list)
        
        return total_goals

    def Against_goals_by_team() -> np.array:
        #Creamos una lista para almacenar los goles en contra de cada equipo
        total_goals_list = []
        for team in final_table['TEAM']:
            
            #Obtenemos el numero de goles a partir del sum 
            local_against_goals = premier_df.loc[premier_df['home_team_name'] == team, 'away_team_goals'].sum()
            away_against_goals = premier_df.loc[premier_df['away_team_name'] == team, 'home_team_goals'].sum()
            
            goals = local_against_goals + away_against_goals
            total_goals_list.append([goals])
        
        #Convertimos la lista a un array de (20,1)    
        total_against_goals_ = np.array(total_goals_list)
        return total_against_goals_
    
    final_table = pd.DataFrame()   #Creamos un df vacio para ir almacenando los datos que tendra la tabla final
    #Creamos la columna 'Team' obteniendo el nombre de cada equipo y ordenado alfabeticamente
    final_table['TEAM'] = premier_df['home_team_name'].drop_duplicates().sort_values()
    
    #Amount_matches retornara 3 columnas con las victorias, empates y derrotas de cada equipo, para despues ser asignadas a nuevas columnas en la tabla final
    matches = np.reshape(Amount_matches(), newshape=(20,3))
    final_table['W'], final_table['D'], final_table['L'] = matches[:, 0], matches[:, 1], matches[: ,2]
    final_table['GP'] = final_table['W'] + final_table['D'] + final_table['L']

    #Creamos una nueva columna en la tabla y le asignamos un array con los puntos de cada equipo
    final_table['PTS'] = np.reshape(Points(), newshape=(20))
    
    #Obtenemos los goles a favor y en contra de cada equipo para asginarlos a las columnas correspondientes en la tabal final
    goals_favor = Goals_by_team()
    goals_against = Against_goals_by_team()
    final_table['GF'], final_table['GA'], final_table['DF'] = goals_favor, goals_against, goals_favor-goals_against
    
    #Reemplazamos los nombre de Everton y Forest para agregar '*' con el fin de enfatizar que tuvieron una reduccion de puntos (en las siguientes lineas es realizada)
    final_table.loc[final_table['TEAM'] == 'Nottingham Forest', 'TEAM'] = 'Nottingham Forest*'
    final_table.loc[final_table['TEAM'] == 'Everton', 'TEAM'] = 'Everton*'
    final_table.loc[(final_table['PTS'] == 36) & (final_table['TEAM'] == 'Nottingham Forest*'), 'PTS'] -= 4
    final_table.loc[(final_table['PTS'] == 48) & (final_table['TEAM'] == 'Everton*'), 'PTS'] -= 8

    final_table.sort_values(by=['PTS'], ascending=False, inplace=True)
    final_table['POS.'] = np.reshape(np.array([i for i in range(1,21)]), newshape=(20,1))
    final_table = final_table[['POS.','TEAM','GP', 'W', 'D', 'L', 'GF','GA','DF', 'PTS']]
    
    return final_table

def Order_table(by: str = 'PTS', ascending: bool = False) -> pd.DataFrame:
    """Order the table by desired parameter

    Args:
        by (str, optional): Order by = 'TEAM', 'W', 'D', 'L', 'GF', 'GA', 'DF', 'PTS' (Default).
        ascending (bool, optional): True | False (Default).

    Returns:
        pd.DataFrame: DataFrame with the table ordered by the specified parameters
    """
    order_table = Generate_table()
    #Creamos la columna con las posiciones 
    order_table['POS.'] = np.reshape(np.array([i for i in range(1,21)]), newshape=(20,1))
    #Ordenamos la tabla por puntos (sera el valor por default)
    order_table.sort_values(by=[by.upper()], ascending=ascending, inplace=True)
    
    order_table = order_table[['POS.', 'TEAM','GP', 'W', 'D', 'L', 'GF','GA','DF', 'PTS']]
    
    return order_table