import streamlit as st


#----------------------------------------------------sidebar
st.sidebar.title('prime drive - aluguel de carros')

carro = ['saveiro', 'vectra', 'skyline R34', 'alfa romeu', 'nissan s15']

modelo = st.sidebar.selectbox('selecione o carro alugado' ,carro)




#----------------------------------------------------principal
st.title('prime drive - aluguel de carros')
st.markdown(f' ## voce escolheu o modelo: {modelo}')
st.image(f'{modelo}.png')

if modelo == 'saveiro':
    diaria = 250

elif modelo == 'vectra':
    diaria = 400

elif modelo == 'skyline R34':
    diaria = 2000

elif modelo == 'alfa romeu': 
    diaria = 300

elif modelo == 'nissan s15':
    diaria = 1000

dias = st.text_input(f'por quantos dias voce alugou o {modelo}?')
km = st.text_input(f'quantos km voce rodou?')

if st.button('calcular'):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel = total_dias + total_km

    st.warning(f'voce alugou o {modelo} por {dias} dias e rodou {km} km. Ovalor do aluguel será R${aluguel}')