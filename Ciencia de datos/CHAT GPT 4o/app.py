import streamlit as st
from openai import OpenAI

#Configure OpenAI
client = OpenAI(
  api_key=st.secrets["OPENAI_API_KEY"]
)

st.title('💬 Chat con GPT-4o')

#Crear variable de sesion de historia de chat
if 'messages' not in st.session_state: #Guarda Variables de secciones
    st.session_state['messages'] = [] #Lista [] va con Append

#Mostrar la historia
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

#Chat input
if prompt:= st.chat_input('Escribe tu mensaje aqui...'):
    with st.chat_message('user'): #ROL USUARIO
        st.markdown(prompt)

    #Añadir el mensaje del usuario a la historia del chat
    st.session_state.messages.append({'role': 'user', 'content': prompt}) #Append va con la lista []

    #Obtener la respuesta de OpenAI
    with st.chat_message('assistant'): #ROL ASISTENTE
        message_placeholder = st.empty()
        try:
            stream = client.chat.completions.create(  # Corregí el typo "stram" a "stream"
                model='gpt-4o',
                messages=[
                    {'role': 'system',
                    'content': '''Eres un asistente útil que responde en español. 
                    Responde de manera concisa y clara.'''},
                    *[{'role': m['role'], 'content': m['content']} for m in st.session_state.messages],
                ],
                stream=True  # ✅ Este parámetro va FUERA de la lista messages
            )
            full_response = ''
            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    content = chunk.choices[0].delta.content
                    full_response += content
                    message_placeholder.markdown(full_response + '▌')
            
            message_placeholder.markdown(full_response)
            st.session_state.messages.append({'role': 'assistant', 'content': full_response})

        except Exception as e:
            st.error(f'Error: {str(e)}')