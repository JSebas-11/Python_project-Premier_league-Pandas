#Importamos las funciones a utilizar y algunas constantes para dar algo de color a la terminal
from PL_files.A_pl_menus import Games_matchday_menu, Games_team_menu, Games_result_menu, Games_goals_menu, Final_postions_menu, Games_dates_menu
from PL_files.B_pl_functions import UNDERLINED_WHITE, SIMPLE_WHITE, YELLOW, RED

#Funcion con el ciclo del menu principal
def main() -> None:
    while True:
        action: int = int(input(f"""\n\t{UNDERLINED_WHITE}Main Menu\nWhat do you want do:{SIMPLE_WHITE}
        {UNDERLINED_WHITE}1.See games by matchday{SIMPLE_WHITE}
        {UNDERLINED_WHITE}2.See games by team{SIMPLE_WHITE}
        {UNDERLINED_WHITE}3.See games by result{SIMPLE_WHITE}
        {UNDERLINED_WHITE}4.See games by goals{SIMPLE_WHITE}
        {UNDERLINED_WHITE}5.See games by dates{SIMPLE_WHITE}
        {UNDERLINED_WHITE}6.See final positions{SIMPLE_WHITE}
        {UNDERLINED_WHITE}0.Exit{SIMPLE_WHITE}
        """))

        if action == 1:
            Games_matchday_menu()
            continue
            
        elif action == 2:
            Games_team_menu()
            
        elif action == 3:
            Games_result_menu()  
            
        elif action == 4:
            Games_goals_menu()  
            
        elif action == 5:
            Games_dates_menu()
            
        elif action == 6:
            Final_postions_menu()
            
        elif action == 0:
            print(f"{RED}Closing program...{SIMPLE_WHITE}")
            break
        
        else:
            print(f"\n{YELLOW}Number invalid, try again{SIMPLE_WHITE}")
            continue

if __name__ == "__main__":
    main()