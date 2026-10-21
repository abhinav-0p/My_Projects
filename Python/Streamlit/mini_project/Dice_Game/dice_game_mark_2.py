import random as rd
import streamlit as st

class Game:
    def __init__(self,name):
        self.name = name
        self.health = 120

    def roll(self):
        num = rd.randint(1,6)
        return num

st.title("⚔️Dice Battle⚔️")

if "game_started" not in st.session_state:
    st.session_state.game_started = False

if "players" not in st.session_state:
    st.session_state.players = []

if "num1" not in st.session_state:
    st.session_state.num1 = None

if "num2" not in st.session_state:
    st.session_state.num2 = None

if "message" not in st.session_state:
    st.session_state.message = ""


if not st.session_state.game_started:
    player1 = st.text_input("Enter First Player Name :").capitalize()
    player2 = st.text_input("Enter Second Player Name :").capitalize()
    if st.button("⏻ start Game"):
        if player1 and player2:
            st.session_state.game_started = True
            st.session_state.players = [Game(player1),Game(player2)]
            st.rerun()
        else:
            st.warning("Enter both player name")
else:

    health_container = st.container()
    dice_button = st.container()
    
    with dice_button:
            players = st.session_state.players

            game_over = players[0].health <=0 or players[1].health <=0

            if not game_over:
                    if st.button("🎲 Roll Dice"):
                        num1 = players[0].roll()
                        num2 = players[1].roll()

                        st.session_state.num1 = num1
                        st.session_state.num2 = num2

                        if num1>num2:
                            damage = (num1-num2)*10
                            players[1].health -= damage

                            st.session_state.message = (f"🔥{players[0].name} Won this round🔥\n ❤️‍🩹{players[1].name}'s Health is cut down by {int((damage/120)*100)}%❤️‍🩹")
                        elif num2>num1:
                            damage = (num2-num1)*10
                            players[0].health -= damage

                            st.session_state.message = (f"🔥{players[1].name} Won this round🔥\n ❤️‍🩹{players[0].name}'s Health is cut down by {int((damage/120)*100)}%❤️‍🩹")
                        else:
                            st.session_state.message = ("🤝 Its a draw")


    with health_container:
            col1, col2 = st.columns(2)

            with col1:
                st.subheader(f"{players[0].name}")
                health_percentage = max(0,((players[0].health)/120)*100)
                st.subheader("❤️")
                st.progress(int(health_percentage))

            with col2:
                st.subheader(f"{players[1].name}")
                health_percentage = max(0,((players[1].health)/120)*100)
                st.subheader("❤️")
                st.progress(int(health_percentage))

            st.divider()


    if st.session_state.num1 is not None and st.session_state.num2 is not None:
        st.subheader("🎲 Dice Result")
        col1, col2 = st.columns(2)

        with col1:
            st.write(f"{players[0].name}")
            st.metric("Dice",st.session_state.num1)

        with col2:
            st.write(f"{players[1].name}")
            st.metric("Dice",st.session_state.num2)

        st.text(st.session_state.message)
        
    if players[0].health <=0:
        st.success(f"🎉 Congratulations {players[1].name}, "
                    f"You Won The Battle!")
        st.balloons()
        if st.button("New Game"):
            st.session_state.clear()
            st.rerun()

    elif players[1].health <= 0:
        st.success(f"🎉 Congratulations {players[0].name}, "
                    f"You Won The Battle!")
        st.balloons()
        if st.button("New Game"):
            st.session_state.clear()
            st.rerun()