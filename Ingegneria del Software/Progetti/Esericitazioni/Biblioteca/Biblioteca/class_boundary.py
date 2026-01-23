import class_control


class UI:
    _con: class_control.Console

    def msgBenvenuto():
		print("Benvenuto\n")

    def msgModAutenticazione():
		print("Cosa vuole effettuare:")
		print("- [registrazione]")
		print("- [login]")
		print("- [chiusura] programma")

    def msgRichiestaAutenticazione():
		print("Inserire una delle modalita' situate nelle parentesi quadre!\n")

    def msgRichiestaCredenzialiReg():
		print("Inserire le seguenti credenziali per la registrazione:\n")

    def msgRichiestaCredenzialiLogin():
		print("Inserire le seguenti credenziali per il login:\n")

    def msgRichiestaRisposta():
		print("Confermi?\n")

    def msgRispostaNonValida():
		print("Risposta inserita non valida!")
	
    def msgRichiestaRispostaValida():
		print("(si/no): ",end=" ")

    def msgRegistrazioneSucc():
		print("Registrazione effettuata con successo!\n")

    def msgRegistrazioneFallita():
		print("Registrazione fallita!\n")

    def msgMostraOpzioni():
		print("------------------------SEZIONE UTENTI----------------------------\n")
		print("- [modifica] account")
		print("- effettua [prestito]")
		print("- [cancellazione] account")
		print("- [logout]\n")

    def msgRichiestaOpzione():
		print("Inserire una delle opzioni citate nelle parentesi quadre!\n")

    def msgRichiestaCredenzialiLibro():
		print("Inserire le seguenti credenziali del libro:\n")

    def msgMostraLibroTrovato():
		print("Libro trovato!\n")

    def msgRichiestaConfermaPrestito():
		print("Confermi prestito? (si/no): ", end=" ")

    def msgPrestitoSalvato():
		print("Salvataggio prestito concluso con successo!\n")

    def msgPrestitoNonSalvato():
		print("Salvataggio prestito annullato!\n")


    def msgAccountSalvato():
		print("Account salvato con successo!\n")

    def msgLoginSuccesso():
		print("Login effettuato con successo!\n")

    def msgLoginFallito():
		print("Login fallito!\n")


	def inserisceAutenticazione() ->str:
		s:str
		s=input("Modalita' Autenticazione: ")

		return s

	def inserisceCredenzialiReg(nominativo : str, email:str, password : str):
		nominativo=input("Nominativo: ")
		email=input("E-mail: ")
		password=input("Password: ")

    def inserisceCredenzialiLogin(email : str, password : str):
		email=input("E-mail: ")
		password=input("Password: ")

    def inseriscePassword()->str:
		s:str
		s=input()

		return s


    def inserisceOpzione()->str:
		s:str
		s=input("Opzione: ")

		return s


    def inserisceRisposta() ->str:
		s:str
		s=input()

		return s

    def inserisceCredenzialiLibro(titolo :str, isbn : str, genere :str) -> str:

