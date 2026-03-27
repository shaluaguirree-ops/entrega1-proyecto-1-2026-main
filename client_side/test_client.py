# test_client.py

from client_transport import GameClient


# Function handling responses from server
def handle_response(response):
    
    print("Response from server:")
    print(response)


def main():

    client = GameClient("ws://127.0.0.1:8765", handle_response)
    client.connect()

    player=input("Enter player name: ")
    client.send_action("join", player_name=player)

    while True:
        command = input("Enter command (get_players/current_player/roll_dice/move_piece/get_board/get_state/exit): ")
        if command == "exit":
            break
   

        if command == "get_players":
            client.send_action("get_players")   
        elif command == "current_player":
            client.send_action("current_player")
        elif command == "roll_dice":
            client.send_action("roll_dice")
        elif command == "get_board":
            client.send_action("get_board")     
        elif command == "get_state":
            client.send_action("get_state")
        elif command == "get_my_id":
            client.send_action("get_my_id")
        else:
            print("Unknown command")
    
    client.close()


if __name__ == "__main__":
    main()