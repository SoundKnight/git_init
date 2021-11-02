# --- OBJETIVO ---
# Crear un programa que emule el clasico juego 
# de Piedra, Papel o Tijeras para 2 Jugadores o
# jugar contra un CPU

# --- MODULOS ---
Import-Module -Name .\funciones.psm1

# --- MENU ---
do{
    Write-Host "--- PIEDRA PAPEL O TIJEARS ---"
    Write-Host "// Seleccionar Opcion // 
    [1] Jugador vs Jugador
    [2] Jugador vs CPU
    [3] Ver Estadisticas
    [4] Salir
    "
    $opcion = read-host "Opcion"
        switch ($opcion){
            1{
                Clear-Host
                j_vs_j
                Read-Host "Presiona Enter Para Continuar"
                Clear-Host
                break
            }
            2{
                Clear-Host
                j_vs_cpu
                Read-Host "Presiona Enter Para Continuar"
                Clear-Host
                break
            }
            3{
                Clear-Host
                ver_estadisticas
                Read-Host "Presiona Enter Para Continuar"
                Clear-Host
                break
            }
            4{
                break
            }
            default{
                Clear-Host
                Write-Host "Valor Invalido
                "
            }  
        }
} while($opcion -ne 4){  
}

archivo_estadisticas