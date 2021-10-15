# --- VARIABLES ---
$global:fecha_hoy = Get-Date
$global:nj = 0 #Partidas Jugadas
$global:gj1 = 0 #Ganadas J1
$global:gj2 = 0 #Ganadas J2
$global:ejj = 0 #Empatadas JvsJ
$global:gjc = 0 #Ganadas JvsCPU
$global:pjc = 0 #Perdidas JvsCPU
$global:ejc = 0 #Empatadas JvsCPU

# --- FUNCIONES ---
function j_vs_j{
    do{
        Write-Host "--- JUGADOR VS JUGADOR ---"
        Write-Host "// Seleccion Jugador 1 //
    [1] Piedra
    [2] Papel
    [3] Tijeras
    "
        $jugador1 = Read-Host "Opcion"
        switch($jugador1){
            1{
                break
            }
            2{
                break
            }
            3{
                break
            }
            default{
                Clear-Host
                Write-Host "Valor Invalido
                "
            }
        }
    } while($jugador1 -ne 1 -and $jugador1 -ne 2 -and $jugador1 -ne 3){
    }
    Clear-Host
    
    do{
        Write-Host "--- JUGADOR VS JUGADOR ---"
        Write-Host "// Seleccion Jugador 2 //
    [1] Piedra
    [2] Papel
    [3] Tijeras
    "
        $jugador2 = Read-Host "Opcion"
        switch($jugador2){
            1{
                break
            }
            2{
                break
            }
            3{
                break
            }
            default{
                Clear-Host
                Write-Host "Valor Invalido
                "
            }
        }
    } while($jugador2 -ne 1 -and $jugador2 -ne 2 -and $jugador2 -ne 3){
    }
    juego_j
    Write-Host ""
}

function j_vs_cpu{
    do{
        Write-Host "--- JUGADOR VS CPU ---"
        Write-Host "// Seleccionar Opcion //
    [1] Piedra
    [2] Papel
    [3] Tijeras
    "
        $jugador1 = Read-Host "Opcion"
        switch($jugador1){
            1{
                break
            }
            2{
                break
            }
            3{
                break
            }
            default{
                Clear-Host
                Write-Host "Valor Invalido
                "
            }
        }
    } while($jugador1 -ne 1 -and $jugador1 -ne 2 -and $jugador1 -ne 3){
    }
    $jugador2 = Get-Random -Minimum 1 -Maximum 4
    Write-Host "Opcion del CPU: $jugador2"
    juego_cpu
    Write-Host ""
}

function juego_j{
    if($jugador1 -eq 1 -and $jugador2 -eq 2){
        $global:nj += 1
        $global:gj2 += 1
        Write-Host "El Jugador 2 Gana"
    }
    elseif($jugador1 -eq 1 -and $jugador2 -eq 3){
        $global:nj += 1
        $global:gj1 += 1
        Write-Host "El Jugador 1 Gana"
    }
    elseif($jugador1 -eq 2 -and $jugador2 -eq 1){
        $global:nj += 1
        $global:gj1 += 1
        Write-Host "El Jugador 1 Gana"
    }
    elseif($jugador1 -eq 2 -and $jugador2 -eq 3){
        $global:nj += 1
        $global:gj2 += 1
        Write-Host "El Jugador 2 Gana"
    }
    elseif($jugador1 -eq 3 -and $jugador2 -eq 1){
        $global:nj += 1
        $global:gj2 += 1
        Write-Host "El Jugador 2 Gana"
    }
    elseif($jugador1 -eq 3 -and $jugador2 -eq 2){
        $global:nj += 1
        $global:gj1 += 1
        Write-Host "El Jugador 1 Gana"
    }
    elseif($jugador1 -eq $jugador2){
        $global:nj += 1
        $global:ejj += 1
        Write-Host "Empate"
    }
}

function juego_cpu{
    if($jugador1 -eq 1 -and $jugador2 -eq 2){
        $global:nj += 1
        $global:pjc += 1
        Write-Host "El CPU Gana"
    }
    elseif($jugador1 -eq 1 -and $jugador2 -eq 3){
        $global:nj += 1
        $global:gjc += 1
        Write-Host "El Usuario Gana"
    }
    elseif($jugador1 -eq 2 -and $jugador2 -eq 1){
        $global:nj += 1
        $global:gjc += 1
        Write-Host "El Usuario Gana"
    }
    elseif($jugador1 -eq 2 -and $jugador2 -eq 3){
        $global:nj += 1
        $global:pjc += 1
        Write-Host "El CPU Gana"
    }
    elseif($jugador1 -eq 3 -and $jugador2 -eq 1){
        $global:nj += 1
        $global:pjc += 1
        Write-Host "El CPU Gana"
    }
    elseif($jugador1 -eq 3 -and $jugador2 -eq 2){
        $global:nj += 1
        $global:gjc += 1
        Write-Host "El Usuario Gana"
    }
    elseif($jugador1 -eq $jugador2){
        $global:nj += 1
        $global:ejc += 1
        Write-Host "Empate"
    }
}

function ver_estadisticas{
    Write-Host $global:fecha_hoy
    Write-Host ""
    Write-Host "--- ESTADISTICAS ---
    Partidas Jugadas: $nj
    
    Jugador vs Jugador
    Partidas Ganadas Jugador 1: $gj1
    Partidas Ganadas Jugador 2: $gj2
    Partidas Empatadas: $ejj
    
    Jugador vs CPU
    Partidas Ganadas: $gjc
    Partidas Perdidas: $pjc
    Partidas Empatadas: $ejc
    "
}

function archivo_estadisticas{
    param(
        [DateTime] $txt_fecha
    )
    New-Item -Path .\Estadisticas.txt
    $txt_fecha = "Fecha: $global:fecha_hoy
    "
    $txt_stats = "--- ESTADISTICAS ---
    Partidas Jugadas: $nj
    
    Jugador vs Jugador
    Partidas Ganadas Jugador 1: $gj1
    Partidas Ganadas Jugador 2: $gj2
    Partidas Empatadas: $ejj
    
    Jugador vs CPU
    Partidas Ganadas: $gjc
    Partidas Perdidas: $pjc
    Partidas Empatadas: $ejc
    
    "
    $txt_fecha >> .\Estadisticas.txt
    $txt_stats >> .\Estadisticas.txt
}