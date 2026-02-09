/*
* Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
*/

package com.mycompany.calcolatrice;

import java.util.*;
import java.io.*;

/**
 *
 * @author antonio
 */

public class Calcolatrice {
	public static void leggiStringa(StringBuilder s) throws IOException {
		try (BufferedReader br = new BufferedReader(new FileReader("file.txt"))) {
			char[] buffer = new char[100];
			int n;

			while ((n = br.read(buffer)) != -1) {
				s.append(buffer, 0, n);
			}
		}
	}

	public static void main(String[] args) {
		StringBuilder operazione = new StringBuilder();
		StringBuilder risposta = new StringBuilder();
		StringBuilder no = new StringBuilder("no");

		System.out.println("----------------- CALCOLATRICE -----------------");
		do {
			System.out.print("Inserire il calcolo da eseguire: ");

			try {
				leggiStringa(operazione);
			} catch (IOException e) {
				e.printStackTrace();
			}

			// console.effettuaOperazione(operazione);

			try {
				leggiStringa(risposta);
			} catch (IOException e) {
				e.printStackTrace();
			}
		} while (!risposta.toString().equals(no.toString()));

		System.out.println("Grazie per avermi usato e auguro una buona giornata :D\n");
	}
}
