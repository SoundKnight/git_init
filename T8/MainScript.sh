#Los correos que desea usar, se deberan poner en correos.txt linea por linea
clear
echo '<=><=><=> ENVIO DE CORREOS <=><=><=>'
echo '--- Informacion del Emisor ---'
echo 'Introduce el Correo Electronico [Dominio: uanl.edu.mx | outlook.com]'
read -p 'Email: ' transmitter
echo ''
echo 'Introduce la Contraseña del Correo Electronico'
read -p 'Contraseña: ' password
echo ''
echo '--- Informacion del Mensaje ---'
echo 'Introduce el Asunto'
read -p 'Asunto: ' subject
echo ''
echo 'Introduce el Mensaje'
read -p 'Mensaje: ' message

while IFS= read -r line
do
    echo ''
    echo $line
    python Envio_Correos.py --transmitter "$transmitter" --password "$password" --receiver "$line" --subject "$subject" --message "$message"
done < correos.txt