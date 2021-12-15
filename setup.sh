mkdir -p ~/.streamlit/

echo "\
[theme]\n\
primaryColor='#4bd0ff'\n\
backgroundColor='#1a1616'\n\
secondaryBackgroundColor='#7c7f83'\n\
textColor='#c2c4ce'\n\
[server]\n\
port = $PORT\n\
enableCORS = true\n\
\n\
"> ~/.streamlit/config.toml