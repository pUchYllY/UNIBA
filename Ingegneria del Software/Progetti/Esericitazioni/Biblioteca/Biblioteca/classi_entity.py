class Data:
    _giorno: int
    _mese: int
    _anno: int

    def __init__(self) -> None:
        self._giorno = 0
        self._mese = 0
        self._anno = 0

    def setData(self, giorno: int, mese: int, anno: int):
        self.setGiorno(giorno)
        self.setMese(mese)
        self.setAnno(anno)

    def setGiorno(self, nuovoGiorno: int):
        self.giorno = nuovoGiorno

    def getGiorno(self) -> int:
        return self.giorno

    def setMese(self, nuovoMese: int):
        self.mese = nuovoMese

    def getMese(self) -> int:
        return self.mese

    def setAnno(self, nuovoAnno: int):
        self.anno = nuovoAnno

    def getAnno(self) -> int:
        return self.anno


class Libro:
    _titolo: str
    _genere: str
    _isbn: str
    _pagine: int
    _numCopieDisp: int

    def __init__(self) -> None:
        self._titolo = ""
        self._genere = ""
        self._isbn = ""
        self.pagine = 0
        self._numCopieDisp = 0

    def setTitolo(self, nuovoTitolo: str):
        self._titolo = nuovoTitolo

    def getTitolo(self) -> str:
        return self._titolo

    def setGenere(self, nuovoGenere: str):
        self._genere = nuovoGenere

    def getGenere(self) -> str:
        return self._genere

    def setIsbn(self, nuovoIsbn: str):
        self._isbn = nuovoIsbn

    def getIsbn(self) -> str:
        return self._isbn

    def setPagine(self, nuovePagine: int):
        self._pagine = nuovePagine

    def getPagine(self) -> int:
        return self._pagine

    def setNumCopieDisp(self, nuovoNumCopieDisp: int):
        self._numCopieDisp = nuovoNumCopieDisp

    def getNumCopieDisp(self) -> int:
        return self._numCopieDisp

    def isDisponibile(self):
        return self._numCopieDisp > 0


class Prestito:
    _libroPrestito: Libro
    _dataPrestito: Data
    _dataScadenza: Data
    _dataRestituzione: Data
    _status: str
    _penale: float

    def __init__(self) -> None:
        self._libroPrestito = Libro()

        self._dataPrestito = Data()
        self._dataScadenza = Data()
        self._dataRestituzione = Data()

        self._status = ""
        self._penale = 0

    def setLibroPrestito(self, nuovoLibro: Libro):
        self._libroPrestito = nuovoLibro

    def getLibroPrestito(self) -> Libro:
        return self._libroPrestito

    def setDataPrestito(self, giorno: int, mese: int, anno: int):
        self._dataPrestito.setData(giorno, mese, anno)

    def getDataPrestito(self) -> Data:
        return self._dataPrestito

    def setDataScadenza(self, giorno: int, mese: int, anno: int):
        self._dataScadenza.setData(giorno, mese, anno)

    def getDataScadenza(self) -> Data:
        return self._dataScadenza

    def setDataRestituzione(self, giorno: int, mese: int, anno: int):
        self._dataScadenza.setData(giorno, mese, anno)

    def getDataRestituzione(self) -> Data:
        return self._dataRestituzione

    def setStatus(self, nuovoStatus: str):
        self._status = nuovoStatus

    def getStatus(self) -> str:
        return self._status

    def setPenale(self, nuovaPenale: float):
        self._penale = nuovaPenale

    def getPenale(self) -> float:
        return self._penale

    def isScaduto(self, data: Data) -> bool:
        return (data.mese > self._dataScadenza.getMese()) or (
            data.anno > self._dataScadenza.getAnno()
        )


class Utente:
    _nominativo: str
    _cod: int
    _email: str
    _password: str
    _listaPrestiti: list[Prestito]

    def __init__(self) -> None:
        self._nominativo = ""
        self._codUtente = 0
        self._email = ""
        self._password = ""

    def setNominativo(self, nuovoNominativo: str):
        self._nominativo = nuovoNominativo

    def getNominativo(self) -> str:
        return self._nominativo

    def setCod(self, nuovoCod: int):
        self._cod = nuovoCod

    def getCod(self) -> int:
        return self._cod

    def setEmail(self, nuovaEmail: str):
        self._email = nuovaEmail

    def getEmail(self) -> str:
        return self._email

    def setPassword(self, nuovaPassword: str):
        self._password = nuovaPassword

    def getPassword(self) -> str:
        return self._password

    def appendiPrestito(self, p: Prestito):
        self._listaPrestiti.append(p)

    def estraiPrestito(self, count: int) -> Prestito:
        return self._listaPrestiti.pop(count - 1)

    def rimuoviPrestito(self, isbn):
        for p in self._listaPrestiti:
            if isbn == p._libroPrestito._isbn:
                self._listaPrestiti.remove(p)
            break

    def ordinaPrestiti(self):
        self._listaPrestiti.sort(key=lambda p: p._dataPrestito._mese)


class RegistroUtenti:
    _registro: list[Utente]

    def aggiungiUtente(self, u: Utente):
        self._registro.append(u)

    def estraiUtente(self, codUtente: int):  # codUtente == utente._cod
        return self._registro.pop(codUtente)

    def rimuoviUtente(self, email: str):
        for u in self._registro:
            if u._email == email:
                self._registro.remove(u)
                break

    def ordinaUtenti(self):
        self._registro.sort(key=lambda u: u._cod)


class Catalogo:
    _depLibri: list[Libro]

    def aggiungiLibro(self, l: Libro):
        self._depLibri.append(l)

    def estraiLibro(self) -> Libro:
        return self._depLibri.pop()

    def rimuoviLibro(self, l: Libro):
        self._depLibri.remove(l)

    def ordinaLibri(self):
        self._depLibri.sort(key=lambda l: l._isbn)
