mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
port=$PORT
headless = true
enableCORS = false\n\
" > ~/.streamlit/config.toml