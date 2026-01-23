import classi_entity
from calendar import isleap


class Console:
    _regUt: classi_entity.RegistroUtenti
    _cat: classi_entity.Catalogo

    _utLog: classi_entity.Utente
    _libPrestito: classi_entity.Libro
    _p: classi_entity.Prestito

    def creaUtente(
        self, nominaitvo: str, email: str, password: str
    ) -> classi_entity.Utente:
        u: classi_entity.Utente
        u = classi_entity.Utente()

        u.setNominativo(nominaitvo)
        u.setEmail(email)
        u.setPassword(password)

        return u

    # Gestione Utenti
    def salvaUtente(self):
        self._regUt.aggiungiUtente(self._utLog)

    def modificaUtente(self, nuovoNominativo: str, nuovaEmail: str, nuovaPass: str):
        self._utLog.setNominativo(nuovoNominativo)
        self._utLog.setEmail(nuovaEmail)
        self._utLog.setPassword(nuovaPass)

    def eliminaUtente(self, email: str):
        self._regUt.rimuoviUtente(email)

    # Gestione Prestiti
    def creaPrestito(self, giorno: int, mese: int, anno: int) -> classi_entity.Prestito:
        p = classi_entity.Prestito()
        self.salvaPrestito(giorno, mese, anno)
        return p

    def salvaPrestito(self, giorno: int, mese: int, anno: int):
        self._p.setLibroPrestito(self._libPrestito)
        self._p.setDataPrestito(giorno, mese, anno)

        if mese + 3 > 12:
            self._p.setDataScadenza(giorno, (mese + 3 - 12), anno)

        self._p.setStatus("attivo")

        self._utLog.appendiPrestito(self._p)

    def eliminaPrestito(self, email: str):
        for u in self._regUt._registro:
            if u._email == email:
                self._regUt._registro.remove(u)

            break
