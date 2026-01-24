import pytest

def test_avvaloramento_veicolo():
	veicolo=Veicolo("Fiat","AB123CD","Mini Berlina","Panda",5,True,True)

	assert veicolo.getMarca() == "Fiat"
	assert veicolo.getTarga() == "AB123CD"
	assert veicolo.getCategoria() == "Mini Berlina"
	assert veicolo.getModello() ==  "Panda"
	assert veicolo.getNum_veicoli() == 5
	assert veicolo.getOfferta() == True
	assert veicolo.getDisponibile() == True

def test_avvaloramento_cliente():
	cliente=Cliente("CL001","Mario","Rossi","mario.rossi@example.com","3391234567")

	assert cliente.getCodice() == "CL001"
	assert cliente.getNome() == "Mario"
	assert cliente.getCognome() == "Rossi"
	assert cliente.getEmail() == "mario.rossi@example.com"
	assert cliente.getTelefono() == "3391234567"

def test_UI():
	ui = UI()
	assert 
	listaVeicoli:list[Veicolo]

	veicolo1=Veicolo("Fiat","AB123CD","Mini Berlina","Panda",5,True,True)
	veicolo2=Veicolo("Peugeot","CD123AB","Economy Berlina","208",10,False,True)
	veicolo3=Veicolo("Skoda","BD321AC","Compatta Berlina Manuale",0,True,False)

	assert veicolo1

