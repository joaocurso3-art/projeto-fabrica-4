import streamlit as st
from streamlit_extras.let_it_rain import rain

st.title("=== 🐂 Ordenador de Bois da Fazenda ===")

st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJHHoYeBJWhdC5z5w7EBf6iyOKu-pq32kC7Q&s")

bois = []
for i in range(1, 4):
    nome_boi = st.text_input(f"Nome do boi {i}", key=f"nome{i}")
    kgs = st.number_input(f"Peso do {nome_boi or f'boi {i}'} (kg)", key=f"peso{i}", min_value=0.0, format="%.2f")
    if nome_boi:
        bois.append((nome_boi, kgs))

if st.button("🔍 Ordenar Bois"):
    if bois:
        bois_ordenados = sorted(bois, key=lambda x: x[1], reverse=True)
        st.success("### 🏁 Resultado da ordenação")
        for pos, (nome, peso) in enumerate(bois_ordenados, start=1):
            st.write(f"**{pos}º lugar:** {nome} — {peso:.2f} kg")
        rain("🐂", font_size=72, animation_length=1)
    else:
        st.warning("Por favor, insira os nomes e pesos dos bois antes de ordenar!")
