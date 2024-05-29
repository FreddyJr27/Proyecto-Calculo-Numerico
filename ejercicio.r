del1al10 <- function() {
    numero  <- readline("Ingrese un número para multiplicar: ")
    numerot <- as.numeric(numero)
    i <- 1

    while (i <= 10) {
        resultado <- numerot * i
        print(paste(numero, "+", i, "=", resultado))
        i <- i + 1
    }
}

del1al10()