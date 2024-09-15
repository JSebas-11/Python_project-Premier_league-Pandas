#Importamos las funciones y constantes a utilizar 
from PL_files.B_pl_functions import UNDERLINED_WHITE, SIMPLE_WHITE, YELLOW, GREEN, STRAIGHT_LINES, Team_name, index_teams, Games_by_matchday, Games_by_team, Games_by_result, Games_by_goals, Order_table, Order_string, Ask_for_date, By_day, By_month

#Funcion con el menu '1.See games by matchday'
def Games_matchday_menu() -> None:
    while True:
        matchday: int = int(input(f"{UNDERLINED_WHITE}Type the matchday that you want to see{SIMPLE_WHITE} => "))
        
        #La variable no puede ser mayor a 38 ya que esos son los partidos que se juegan
        if matchday < 1 or matchday > 38:
            print(f"{YELLOW}Matchday isn't valid{SIMPLE_WHITE}")
            continue
        
        #Retornamos el numero de la jornada y el df con los datos correspondientes
        matchday, games = Games_by_matchday(matchday)
        print(f"\n{STRAIGHT_LINES}{GREEN}\nMatchday {matchday}:\n{games}\n{STRAIGHT_LINES}")
        break
    
#Funcion con el menu '2.See games by team'
def Games_team_menu() -> None:
    while True:
        #Llamamos la funcion index_teams encargada de imprimir los equipos con un respectivo numero
        team_user = int(input(f"\n{STRAIGHT_LINES}\n{GREEN}{index_teams()}\n{STRAIGHT_LINES}\n{UNDERLINED_WHITE}Type the team's number =>{SIMPLE_WHITE} "))
        
        if team_user < 1 or team_user > 20:
            print(f"{YELLOW}The number isn't in range, try again{SIMPLE_WHITE}")
            continue
        
        team_user = Team_name(team_user)
        
        #Despues de verificar como correcto el numero del equipo entramos en un submenu
        while True:
            local_away = int(input(f"""\n\t{UNDERLINED_WHITE}1.Home matches{SIMPLE_WHITE}
        {UNDERLINED_WHITE}2.Away matches{SIMPLE_WHITE}
        {UNDERLINED_WHITE}3.All matches{SIMPLE_WHITE}
        {UNDERLINED_WHITE}0.Back to menu{SIMPLE_WHITE}
        """))
            
            if local_away >= 1 and local_away < 4:
                output = Games_by_team(team_user, local_away)
                print(f"\n{STRAIGHT_LINES}\n{GREEN}{team_user}:\n{output}\n{STRAIGHT_LINES}")
                
            elif local_away == 0:
                break
            
            else:
                print(f"\n{YELLOW}Number isn't valid, try again{SIMPLE_WHITE}")
                continue
        break

#Funcion con el menu '3.See games by result'
def Games_result_menu() -> None:
    while True:
        #Llamamos la funcion index_teams encargada de imprimir los equipos con un respectivo numero
        team_number =  int(input(f"\n{STRAIGHT_LINES}\n{GREEN}{index_teams()}\n{STRAIGHT_LINES}\n{UNDERLINED_WHITE}Type the team's number =>{SIMPLE_WHITE} "))
        
        if team_number < 1 or team_number > 20:
            print(f"{YELLOW}The number isn't in range, try again{SIMPLE_WHITE}")
            continue
        
        team = Team_name(team_number)
        
        #Despues de verificar como correcto el numero del equipo entramos en un submenu
        while True:
            results = int(input(f"""\n\t{UNDERLINED_WHITE}1.Winners{SIMPLE_WHITE}
        {UNDERLINED_WHITE}2.Losers{SIMPLE_WHITE}
        {UNDERLINED_WHITE}3.Draws{SIMPLE_WHITE}
        {UNDERLINED_WHITE}0.Back to menu{SIMPLE_WHITE}
        """))    
        
        #Devolvemos el df con los resultados y el amout contiene la cantidad de los mismos 
            if results == 1:
                wins, amout = Games_by_result(1, team) 
                print(f"\n{STRAIGHT_LINES}\n{GREEN}{team} wins ({amout}):\n{wins}\n{STRAIGHT_LINES}")     
            elif results == 2:
                defeats, amout = Games_by_result(2, team) 
                print(f"\n{STRAIGHT_LINES}\n{GREEN}{team} defeats ({amout}):\n{defeats}\n{STRAIGHT_LINES}")  
            elif results == 3:
                draws, amout = Games_by_result(3, team) 
                print(f"\n{STRAIGHT_LINES}\n{GREEN}{team} draws ({amout}):\n{draws}\n{STRAIGHT_LINES}")
            elif results == 0:
                break
            else:
                print(f"\n{YELLOW}Number invalid, try again{SIMPLE_WHITE}")
                continue
        break

