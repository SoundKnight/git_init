# !/bin/bash

# ---<=> Funciones <=>---
function SumNum() {
    echo "<=><=><=> CALCULADORA SIMPLE <=><=><=>"
    echo ""
    echo "-------- SUMA --------"
    echo "Introduzca el Primer Numero"
    echo -n "Numero 1: "
    read Num1
    echo ""
    echo "Introduzca el Segundo Numero"
    echo -n "Numero 2: "
    read Num2 
    echo ""
    echo "Resultado de la Suma"
    echo $Num1 + $Num2 = $(($Num1 + $Num2))
    echo ""
}

function ResNum() {
    echo "<=><=><=> CALCULADORA SIMPLE <=><=><=>"
    echo ""
    echo "-------- RESTA --------"
    echo "Introduzca el Primer Numero"
    echo -n "Numero 1: "
    read Num1
    echo ""
    echo "Introduzca el Segundo Numero"
    echo -n "Numero 2: "
    read Num2 
    echo ""
    echo "Resultado de la Suma"
    echo $Num1 - $Num2 = $(($Num1 - $Num2))
    echo ""
}

until [ $Eleccion == "3" ] 
do
    echo "<=><=><=> CALCULADORA SIMPLE <=><=><=>"
    echo "-------- MENU --------"
    echo "1. SUMA"
    echo "2. RESTA"
    echo "3. SALIR"
    echo ""
    echo "Selecciona una Opcion"
    echo -n "Eleccion: "
    read Eleccion 
    echo ""

    if [ $Eleccion = "1" ]; then
        SumNum
    elif [ $Eleccion = "2" ]; then
        ResNum
    elif [ $Eleccion = "3" ]; then
        exit
    else
        echo "Valor Invalido"
        echo ""
    fi
done