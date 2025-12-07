import streamlit as st
import requests

BASE_URL = "https://delivery-api-drhh.onrender.com"  # endereço da sua API

              
st.title("GANGUE DE VIP")

# ---------------------------
# Função de headers (sem login)
# ---------------------------
def auth_headers():
    return {}

# ---------------------------
# Formulário de cadastro
# ---------------------------
st.subheader("Cadastro VIP")
with st.form("form_cadastro"):
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    numero = st.text_input("Número de Telemóvel")
    btn_cadastro = st.form_submit_button("Cadastrar para obter número de usuário")

if btn_cadastro:
    if not nome or not email or not numero:
        st.warning("Preencha todos os campos!")
    else:
        payload = {
            "nome": nome,
            "email": email,
            "numero": numero
        }
        try:
            res = requests.post(f"{BASE_URL}/auth/cadastro", json=payload, timeout=50)
            if res.status_code in (200, 201):
                st.success("Usuário cadastrado com sucesso!")
                try:
                    st.json(res.json())
                except ValueError:
                    st.write(res.text)
            else:
                try:
                    st.error(res.json().get("detail", res.text))
                except ValueError:
                    st.error(res.text)
        except Exception as e:
            st.error(f"Erro ao conectar: {e}")

st.markdown("---")

# ---------------------------
# Botão para ver link
# ---------------------------
st.subheader("Acesso ao Grupo VIP")
usuario_id = st.text_input("Digite seu numero de usuário para ver o link")
if st.button("Obter o link do grupo"):
    if not usuario_id:
        st.warning("Informe o ID do usuário")
    else:
        try:
            res = requests.get(f"{BASE_URL}/usuario/meu_link/{usuario_id}", headers=auth_headers(), timeout=20)
            if res.status_code == 200:
                link = res.json().get("link do grupo")
                st.success("Acesso liberado!")
                st.markdown(f"[Clique aqui para acessar o grupo]({link})")
                st.markdown("OBS" ":" "2000 kz Subscrição mensal")
                st.markdown("Número para fazer pagamento por Express:   922715666" )
                st.markdown("Número para enviar o comprovativo:  926710597"  )
                
            else:
                try:
                    st.error(res.json().get("detail", res.text))
                except ValueError:
                    st.error(res.text)
        except Exception as e:
            st.error(f"Erro: {e}")
