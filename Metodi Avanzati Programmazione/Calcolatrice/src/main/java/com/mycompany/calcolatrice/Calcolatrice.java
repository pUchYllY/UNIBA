 /*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

import java.util.*
import java.io.*

package com.mycompany.calcolatrice;
import com.mycompany.calcolatrice.util.Console
import com.mycompany.calcolatrice.util.Operazioni
import com.mycompany.calcolatrice.util.Memoria
//import Operazioni.java

/**
 *
 * @author antonio
 */

public class Calcolatrice {
	 public void leggiOperazione(BufferedReader br){
		 br=new BufferedReader(new InputStreamReader(System.in)); // modo piu' efficiente di new Scanner(System.in)
	 }
	 public static void main(String[] args) {
		 BufferedReader br;
		 String operazione;
		 String risposta;

		 System.out.println("----------------- CALCOLATRICE -----------------");
		 do{
			 System.out.print("Inserire il calcolo da eseguire: ");

			 leggiOperazione(br);
			 operazione=br.readLine();

			 //console.effettuaOperazione(operazione);
		 }while(risposta!="no")
	 }
 }
