from pydoc import describe

import streamlit as st
#Configuração da página
st.set_page_config(
    page_title="Mundo Geek Verse",
    page_icon="🤖",
    layout="wide",
)

#Estilo visual
st.markdown("""
<style>
    .stApp {
        background-color:  #0b0b14
        color: #ffffff;
    }
    [data-testid="stSidebar"] {
        backoud-color: #151525;
        }
        h1, h2, h3 {
        color: #a78bfa;
        }
        .card {
        .stButton button  {
        paddig: 22px
       border-radius: 15px
       border: 1px solid #40356b;
       margin-bottom: 15px;
       }
       card h3{
       color:#c4b5fd:
       }

       .stbutton button{
       background-color: #7c3aed;
       color: purple;
       border-radius: 10px;
       borde: none;
       }
       </style>
       """, unsafe_allow_html=True)

#Menu lateral
st.sidebar.title("Mundo Geek Verse")
st.sidebar.write("Seu uiverso geek em um só lugar!")

pagina = st.sidebar.radio(
    "Navegação",
    ["Inicio", "Games",  "Animes", "Filmes", "Séries", "HQs"]
)
#Cabeçalho
st.title("Bem-vindo ao Mundo Geek Verse!")
st.write("Seu portal de cultura geek,  games e entretenimento!")
st.divider()

#Barra de pesquisa
pesquisa = st.text_input(
    "Pesquise no Mundo Geek...",
    placeholder="Digite um jogo, anime, filme, série ou HQ que deseja pesquisar"
)

if pesquisa:
    st.info(f"Você pesquisou por: {pesquisa}")

#Página inicial
if pagina == "Inicio":
    st.subheader("Painel Principal")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
       <div class="card">
         <h3> Animes</h3>
            <p>Explore o mundo dos animes, descubra novos títulos e acompanhe seus favoritos.</p>
         </div>
         """,  unsafe_allow_html=True)
    with col2:
        st.markdown("""
       <div class="card">
         <h3>Games</h3>
            <p>Descubra jogos e aveturas emocionantes, dicas e análises de jogos populares.</p>
         </div>
         """,  unsafe_allow_html=True)
    with col3:
        st.markdown("""
       <div class="card">
         <h3>Filmes e Séries</h3>
            <p>Encontre seu proximo filme ou série favorito.</p>
         </div>
         """,  unsafe_allow_html=True)
    st.subheader("Destaques do Mundo Geek")

    destaques = st.columns(3)

    itens = [
        ("Universo Marvel", "Heróis e vilões"),
        ("Mundo da fantasia", "Magia e aventuras"),
        ("Games clássicos", "Nostalgia gamer"),
    ]
    for coluna, item in zip(destaques, itens):
        with coluna:
            st.markdown(f"""
<div class="card">
    <h2>{item[0]}</h2>
    <p>{item[1]}</p>
</div>
""", unsafe_allow_html=True)
elif pagina == "Animes":
    st.header("Mundo dos animes")
    anime = st.selectbox(
        "Escolha uma categoria",
        ["Aventura", "Ação", "Fantasia", "Comedia"]
    )
    st.write(f"Categoria selecionada: **{anime}**")
    st.info("Adicione seus animes favoritos aqui")
elif pagina == "Games":
    st.header("Central dos games")
    st.write("Explore o mundo dos games")

    jogos = [
        ("Minecraft", "Construa seu próprio universo"),
        ("Cuphead", "Desafios com visual de desenho clássico"),
        ("God of War", "Uma aventura épica de mitologia"),
    ]
    for jogo, descricao in jogos:
        with st.expander(jogo):
            st.write(descricao)

    #Pagina de filmes e series
elif pagina in ("Filmes", "Séries"):
    st.header("Central de  Filmes e series")
    genero = st.selectbox(
        "Escolha um gênero",
        ["Ficção científica", "Aventura", "Fantasia", "Heróis"]
    )
    st.write(f"Gênero escolhido: **{genero}**")
    st.info("Aqui voce podera montar seu catalogo de filmes e series")

#Página de quadrinhos
elif pagina == "HQs":
    st.header("Mundo dos quadrinhos")

    st.markdown("""
<div class= "card">
<h3> Heróis</h3>
<p> Marvel, DC e outros uiversos dos quadrinhos.</p>
</div>
""", unsafe_allow_html=True)

    favorito = st.text_input("Qual é sua hq favorita?")

    

    