#Funcion con el menu '4.See games by goals'
def Games_goals_menu() -> None:
    
    while True:
        lineament = int(input(f"""{STRAIGHT_LINES}\n\t{UNDERLINED_WHITE}1.Specific amount of goals{SIMPLE_WHITE}
        {UNDERLINED_WHITE}2.More goals than{SIMPLE_WHITE}
        {UNDERLINED_WHITE}3.Fewer goals than{SIMPLE_WHITE}
        {UNDERLINED_WHITE}0.Back to menu{SIMPLE_WHITE}
        """))    
        
        #Verificamos que sea el rango correcto y entramos en el submenu para pedir la cantidad de goles
        if lineament >= 1 and lineament <= 3:
            
            while True:
                amount = int(input(f"\n{UNDERLINED_WHITE}Type the amount of goals to be compared =>{SIMPLE_WHITE} ")) 
                
                if amount >= 0:
                    
                    if lineament == 1:
                        df_output, amout = Games_by_goals(lineament, amount) 
                        print(f"\n{STRAIGHT_LINES}\n{GREEN}There were {amout} matches with {amount} goals:\n{df_output}")     
                        break
                    elif lineament == 2:
                        df_output, amout = Games_by_goals(lineament, amount) 
                        print(f"\n{STRAIGHT_LINES}\n{GREEN}There were {amout} matches with more than {amount} goals:\n{df_output}")
                        break     
                    elif lineament == 3:
                        df_output, amout = Games_by_goals(lineament, amount) 
                        print(f"\n{STRAIGHT_LINES}\n{GREEN}There were {amout} matches with fewer than {amount} goals:\n{df_output}")     
                        break
                else:
                    print(f"\n{YELLOW}Number out of range, try again{SIMPLE_WHITE}")
                    continue
                        
        elif lineament == 0:
            break
        else:
            print(f"\n{YELLOW}Number invalid, try again{SIMPLE_WHITE}")
            continue
        
#Funcion con el menu '5.See games dates'
def Games_dates_menu() -> None:
   while True: 
        lineament = int(input(f"""\n\t{UNDERLINED_WHITE}1.Specific day{SIMPLE_WHITE}
        {UNDERLINED_WHITE}2.Specific Month{SIMPLE_WHITE}
        {UNDERLINED_WHITE}0.Back to menu{SIMPLE_WHITE}
        """))
        
        if lineament == 1:
            year, month, day = Ask_for_date(lineament="d")
            day_matches = By_day(year, month, day)
            
            if day_matches.empty:
                print(f"{STRAIGHT_LINES}\n{GREEN}There were no matches that day\n{STRAIGHT_LINES}{SIMPLE_WHITE}")
            else:
                print(f"{STRAIGHT_LINES}\n{GREEN}Date: {f'{year}/{month}/{day}'}\n{day_matches}\n{STRAIGHT_LINES}{SIMPLE_WHITE}")
                
        elif lineament == 2:
            year, month = Ask_for_date(lineament="m")
            month_matches = By_month(year, month)
            
            if month_matches.empty:
                print(f"{STRAIGHT_LINES}\n{GREEN}There were no matches that month\n{STRAIGHT_LINES}{SIMPLE_WHITE}")
            else:
                print(f"{STRAIGHT_LINES}\n{GREEN}Month: {month}\n{month_matches}\n{STRAIGHT_LINES}{SIMPLE_WHITE}")
                
        elif lineament == 0:
            break
        
        else:  
            print(f"\n{YELLOW}Number invalid, try again{SIMPLE_WHITE}")
            continue 

#Funcion con el menu '6.See final positions'
def Final_postions_menu() -> None:
    print(f"{STRAIGHT_LINES}\n{GREEN}Ordered by Position\n{Order_table(ascending=False)}\n{STRAIGHT_LINES}")
    while True:
        order = int(input(f"""\t{UNDERLINED_WHITE}1.Order by{SIMPLE_WHITE}
        {UNDERLINED_WHITE}0.Back to menu{SIMPLE_WHITE}
        """))
        if order == 1:
            while True:
                order_by = int(input(f"""{STRAIGHT_LINES}\n{UNDERLINED_WHITE}Order by:{SIMPLE_WHITE}
            {UNDERLINED_WHITE}1.Position (Ascending){SIMPLE_WHITE}
            {UNDERLINED_WHITE}2.Alphabetically{SIMPLE_WHITE}
            {UNDERLINED_WHITE}3.Games won{SIMPLE_WHITE}
            {UNDERLINED_WHITE}4.Games drawn{SIMPLE_WHITE}
            {UNDERLINED_WHITE}5.Games lost{SIMPLE_WHITE}
            {UNDERLINED_WHITE}6.Goals for{SIMPLE_WHITE}
            {UNDERLINED_WHITE}7.Goals against{SIMPLE_WHITE}
            {UNDERLINED_WHITE}8.Goal difference{SIMPLE_WHITE}
            {UNDERLINED_WHITE}9.Points (Ascending){SIMPLE_WHITE}
            {UNDERLINED_WHITE}0.Back{SIMPLE_WHITE}
            """))
                if order_by >=1 and order_by <=9:
                    if order_by == 1 or order_by == 2 or order_by == 9: 
                        table = Order_table(by=Order_string(order_by), ascending=True)
                        print(f"{STRAIGHT_LINES}\n{GREEN}Ordered by {Order_string(order_by)}:\n{table}{SIMPLE_WHITE}\n{STRAIGHT_LINES}")
                        break
                    elif order_by == 3 or order_by == 4 or order_by == 5 or order_by == 6 or order_by == 7 or order_by == 8:  
                        table = Order_table(by=Order_string(order_by), ascending=False)
                        print(f"{STRAIGHT_LINES}\n{GREEN}Ordered by {Order_string(order_by)}:\n{table}{SIMPLE_WHITE}\n{STRAIGHT_LINES}")
                        break
                elif order_by == 0:
                    break
                else:
                    print(f"\n{YELLOW}Number invalid, try again{SIMPLE_WHITE}")
                    continue 
        elif order == 0:
            break
        else:  
            print(f"\n{YELLOW}Number invalid, try again{SIMPLE_WHITE}")
            continue 